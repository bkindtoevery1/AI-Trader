from decimal import Decimal

from aitrader.config import load_config
from aitrader.data import load_candles_csv
from aitrader.indicators import rsi, sma
from aitrader.strategy import DipSellPeakStrategy, MovingAverageRsiStrategy, build_strategy_variants


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


def test_dip_sell_peak_strategy_buys_dip_and_sells_peak():
    config = load_config("config/strategy.yaml")
    strategy = build_strategy_variants(config.strategy)[0]

    assert isinstance(strategy, DipSellPeakStrategy)

    buy_signal = strategy.signal(
        "SOXL",
        [
            _candle("SOXL", "2026-07-01", "100"),
            _candle("SOXL", "2026-07-02", "99.98"),
        ],
    )
    sell_signal = strategy.signal(
        "SOXL",
        [
            _candle("SOXL", "2026-07-01", "100"),
            _candle("SOXL", "2026-07-02", "100.02"),
        ],
    )

    assert buy_signal.side == "BUY"
    assert "buy dip" in buy_signal.reason
    assert sell_signal.side == "SELL"
    assert "sell peak" in sell_signal.reason


def _candle(symbol: str, date: str, close: str):
    return __import__("aitrader.models").models.Candle(
        symbol=symbol,
        timestamp=__import__("datetime").datetime.fromisoformat(f"{date}T00:00:00+09:00"),
        open=Decimal(close),
        high=Decimal(close),
        low=Decimal(close),
        close=Decimal(close),
        volume=Decimal("1000"),
        currency="USD",
    )
