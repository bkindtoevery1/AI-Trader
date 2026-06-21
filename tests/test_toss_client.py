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

