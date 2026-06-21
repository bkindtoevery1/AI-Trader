from __future__ import annotations

import argparse
import json
import os
from datetime import datetime
from pathlib import Path

from .backtest import find_improvements, run_backtest
from .broker import TradingBroker, build_order_intent
from .config import load_config
from .data import load_candles_csv, write_candles_csv
from .models import Candle
from .reporting import write_dashboard_json, write_markdown_report
from .strategy import MovingAverageRsiStrategy
from .toss_client import TossInvestClient


def _load_config(args: argparse.Namespace):
    return load_config(args.config)


def _collect_results(config, candles_by_symbol: dict[str, list[Candle]]):
    results = []
    improvements = []
    signals = []
    strategy = MovingAverageRsiStrategy(config.strategy)
    for symbol in config.strategy.symbols:
        candles = candles_by_symbol.get(symbol)
        if not candles:
            raise SystemExit(f"No candle data found for {symbol}")
        results.append(run_backtest(symbol, candles, config))
        improvements.extend(find_improvements(symbol, candles, config)[:2])
        signals.append(strategy.signal(symbol, candles))
    return results, improvements, signals


def cmd_backtest(args: argparse.Namespace) -> int:
    config = _load_config(args)
    candles_by_symbol = load_candles_csv(args.data)
    results, improvements, signals = _collect_results(config, candles_by_symbol)
    generated_at = datetime.now().astimezone()
    if args.out:
        write_markdown_report(
            args.out,
            generated_at=generated_at,
            results=results,
            improvements=improvements,
            signals=signals,
        )
    if args.json:
        Path(args.json).parent.mkdir(parents=True, exist_ok=True)
        Path(args.json).write_text(
            json.dumps([result.to_dict() for result in results], ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
    for result in results:
        print(
            f"{result.symbol}: return={result.total_return_pct:.2f}% "
            f"mdd={result.max_drawdown_pct:.2f}% trades={len(result.trades)}"
        )
    return 0


def cmd_daily(args: argparse.Namespace) -> int:
    config = _load_config(args)
    candles_by_symbol = load_candles_csv(args.data)
    results, improvements, signals = _collect_results(config, candles_by_symbol)
    generated_at = datetime.now().astimezone()
    report_dir = Path(args.report_dir)
    report_name = f"daily-{generated_at.date().isoformat()}.md"
    write_markdown_report(
        report_dir / report_name,
        generated_at=generated_at,
        results=results,
        improvements=improvements,
        signals=signals,
    )
    write_dashboard_json(
        args.dashboard,
        generated_at=generated_at,
        results=results,
        improvements=improvements,
        signals=signals,
    )
    print(f"wrote {report_dir / report_name}")
    print(f"wrote {args.dashboard}")
    return 0


def cmd_trade(args: argparse.Namespace) -> int:
    config = _load_config(args)
    if args.live_data:
        client = _market_client_from_env(config)
        candles_by_symbol = _fetch_candles(client, config)
    else:
        candles_by_symbol = load_candles_csv(args.data)
    strategy = MovingAverageRsiStrategy(config.strategy)
    signals = [strategy.signal(symbol, candles_by_symbol[symbol]) for symbol in config.strategy.symbols]
    intents = []
    for signal in signals:
        intent = build_order_intent(
            signal,
            config=config,
            available_cash=config.risk.initial_cash,
            held_quantity=config.risk.initial_cash * 0,
            dry_run=not args.execute,
        )
        if intent is not None:
            intents.append(intent)

    client = None
    if args.execute:
        client = _client_from_env(config)
    previews = TradingBroker(client, config).submit(intents, execute=args.execute)
    print(json.dumps([preview.to_dict() for preview in previews], ensure_ascii=False, indent=2))
    return 0


def cmd_fetch_candles(args: argparse.Namespace) -> int:
    config = _load_config(args)
    symbols = tuple(args.symbols or config.strategy.symbols)
    client = _market_client_from_env(config)
    candles_by_symbol = _fetch_candles(client, config, symbols=symbols)
    write_candles_csv(args.out, candles_by_symbol)
    print(f"wrote {args.out}")
    return 0


def _fetch_candles(
    client: TossInvestClient,
    config,
    *,
    symbols: tuple[str, ...] | None = None,
) -> dict[str, list[Candle]]:
    candles_by_symbol: dict[str, list[Candle]] = {}
    for symbol in symbols or config.strategy.symbols:
        payload = client.get_candles(
            symbol,
            interval=config.strategy.interval,
            count=config.strategy.candle_count,
            adjusted=True,
        )
        rows = payload.get("candles", [])
        if not isinstance(rows, list):
            raise SystemExit(f"Unexpected candle response for {symbol}")
        candles_by_symbol[symbol] = [Candle.from_mapping(symbol, row) for row in rows]
    return candles_by_symbol


def _market_client_from_env(config) -> TossInvestClient:
    client_id = os.environ.get(config.toss.client_id_env)
    client_secret = os.environ.get(config.toss.client_secret_env)
    missing = [
        name
        for name, value in {
            config.toss.client_id_env: client_id,
            config.toss.client_secret_env: client_secret,
        }.items()
        if not value
    ]
    if missing:
        raise SystemExit(f"Missing Toss Invest environment variables: {', '.join(missing)}")
    return TossInvestClient(
        base_url=config.toss.base_url,
        client_id=str(client_id),
        client_secret=str(client_secret),
        account_seq=os.environ.get(config.toss.account_seq_env),
    )


def _client_from_env(config) -> TossInvestClient:
    client_id = os.environ.get(config.toss.client_id_env)
    client_secret = os.environ.get(config.toss.client_secret_env)
    account_seq = os.environ.get(config.toss.account_seq_env)
    missing = [
        name
        for name, value in {
            config.toss.client_id_env: client_id,
            config.toss.client_secret_env: client_secret,
            config.toss.account_seq_env: account_seq,
        }.items()
        if not value
    ]
    if missing:
        raise SystemExit(f"Missing Toss Invest environment variables: {', '.join(missing)}")
    return TossInvestClient(
        base_url=config.toss.base_url,
        client_id=str(client_id),
        client_secret=str(client_secret),
        account_seq=str(account_seq),
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="ai-trader")
    parser.add_argument("--config", default=os.environ.get("AI_TRADER_CONFIG", "config/strategy.yaml"))
    subparsers = parser.add_subparsers(dest="command", required=True)

    backtest = subparsers.add_parser("backtest")
    backtest.add_argument("--data", default="data/sample_candles.csv")
    backtest.add_argument("--out", default="reports/backtest.md")
    backtest.add_argument("--json", default="reports/backtest.json")
    backtest.set_defaults(func=cmd_backtest)

    daily = subparsers.add_parser("daily")
    daily.add_argument("--data", default="data/sample_candles.csv")
    daily.add_argument("--report-dir", default="reports")
    daily.add_argument("--dashboard", default="web/public/dashboard-data.json")
    daily.set_defaults(func=cmd_daily)

    trade = subparsers.add_parser("trade")
    trade.add_argument("--data", default="data/sample_candles.csv")
    trade.add_argument("--live-data", action="store_true")
    trade.add_argument("--execute", action="store_true")
    trade.set_defaults(func=cmd_trade)

    fetch = subparsers.add_parser("fetch-candles")
    fetch.add_argument("--symbols", nargs="*")
    fetch.add_argument("--out", default="data/live_candles.csv")
    fetch.set_defaults(func=cmd_fetch_candles)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return int(args.func(args))
