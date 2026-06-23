from __future__ import annotations

from dataclasses import dataclass, replace
from decimal import Decimal, ROUND_DOWN
from math import isfinite, sqrt

from .config import AppConfig
from .models import BacktestResult, Candle, Improvement, Trade
from .strategy import DipSellPeakStrategy, MovingAverageRsiStrategy, TradingStrategy, build_strategy_variants


@dataclass
class _TierPosition:
    tier: int
    buy_price: Decimal
    quantity: Decimal
    buy_index: int
    sell_limit_price: Decimal


@dataclass(frozen=True)
class _PendingTierBuy:
    tier: int
    amount: Decimal
    limit_price: Decimal
    quantity: Decimal


def _fee(amount: Decimal, fee_bps: Decimal) -> Decimal:
    return amount * fee_bps / Decimal("10000")


def _slipped(price: Decimal, side: str, slippage_bps: Decimal) -> Decimal:
    ratio = slippage_bps / Decimal("10000")
    return price * (Decimal("1") + ratio if side == "BUY" else Decimal("1") - ratio)


def _quantity_for_budget(budget: Decimal, price: Decimal) -> Decimal:
    if price <= 0:
        return Decimal("0")
    return (budget / price).quantize(Decimal("0.000001"), rounding=ROUND_DOWN)


def _floor_price(price: Decimal) -> Decimal:
    return price.quantize(Decimal("0.01"), rounding=ROUND_DOWN)


def _whole_share_quantity(amount: Decimal, price: Decimal) -> Decimal:
    if amount <= 0 or price <= 0:
        return Decimal("0")
    return (amount / price).quantize(Decimal("1"), rounding=ROUND_DOWN)


def _max_drawdown(curve: list[tuple[object, Decimal]]) -> Decimal:
    if not curve:
        return Decimal("0")
    peak = curve[0][1]
    worst = Decimal("0")
    for _, equity in curve:
        peak = max(peak, equity)
        if peak > 0:
            worst = min(worst, (equity - peak) / peak)
    return abs(worst) * Decimal("100")


def _period_returns(curve: list[tuple[object, Decimal]]) -> list[Decimal]:
    returns: list[Decimal] = []
    for (_, previous), (_, current) in zip(curve, curve[1:]):
        if previous:
            returns.append((current - previous) / previous)
    return returns


def _sharpe_from_returns(returns: list[Decimal]) -> Decimal:
    if len(returns) < 2:
        return Decimal("0")
    values = [float(item) for item in returns]
    mean = sum(values) / len(values)
    variance = sum((item - mean) ** 2 for item in values) / (len(values) - 1)
    if variance == 0:
        return Decimal("0")
    return Decimal(str(mean / sqrt(variance) * sqrt(252)))


def _sortino_from_returns(returns: list[Decimal]) -> Decimal:
    downside = [float(item) for item in returns if item < 0]
    if len(returns) < 2 or not downside:
        return Decimal("0")
    values = [float(item) for item in returns]
    mean = sum(values) / len(values)
    downside_deviation = sqrt(sum(item**2 for item in downside) / len(downside))
    if downside_deviation == 0:
        return Decimal("0")
    return Decimal(str(mean / downside_deviation * sqrt(252)))


def _volatility_from_returns(returns: list[Decimal]) -> Decimal:
    if len(returns) < 2:
        return Decimal("0")
    values = [float(item) for item in returns]
    mean = sum(values) / len(values)
    variance = sum((item - mean) ** 2 for item in values) / (len(values) - 1)
    if variance == 0:
        return Decimal("0")
    return Decimal(str(sqrt(variance) * sqrt(252) * 100))


def _return_curve(curve: list[tuple[object, Decimal]]) -> list[tuple[object, Decimal]]:
    if not curve:
        return []
    points = [(curve[0][0], Decimal("0"))]
    for (timestamp, current), (_, previous) in zip(curve[1:], curve[:-1]):
        value = Decimal("0") if previous == 0 else (current - previous) / previous * Decimal("100")
        points.append((timestamp, value))
    return points


