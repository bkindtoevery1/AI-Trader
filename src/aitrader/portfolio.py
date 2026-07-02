from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Any

from .account import AccountSnapshot
from .config import AppConfig
from .models import decimal_str, to_decimal
from .toss_client import TossApiError, TossInvestClient


@dataclass(frozen=True)
class PositionEvaluation:
    symbol: str
    name: str
    quantity: Decimal
    sellable_quantity: Decimal
    average_purchase_price: Decimal
    last_price: Decimal
    purchase_amount: Decimal
    market_amount: Decimal
    market_amount_after_cost: Decimal
    profit_loss_amount: Decimal
    profit_loss_amount_after_cost: Decimal
    profit_loss_rate: Decimal
    profit_loss_rate_after_cost: Decimal
    daily_profit_loss_amount: Decimal
    daily_profit_loss_rate: Decimal
    currency: str
    weight_pct: Decimal = Decimal("0")

    def with_weight(self, total_equity: Decimal) -> "PositionEvaluation":
        if total_equity <= 0:
            return self
        return PositionEvaluation(
            **{
                **self.__dict__,
                "weight_pct": self.market_amount / total_equity * Decimal("100"),
            }
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "symbol": self.symbol,
            "name": self.name,
            "quantity": decimal_str(self.quantity, 6),
            "sellableQuantity": decimal_str(self.sellable_quantity, 6),
            "averagePurchasePrice": decimal_str(self.average_purchase_price, 4),
            "lastPrice": decimal_str(self.last_price, 4),
            "purchaseAmount": decimal_str(self.purchase_amount, 2),
            "marketAmount": decimal_str(self.market_amount, 2),
            "marketAmountAfterCost": decimal_str(self.market_amount_after_cost, 2),
            "profitLossAmount": decimal_str(self.profit_loss_amount, 2),
            "profitLossAmountAfterCost": decimal_str(self.profit_loss_amount_after_cost, 2),
            "profitLossRatePct": decimal_str(self.profit_loss_rate * Decimal("100"), 2),
            "profitLossRateAfterCostPct": decimal_str(
                self.profit_loss_rate_after_cost * Decimal("100"), 2
            ),
            "dailyProfitLossAmount": decimal_str(self.daily_profit_loss_amount, 2),
            "dailyProfitLossRatePct": decimal_str(self.daily_profit_loss_rate * Decimal("100"), 2),
            "currency": self.currency,
            "weightPct": decimal_str(self.weight_pct, 2),
        }


@dataclass(frozen=True)
class PortfolioEvaluation:
    generated_at: datetime
    positions: tuple[PositionEvaluation, ...]
    buying_power: dict[str, Decimal]
    total_purchase_amount: Decimal
    total_market_amount: Decimal
    total_market_amount_after_cost: Decimal
    total_profit_loss_amount: Decimal
    total_profit_loss_amount_after_cost: Decimal
    total_profit_loss_rate: Decimal
    total_profit_loss_rate_after_cost: Decimal
    total_daily_profit_loss_amount: Decimal
    total_daily_profit_loss_rate: Decimal
    total_equity: Decimal
    currency: str
    errors: tuple[str, ...] = ()

    def to_dict(self) -> dict[str, Any]:
        return {
            "generatedAt": self.generated_at.isoformat(),
            "currency": self.currency,
            "buyingPower": {
                currency: decimal_str(value, 2) for currency, value in self.buying_power.items()
            },
            "totalPurchaseAmount": decimal_str(self.total_purchase_amount, 2),
            "totalMarketAmount": decimal_str(self.total_market_amount, 2),
            "totalMarketAmountAfterCost": decimal_str(self.total_market_amount_after_cost, 2),
            "totalProfitLossAmount": decimal_str(self.total_profit_loss_amount, 2),
            "totalProfitLossAmountAfterCost": decimal_str(
                self.total_profit_loss_amount_after_cost, 2
            ),
            "totalProfitLossRatePct": decimal_str(self.total_profit_loss_rate * Decimal("100"), 2),
            "totalProfitLossRateAfterCostPct": decimal_str(
                self.total_profit_loss_rate_after_cost * Decimal("100"), 2
            ),
            "totalDailyProfitLossAmount": decimal_str(self.total_daily_profit_loss_amount, 2),
            "totalDailyProfitLossRatePct": decimal_str(
                self.total_daily_profit_loss_rate * Decimal("100"), 2
            ),
            "totalEquity": decimal_str(self.total_equity, 2),
            "positions": [position.to_dict() for position in self.positions],
            "errors": list(self.errors),
        }


