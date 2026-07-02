from __future__ import annotations

import os
from dataclasses import dataclass
from decimal import Decimal
from typing import Any

import requests

from .account import AccountSnapshot
from .config import AppConfig
from .models import Signal, decimal_str


class TelegramError(RuntimeError):
    pass


@dataclass(frozen=True)
class TelegramConfig:
    bot_token: str
    chat_id: str

    @classmethod
    def from_env(cls) -> "TelegramConfig | None":
        token = os.environ.get("TELEGRAM_BOT_TOKEN") or os.environ.get("ELC_TELEGRAM_BOT_TOKEN")
        chat_id = os.environ.get("TELEGRAM_CHAT_ID") or os.environ.get("ELC_TELEGRAM_CHAT_ID")
        if not token or not chat_id:
            return None
        return cls(bot_token=token, chat_id=chat_id)


def send_telegram_message(config: TelegramConfig, text: str) -> dict[str, Any]:
    response = requests.post(
        f"https://api.telegram.org/bot{config.bot_token}/sendMessage",
        json={
            "chat_id": config.chat_id,
            "text": text[:4096],
            "disable_web_page_preview": True,
        },
        timeout=15,
    )
    payload = _json_payload(response)
    if response.status_code >= 400 or payload.get("ok") is not True:
        description = payload.get("description", "Telegram sendMessage failed")
        raise TelegramError(str(description))
    return payload


def build_strategy_digest(
    *,
    generated_at,
    config: AppConfig,
    signals: list[Signal],
    decisions: list[Any],
    account: AccountSnapshot,
) -> str:
    lines = [
        "AI 증권 분석 리포트",
        f"기준시각: {generated_at.isoformat(timespec='minutes')}",
        f"전략: {config.strategy.name}",
        f"종목: {', '.join(config.strategy.symbols)}",
        (
            "리스크: "
            f"일일 최대 {config.risk.max_daily_orders}건, "
            f"SOXS 최대 {_symbol_cap_text(config, 'SOXS')}, "
            f"실거래 {'허용' if config.risk.allow_live_trading else '차단'}"
        ),
        "",
        "신호",
    ]
    for signal in signals:
        lines.append(
            f"- {signal.symbol}: {signal.side} @ {decimal_str(signal.price, 4)} "
            f"(score {signal.score:.2f})"
        )
        lines.append(f"  {signal.reason}")

    lines.append("")
    lines.append("주문 후보")
    if decisions:
        for decision in decisions:
            payload = decision.to_dict()
            lines.append(
                f"- {payload['symbol']}: {payload['action']} "
                f"qty {payload['quantity']} notional {payload['notional']} "
                f"=> {payload['reason']}"
            )
    else:
        lines.append("- 없음")

    if account.buying_power:
        cash = ", ".join(
            f"{currency} {decimal_str(value, 2)}"
            for currency, value in sorted(account.buying_power.items())
        )
        lines.append("")
        lines.append(f"매수가능금액: {cash}")
    if account.errors:
        lines.append("")
        lines.append("계좌 조회 오류")
        lines.extend(f"- {error}" for error in account.errors[:3])
    return "\n".join(lines)


def _symbol_cap_text(config: AppConfig, symbol: str) -> str:
    cap = config.risk.symbol_position_caps.get(symbol)
    if cap is None:
        return "없음"
    return f"{decimal_str(cap * Decimal('100'), 2)}%"


def _json_payload(response: requests.Response) -> dict[str, Any]:
    try:
        payload = response.json()
    except ValueError as exc:
        raise TelegramError("Telegram returned a non-JSON response") from exc
    if not isinstance(payload, dict):
        raise TelegramError("Telegram returned an unexpected payload")
    return payload
