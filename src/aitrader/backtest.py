from __future__ import annotations

from dataclasses import replace
from decimal import Decimal, ROUND_DOWN
from math import sqrt

from .config import AppConfig
from .models import BacktestResult, Candle, Improvement, Trade
from .strategy import MovingAverageRsiStrategy


def _fee(amount: Decimal, fee_bps: Decimal) -> Decimal:
    return amount * fee_bps / Decimal("10000")


def _slipped(price: Decimal, side: str, slippage_bps: Decimal) -> Decimal:
    ratio = slippage_bps / Decimal("10000")
    return price * (Decimal("1") + ratio if side == "BUY" else Decimal("1") - ratio)


def _quantity_for_budget(budget: Decimal, price: Decimal) -> Decimal:
    if price <= 0:
        return Decimal("0")
    return (budget / price).quantize(Decimal("0.000001"), rounding=ROUND_DOWN)


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


def _sharpe(curve: list[tuple[object, Decimal]]) -> Decimal:
    if len(curve) < 3:
        return Decimal("0")
    returns: list[float] = []
    for (_, previous), (_, current) in zip(curve, curve[1:]):
        if previous:
            returns.append(float((current - previous) / previous))
    if len(returns) < 2:
        return Decimal("0")
    mean = sum(returns) / len(returns)
    variance = sum((item - mean) ** 2 for item in returns) / (len(returns) - 1)
    if variance == 0:
        return Decimal("0")
    return Decimal(str(mean / sqrt(variance) * sqrt(252)))


def run_backtest(symbol: str, candles: list[Candle], config: AppConfig) -> BacktestResult:
    ordered = sorted(candles, key=lambda item: item.timestamp)
    if len(ordered) < config.strategy.long_window + 1:
        raise ValueError(f"{symbol} needs at least {config.strategy.long_window + 1} candles")

    strategy = MovingAverageRsiStrategy(config.strategy)
    cash = config.risk.initial_cash
    quantity = Decimal("0")
    trades: list[Trade] = []
    equity_curve: list[tuple[object, Decimal]] = []

    for index, candle in enumerate(ordered):
        price = candle.close
        equity = cash + quantity * price
        signal = strategy.signal(symbol, ordered[: index + 1])
        can_trade = index >= config.strategy.long_window

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

        equity_curve.append((candle.timestamp, cash + quantity * price))

    final_equity = equity_curve[-1][1]
    total_return = (final_equity - config.risk.initial_cash) / config.risk.initial_cash * Decimal("100")
    return BacktestResult(
        symbol=symbol,
        start=ordered[0].timestamp,
        end=ordered[-1].timestamp,
        initial_cash=config.risk.initial_cash,
        final_equity=final_equity,
        total_return_pct=total_return,
        max_drawdown_pct=_max_drawdown(equity_curve),
        sharpe=_sharpe(equity_curve),
        trades=tuple(trades),
        equity_curve=tuple(equity_curve),
        parameters={
            "shortWindow": config.strategy.short_window,
            "longWindow": config.strategy.long_window,
            "rsiPeriod": config.strategy.rsi_period,
            "feeBps": str(config.risk.fee_bps),
            "slippageBps": str(config.risk.slippage_bps),
        },
    )


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