def _drawdown_curve(curve: list[tuple[object, Decimal]]) -> list[tuple[object, Decimal]]:
    if not curve:
        return []
    peak = curve[0][1]
    points: list[tuple[object, Decimal]] = []
    for timestamp, equity in curve:
        peak = max(peak, equity)
        drawdown = Decimal("0") if peak == 0 else (equity - peak) / peak * Decimal("100")
        points.append((timestamp, drawdown))
    return points


def _cagr(curve: list[tuple[object, Decimal]]) -> Decimal:
    if len(curve) < 2 or curve[0][1] <= 0:
        return Decimal("0")
    total_return = float(curve[-1][1] / curve[0][1])
    years = max((len(curve) - 1) / 252, 1 / 252)
    cagr = (total_return ** (1 / years) - 1) * 100
    if not isfinite(cagr):
        return Decimal("0")
    return Decimal(str(cagr))


def _trade_metrics(trades: list[Trade]) -> dict[str, Decimal | int | str]:
    entry_cost = Decimal("0")
    entry_quantity = Decimal("0")
    entry_fees = Decimal("0")
    round_returns: list[Decimal] = []
    round_pnls: list[Decimal] = []

    for trade in trades:
        gross = trade.price * trade.quantity
        if trade.side == "BUY":
            entry_cost += gross
            entry_quantity += trade.quantity
            entry_fees += trade.fee
            continue
        if entry_quantity <= 0 or entry_cost <= 0:
            continue
        exit_gross = trade.price * trade.quantity
        entry_share = min(Decimal("1"), trade.quantity / entry_quantity)
        allocated_cost = entry_cost * entry_share
        allocated_fee = entry_fees * entry_share
        pnl = exit_gross - allocated_cost - allocated_fee - trade.fee
        round_pnls.append(pnl)
        round_returns.append(pnl / allocated_cost * Decimal("100"))
        entry_cost -= allocated_cost
        entry_quantity -= trade.quantity
        entry_fees -= allocated_fee

    closed = len(round_returns)
    wins = sum(1 for item in round_returns if item > 0)
    gross_win = sum((item for item in round_pnls if item > 0), Decimal("0"))
    gross_loss = abs(sum((item for item in round_pnls if item < 0), Decimal("0")))
    profit_factor = Decimal("0")
    if gross_loss > 0:
        profit_factor = gross_win / gross_loss
    elif gross_win > 0:
        profit_factor = Decimal("999")

    return {
        "closedTrades": closed,
        "winRatePct": Decimal("0") if closed == 0 else Decimal(wins) / Decimal(closed) * Decimal("100"),
        "avgTradeReturnPct": Decimal("0")
        if closed == 0
        else sum(round_returns, Decimal("0")) / Decimal(closed),
        "bestTradePct": max(round_returns) if round_returns else Decimal("0"),
        "worstTradePct": min(round_returns) if round_returns else Decimal("0"),
        "profitFactor": profit_factor,
    }


