from decimal import Decimal
from dataclasses import replace

from aitrader.broker import RiskManager, TradingBroker, build_order_intent, build_trade_decisions
from aitrader.config import load_config
from aitrader.models import Signal


def test_build_order_intent_respects_budget_and_dry_run():
    config = load_config("config/strategy.yaml")
    signal = Signal(
        symbol="SOXL",
        side="BUY",
        score=0.8,
        price=Decimal("70"),
        timestamp=__import__("datetime").datetime.fromisoformat("2026-05-22T00:00:00+09:00"),
        reason="test",
    )

    intent = build_order_intent(signal, config=config, available_cash=Decimal("2000"))

    assert intent is not None
    assert intent.dry_run is True
    assert intent.notional <= config.risk.max_order_value
    assert intent.quantity == Decimal("25")


def test_build_order_intent_skips_kr_buy_when_budget_cannot_buy_one_share():
    config = load_config("config/strategy.yaml")
    signal = Signal(
        symbol="005930",
        side="BUY",
        score=0.8,
        price=Decimal("316000"),
        timestamp=__import__("datetime").datetime.fromisoformat("2026-07-02T00:00:00+09:00"),
        reason="test",
    )

    intent = build_order_intent(signal, config=config, available_cash=Decimal("2"))

    assert intent is None


def test_build_order_intent_rounds_kr_limit_price_to_tick():
    config = load_config("config/strategy.yaml")
    config = replace(
        config,
        risk=replace(
            config.risk,
            initial_cash=Decimal("10000000"),
            max_order_value=Decimal("1000000"),
        ),
    )
    signal = Signal(
        symbol="005930",
        side="BUY",
        score=0.8,
        price=Decimal("316000"),
        timestamp=__import__("datetime").datetime.fromisoformat("2026-07-02T00:00:00+09:00"),
        reason="test",
    )

    intent = build_order_intent(signal, config=config, available_cash=Decimal("2000000"))

    assert intent is not None
    assert intent.quantity == Decimal("3")
    assert intent.limit_price == Decimal("316500")


def test_build_order_intent_rounds_us_limit_price_to_supported_scale():
    config = load_config("config/strategy.yaml")
    signal = Signal(
        symbol="AAPL",
        side="SELL",
        score=0.8,
        price=Decimal("294.38"),
        timestamp=__import__("datetime").datetime.fromisoformat("2026-07-02T00:00:00+09:00"),
        reason="test",
    )

    intent = build_order_intent(
        signal,
        config=config,
        available_cash=Decimal("0"),
        held_quantity=Decimal("2.9"),
    )

    assert intent is not None
    assert intent.quantity == Decimal("2")
    assert intent.limit_price == Decimal("294.08")


def test_build_order_intent_allows_fractional_us_market_sell():
    config = load_config("config/strategy.yaml")
    config = replace(config, execution=replace(config.execution, order_type="MARKET"))
    signal = Signal(
        symbol="AAPL",
        side="SELL",
        score=0.8,
        price=Decimal("294.38"),
        timestamp=__import__("datetime").datetime.fromisoformat("2026-07-02T00:00:00+09:00"),
        reason="test",
    )

    intent = build_order_intent(
        signal,
        config=config,
        available_cash=Decimal("0"),
        held_quantity=Decimal("2.1234567"),
    )

    assert intent is not None
    assert intent.quantity == Decimal("2.123456")
    assert intent.limit_price is None


def test_trade_decisions_cap_soxs_at_twenty_percent_of_portfolio():
    config = load_config("config/strategy.yaml")
    signal = Signal(
        symbol="SOXS",
        side="BUY",
        score=0.8,
        price=Decimal("10"),
        timestamp=__import__("datetime").datetime.fromisoformat("2026-07-02T00:00:00+09:00"),
        reason="test",
    )

    decisions = build_trade_decisions(
        [signal],
        config=config,
        available_cash=Decimal("1000"),
        available_cash_by_symbol={"SOXS": Decimal("1000")},
        held_quantities={"SOXS": Decimal("15")},
    )

    assert decisions[0].intent is not None
    assert decisions[0].intent.notional <= Decimal("80")


def test_trade_decisions_skip_soxs_buy_when_cap_is_reached():
    config = load_config("config/strategy.yaml")
    signal = Signal(
        symbol="SOXS",
        side="BUY",
        score=0.8,
        price=Decimal("10"),
        timestamp=__import__("datetime").datetime.fromisoformat("2026-07-02T00:00:00+09:00"),
        reason="test",
    )

    decisions = build_trade_decisions(
        [signal],
        config=config,
        available_cash=Decimal("1000"),
        available_cash_by_symbol={"SOXS": Decimal("1000")},
        held_quantities={"SOXS": Decimal("25")},
    )

    assert decisions[0].intent is None
    assert decisions[0].reason == "symbol position cap reached"


def test_trade_decisions_respect_existing_orders_today():
    config = load_config("config/strategy.yaml")
    signal = Signal(
        symbol="SOXL",
        side="BUY",
        score=0.8,
        price=Decimal("10"),
        timestamp=__import__("datetime").datetime.fromisoformat("2026-07-02T00:00:00+09:00"),
        reason="test",
    )

    decisions = build_trade_decisions(
        [signal],
        config=config,
        available_cash=Decimal("1000"),
        available_cash_by_symbol={"SOXL": Decimal("1000")},
        orders_today=2,
    )

    assert decisions[0].intent is not None
    assert decisions[0].accepted is False
    assert decisions[0].reason == "daily order limit reached"


def test_trading_broker_submit_counts_existing_orders_today():
    config = load_config("config/strategy.yaml")
    signal = Signal(
        symbol="SOXL",
        side="BUY",
        score=0.8,
        price=Decimal("10"),
        timestamp=__import__("datetime").datetime.fromisoformat("2026-07-02T00:00:00+09:00"),
        reason="test",
    )
    first = build_order_intent(signal, config=config, available_cash=Decimal("1000"))
    second = build_order_intent(signal, config=config, available_cash=Decimal("1000"))

    previews = TradingBroker(None, config).submit(
        [first, second],  # type: ignore[list-item]
        orders_today=1,
    )

    assert [preview.accepted for preview in previews] == [True, False]
    assert previews[1].reason == "daily order limit reached"


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
