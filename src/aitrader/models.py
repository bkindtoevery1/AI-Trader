from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal, ROUND_DOWN
from typing import Any, Literal


Side = Literal["BUY", "SELL", "HOLD"]


def to_decimal(value: Any) -> Decimal:
    if isinstance(value, Decimal):
        return value
    return Decimal(str(value))


def decimal_str(value: Decimal, places: int | None = None) -> str:
    if places is not None:
        quantum = Decimal("1").scaleb(-places)
        value = value.quantize(quantum, rounding=ROUND_DOWN)
    normalized = value.normalize()
    return format(normalized, "f")


@dataclass(frozen=True)
class Candle:
    symbol: str
    timestamp: datetime
    open: Decimal
    high: Decimal
    low: Decimal
    close: Decimal
    volume: Decimal
    currency: str = "KRW"

    @classmethod
    def from_mapping(cls, symbol: str, payload: dict[str, Any]) -> "Candle":
        return cls(
            symbol=symbol,
            timestamp=datetime.fromisoformat(str(payload["timestamp"])),
            open=to_decimal(payload.get("openPrice", payload.get("open"))),
            high=to_decimal(payload.get("highPrice", payload.get("high"))),
            low=to_decimal(payload.get("lowPrice", payload.get("low"))),
            close=to_decimal(payload.get("closePrice", payload.get("close"))),
            volume=to_decimal(payload["volume"]),
            currency=str(payload.get("currency", "KRW")),
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "symbol": self.symbol,
            "timestamp": self.timestamp.isoformat(),
            "open": decimal_str(self.open),
            "high": decimal_str(self.high),
            "low": decimal_str(self.low),
            "close": decimal_str(self.close),
            "volume": decimal_str(self.volume),
            "currency": self.currency,
        }


@dataclass(frozen=True)
class Signal:
    symbol: str
    side: Side
    score: float
    price: Decimal
    timestamp: datetime
    reason: str


@dataclass(frozen=True)
class OrderIntent:
    symbol: str
    side: Literal["BUY", "SELL"]
    quantity: Decimal
    order_type: Literal["LIMIT", "MARKET"]
    limit_price: Decimal | None
    notional: Decimal
    client_order_id: str
    reason: str
    dry_run: bool = True

    def to_toss_payload(self) -> dict[str, Any]:
        payload: dict[str, Any] = {
            "clientOrderId": self.client_order_id[:36],
            "symbol": self.symbol,
            "side": self.side,
            "orderType": self.order_type,
            "quantity": decimal_str(self.quantity, 6).rstrip("0").rstrip("."),
        }
        if self.limit_price is not None:
            payload["price"] = decimal_str(self.limit_price, 4).rstrip("0").rstrip(".")
        return payload


@dataclass(frozen=True)
class Trade:
    symbol: str
    side: Literal["BUY", "SELL"]
    timestamp: datetime
    price: Decimal
    quantity: Decimal
    fee: Decimal
    cash_after: Decimal
    reason: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "symbol": self.symbol,
            "side": self.side,
            "timestamp": self.timestamp.isoformat(),
            "price": decimal_str(self.price, 4),
            "quantity": decimal_str(self.quantity, 6),
            "fee": decimal_str(self.fee, 4),
            "cashAfter": decimal_str(self.cash_after, 4),
            "reason": self.reason,
        }


@dataclass(frozen=True)
class BacktestResult:
    symbol: str
    start: datetime
    end: datetime
    initial_cash: Decimal
    final_equity: Decimal
    total_return_pct: Decimal
    max_drawdown_pct: Decimal
    sharpe: Decimal
    trades: tuple[Trade, ...]
    equity_curve: tuple[tuple[datetime, Decimal], ...]
    parameters: dict[str, Any]

    def to_dict(self) -> dict[str, Any]:
        return {
            "symbol": self.symbol,
            "start": self.start.date().isoformat(),
            "end": self.end.date().isoformat(),
            "initialCash": decimal_str(self.initial_cash, 2),
            "finalEquity": decimal_str(self.final_equity, 2),
            "totalReturnPct": decimal_str(self.total_return_pct, 4),
            "maxDrawdownPct": decimal_str(self.max_drawdown_pct, 4),
            "sharpe": decimal_str(self.sharpe, 4),
            "tradeCount": len(self.trades),
            "trades": [trade.to_dict() for trade in self.trades],
            "equityCurve": [
                {"date": ts.date().isoformat(), "equity": decimal_str(equity, 2)}
                for ts, equity in self.equity_curve
            ],
            "parameters": self.parameters,
        }


@dataclass(frozen=True)
class Improvement:
    title: str
    rationale: str
    expected_delta_pct: Decimal
    parameters: dict[str, Any]

    def to_dict(self) -> dict[str, Any]:
        return {
            "title": self.title,
            "rationale": self.rationale,
            "expectedDeltaPct": decimal_str(self.expected_delta_pct, 4),
            "parameters": self.parameters,
        }