def run_backtest(
    symbol: str,
    candles: list[Candle],
    config: AppConfig,
    strategy: TradingStrategy | None = None,
) -> BacktestResult:
    ordered = sorted(candles, key=lambda item: item.timestamp)
    active_strategy = strategy or MovingAverageRsiStrategy(config.strategy)
    if isinstance(active_strategy, DipSellPeakStrategy):
        return _run_dip_sell_peak_backtest(symbol, ordered, config, active_strategy)

    strategy_config = getattr(active_strategy, "config", config.strategy)
    warmup_window = active_strategy.warmup_window
    if len(ordered) < warmup_window + 1:
        raise ValueError(f"{symbol} needs at least {warmup_window + 1} candles")

    cash = config.risk.initial_cash
    quantity = Decimal("0")
    trades: list[Trade] = []
    equity_curve: list[tuple[object, Decimal]] = []
    exposure_days = 0

    for index, candle in enumerate(ordered):
        price = candle.close
        equity = cash + quantity * price
        signal = active_strategy.signal(symbol, ordered[: index + 1])
        can_trade = index >= warmup_window

        if can_trade and signal.side == "BUY" and quantity == 0:
            max_position_value = equity * config.risk.max_position_pct
            available_cash = max(Decimal("0"), cash * (Decimal("1") - config.risk.reserve_cash_pct))
            budget = min(config.risk.max_order_value, max_position_value, available_cash)
            execution_price = _slipped(price, "BUY", config.risk.slippage_bps)
            buy_quantity = _quantity_for_budget(budget, execution_price)
            gross = buy_quantity * execution_price
            fee = _fee(gross, config.risk.fee_bps)
            if buy_quantity > 0 and cash >= gross + fee:
                cash -= gross + fee
                quantity += buy_quantity
                trades.append(
                    Trade(symbol, "BUY", candle.timestamp, execution_price, buy_quantity, fee, cash, signal.reason)
                )
        elif can_trade and signal.side == "SELL" and quantity > 0:
            execution_price = _slipped(price, "SELL", config.risk.slippage_bps)
            gross = quantity * execution_price
            fee = _fee(gross, config.risk.fee_bps)
            cash += gross - fee
            trades.append(
                Trade(symbol, "SELL", candle.timestamp, execution_price, quantity, fee, cash, signal.reason)
            )
            quantity = Decimal("0")

        if quantity > 0:
            exposure_days += 1
        equity_curve.append((candle.timestamp, cash + quantity * price))

    final_equity = equity_curve[-1][1]
    total_return = (final_equity - config.risk.initial_cash) / config.risk.initial_cash * Decimal("100")
    period_returns = _period_returns(equity_curve)
    max_drawdown = _max_drawdown(equity_curve)
    cagr = _cagr(equity_curve)
    calmar = Decimal("0") if max_drawdown == 0 else cagr / max_drawdown
    buy_hold_return = (
        (ordered[-1].close - ordered[0].close) / ordered[0].close * Decimal("100")
        if ordered[0].close
        else Decimal("0")
    )
    metrics = {
        **_trade_metrics(trades),
        "cagrPct": cagr,
        "volatilityPct": _volatility_from_returns(period_returns),
        "sortino": _sortino_from_returns(period_returns),
        "calmar": calmar,
        "exposurePct": Decimal(exposure_days) / Decimal(len(ordered)) * Decimal("100"),
        "buyHoldReturnPct": buy_hold_return,
        "bestEquity": max((equity for _, equity in equity_curve), default=Decimal("0")),
        "worstEquity": min((equity for _, equity in equity_curve), default=Decimal("0")),
    }
    return BacktestResult(
        symbol=symbol,
        strategy_name=active_strategy.name,
        start=ordered[0].timestamp,
        end=ordered[-1].timestamp,
        initial_cash=config.risk.initial_cash,
        final_equity=final_equity,
        total_return_pct=total_return,
        max_drawdown_pct=max_drawdown,
        sharpe=_sharpe_from_returns(period_returns),
        trades=tuple(trades),
        equity_curve=tuple(equity_curve),
        parameters={
            "strategy": active_strategy.name,
            "shortWindow": strategy_config.short_window,
            "longWindow": strategy_config.long_window,
            "rsiPeriod": strategy_config.rsi_period,
            "feeBps": str(config.risk.fee_bps),
            "slippageBps": str(config.risk.slippage_bps),
        },
        metrics=metrics,
        drawdown_curve=tuple(_drawdown_curve(equity_curve)),
        return_curve=tuple(_return_curve(equity_curve)),
        price_curve=tuple((candle.timestamp, candle.close) for candle in ordered),
    )


