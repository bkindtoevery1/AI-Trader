from __future__ import annotations

from dataclasses import dataclass, replace
from decimal import Decimal
from typing import Protocol

from .config import StrategyConfig, StrategyVariantConfig
from .indicators import rsi, sma
from .models import Candle, Signal


class TradingStrategy(Protocol):
    name: str

    @property
    def warmup_window(self) -> int:
        ...

    def signal(self, symbol: str, candles: list[Candle]) -> Signal:
        ...


@dataclass(frozen=True)
class DipSellPeakStrategy:
    """Buy Dip Sell Peak Pro tier strategy."""

    name: str
    pro: str
    tier_ratios: tuple[Decimal, ...]
    buy_threshold: Decimal
    sell_threshold: Decimal
    stop_loss_days: int
    config: StrategyConfig

    @property
    def warmup_window(self) -> int:
        return 1

    def signal(self, symbol: str, candles: list[Candle]) -> Signal:
        latest = sorted(candles, key=lambda item: item.timestamp)[-1]
        return Signal(
            symbol,
            "HOLD",
            0.0,
            latest.close,
            latest.timestamp,
            f"{self.pro} uses stateful tier backtest logic",
        )


class MovingAverageRsiStrategy:
    """Conservative trend-following rule with an RSI heat filter."""

    def __init__(self, config: StrategyConfig) -> None:
        self.config = config
        self.name = config.name

    @property
    def warmup_window(self) -> int:
        return max(self.config.long_window, self.config.rsi_period + 1)

    def signal(self, symbol: str, candles: list[Candle]) -> Signal:
        ordered = sorted(candles, key=lambda item: item.timestamp)
        if len(ordered) < self.warmup_window + 1:
            latest = ordered[-1]
            return Signal(symbol, "HOLD", 0.0, latest.close, latest.timestamp, "not enough candles")

        closes = [candle.close for candle in ordered]
        short_now = sma(closes, self.config.short_window)
        long_now = sma(closes, self.config.long_window)
        short_prev = sma(closes[:-1], self.config.short_window)
        long_prev = sma(closes[:-1], self.config.long_window)
        current_rsi = rsi(closes, self.config.rsi_period)
        latest = ordered[-1]

        if None in {short_now, long_now, short_prev, long_prev, current_rsi}:
            return Signal(symbol, "HOLD", 0.0, latest.close, latest.timestamp, "indicator warmup")

        crossed_up = short_prev <= long_prev and short_now > long_now
        crossed_down = short_prev >= long_prev and short_now < long_now
        uptrend = short_now > long_now
        downtrend = short_now < long_now
        overheating = current_rsi >= self.config.rsi_sell_above
        acceptable_heat = current_rsi < self.config.rsi_sell_above

        if (crossed_up or uptrend) and acceptable_heat:
            gap = (short_now - long_now) / long_now if long_now else Decimal("0")
            base = Decimal("0.55") if crossed_up else Decimal("0.42")
            score = float(min(Decimal("1"), gap * Decimal("20") + base))
            reason = "short SMA crossed above long SMA" if crossed_up else "short SMA remains above long SMA"
            return Signal(
                symbol,
                "BUY",
                score,
                latest.close,
                latest.timestamp,
                f"{reason}; RSI={current_rsi:.2f}",
            )
        if crossed_down or downtrend or overheating:
            if crossed_down:
                reason = "short SMA crossed below long SMA"
            elif downtrend:
                reason = "short SMA remains below long SMA"
            else:
                reason = f"RSI overheated at {current_rsi:.2f}"
            return Signal(symbol, "SELL", 0.75, latest.close, latest.timestamp, reason)

        trend_gap = abs((short_now - long_now) / long_now) if long_now else Decimal("0")
        return Signal(
            symbol,
            "HOLD",
            float(min(Decimal("1"), trend_gap * Decimal("10"))),
            latest.close,
            latest.timestamp,
            f"no crossover; RSI={current_rsi:.2f}",
        )

    def with_windows(self, short_window: int, long_window: int) -> "MovingAverageRsiStrategy":
        return MovingAverageRsiStrategy(
            replace(self.config, short_window=short_window, long_window=long_window)
        )


