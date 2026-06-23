from __future__ import annotations

import csv
from collections import defaultdict
from datetime import date, datetime
from pathlib import Path

from .models import Candle, to_decimal


def load_candles_csv(path: str | Path) -> dict[str, list[Candle]]:
    candles: dict[str, list[Candle]] = defaultdict(list)
    with Path(path).open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            symbol = row["symbol"].upper()
            candles[symbol].append(
                Candle(
                    symbol=symbol,
                    timestamp=datetime.fromisoformat(row["timestamp"]),
                    open=to_decimal(row["open"]),
                    high=to_decimal(row["high"]),
                    low=to_decimal(row["low"]),
                    close=to_decimal(row["close"]),
                    volume=to_decimal(row["volume"]),
                    currency=row.get("currency", "KRW"),
                )
            )
    return {symbol: sorted(items, key=lambda item: item.timestamp) for symbol, items in candles.items()}


def filter_candles_before_date(
    candles_by_symbol: dict[str, list[Candle]],
    cutoff_date: date,
) -> dict[str, list[Candle]]:
    return {
        symbol: [candle for candle in candles if candle.timestamp.date() < cutoff_date]
        for symbol, candles in candles_by_symbol.items()
    }


def drop_today_candles(
    candles_by_symbol: dict[str, list[Candle]],
    *,
    today: date | None = None,
) -> dict[str, list[Candle]]:
    return filter_candles_before_date(candles_by_symbol, today or datetime.now().astimezone().date())


def write_candles_csv(path: str | Path, candles_by_symbol: dict[str, list[Candle]]) -> None:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["symbol", "timestamp", "open", "high", "low", "close", "volume", "currency"],
        )
        writer.writeheader()
        for symbol in sorted(candles_by_symbol):
            for candle in sorted(candles_by_symbol[symbol], key=lambda item: item.timestamp):
                writer.writerow(
                    {
                        "symbol": candle.symbol,
                        "timestamp": candle.timestamp.isoformat(),
                        "open": str(candle.open),
                        "high": str(candle.high),
                        "low": str(candle.low),
                        "close": str(candle.close),
                        "volume": str(candle.volume),
                        "currency": candle.currency,
                    }
                )