def _run_dip_sell_peak_backtest(
    symbol: str,
    ordered: list[Candle],
    config: AppConfig,
    strategy: DipSellPeakStrategy,
) -> BacktestResult:
    if len(ordered) < 2:
        raise ValueError(f"{symbol} needs at least 2 candles")

    cash = config.risk.initial_cash
    cycle_initial_cash = cash
    has_traded_in_cycle = False
    reset_cycle_next_day = False
    completed_cycles = 0
    active_tiers: dict[int, _TierPosition] = {}
    trades: list[Trade] = []
    equity_curve: list[tuple[object, Decimal]] = [(ordered[0].timestamp, cash)]
    exposure_days = 0

    for index in range(1, len(ordered)):
        candle = ordered[index]
        previous = ordered[index - 1]
        if reset_cycle_next_day:
            cycle_initial_cash = cash
            has_traded_in_cycle = False
            reset_cycle_next_day = False

        pending_buy = _pending_dip_sell_peak_buy(
            active_tiers=active_tiers,
            cash=cash,
            cycle_initial_cash=cycle_initial_cash,
            previous_close=previous.close,
            strategy=strategy,
        )

        stop_loss_tiers = {
            tier
            for tier, position in active_tiers.items()
            if index - position.buy_index >= strategy.stop_loss_days
        }

        for tier in sorted(list(active_tiers)):
            if tier in stop_loss_tiers:
                continue
            position = active_tiers[tier]
            if candle.close < position.sell_limit_price:
                continue
            gross = position.quantity * candle.close
            cash += gross
            trades.append(
                Trade(
                    symbol,
                    "SELL",
                    candle.timestamp,
                    candle.close,
                    position.quantity,
                    Decimal("0"),
                    cash,
                    (
                        f"{strategy.pro} tier {tier} LOC sell; "
                        f"close {candle.close} >= limit {position.sell_limit_price}"
                    ),
                )
            )
            del active_tiers[tier]

        for tier in sorted(stop_loss_tiers):
            position = active_tiers.get(tier)
            if position is None:
                continue
            gross = position.quantity * candle.close
            cash += gross
            trades.append(
                Trade(
                    symbol,
                    "SELL",
                    candle.timestamp,
                    candle.close,
                    position.quantity,
                    Decimal("0"),
                    cash,
                    f"{strategy.pro} tier {tier} stop-loss MOC after {index - position.buy_index} days",
                )
            )
            del active_tiers[tier]

        if (
            pending_buy is not None
            and candle.close <= pending_buy.limit_price
            and pending_buy.quantity * candle.close <= cash
        ):
            gross = pending_buy.quantity * candle.close
            cash -= gross
            sell_limit_price = _floor_price(candle.close * (Decimal("1") + strategy.sell_threshold))
            active_tiers[pending_buy.tier] = _TierPosition(
                tier=pending_buy.tier,
                buy_price=candle.close,
                quantity=pending_buy.quantity,
                buy_index=index,
                sell_limit_price=sell_limit_price,
            )
            has_traded_in_cycle = True
            trades.append(
                Trade(
                    symbol,
                    "BUY",
                    candle.timestamp,
                    candle.close,
                    pending_buy.quantity,
                    Decimal("0"),
                    cash,
                    (
                        f"{strategy.pro} tier {pending_buy.tier} LOC buy; "
                        f"previous close {previous.close}, limit {pending_buy.limit_price}"
                    ),
                )
            )

        if has_traded_in_cycle and not active_tiers:
            completed_cycles += 1
            reset_cycle_next_day = True

        if active_tiers:
            exposure_days += 1
        equity_curve.append((candle.timestamp, cash + _tier_market_value(active_tiers, candle.close)))

    final_equity = equity_curve[-1][1]
    total_return = (final_equity - config.risk.initial_cash) / config.risk.initial_cash * Decimal("100")
    period_returns = _period_returns(equity_curve)
    max_drawdown = _max_drawdown(equity_curve)
    cagr = _cagr(equity_curve)
    calmar = Decimal("0") if max_drawdown == 0 else cagr / max_drawdown
    buy_hold_return = (
        (ordered[-1].close - ordered[0].close) / ordered[0].close * Decimal("100")
        if ordered[0].close
        else Decimal("0")
    )
    metrics = {
        **_trade_metrics(trades),
        "cagrPct": cagr,
        "volatilityPct": _volatility_from_returns(period_returns),
        "sortino": _sortino_from_returns(period_returns),
        "calmar": calmar,
        "exposurePct": Decimal(exposure_days) / Decimal(len(ordered)) * Decimal("100"),
        "buyHoldReturnPct": buy_hold_return,
        "bestEquity": max((equity for _, equity in equity_curve), default=Decimal("0")),
        "worstEquity": min((equity for _, equity in equity_curve), default=Decimal("0")),
        "completedCycles": completed_cycles,
        "activeTiers": len(active_tiers),
        "tierCount": 7,
    }
    return BacktestResult(
        symbol=symbol,
        strategy_name=strategy.name,
        start=ordered[0].timestamp,
        end=ordered[-1].timestamp,
        initial_cash=config.risk.initial_cash,
        final_equity=final_equity,
        total_return_pct=total_return,
        max_drawdown_pct=max_drawdown,
        sharpe=_sharpe_from_returns(period_returns),
        trades=tuple(trades),
        equity_curve=tuple(equity_curve),
        parameters={
            "strategy": strategy.name,
            "pro": strategy.pro,
            "tierRatios": [str(ratio) for ratio in strategy.tier_ratios],
            "buyThresholdPct": str(strategy.buy_threshold * Decimal("100")),
            "sellThresholdPct": str(strategy.sell_threshold * Decimal("100")),
            "stopLossDays": strategy.stop_loss_days,
            "feeBps": "0",
            "slippageBps": "0",
            "sourceLogic": "buy-dip-sell-peak",
            "executionModel": "daily close LOC/MOC historical rule evaluation",
        },
        metrics=metrics,
        drawdown_curve=tuple(_drawdown_curve(equity_curve)),
        return_curve=tuple(_return_curve(equity_curve)),
        price_curve=tuple((candle.timestamp, candle.close) for candle in ordered),
    )


