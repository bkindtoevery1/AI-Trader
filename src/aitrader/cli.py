from __future__ import annotations

import argparse
import json
import os
from datetime import datetime
from pathlib import Path

from .account import cash_by_symbol, fetch_account_snapshot, simulated_account_snapshot
from .backtest import find_improvements, run_backtest
from .broker import TradingBroker, build_trade_decisions
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
    client = None
    if args.account_snapshot:
        client = _client_from_env(config)
    elif args.live_data:
        client = _market_client_from_env(config)

    if args.live_data:
        if client is None:
            client = _market_client_from_env(config)
        candles_by_symbol = _fetch_candles(client, config)
        if args.save_data:
            write_candles_csv(args.save_data, candles_by_symbol)
    else:
        candles_by_symbol = load_candles_csv(args.data)

    results, improvements, signals = _collect_results(config, candles_by_symbol)
    account = (
        fetch_account_snapshot(client, config, symbols=config.strategy.symbols)
        if args.account_snapshot and client is not None
        else simulated_account_snapshot(config)
    )
    decisions = build_trade_decisions(
        signals,
        config=config,
        available_cash=account.buying_power.get(config.risk.currency, config.risk.initial_cash),
        available_cash_by_symbol=cash_by_symbol(account, config.strategy.symbols),
        held_quantities=account.sellable_quantities or account.holdings,
        dry_run=True,
    )
    generated_at = datetime.now().astimezone()
    report_dir = Path(args.report_dir)
    report_name = f"daily-{generated_at.date().isoformat()}.md"
    write_markdown_report(
        report_dir / report_name,
        generated_at=generated_at,
        results=results,
        improvements=improvements,
        signals=signals,
        decisions=decisions,
        account=account,
    )
    write_dashboard_json(
        args.dashboard,
        generated_at=generated_at,
        results=results,
        improvements=improvements,
        signals=signals,
        decisions=decisions,
        config=config,
        account=account,
    )
    print(f"wrote {report_dir / report_name}")
    print(f"wrote {args.dashboard}")
    return 0


def cmd_trade(args: argparse.Namespace) -> int:
    config = _load_config(args)
    account = simulated_account_snapshot(config)
    account_client = None
    if args.account_snapshot or args.execute:
        account_client = _client_from_env(config)
        account = fetch_account_snapshot(account_client, config, symbols=config.strategy.symbols)

    if args.live_data:
        market_client = account_client or _market_client_from_env(config)
        candles_by_symbol = _fetch_candles(market_client, config)
    else:
        candles_by_symbol = load_candles_csv(args.data)
    strategy = MovingAverageRsiStrategy(config.strategy)
    signals = [strategy.signal(symbol, candles_by_symbol[symbol]) for symbol in config.strategy.symbols]
    decisions = build_trade_decisions(
        signals,
        config=config,
        available_cash=account.buying_power.get(config.risk.currency, config.risk.initial_cash),
        available_cash_by_symbol=cash_by_symbol(account, config.strategy.symbols),
        held_quantities=account.sellable_quantities or account.holdings,
        dry_run=not args.execute,
    )
    intents = [decision.intent for decision in decisions if decision.accepted and decision.intent is not None]

    client = None
    if args.execute:
        client = account_client or _client_from_env(config)
    previews = TradingBroker(client, config).submit(intents, execute=args.execute)
    print(
        json.dumps(
            {
                "decisions": [decision.to_dict() for decision in decisions],
                "submissions": [preview.to_dict() for preview in previews],
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


def cmd_account(args: argparse.Namespace) -> int:
    config = _load_config(args)
    client = _client_from_env(config)
    snapshot = fetch_account_snapshot(client, config, symbols=tuple(args.symbols or config.strategy.symbols))
    print(json.dumps(snapshot.to_dict(), ensure_ascii=False, indent=2))
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
    daily.add_argument("--live-data", action="store_true")
    daily.add_argument("--account-snapshot", action="store_true")
    daily.add_argument("--save-data")
    daily.add_argument("--report-dir", default="reports")
    daily.add_argument("--dashboard", default="web/public/dashboard-data.json")
    daily.set_defaults(func=cmd_daily)

    trade = subparsers.add_parser("trade")
    trade.add_argument("--data", default="data/sample_candles.csv")
    trade.add_argument("--live-data", action="store_true")
    trade.add_argument("--account-snapshot", action="store_true")
    trade.add_argument("--execute", action="store_true")
    trade.set_defaults(func=cmd_trade)

    account = subparsers.add_parser("account")
    account.add_argument("--symbols", nargs="*")
    account.set_defaults(func=cmd_account)

    fetch = subparsers.add_parser("fetch-candles")
    fetch.add_argument("--symbols", nargs="*")
    fetch.add_argument("--out", default="data/live_candles.csv")
    fetch.set_defaults(func=cmd_fetch_candles)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return int(args.func(args))
