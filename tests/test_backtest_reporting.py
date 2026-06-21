import json
from datetime import datetime, timezone

from aitrader.backtest import find_improvements, run_backtest
from aitrader.broker import build_trade_decisions
from aitrader.config import load_config
from aitrader.data import load_candles_csv, write_candles_csv
from aitrader.reporting import write_dashboard_json, write_markdown_report
from aitrader.strategy import MovingAverageRsiStrategy


def test_backtest_produces_equity_curve_and_metrics():
    config = load_config("config/strategy.yaml")
    candles = load_candles_csv("data/sample_candles.csv")["AAPL"]
    result = run_backtest("AAPL", candles, config)

    assert result.symbol == "AAPL"
    assert result.final_equity > 0
    assert len(result.equity_curve) == len(candles)
    assert "shortWindow" in result.parameters


def test_improvement_finder_always_returns_recommendation():
    config = load_config("config/strategy.yaml")
    candles = load_candles_csv("data/sample_candles.csv")["005930"]

    improvements = find_improvements("005930", candles, config)

    assert improvements
    assert improvements[0].title


def test_report_writers_create_markdown_and_dashboard_json(tmp_path):
    config = load_config("config/strategy.yaml")
    candles_by_symbol = load_candles_csv("data/sample_candles.csv")
    result = run_backtest("AAPL", candles_by_symbol["AAPL"], config)
    signal = MovingAverageRsiStrategy(config.strategy).signal("AAPL", candles_by_symbol["AAPL"])
    improvements = find_improvements("AAPL", candles_by_symbol["AAPL"], config)
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
    assert payload["results"][0]["symbol"] == "AAPL"
    assert payload["decisions"][0]["symbol"] == "AAPL"
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
