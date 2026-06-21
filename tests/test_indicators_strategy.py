from decimal import Decimal

from aitrader.config import load_config
from aitrader.data import load_candles_csv
from aitrader.indicators import rsi, sma
from aitrader.strategy import MovingAverageRsiStrategy


def test_sma_returns_latest_window_average():
    assert sma([Decimal("1"), Decimal("2"), Decimal("3")], 2) == Decimal("2.5")


def test_rsi_handles_all_gains():
    values = [Decimal(index) for index in range(1, 20)]
    assert rsi(values, 14) == Decimal("100")


def test_strategy_returns_actionable_signal_after_warmup():
    config = load_config("config/strategy.yaml")
    candles = load_candles_csv("data/sample_candles.csv")["005930"]
    signal = MovingAverageRsiStrategy(config.strategy).signal("005930", candles)

    assert signal.symbol == "005930"
    assert signal.side in {"BUY", "SELL", "HOLD"}
    assert signal.price > 0
    assert signal.reason

