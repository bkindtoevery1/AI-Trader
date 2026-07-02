from datetime import datetime
from decimal import Decimal

from aitrader.models import OrderIntent
from aitrader.order_ledger import count_logged_orders, record_submitted_order


def test_order_ledger_counts_only_matching_trade_date(tmp_path):
    ledger = tmp_path / "orders.jsonl"
    first = OrderIntent(
        symbol="SOXL",
        side="BUY",
        quantity=Decimal("4"),
        order_type="LIMIT",
        limit_price=Decimal("217.76"),
        notional=Decimal("871.04"),
        client_order_id="ait-20260702-test",
        reason="test",
        dry_run=False,
    )
    second = OrderIntent(
        symbol="SOXS",
        side="SELL",
        quantity=Decimal("63"),
        order_type="MARKET",
        limit_price=None,
        notional=Decimal("237.51"),
        client_order_id="ait-20260703-test",
        reason="test",
        dry_run=False,
    )

    record_submitted_order(
        ledger,
        first,
        {"orderId": "order-1"},
        submitted_at=datetime.fromisoformat("2026-07-02T22:00:00+09:00"),
    )
    record_submitted_order(
        ledger,
        second,
        {"orderId": "order-2"},
        submitted_at=datetime.fromisoformat("2026-07-03T22:00:00+09:00"),
    )

    assert count_logged_orders(ledger, "2026-07-02") == 1
    assert count_logged_orders(ledger, "2026-07-03") == 1
    assert count_logged_orders(ledger, "2026-07-04") == 0


def test_order_ledger_ignores_missing_and_corrupt_lines(tmp_path):
    ledger = tmp_path / "orders.jsonl"

    assert count_logged_orders(ledger, "2026-07-02") == 0

    ledger.write_text('not-json\n{"tradeDate": "2026-07-02"}\n', encoding="utf-8")

    assert count_logged_orders(ledger, "2026-07-02") == 1
