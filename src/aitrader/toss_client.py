from __future__ import annotations

import time
from dataclasses import dataclass
from typing import Any

import requests


class TossApiError(RuntimeError):
    def __init__(self, message: str, status_code: int | None = None, payload: dict[str, Any] | None = None) -> None:
        super().__init__(message)
        self.status_code = status_code
        self.payload = payload or {}


@dataclass
class TokenState:
    access_token: str
    expires_at: float


class TossInvestClient:
    def __init__(
        self,
        *,
        base_url: str,
        client_id: str,
        client_secret: str,
        account_seq: str | None = None,
        session: requests.Session | None = None,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.client_id = client_id
        self.client_secret = client_secret
        self.account_seq = account_seq
        self.session = session or requests.Session()
        self._token: TokenState | None = None

    def issue_token(self) -> str:
        response = self.session.post(
            f"{self.base_url}/oauth2/token",
            data={
                "grant_type": "client_credentials",
                "client_id": self.client_id,
                "client_secret": self.client_secret,
            },
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            timeout=15,
        )
        payload = _json_or_error(response)
        if response.status_code >= 400:
            raise TossApiError("Failed to issue Toss Invest access token", response.status_code, payload)
        token = payload.get("access_token")
        if not token:
            raise TossApiError("Toss token response did not contain access_token", response.status_code, payload)
        expires_in = int(payload.get("expires_in", 3600))
        self._token = TokenState(str(token), time.time() + max(60, expires_in - 30))
        return self._token.access_token

    def access_token(self) -> str:
        if self._token is None or self._token.expires_at <= time.time():
            return self.issue_token()
        return self._token.access_token

    def request(
        self,
        method: str,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        json: dict[str, Any] | None = None,
        account_required: bool = False,
        retries: int = 2,
    ) -> dict[str, Any]:
        headers = {"Authorization": f"Bearer {self.access_token()}"}
        if account_required:
            if not self.account_seq:
                raise TossApiError("X-Tossinvest-Account is required for this endpoint")
            headers["X-Tossinvest-Account"] = str(self.account_seq)

        attempt = 0
        while True:
            response = self.session.request(
                method,
                f"{self.base_url}{path}",
                params=params,
                json=json,
                headers=headers,
                timeout=20,
            )
            payload = _json_or_error(response)
            if response.status_code == 429 and attempt < retries:
                retry_after = float(response.headers.get("Retry-After", 1 + attempt))
                time.sleep(retry_after)
                attempt += 1
                continue
            if response.status_code >= 400:
                message = payload.get("error", {}).get("message", "Toss Invest API request failed")
                raise TossApiError(message, response.status_code, payload)
            return payload.get("result", payload)

    def get_prices(self, symbols: list[str]) -> dict[str, Any]:
        return self.request("GET", "/api/v1/prices", params={"symbols": ",".join(symbols)})

    def get_orderbook(self, symbol: str) -> dict[str, Any]:
        return self.request("GET", "/api/v1/orderbook", params={"symbol": symbol})

    def get_trades(self, symbol: str, *, count: int = 50) -> dict[str, Any]:
        return self.request("GET", "/api/v1/trades", params={"symbol": symbol, "count": count})

    def get_price_limits(self, symbol: str) -> dict[str, Any]:
        return self.request("GET", "/api/v1/price-limits", params={"symbol": symbol})

    def get_candles(
        self,
        symbol: str,
        *,
        interval: str = "1d",
        count: int = 100,
        before: str | None = None,
        adjusted: bool = True,
    ) -> dict[str, Any]:
        params: dict[str, Any] = {
            "symbol": symbol,
            "interval": interval,
            "count": count,
            "adjusted": str(adjusted).lower(),
        }
        if before:
            params["before"] = before
        return self.request("GET", "/api/v1/candles", params=params)

    def get_stocks(self, symbols: list[str]) -> dict[str, Any]:
        return self.request("GET", "/api/v1/stocks", params={"symbols": ",".join(symbols)})

    def get_stock_warnings(self, symbol: str) -> dict[str, Any]:
        return self.request("GET", f"/api/v1/stocks/{symbol}/warnings")

    def get_exchange_rate(
        self,
        *,
        base_currency: str,
        quote_currency: str,
        date_time: str | None = None,
    ) -> dict[str, Any]:
        params = {"baseCurrency": base_currency, "quoteCurrency": quote_currency}
        if date_time:
            params["dateTime"] = date_time
        return self.request("GET", "/api/v1/exchange-rate", params=params)

    def get_kr_market_calendar(self, date: str | None = None) -> dict[str, Any]:
        params = {"date": date} if date else None
        return self.request("GET", "/api/v1/market-calendar/KR", params=params)

    def get_us_market_calendar(self, date: str | None = None) -> dict[str, Any]:
        params = {"date": date} if date else None
        return self.request("GET", "/api/v1/market-calendar/US", params=params)

    def get_accounts(self) -> dict[str, Any]:
        return self.request("GET", "/api/v1/accounts")

    def get_holdings(self, symbol: str | None = None) -> dict[str, Any]:
        params = {"symbol": symbol} if symbol else None
        return self.request("GET", "/api/v1/holdings", params=params, account_required=True)

    def get_buying_power(self, currency: str) -> dict[str, Any]:
        return self.request(
            "GET",
            "/api/v1/buying-power",
            params={"currency": currency},
            account_required=True,
        )

    def get_sellable_quantity(self, symbol: str) -> dict[str, Any]:
        return self.request(
            "GET",
            "/api/v1/sellable-quantity",
            params={"symbol": symbol},
            account_required=True,
        )

    def get_commissions(self) -> dict[str, Any]:
        return self.request("GET", "/api/v1/commissions", account_required=True)

    def create_order(self, payload: dict[str, Any]) -> dict[str, Any]:
        return self.request("POST", "/api/v1/orders", json=payload, account_required=True)

    def modify_order(self, order_id: str, payload: dict[str, Any]) -> dict[str, Any]:
        return self.request("POST", f"/api/v1/orders/{order_id}/modify", json=payload, account_required=True)

    def cancel_order(self, order_id: str) -> dict[str, Any]:
        return self.request("POST", f"/api/v1/orders/{order_id}/cancel", json={}, account_required=True)

    def get_orders(
        self,
        *,
        status: str,
        symbol: str | None = None,
        from_date: str | None = None,
        to_date: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:
        params: dict[str, Any] = {"status": status}
        if symbol:
            params["symbol"] = symbol
        if from_date:
            params["from"] = from_date
        if to_date:
            params["to"] = to_date
        if cursor:
            params["cursor"] = cursor
        if limit is not None:
            params["limit"] = limit
        return self.request("GET", "/api/v1/orders", params=params, account_required=True)

    def get_order(self, order_id: str) -> dict[str, Any]:
        return self.request("GET", f"/api/v1/orders/{order_id}", account_required=True)


def _json_or_error(response: requests.Response) -> dict[str, Any]:
    try:
        payload = response.json()
    except ValueError as exc:
        raise TossApiError("Toss Invest API returned a non-JSON response", response.status_code) from exc
    if not isinstance(payload, dict):
        raise TossApiError("Toss Invest API returned an unexpected JSON payload", response.status_code)
    return payload
