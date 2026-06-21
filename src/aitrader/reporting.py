from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path

from .models import BacktestResult, Improvement, Signal, decimal_str


def write_markdown_report(
    path: str | Path,
    *,
    generated_at: datetime,
    results: list[BacktestResult],
    improvements: list[Improvement],
    signals: list[Signal],
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
    }
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