def _pending_dip_sell_peak_buy(
    *,
    active_tiers: dict[int, _TierPosition],
    cash: Decimal,
    cycle_initial_cash: Decimal,
    previous_close: Decimal,
    strategy: DipSellPeakStrategy,
) -> _PendingTierBuy | None:
    tier = _next_buy_tier(active_tiers, cash)
    if tier is None:
        return None
    amount = cash if tier == 7 else cycle_initial_cash * strategy.tier_ratios[tier - 1]
    limit_price = _floor_price(previous_close * (Decimal("1") + strategy.buy_threshold))
    quantity = _whole_share_quantity(amount, limit_price)
    if quantity <= 0:
        return None
    return _PendingTierBuy(tier=tier, amount=amount, limit_price=limit_price, quantity=quantity)


def _next_buy_tier(active_tiers: dict[int, _TierPosition], cash: Decimal) -> int | None:
    for tier in range(1, 7):
        if tier not in active_tiers:
            return tier
    if cash > 0 and 7 not in active_tiers:
        return 7
    return None


def _tier_market_value(active_tiers: dict[int, _TierPosition], close: Decimal) -> Decimal:
    return sum((position.quantity * close for position in active_tiers.values()), Decimal("0"))


def run_strategy_suite(symbol: str, candles: list[Candle], config: AppConfig) -> list[BacktestResult]:
    return [run_backtest(symbol, candles, config, strategy) for strategy in build_strategy_variants(config.strategy)]


def find_improvements(symbol: str, candles: list[Candle], config: AppConfig) -> list[Improvement]:
    baseline = run_backtest(symbol, candles, config)
    candidates: list[BacktestResult] = []
    for short_window in (3, 5, 8, 10):
        for long_window in (15, 20, 30, 40):
            if short_window >= long_window or len(candles) < long_window + 1:
                continue
            strategy = replace(config.strategy, short_window=short_window, long_window=long_window)
            candidate_config = replace(config, strategy=strategy)
            candidates.append(run_backtest(symbol, candles, candidate_config))

    candidates.sort(key=lambda item: (item.total_return_pct, -item.max_drawdown_pct), reverse=True)
    suggestions: list[Improvement] = []
    for candidate in candidates[:3]:
        delta = candidate.total_return_pct - baseline.total_return_pct
        if delta <= 0:
            continue
        suggestions.append(
            Improvement(
                title=f"{symbol}: SMA {candidate.parameters['shortWindow']}/{candidate.parameters['longWindow']} 검증",
                rationale=(
                    f"동일 데이터에서 기준 전략 대비 수익률이 {delta:.2f}%p 높았고 "
                    f"최대 낙폭은 {candidate.max_drawdown_pct:.2f}%였습니다."
                ),
                expected_delta_pct=delta,
                parameters=candidate.parameters,
            )
        )
    if suggestions:
        return suggestions
    return [
        Improvement(
            title=f"{symbol}: 현 파라미터 유지",
            rationale="그리드 탐색에서 기준 전략을 명확히 이긴 조합이 없어 운영 파라미터 변경을 보류합니다.",
            expected_delta_pct=Decimal("0"),
            parameters=baseline.parameters,
        )
    ]