class SmaCrossoverStrategy:
    """Trend-following strategy without the RSI heat filter."""

    def __init__(self, config: StrategyConfig, *, name: str | None = None) -> None:
        self.config = config
        self.name = name or "sma-crossover"

    @property
    def warmup_window(self) -> int:
        return self.config.long_window

    def signal(self, symbol: str, candles: list[Candle]) -> Signal:
        ordered = sorted(candles, key=lambda item: item.timestamp)
        latest = ordered[-1]
        if len(ordered) < self.config.long_window + 1:
            return Signal(symbol, "HOLD", 0.0, latest.close, latest.timestamp, "not enough candles")

        closes = [candle.close for candle in ordered]
        short_now = sma(closes, self.config.short_window)
        long_now = sma(closes, self.config.long_window)
        short_prev = sma(closes[:-1], self.config.short_window)
        long_prev = sma(closes[:-1], self.config.long_window)
        if None in {short_now, long_now, short_prev, long_prev}:
            return Signal(symbol, "HOLD", 0.0, latest.close, latest.timestamp, "indicator warmup")

        crossed_up = short_prev <= long_prev and short_now > long_now
        crossed_down = short_prev >= long_prev and short_now < long_now
        if crossed_up or short_now > long_now:
            gap = (short_now - long_now) / long_now if long_now else Decimal("0")
            return Signal(
                symbol,
                "BUY",
                float(min(Decimal("1"), Decimal("0.45") + gap * Decimal("18"))),
                latest.close,
                latest.timestamp,
                "short SMA above long SMA" if not crossed_up else "short SMA crossed above long SMA",
            )
        if crossed_down or short_now < long_now:
            return Signal(symbol, "SELL", 0.72, latest.close, latest.timestamp, "short SMA below long SMA")
        return Signal(symbol, "HOLD", 0.1, latest.close, latest.timestamp, "SMA spread is flat")


class RsiMeanReversionStrategy:
    """Mean-reversion rule that buys weakness and exits strength."""

    def __init__(self, config: StrategyConfig, *, name: str | None = None) -> None:
        self.config = config
        self.name = name or "rsi-mean-reversion"

    @property
    def warmup_window(self) -> int:
        return self.config.rsi_period + 1

    def signal(self, symbol: str, candles: list[Candle]) -> Signal:
        ordered = sorted(candles, key=lambda item: item.timestamp)
        latest = ordered[-1]
        if len(ordered) < self.warmup_window + 1:
            return Signal(symbol, "HOLD", 0.0, latest.close, latest.timestamp, "not enough candles")

        current_rsi = rsi([candle.close for candle in ordered], self.config.rsi_period)
        if current_rsi is None:
            return Signal(symbol, "HOLD", 0.0, latest.close, latest.timestamp, "indicator warmup")
        if current_rsi <= self.config.rsi_buy_below:
            score = Decimal("1") - (current_rsi / Decimal("100"))
            return Signal(symbol, "BUY", float(score), latest.close, latest.timestamp, f"RSI weak at {current_rsi:.2f}")
        if current_rsi >= self.config.rsi_sell_above:
            return Signal(symbol, "SELL", 0.75, latest.close, latest.timestamp, f"RSI recovered to {current_rsi:.2f}")
        return Signal(symbol, "HOLD", 0.2, latest.close, latest.timestamp, f"RSI neutral at {current_rsi:.2f}")


class BuyAndHoldStrategy:
    """Baseline that enters once and holds through the sample."""

    name = "buy-and-hold"
    warmup_window = 1

    def signal(self, symbol: str, candles: list[Candle]) -> Signal:
        latest = sorted(candles, key=lambda item: item.timestamp)[-1]
        return Signal(symbol, "BUY", 1.0, latest.close, latest.timestamp, "baseline buy and hold")


def build_strategy_variants(config: StrategyConfig) -> list[TradingStrategy]:
    variants: list[TradingStrategy] = []
    for variant in config.variants:
        variants.append(_build_strategy_variant(config, variant))
    return variants or [MovingAverageRsiStrategy(config)]


