from __future__ import annotations

import hashlib
from dataclasses import dataclass
from datetime import datetime, timezone
from decimal import Decimal, ROUND_DOWN

from .config import AppConfig
from .models import OrderIntent, Signal, decimal_str
from .toss_client import TossInvestClient


@dataclass(frozen=True)
class OrderPreview:
    intent: OrderIntent
    accepted: bool
    reason: str
    response: dict | None = None

    def to_dict(self) -> dict:
        return {
            "symbol": self.intent.symbol,
            "side": self.intent.side,
            "quantity": decimal_str(self.intent.quantity, 6),
            "orderType": self.intent.order_type,
            "limitPrice": decimal_str(self.intent.limit_price, 4) if self.intent.limit_price else None,
            "notional": decimal_str(self.intent.notional, 2),
            "clientOrderId": self.intent.client_order_id,
            "dryRun": self.intent.dry_run,
            "accepted": self.accepted,
            "reason": self.reason,
            "response": self.response,
        }


@dataclass(frozen=True)
class TradeDecision:
    signal: Signal
    intent: OrderIntent | None
    accepted: bool
    reason: str
    dry_run: bool

    def to_dict(self) -> dict:
        return {
            "symbol": self.signal.symbol,
            "signal": self.signal.side,
            "action": self.intent.side if self.intent else "SKIP",
            "score": self.signal.score,
            "price": decimal_str(self.signal.price, 4),
            "quantity": decimal_str(self.intent.quantity, 6) if self.intent else "0",
            "notional": decimal_str(self.intent.notional, 2) if self.intent else "0",
            "orderType": self.intent.order_type if self.intent else None,
            "limitPrice": decimal_str(self.intent.limit_price, 4) if self.intent and self.intent.limit_price else None,
            "clientOrderId": self.intent.client_order_id if self.intent else None,
            "accepted": self.accepted,
            "reason": self.reason,
            "dryRun": self.dry_run,
        }


class RiskManager:
    def __init__(self, config: AppConfig) -> None:
        self.config = config

    def validate(self, intent: OrderIntent, orders_today: int) -> tuple[bool, str]:
        if orders_today >= self.config.risk.max_daily_orders:
            return False, "daily order limit reached"
        if intent.notional > self.config.risk.max_order_value:
            return False, "order notional exceeds max_order_value"
        if not intent.dry_run and not self.config.risk.allow_live_trading:
            return False, "live trading is disabled by risk.allow_live_trading"
        if intent.quantity <= 0:
            return False, "quantity must be positive"
        return True, "accepted"


def build_trade_decisions(
    signals: list[Signal],
    *,
    config: AppConfig,
    available_cash: Decimal,
    available_cash_by_symbol: dict[str, Decimal] | None = None,
    held_quantities: dict[str, Decimal] | None = None,
    dry_run: bool = True,
) -> list[TradeDecision]:
    held_quantities = held_quantities or {}
    available_cash_by_symbol = available_cash_by_symbol or {}
    risk = RiskManager(config)
    decisions: list[TradeDecision] = []
    accepted_orders = 0

    for signal in signals:
        if signal.side == "HOLD":
            decisions.append(TradeDecision(signal, None, True, "hold signal", dry_run))
            continue

        held_quantity = held_quantities.get(signal.symbol, Decimal("0"))
        intent = build_order_intent(
            signal,
            config=config,
            available_cash=available_cash_by_symbol.get(signal.symbol, available_cash),
            held_quantity=held_quantity,
            dry_run=dry_run,
        )
        if intent is None:
            reason = "no sellable quantity" if signal.side == "SELL" else "insufficient buying budget"
            decisions.append(TradeDecision(signal, None, False, reason, dry_run))
            continue

        accepted, reason = risk.validate(intent, accepted_orders)
        if accepted:
            accepted_orders += 1
        decisions.append(TradeDecision(signal, intent, accepted, reason, dry_run))

    return decisions


def build_order_intent(
    signal: Signal,
    *,
    config: AppConfig,
    available_cash: Decimal,
    held_quantity: Decimal = Decimal("0"),
    dry_run: bool = True,
) -> OrderIntent | None:
    if signal.side == "HOLD":
        return None

    order_type = config.execution.order_type
    price_offset = config.execution.price_offset_bps / Decimal("10000")
    if signal.side == "BUY":
        budget = min(
            config.risk.max_order_value,
            available_cash * (Decimal("1") - config.risk.reserve_cash_pct),
            config.risk.initial_cash * config.risk.max_position_pct,
        )
        limit_price = signal.price * (Decimal("1") + price_offset) if order_type == "LIMIT" else None
        reference_price = limit_price or signal.price
        quantity = (budget / reference_price).quantize(Decimal("0.000001"), rounding=ROUND_DOWN)
        notional = quantity * reference_price
    else:
        quantity = held_quantity.quantize(Decimal("0.000001"), rounding=ROUND_DOWN)
        limit_price = signal.price * (Decimal("1") - price_offset) if order_type == "LIMIT" else None
        reference_price = limit_price or signal.price
        notional = quantity * reference_price

    if quantity <= 0:
        return None

    digest = hashlib.sha1(
        f"{signal.symbol}:{signal.side}:{signal.timestamp.isoformat()}:{decimal_str(quantity, 6)}".encode()
    ).hexdigest()[:16]
    client_order_id = f"ait-{datetime.now(timezone.utc):%Y%m%d}-{digest}"
    return OrderIntent(
        symbol=signal.symbol,
        side=signal.side,
        quantity=quantity,
        order_type=order_type,  # type: ignore[arg-type]
        limit_price=limit_price,
        notional=notional,
        client_order_id=client_order_id,
        reason=signal.reason,
        dry_run=dry_run,
    )


class TradingBroker:
    def __init__(self, client: TossInvestClient | None, config: AppConfig) -> None:
        self.client = client
        self.config = config
        self.risk = RiskManager(config)

    def submit(self, intents: list[OrderIntent], *, execute: bool = False) -> list[OrderPreview]:
        previews: list[OrderPreview] = []
        for index, intent in enumerate(intents):
            live_intent = OrderIntent(
                symbol=intent.symbol,
                side=intent.side,
                quantity=intent.quantity,
                order_type=intent.order_type,
                limit_price=intent.limit_price,
                notional=intent.notional,
                client_order_id=intent.client_order_id,
                reason=intent.reason,
                dry_run=not execute,
            )
            accepted, reason = self.risk.validate(live_intent, index)
            if not accepted:
                previews.append(OrderPreview(live_intent, False, reason))
                continue
            if not execute:
                previews.append(OrderPreview(live_intent, True, "dry-run preview"))
                continue
            if self.client is None:
                previews.append(OrderPreview(live_intent, False, "TossInvestClient is not configured"))
                continue
            response = self.client.create_order(live_intent.to_toss_payload())
            previews.append(OrderPreview(live_intent, True, "submitted", response))
        return previews
