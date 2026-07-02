from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Any

from .models import OrderIntent, decimal_str


DEFAULT_ORDER_LEDGER_PATH = Path("state/order-ledger.jsonl")


def record_submitted_order(
    path: str | Path,
    intent: OrderIntent,
    response: dict[str, Any] | None,
    *,
    submitted_at: datetime | None = None,
) -> None:
    timestamp = submitted_at or datetime.now().astimezone()
    record = {
        "submittedAt": timestamp.isoformat(),
        "tradeDate": timestamp.date().isoformat(),
        "clientOrderId": intent.client_order_id,
        "symbol": intent.symbol,
        "side": intent.side,
        "quantity": decimal_str(intent.quantity, 6),
        "orderType": intent.order_type,
        "limitPrice": decimal_str(intent.limit_price, 4) if intent.limit_price else None,
        "notional": decimal_str(intent.notional, 2),
        "responseOrderId": _response_order_id(response),
    }
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("a", encoding="utf-8") as file:
        file.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")


def count_logged_orders(path: str | Path, trade_date: str) -> int:
    target = Path(path)
    if not target.exists():
        return 0
    count = 0
    for line in target.read_text(encoding="utf-8").splitlines():
        try:
            record = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(record, dict) and record.get("tradeDate") == trade_date:
            count += 1
    return count


def _response_order_id(response: dict[str, Any] | None) -> str | None:
    if not isinstance(response, dict):
        return None
    for key in ("orderId", "id"):
        value = response.get(key)
        if value:
            return str(value)
    result = response.get("result")
    if isinstance(result, dict):
        return _response_order_id(result)
    return None
