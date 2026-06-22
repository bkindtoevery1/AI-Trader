import json

import requests

from aitrader.toss_client import TossApiError, TossInvestClient


class FakeResponse:
    def __init__(self, status_code, payload, headers=None):
        self.status_code = status_code
        self._payload = payload
        self.headers = headers or {}

    def json(self):
        return self._payload


class FakeSession:
    def __init__(self):
        self.calls = []

    def post(self, url, data=None, headers=None, timeout=None):
        self.calls.append(("POST", url, data, headers))
        return FakeResponse(200, {"access_token": "token-1", "expires_in": 3600})

    def request(self, method, url, params=None, json=None, headers=None, timeout=None):
        self.calls.append((method, url, params, headers))
        return FakeResponse(200, {"result": {"ok": True}})


def test_client_issues_token_and_sends_account_header():
    session = FakeSession()
    client = TossInvestClient(
        base_url="https://example.test",
        client_id="id",
        client_secret="secret",
        account_seq="1",
        session=session,  # type: ignore[arg-type]
    )

    result = client.get_holdings()

    assert result == {"ok": True}
    request_headers = session.calls[-1][3]
    assert request_headers["Authorization"] == "Bearer token-1"
    assert request_headers["X-Tossinvest-Account"] == "1"


def test_client_requires_account_header_before_account_endpoint_call():
    client = TossInvestClient(
        base_url="https://example.test",
        client_id="id",
        client_secret="secret",
        session=FakeSession(),  # type: ignore[arg-type]
    )

    try:
        client.get_holdings()
    except TossApiError as exc:
        assert "X-Tossinvest-Account" in str(exc)
    else:
        raise AssertionError("expected TossApiError")


def test_market_data_and_info_methods_use_expected_paths_and_params():
    session = FakeSession()
    client = TossInvestClient(
        base_url="https://example.test",
        client_id="id",
        client_secret="secret",
        session=session,  # type: ignore[arg-type]
    )

    client.get_orderbook("005930")
    assert session.calls[-1][1].endswith("/api/v1/orderbook")
    assert session.calls[-1][2] == {"symbol": "005930"}

    client.get_trades("AAPL", count=10)
    assert session.calls[-1][1].endswith("/api/v1/trades")
    assert session.calls[-1][2] == {"symbol": "AAPL", "count": 10}

    client.get_price_limits("005930")
    assert session.calls[-1][1].endswith("/api/v1/price-limits")

    client.get_stocks(["005930", "AAPL"])
    assert session.calls[-1][1].endswith("/api/v1/stocks")
    assert session.calls[-1][2] == {"symbols": "005930,AAPL"}

    client.get_stock_warnings("005930")
    assert session.calls[-1][1].endswith("/api/v1/stocks/005930/warnings")

    client.get_exchange_rate(base_currency="USD", quote_currency="KRW", date_time="2026-03-25T09:30:00+09:00")
    assert session.calls[-1][1].endswith("/api/v1/exchange-rate")
    assert session.calls[-1][2] == {
        "baseCurrency": "USD",
        "quoteCurrency": "KRW",
        "dateTime": "2026-03-25T09:30:00+09:00",
    }

    client.get_kr_market_calendar("2026-03-25")
    assert session.calls[-1][1].endswith("/api/v1/market-calendar/KR")
    assert session.calls[-1][2] == {"date": "2026-03-25"}

    client.get_us_market_calendar()
    assert session.calls[-1][1].endswith("/api/v1/market-calendar/US")
    assert session.calls[-1][2] is None


def test_order_and_account_methods_use_account_header():
    session = FakeSession()
    client = TossInvestClient(
        base_url="https://example.test",
        client_id="id",
        client_secret="secret",
        account_seq="7",
        session=session,  # type: ignore[arg-type]
    )

    client.get_commissions()
    assert session.calls[-1][1].endswith("/api/v1/commissions")
    assert session.calls[-1][3]["X-Tossinvest-Account"] == "7"

    client.get_orders(status="CLOSED", symbol="AAPL", from_date="2026-03-01", to_date="2026-03-31", limit=50)
    assert session.calls[-1][1].endswith("/api/v1/orders")
    assert session.calls[-1][2] == {
        "status": "CLOSED",
        "symbol": "AAPL",
        "from": "2026-03-01",
        "to": "2026-03-31",
        "limit": 50,
    }

    client.get_order("order-1")
    assert session.calls[-1][1].endswith("/api/v1/orders/order-1")

    client.modify_order("order-1", {"orderType": "LIMIT", "price": "71000", "quantity": "1"})
    assert session.calls[-1][0] == "POST"
    assert session.calls[-1][1].endswith("/api/v1/orders/order-1/modify")

    client.cancel_order("order-1")
    assert session.calls[-1][0] == "POST"
    assert session.calls[-1][1].endswith("/api/v1/orders/order-1/cancel")
