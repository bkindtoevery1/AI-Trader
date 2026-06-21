from __future__ import annotations

from dataclasses import replace
from decimal import Decimal

from .config import StrategyConfig
from .indicators import rsi, sma
from .models import Candle, Signal


class MovingAverageRsiStrategy:
    """Conservative trend-following rule with an RSI heat filter."""

    def __init__(self, config: StrategyConfig) -> None:
        self.config = config

    def signal(self, symbol: str, candles: list[Candle]) -> Signal:
        ordered = sorted(candles, key=lambda item: item.timestamp)
        if len(ordered) < self.config.long_window + 1:
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