def fetch_portfolio_evaluation(
    client: TossInvestClient,
    config: AppConfig,
    account: AccountSnapshot,
) -> PortfolioEvaluation:
    errors: list[str] = []
    positions: list[PositionEvaluation] = []
    try:
        payload = client.get_holdings()
        for item in _extract_holdings_items(payload):
            symbol = str(item.get("symbol", "")).upper()
            if not symbol:
                continue
            positions.append(
                PositionEvaluation(
                    symbol=symbol,
                    name=str(item.get("name", symbol)),
                    quantity=_decimal(item.get("quantity")),
                    sellable_quantity=account.sellable_quantities.get(symbol, Decimal("0")),
                    average_purchase_price=_decimal(item.get("averagePurchasePrice")),
                    last_price=_decimal(item.get("lastPrice")),
                    purchase_amount=_decimal(_nested(item, "marketValue", "purchaseAmount")),
                    market_amount=_decimal(_nested(item, "marketValue", "amount")),
                    market_amount_after_cost=_decimal(_nested(item, "marketValue", "amountAfterCost")),
                    profit_loss_amount=_decimal(_nested(item, "profitLoss", "amount")),
                    profit_loss_amount_after_cost=_decimal(_nested(item, "profitLoss", "amountAfterCost")),
                    profit_loss_rate=_decimal(_nested(item, "profitLoss", "rate")),
                    profit_loss_rate_after_cost=_decimal(_nested(item, "profitLoss", "rateAfterCost")),
                    daily_profit_loss_amount=_decimal(_nested(item, "dailyProfitLoss", "amount")),
                    daily_profit_loss_rate=_decimal(_nested(item, "dailyProfitLoss", "rate")),
                    currency=str(item.get("currency", config.risk.currency)),
                )
            )
    except TossApiError as exc:
        errors.append(f"holdings detail: {exc}")

    total_purchase = sum((position.purchase_amount for position in positions), Decimal("0"))
    total_market = sum((position.market_amount for position in positions), Decimal("0"))
    total_after_cost = sum((position.market_amount_after_cost for position in positions), Decimal("0"))
    total_profit = sum((position.profit_loss_amount for position in positions), Decimal("0"))
    total_profit_after_cost = sum(
        (position.profit_loss_amount_after_cost for position in positions), Decimal("0")
    )
    total_daily_profit = sum((position.daily_profit_loss_amount for position in positions), Decimal("0"))
    cash = account.buying_power.get(config.risk.currency, Decimal("0"))
    total_equity = cash + total_market
    weighted_positions = tuple(position.with_weight(total_equity) for position in positions)
    total_profit_rate = Decimal("0") if total_purchase <= 0 else total_profit / total_purchase
    total_profit_rate_after_cost = (
        Decimal("0") if total_purchase <= 0 else total_profit_after_cost / total_purchase
    )
    previous_market = total_market - total_daily_profit
    total_daily_rate = Decimal("0") if previous_market <= 0 else total_daily_profit / previous_market
    return PortfolioEvaluation(
        generated_at=datetime.now().astimezone(),
        positions=weighted_positions,
        buying_power=account.buying_power,
        total_purchase_amount=total_purchase,
        total_market_amount=total_market,
        total_market_amount_after_cost=total_after_cost,
        total_profit_loss_amount=total_profit,
        total_profit_loss_amount_after_cost=total_profit_after_cost,
        total_profit_loss_rate=total_profit_rate,
        total_profit_loss_rate_after_cost=total_profit_rate_after_cost,
        total_daily_profit_loss_amount=total_daily_profit,
        total_daily_profit_loss_rate=total_daily_rate,
        total_equity=total_equity,
        currency=config.risk.currency,
        errors=tuple(errors),
    )


def _extract_holdings_items(payload: dict[str, Any]) -> list[dict[str, Any]]:
    if isinstance(payload.get("items"), list):
        return [item for item in payload["items"] if isinstance(item, dict)]
    if isinstance(payload.get("holdings"), list):
        return [item for item in payload["holdings"] if isinstance(item, dict)]
    result = payload.get("result")
    if isinstance(result, dict):
        return _extract_holdings_items(result)
    return []


def _nested(payload: dict[str, Any], key: str, nested_key: str) -> Any:
    value = payload.get(key)
    if isinstance(value, dict):
        return value.get(nested_key)
    return None


def _decimal(value: Any) -> Decimal:
    if value in (None, ""):
        return Decimal("0")
    return to_decimal(value)
