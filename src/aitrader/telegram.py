from __future__ import annotations

import os
from dataclasses import dataclass
from decimal import Decimal
from typing import Any

import requests

from .account import AccountSnapshot
from .config import AppConfig
from .market_schedule import ReportPhase
from .models import Signal, decimal_str
from .portfolio import PortfolioEvaluation


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
    phase: ReportPhase = "daily",
    portfolio: PortfolioEvaluation | None = None,
) -> str:
    phase_title = {
        "daily": "AI 증권 분석 리포트",
        "open": "AI 증권 분석 리포트 - 미장 시작 전략",
        "close": "AI 증권 분석 리포트 - 미장 마감 성과",
    }[phase]
    lines = [
        phase_title,
        f"기준시각: {generated_at.isoformat(timespec='minutes')}",
        f"전략: {config.strategy.name}",
        f"종목: {', '.join(config.strategy.symbols)}",
        (
            "리스크: "
            f"일일 최대 {config.risk.max_daily_orders}건, "
            f"SOXS 최대 {_symbol_cap_text(config, 'SOXS')}, "
            f"실거래 {'허용' if config.risk.allow_live_trading else '차단'}"
        ),
    ]

    if portfolio is not None:
        lines.extend(_portfolio_lines(portfolio, phase=phase))

    lines.extend(["", "전략 신호" if phase != "close" else "마감 기준 전략 신호"])
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


def _portfolio_lines(portfolio: PortfolioEvaluation, *, phase: ReportPhase) -> list[str]:
    if phase == "close":
        headline = (
            f"하루 성과: {decimal_str(portfolio.total_daily_profit_loss_amount, 2)} "
            f"{portfolio.currency} "
            f"({decimal_str(portfolio.total_daily_profit_loss_rate * Decimal('100'), 2)}%)"
        )
    else:
        headline = (
            f"포트폴리오: 평가 {decimal_str(portfolio.total_market_amount, 2)} "
            f"{portfolio.currency}, 현금 "
            f"{decimal_str(portfolio.buying_power.get(portfolio.currency, Decimal('0')), 2)} "
            f"{portfolio.currency}"
        )
    lines = [
        "",
        headline,
        (
            f"총손익: {decimal_str(portfolio.total_profit_loss_amount_after_cost, 2)} "
            f"{portfolio.currency} "
            f"({decimal_str(portfolio.total_profit_loss_rate_after_cost * Decimal('100'), 2)}%)"
        ),
        f"총자산 추정: {decimal_str(portfolio.total_equity, 2)} {portfolio.currency}",
    ]
    if portfolio.positions:
        lines.append("보유 포지션")
    for position in portfolio.positions:
        lines.append(
            f"- {position.symbol}: {decimal_str(position.quantity, 6)}주 "
            f"평단 {decimal_str(position.average_purchase_price, 4)}, "
            f"현재 {decimal_str(position.last_price, 4)}, "
            f"비중 {decimal_str(position.weight_pct, 2)}%"
        )
        lines.append(
            f"  손익 {decimal_str(position.profit_loss_amount_after_cost, 2)} "
            f"({decimal_str(position.profit_loss_rate_after_cost * Decimal('100'), 2)}%), "
            f"당일 {decimal_str(position.daily_profit_loss_amount, 2)} "
            f"({decimal_str(position.daily_profit_loss_rate * Decimal('100'), 2)}%)"
        )
    if portfolio.errors:
        lines.append("포트폴리오 평가 오류")
        lines.extend(f"- {error}" for error in portfolio.errors[:3])
    return lines


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
