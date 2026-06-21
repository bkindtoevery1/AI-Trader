from decimal import Decimal

from aitrader.broker import RiskManager, build_order_intent, build_trade_decisions
from aitrader.config import load_config
from aitrader.models import Signal


def test_build_order_intent_respects_budget_and_dry_run():
    config = load_config("config/strategy.yaml")
    signal = Signal(
        symbol="005930",
        side="BUY",
        score=0.8,
        price=Decimal("70000"),
        timestamp=__import__("datetime").datetime.fromisoformat("2026-05-22T00:00:00+09:00"),
        reason="test",
    )

    intent = build_order_intent(signal, config=config, available_cash=Decimal("2000000"))

    assert intent is not None
    assert intent.dry_run is True
    assert intent.notional <= config.risk.max_order_value


def test_risk_manager_blocks_live_trading_when_disabled():
    config = load_config("config/strategy.yaml")
    signal = Signal(
        symbol="AAPL",
        side="BUY",
        score=0.9,
        price=Decimal("200"),
        timestamp=__import__("datetime").datetime.fromisoformat("2026-05-22T00:00:00+09:00"),
        reason="test",
    )
    intent = build_order_intent(
        signal,
        config=config,
        available_cash=Decimal("1000000"),
        dry_run=False,
    )

    assert intent is not None
    accepted, reason = RiskManager(config).validate(intent, orders_today=0)
    assert not accepted
    assert "live trading is disabled" in reason


def test_trade_decisions_include_skipped_sell_without_holdings():
    config = load_config("config/strategy.yaml")
    signal = Signal(
        symbol="AAPL",
        side="SELL",
        score=0.8,
        price=Decimal("200"),
        timestamp=__import__("datetime").datetime.fromisoformat("2026-05-22T00:00:00+09:00"),
        reason="test",
    )

    decisions = build_trade_decisions(
        [signal],
        config=config,
        available_cash=Decimal("1000000"),
        held_quantities={},
    )

    assert decisions[0].intent is None
    assert not decisions[0].accepted
    assert decisions[0].reason == "no sellable quantity"
