from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Any

from .config import AppConfig
from .models import decimal_str, to_decimal
from .toss_client import TossApiError, TossInvestClient


@dataclass(frozen=True)
class AccountSnapshot:
    generated_at: datetime
    buying_power: dict[str, Decimal]
    holdings: dict[str, Decimal]
    sellable_quantities: dict[str, Decimal]
    source: str
    errors: tuple[str, ...] = ()

    def to_dict(self) -> dict[str, Any]:
        return {
            "generatedAt": self.generated_at.isoformat(),
            "source": self.source,
            "buyingPower": {currency: decimal_str(value, 4) for currency, value in self.buying_power.items()},
            "holdings": {symbol: decimal_str(value, 6) for symbol, value in self.holdings.items()},
            "sellableQuantities": {
                symbol: decimal_str(value, 6) for symbol, value in self.sellable_quantities.items()
            },
            "errors": list(self.errors),
        }


def simulated_account_snapshot(config: AppConfig) -> AccountSnapshot:
    return AccountSnapshot(
        generated_at=datetime.now().astimezone(),
        buying_power={config.risk.currency: config.risk.initial_cash},
        holdings={},
        sellable_quantities={},
        source="simulated",
    )


def fetch_account_snapshot(
    client: TossInvestClient,
    config: AppConfig,
    *,
    symbols: tuple[str, ...],
) -> AccountSnapshot:
    errors: list[str] = []
    holdings: dict[str, Decimal] = {}
    sellable: dict[str, Decimal] = {}
    buying_power: dict[str, Decimal] = {}

    try:
        holdings_payload = client.get_holdings()
        for item in _extract_holdings_items(holdings_payload):
            symbol = str(item.get("symbol", "")).upper()
            if symbol:
                holdings[symbol] = to_decimal(item.get("quantity", "0"))
    except TossApiError as exc:
        errors.append(f"holdings: {exc}")

    for currency in sorted({_symbol_currency(symbol) for symbol in symbols} | {config.risk.currency}):
        try:
            payload = client.get_buying_power(currency)
            buying_power[currency] = to_decimal(payload.get("cashBuyingPower", "0"))
        except TossApiError as exc:
            errors.append(f"buying-power {currency}: {exc}")

    for symbol in symbols:
        try:
            payload = client.get_sellable_quantity(symbol)
            sellable[symbol] = to_decimal(payload.get("sellableQuantity", holdings.get(symbol, Decimal("0"))))
        except TossApiError as exc:
            errors.append(f"sellable {symbol}: {exc}")
            if symbol in holdings:
                sellable[symbol] = holdings[symbol]

    return AccountSnapshot(
        generated_at=datetime.now().astimezone(),
        buying_power=buying_power,
        holdings=holdings,
        sellable_quantities=sellable,
        source="toss",
        errors=tuple(errors),
    )


def cash_by_symbol(snapshot: AccountSnapshot, symbols: tuple[str, ...]) -> dict[str, Decimal]:
    return {
        symbol: snapshot.buying_power.get(_symbol_currency(symbol), Decimal("0"))
        for symbol in symbols
    }


def _extract_holdings_items(payload: dict[str, Any]) -> list[dict[str, Any]]:
    if isinstance(payload.get("items"), list):
        return [item for item in payload["items"] if isinstance(item, dict)]
    if isinstance(payload.get("holdings"), list):
        return [item for item in payload["holdings"] if isinstance(item, dict)]
    return []


def _symbol_currency(symbol: str) -> str:
    return "KRW" if symbol.isdigit() else "USD"