def _build_strategy_variant(config: StrategyConfig, variant: StrategyVariantConfig) -> TradingStrategy:
    strategy_config = _config_for_variant(config, variant)
    if variant.type in {"dip_sell_peak", "buy_dip_sell_peak", "bdsp"}:
        return _build_dip_sell_peak_strategy(strategy_config, variant)
    if variant.type in {"ma_rsi", "ma_rsi_core"}:
        strategy = MovingAverageRsiStrategy(replace(strategy_config, name=variant.name))
        strategy.name = variant.name
        return strategy
    if variant.type in {"sma_crossover", "sma"}:
        return SmaCrossoverStrategy(strategy_config, name=variant.name)
    if variant.type in {"rsi_mean_reversion", "rsi_reversion", "mean_reversion"}:
        return RsiMeanReversionStrategy(strategy_config, name=variant.name)
    if variant.type in {"buy_and_hold", "buy_hold", "baseline"}:
        strategy = BuyAndHoldStrategy()
        strategy.name = variant.name
        return strategy
    raise ValueError(f"Unknown strategy variant type: {variant.type}")


def _build_dip_sell_peak_strategy(config: StrategyConfig, variant: StrategyVariantConfig) -> DipSellPeakStrategy:
    pro = _normalize_pro_name(str(variant.parameters.get("pro", variant.name)))
    profile = _dip_sell_peak_profile(pro)
    return DipSellPeakStrategy(
        name=variant.name,
        pro=pro,
        tier_ratios=profile["tier_ratios"],
        buy_threshold=profile["buy_threshold"],
        sell_threshold=profile["sell_threshold"],
        stop_loss_days=int(profile["stop_loss_days"]),
        config=replace(config, name=variant.name),
    )


def _normalize_pro_name(raw: str) -> str:
    value = raw.upper().replace("-", "").replace("_", "").replace(" ", "")
    if value.endswith("PRO1") or value == "1":
        return "Pro1"
    if value.endswith("PRO2") or value == "2":
        return "Pro2"
    if value.endswith("PRO3") or value == "3":
        return "Pro3"
    raise ValueError(f"Unknown dip-sell-peak pro profile: {raw}")


def _dip_sell_peak_profile(pro: str) -> dict[str, tuple[Decimal, ...] | Decimal | int]:
    equal_six = tuple(Decimal("1") / Decimal("6") for _ in range(6))
    profiles: dict[str, dict[str, tuple[Decimal, ...] | Decimal | int]] = {
        "Pro1": {
            "tier_ratios": (
                Decimal("0.05"),
                Decimal("0.10"),
                Decimal("0.15"),
                Decimal("0.20"),
                Decimal("0.25"),
                Decimal("0.25"),
            ),
            "buy_threshold": Decimal("-0.0001"),
            "sell_threshold": Decimal("0.0001"),
            "stop_loss_days": 10,
        },
        "Pro2": {
            "tier_ratios": (
                Decimal("0.10"),
                Decimal("0.15"),
                Decimal("0.20"),
                Decimal("0.25"),
                Decimal("0.20"),
                Decimal("0.10"),
            ),
            "buy_threshold": Decimal("-0.0001"),
            "sell_threshold": Decimal("0.015"),
            "stop_loss_days": 10,
        },
        "Pro3": {
            "tier_ratios": equal_six,
            "buy_threshold": Decimal("-0.001"),
            "sell_threshold": Decimal("0.02"),
            "stop_loss_days": 12,
        },
    }
    return profiles[pro]


def _config_for_variant(config: StrategyConfig, variant: StrategyVariantConfig) -> StrategyConfig:
    parameters = variant.parameters
    return replace(
        config,
        name=variant.name,
        short_window=int(parameters.get("short_window", config.short_window)),
        long_window=int(parameters.get("long_window", config.long_window)),
        rsi_period=int(parameters.get("rsi_period", config.rsi_period)),
        rsi_buy_below=Decimal(str(parameters.get("rsi_buy_below", config.rsi_buy_below))),
        rsi_sell_above=Decimal(str(parameters.get("rsi_sell_above", config.rsi_sell_above))),
    )
