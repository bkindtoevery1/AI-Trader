from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path

from .account import AccountSnapshot, simulated_account_snapshot
from .broker import TradeDecision
from .config import AppConfig
from .models import BacktestResult, Improvement, Signal, decimal_str


def write_markdown_report(
    path: str | Path,
    *,
    generated_at: datetime,
    results: list[BacktestResult],
    improvements: list[Improvement],
    signals: list[Signal],
    decisions: list[TradeDecision] | None = None,
    account: AccountSnapshot | None = None,
) -> None:
    lines = [
        "# AI Trader Daily Report",
        "",
        f"- Generated at: `{generated_at.isoformat()}`",
        f"- Symbols: `{', '.join(result.symbol for result in results)}`",
        "",
        "## Backtest Summary",
        "",
        "| Symbol | Return | Max DD | Sharpe | Trades |",
        "|---|---:|---:|---:|---:|",
    ]
    for result in results:
        lines.append(
            f"| {result.symbol} | {result.total_return_pct:.2f}% | "
            f"{result.max_drawdown_pct:.2f}% | {result.sharpe:.2f} | {len(result.trades)} |"
        )

    lines.extend(["", "## Latest Signals", "", "| Symbol | Side | Score | Reason |", "|---|---:|---:|---|"])
    for signal in signals:
        lines.append(f"| {signal.symbol} | {signal.side} | {signal.score:.2f} | {signal.reason} |")

    if decisions is not None:
        lines.extend(
            [
                "",
                "## Order Preview",
                "",
                "| Symbol | Signal | Action | Quantity | Notional | Accepted | Reason |",
                "|---|---:|---:|---:|---:|---:|---|",
            ]
        )
        for decision in decisions:
            payload = decision.to_dict()
            lines.append(
                f"| {payload['symbol']} | {payload['signal']} | {payload['action']} | "
                f"{payload['quantity']} | {payload['notional']} | {payload['accepted']} | {payload['reason']} |"
            )

    if account is not None:
        lines.extend(["", "## Account Snapshot", ""])
        lines.append(f"- Source: `{account.source}`")
        lines.append(
            "- Buying power: "
            + ", ".join(f"{currency} {value}" for currency, value in account.to_dict()["buyingPower"].items())
        )
        lines.append(
            "- Holdings: "
            + (", ".join(f"{symbol} {qty}" for symbol, qty in account.to_dict()["holdings"].items()) or "none")
        )

    lines.extend(["", "## Improvement Candidates", ""])
    for item in improvements:
        lines.append(f"- **{item.title}**: {item.rationale} (`delta={item.expected_delta_pct:.2f}%p`)")

    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_dashboard_json(
    path: str | Path,
    *,
    generated_at: datetime,
    results: list[BacktestResult],
    improvements: list[Improvement],
    signals: list[Signal],
    decisions: list[TradeDecision] | None = None,
    config: AppConfig | None = None,
    account: AccountSnapshot | None = None,
) -> None:
    best_result = max(results, key=lambda item: item.total_return_pct)
    payload = {
        "generatedAt": generated_at.isoformat(),
        "mode": "dry-run",
        "status": "ready",
        "summary": {
            "symbols": [result.symbol for result in results],
            "bestSymbol": best_result.symbol,
            "bestReturnPct": decimal_str(best_result.total_return_pct, 4),
            "tradeCount": sum(len(result.trades) for result in results),
            "maxDrawdownPct": decimal_str(max(result.max_drawdown_pct for result in results), 4),
        },
        "results": [result.to_dict() for result in results],
        "signals": [
            {
                "symbol": signal.symbol,
                "side": signal.side,
                "score": signal.score,
                "price": str(signal.price),
                "timestamp": signal.timestamp.isoformat(),
                "reason": signal.reason,
            }
            for signal in signals
        ],
        "improvements": [item.to_dict() for item in improvements],
        "decisions": [item.to_dict() for item in decisions or []],
    }
    if config is not None:
        account = account or simulated_account_snapshot(config)
        payload["strategy"] = {
            "name": config.strategy.name,
            "symbols": list(config.strategy.symbols),
            "interval": config.strategy.interval,
            "candleCount": config.strategy.candle_count,
            "shortWindow": config.strategy.short_window,
            "longWindow": config.strategy.long_window,
            "rsiPeriod": config.strategy.rsi_period,
            "rsiBuyBelow": decimal_str(config.strategy.rsi_buy_below, 2),
            "rsiSellAbove": decimal_str(config.strategy.rsi_sell_above, 2),
        }
        payload["risk"] = {
            "initialCash": decimal_str(config.risk.initial_cash, 2),
            "currency": config.risk.currency,
            "maxPositionPct": decimal_str(config.risk.max_position_pct * 100, 2),
            "reserveCashPct": decimal_str(config.risk.reserve_cash_pct * 100, 2),
            "maxOrderValue": decimal_str(config.risk.max_order_value, 2),
            "maxDailyOrders": config.risk.max_daily_orders,
            "feeBps": decimal_str(config.risk.fee_bps, 2),
            "slippageBps": decimal_str(config.risk.slippage_bps, 2),
            "allowLiveTrading": config.risk.allow_live_trading,
        }
        payload["execution"] = {
            "mode": config.execution.mode,
            "orderType": config.execution.order_type,
            "priceOffsetBps": decimal_str(config.execution.price_offset_bps, 2),
        }
        payload["account"] = account.to_dict()
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
