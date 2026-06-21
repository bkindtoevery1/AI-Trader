from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
from pathlib import Path
from typing import Any

import yaml

from .models import to_decimal


@dataclass(frozen=True)
class StrategyConfig:
    name: str
    symbols: tuple[str, ...]
    interval: str
    candle_count: int
    short_window: int
    long_window: int
    rsi_period: int
    rsi_buy_below: Decimal
    rsi_sell_above: Decimal


@dataclass(frozen=True)
class RiskConfig:
    initial_cash: Decimal
    currency: str
    max_position_pct: Decimal
    reserve_cash_pct: Decimal
    max_order_value: Decimal
    max_daily_orders: int
    fee_bps: Decimal
    slippage_bps: Decimal
    allow_live_trading: bool


@dataclass(frozen=True)
class ExecutionConfig:
    mode: str
    order_type: str
    price_offset_bps: Decimal


@dataclass(frozen=True)
class TossConfig:
    base_url: str
    client_id_env: str
    client_secret_env: str
    account_seq_env: str


@dataclass(frozen=True)
class AppConfig:
    strategy: StrategyConfig
    risk: RiskConfig
    execution: ExecutionConfig
    toss: TossConfig


def _section(data: dict[str, Any], name: str) -> dict[str, Any]:
    value = data.get(name, {})
    if not isinstance(value, dict):
        raise ValueError(f"Config section '{name}' must be an object")
    return value


def load_config(path: str | Path) -> AppConfig:
    raw = yaml.safe_load(Path(path).read_text(encoding="utf-8")) or {}
    if not isinstance(raw, dict):
        raise ValueError("Config file must contain a mapping")

    strategy = _section(raw, "strategy")
    risk = _section(raw, "risk")
    execution = _section(raw, "execution")
    toss = _section(raw, "toss")

    strategy_config = StrategyConfig(
        name=str(strategy.get("name", "ma-rsi-core")),
        symbols=tuple(str(symbol).upper() for symbol in strategy.get("symbols", [])),
        interval=str(strategy.get("interval", "1d")),
        candle_count=int(strategy.get("candle_count", 120)),
        short_window=int(strategy.get("short_window", 5)),
        long_window=int(strategy.get("long_window", 20)),
        rsi_period=int(strategy.get("rsi_period", 14)),
        rsi_buy_below=to_decimal(strategy.get("rsi_buy_below", "62")),
        rsi_sell_above=to_decimal(strategy.get("rsi_sell_above", "72")),
    )
    if not strategy_config.symbols:
        raise ValueError("At least one strategy.symbols value is required")
    if strategy_config.short_window >= strategy_config.long_window:
        raise ValueError("strategy.short_window must be lower than strategy.long_window")

    risk_config = RiskConfig(
        initial_cash=to_decimal(risk.get("initial_cash", "10000000")),
        currency=str(risk.get("currency", "KRW")).upper(),
        max_position_pct=to_decimal(risk.get("max_position_pct", "0.30")),
        reserve_cash_pct=to_decimal(risk.get("reserve_cash_pct", "0.15")),
        max_order_value=to_decimal(risk.get("max_order_value", "1000000")),
        max_daily_orders=int(risk.get("max_daily_orders", 3)),
        fee_bps=to_decimal(risk.get("fee_bps", "1.5")),
        slippage_bps=to_decimal(risk.get("slippage_bps", "5")),
        allow_live_trading=bool(risk.get("allow_live_trading", False)),
    )
    for name, value in {
        "max_position_pct": risk_config.max_position_pct,
        "reserve_cash_pct": risk_config.reserve_cash_pct,
    }.items():
        if value < 0 or value >= 1:
            raise ValueError(f"risk.{name} must be in [0, 1)")

    execution_config = ExecutionConfig(
        mode=str(execution.get("mode", "dry-run")),
        order_type=str(execution.get("order_type", "LIMIT")).upper(),
        price_offset_bps=to_decimal(execution.get("price_offset_bps", "10")),
    )
    if execution_config.mode not in {"dry-run", "live"}:
        raise ValueError("execution.mode must be 'dry-run' or 'live'")
    if execution_config.order_type not in {"LIMIT", "MARKET"}:
        raise ValueError("execution.order_type must be LIMIT or MARKET")

    toss_config = TossConfig(
        base_url=str(toss.get("base_url", "https://openapi.tossinvest.com")).rstrip("/"),
        client_id_env=str(toss.get("client_id_env", "TOSSINVEST_CLIENT_ID")),
        client_secret_env=str(toss.get("client_secret_env", "TOSSINVEST_CLIENT_SECRET")),
        account_seq_env=str(toss.get("account_seq_env", "TOSSINVEST_ACCOUNT_SEQ")),
    )
    return AppConfig(strategy_config, risk_config, execution_config, toss_config)

