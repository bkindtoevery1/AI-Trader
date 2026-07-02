from datetime import datetime, timezone
from decimal import Decimal

from aitrader.account import AccountSnapshot
from aitrader.broker import build_trade_decisions
from aitrader.config import load_config
from aitrader.models import Signal
from aitrader.portfolio import PortfolioEvaluation, PositionEvaluation
from aitrader.telegram import TelegramConfig, build_strategy_digest


def test_telegram_config_reads_generic_or_elc_env(monkeypatch):
    monkeypatch.delenv("TELEGRAM_BOT_TOKEN", raising=False)
    monkeypatch.delenv("TELEGRAM_CHAT_ID", raising=False)
    monkeypatch.setenv("ELC_TELEGRAM_BOT_TOKEN", "token")
    monkeypatch.setenv("ELC_TELEGRAM_CHAT_ID", "chat")

    config = TelegramConfig.from_env()

    assert config is not None
    assert config.bot_token == "token"
    assert config.chat_id == "chat"


def test_strategy_digest_includes_daily_limit_and_soxs_cap():
    config = load_config("config/strategy.yaml")
    signal = Signal(
        symbol="SOXS",
        side="BUY",
        score=0.7,
        price=Decimal("10"),
        timestamp=datetime(2026, 7, 2, tzinfo=timezone.utc),
        reason="dip",
    )
    decisions = build_trade_decisions(
        [signal],
        config=config,
        available_cash=Decimal("1000"),
        available_cash_by_symbol={"SOXS": Decimal("1000")},
        held_quantities={"SOXS": Decimal("25")},
    )
    account = AccountSnapshot(
        generated_at=datetime(2026, 7, 2, tzinfo=timezone.utc),
        buying_power={"USD": Decimal("1000")},
        holdings={},
        sellable_quantities={},
        source="test",
    )

    digest = build_strategy_digest(
        generated_at=datetime(2026, 7, 2, tzinfo=timezone.utc),
        config=config,
        signals=[signal],
        decisions=decisions,
        account=account,
        phase="close",
        portfolio=PortfolioEvaluation(
            generated_at=datetime(2026, 7, 2, tzinfo=timezone.utc),
            positions=(
                PositionEvaluation(
                    symbol="SOXL",
                    name="SOXL",
                    quantity=Decimal("1"),
                    sellable_quantity=Decimal("1"),
                    average_purchase_price=Decimal("248.598"),
                    last_price=Decimal("225"),
                    purchase_amount=Decimal("248.598"),
                    market_amount=Decimal("225"),
                    market_amount_after_cost=Decimal("224.54"),
                    profit_loss_amount=Decimal("-23.598"),
                    profit_loss_amount_after_cost=Decimal("-24.058"),
                    profit_loss_rate=Decimal("-0.0949"),
                    profit_loss_rate_after_cost=Decimal("-0.0967"),
                    daily_profit_loss_amount=Decimal("7.45"),
                    daily_profit_loss_rate=Decimal("0.0299"),
                    currency="USD",
                    weight_pct=Decimal("18.34"),
                ),
            ),
            buying_power={"USD": Decimal("1000")},
            total_purchase_amount=Decimal("248.598"),
            total_market_amount=Decimal("225"),
            total_market_amount_after_cost=Decimal("224.54"),
            total_profit_loss_amount=Decimal("-23.598"),
            total_profit_loss_amount_after_cost=Decimal("-24.058"),
            total_profit_loss_rate=Decimal("-0.0949"),
            total_profit_loss_rate_after_cost=Decimal("-0.0967"),
            total_daily_profit_loss_amount=Decimal("7.45"),
            total_daily_profit_loss_rate=Decimal("0.0342"),
            total_equity=Decimal("1225"),
            currency="USD",
        ),
    )

    assert "AI 증권 분석 리포트 - 미장 마감 성과" in digest
    assert "일일 최대 2건" in digest
    assert "SOXS 최대 20%" in digest
    assert "하루 성과: 7.45 USD" in digest
    assert "SOXL: 1주 평단 248.598" in digest
    assert "symbol position cap reached" in digest
