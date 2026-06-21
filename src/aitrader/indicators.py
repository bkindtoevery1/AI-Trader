from __future__ import annotations

from decimal import Decimal


def sma(values: list[Decimal], window: int) -> Decimal | None:
    if window <= 0:
        raise ValueError("window must be positive")
    if len(values) < window:
        return None
    return sum(values[-window:]) / Decimal(window)


def rsi(values: list[Decimal], period: int) -> Decimal | None:
    if period <= 0:
        raise ValueError("period must be positive")
    if len(values) <= period:
        return None

    gains = Decimal("0")
    losses = Decimal("0")
    recent = values[-(period + 1) :]
    for previous, current in zip(recent, recent[1:]):
        change = current - previous
        if change >= 0:
            gains += change
        else:
            losses += abs(change)

    average_gain = gains / Decimal(period)
    average_loss = losses / Decimal(period)
    if average_loss == 0:
        return Decimal("100")
    relative_strength = average_gain / average_loss
    return Decimal("100") - (Decimal("100") / (Decimal("1") + relative_strength))

