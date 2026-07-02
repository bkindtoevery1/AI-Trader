from datetime import datetime
from decimal import Decimal

from aitrader.account import AccountSnapshot
from aitrader.config import load_config
from aitrader.portfolio import fetch_portfolio_evaluation


class FakePortfolioClient:
    def get_holdings(self):
        return {
            "items": [
                {
                    "symbol": "SOXL",
                    "name": "SOXL",
                    "quantity": "1",
                    "averagePurchasePrice": "248.598",
                    "lastPrice": "225",
                    "marketValue": {
                        "purchaseAmount": "248.598",
                        "amount": "225",
                        "amountAfterCost": "224.54",
                    },
                    "profitLoss": {
                        "amount": "-23.598",
                        "amountAfterCost": "-24.058",
                        "rate": "-0.0949",
                        "rateAfterCost": "-0.0967",
                    },
                    "dailyProfitLoss": {
                        "amount": "7.45",
                        "rate": "0.0299",
                    },
                    "currency": "USD",
                }
            ]
        }


def test_fetch_portfolio_evaluation_aggregates_holding_metrics():
    config = load_config("config/strategy.yaml")
    account = AccountSnapshot(
        generated_at=datetime.now().astimezone(),
        buying_power={"USD": Decimal("1002.08")},
        holdings={"SOXL": Decimal("1")},
        sellable_quantities={"SOXL": Decimal("1")},
        source="test",
    )

    portfolio = fetch_portfolio_evaluation(  # type: ignore[arg-type]
        FakePortfolioClient(),
        config,
        account,
    )

    assert portfolio.total_market_amount == Decimal("225")
    assert portfolio.total_equity == Decimal("1227.08")
    assert portfolio.total_daily_profit_loss_amount == Decimal("7.45")
    assert portfolio.positions[0].average_purchase_price == Decimal("248.598")
    assert portfolio.positions[0].sellable_quantity == Decimal("1")
