import json
from datetime import datetime, timezone
from decimal import Decimal

from aitrader.backtest import find_improvements, run_backtest, run_strategy_suite
from aitrader.broker import build_trade_decisions
from aitrader.config import load_config
from aitrader.data import drop_today_candles, load_candles_csv, write_candles_csv
from aitrader.models import Candle
from aitrader.reporting import write_dashboard_json, write_markdown_report
from aitrader.strategy import DipSellPeakStrategy, MovingAverageRsiStrategy, build_strategy_variants


def test_backtest_produces_equity_curve_and_metrics():
    config = load_config("config/strategy.yaml")
    candles = load_candles_csv("data/sample_candles.csv")["AAPL"]
    result = run_backtest("AAPL", candles, config)

    assert result.symbol == "AAPL"
    assert result.final_equity > 0
    assert len(result.equity_curve) == len(candles)
    assert len(result.drawdown_curve) == len(candles)
    assert "shortWindow" in result.parameters
    assert "cagrPct" in result.metrics


def test_strategy_suite_runs_configured_variants():
    config = load_config("config/strategy.yaml")
    candles = load_candles_csv("data/sample_candles.csv")["AAPL"]

    results = run_strategy_suite("AAPL", candles, config)

    assert len(results) == len(config.strategy.variants)
    assert {result.strategy_name for result in results}


def test_soxl_config_uses_buy_dip_sell_peak_profiles():
    config = load_config("config/soxl-soxs.yaml")
    strategies = build_strategy_variants(config.strategy)

    assert [strategy.name for strategy in strategies] == ["bdsp-pro1", "bdsp-pro2", "bdsp-pro3"]
    assert all(isinstance(strategy, DipSellPeakStrategy) for strategy in strategies)
    assert strategies[1].sell_threshold == Decimal("0.015")


def test_buy_dip_sell_peak_backtest_runs_tier_cycle():
    config = load_config("config/soxl-soxs.yaml")
    strategy = build_strategy_variants(config.strategy)[0]
    candles = [
        _candle("SOXL", 1, "100"),
        _candle("SOXL", 2, "99.98"),
        _candle("SOXL", 3, "100.01"),
    ]

    result = run_backtest("SOXL", candles, config, strategy)

    assert result.strategy_name == "bdsp-pro1"
    assert [trade.side for trade in result.trades] == ["BUY", "SELL"]
    assert result.trades[0].quantity == Decimal("5000")
    assert result.final_equity > result.initial_cash
    assert result.metrics["completedCycles"] == 1
    assert result.parameters["sourceLogic"] == "buy-dip-sell-peak"


def test_improvement_finder_always_returns_recommendation():
    config = load_config("config/strategy.yaml")
    candles = load_candles_csv("data/sample_candles.csv")["005930"]

    improvements = find_improvements("005930", candles, config)

    assert improvements
    assert improvements[0].title


def test_report_writers_create_markdown_and_dashboard_json(tmp_path):
    config = load_config("config/strategy.yaml")
    candles_by_symbol = load_candles_csv("data/sample_candles.csv")
    strategy = build_strategy_variants(config.strategy)[0]
    result = run_backtest("SOXL", candles_by_symbol["SOXL"], config, strategy)
    signal = strategy.signal("SOXL", candles_by_symbol["SOXL"])
    improvements = find_improvements("SOXL", candles_by_symbol["SOXL"], config)
    decisions = build_trade_decisions([signal], config=config, available_cash=config.risk.initial_cash)
    generated_at = datetime.now(timezone.utc)
    md_path = tmp_path / "daily.md"
    json_path = tmp_path / "dashboard.json"

    write_markdown_report(
        md_path,
        generated_at=generated_at,
        results=[result],
        improvements=improvements,
        signals=[signal],
        decisions=decisions,
    )
    write_dashboard_json(
        json_path,
        generated_at=generated_at,
        results=[result],
        improvements=improvements,
        signals=[signal],
        decisions=decisions,
        config=config,
    )

    assert "Backtest Summary" in md_path.read_text(encoding="utf-8")
    payload = json.loads(json_path.read_text(encoding="utf-8"))
    assert payload["results"][0]["symbol"] == "SOXL"
    assert payload["results"][0]["strategyName"]
    assert payload["results"][0]["drawdownCurve"]
    assert "cagrPct" in payload["results"][0]["metrics"]
    assert payload["decisions"][0]["symbol"] == "SOXL"
    assert payload["strategyPlans"][0]["symbol"] == "SOXL"
    assert payload["strategyPlans"][0]["action"] in {"BUY", "SELL", "HOLD"}
    assert "buyLimit" in payload["strategyPlans"][0]
    assert "sellTrigger" in payload["strategyPlans"][0]
    assert payload["risk"]["allowLiveTrading"] is False
    assert payload["account"]["source"] == "simulated"


def test_candle_csv_round_trip(tmp_path):
    candles_by_symbol = load_candles_csv("data/sample_candles.csv")
    out = tmp_path / "candles.csv"

    write_candles_csv(out, {"AAPL": candles_by_symbol["AAPL"][:3]})
    reloaded = load_candles_csv(out)

    assert list(reloaded) == ["AAPL"]
    assert len(reloaded["AAPL"]) == 3
    assert reloaded["AAPL"][0].close == candles_by_symbol["AAPL"][0].close


def test_drop_today_candles_uses_previous_completed_date_only():
    candles_by_symbol = {
        "SOXL": [
            _candle("SOXL", 22, "300.77"),
            _candle("SOXL", 23, "249.34"),
        ]
    }

    filtered = drop_today_candles(candles_by_symbol, today=datetime(2024, 1, 23).date())

    assert [candle.timestamp.day for candle in filtered["SOXL"]] == [22]


def _candle(symbol: str, day: int, close: str) -> Candle:
    price = Decimal(close)
    return Candle(
        symbol=symbol,
        timestamp=datetime(2024, 1, day, tzinfo=timezone.utc),
        open=price,
        high=price,
        low=price,
        close=price,
        volume=Decimal("1000"),
        currency="USD",
    )
