from decimal import Decimal

from aitrader.account import cash_by_symbol, fetch_account_snapshot, simulated_account_snapshot
from aitrader.config import load_config


class FakeAccountClient:
    def get_holdings(self):
        return {
            "items": [
                {"symbol": "005930", "quantity": "7"},
                {"symbol": "AAPL", "quantity": "1.25"},
            ]
        }

    def get_buying_power(self, currency):
        return {"currency": currency, "cashBuyingPower": "1000" if currency == "USD" else "500000"}

    def get_sellable_quantity(self, symbol):
        return {"sellableQuantity": "3" if symbol == "005930" else "1.25"}


def test_fetch_account_snapshot_normalizes_account_values():
    config = load_config("config/strategy.yaml")

    snapshot = fetch_account_snapshot(  # type: ignore[arg-type]
        FakeAccountClient(),
        config,
        symbols=("005930", "AAPL"),
    )

    assert snapshot.source == "toss"
    assert snapshot.buying_power["KRW"] == Decimal("500000")
    assert snapshot.buying_power["USD"] == Decimal("1000")
    assert snapshot.holdings["AAPL"] == Decimal("1.25")
    assert snapshot.sellable_quantities["005930"] == Decimal("3")
    assert cash_by_symbol(snapshot, ("005930", "AAPL")) == {
        "005930": Decimal("500000"),
        "AAPL": Decimal("1000"),
    }


def test_simulated_account_snapshot_uses_config_cash():
    config = load_config("config/strategy.yaml")

    snapshot = simulated_account_snapshot(config)

    assert snapshot.source == "simulated"
    assert snapshot.buying_power[config.risk.currency] == config.risk.initial_cash

