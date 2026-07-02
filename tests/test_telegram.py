from datetime import datetime, timezone
from decimal import Decimal

from aitrader.account import AccountSnapshot
from aitrader.broker import build_trade_decisions
from aitrader.config import load_config
from aitrader.models import Signal
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
    )

    assert "AI 증권 분석 리포트" in digest
    assert "일일 최대 2건" in digest
    assert "SOXS 최대 20%" in digest
    assert "symbol position cap reached" in digest
