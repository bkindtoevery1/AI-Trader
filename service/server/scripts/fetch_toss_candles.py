from __future__ import annotations

import argparse
import csv
import os
import sqlite3
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

import requests
from dotenv import load_dotenv


ROOT_DIR = Path(__file__).resolve().parents[3]
DEFAULT_DB_PATH = ROOT_DIR / "service" / "server" / "data" / "market_data.db"
DEFAULT_EXPORT_DIR = ROOT_DIR / "service" / "server" / "data" / "exports"
TOSS_BASE_URL = os.getenv("TOSSINVEST_BASE_URL", "https://openapi.tossinvest.com").rstrip("/")


def _load_env() -> None:
    load_dotenv(ROOT_DIR / ".env")


def _require_env(name: str) -> str:
    value = os.getenv(name, "").strip()
    if not value:
        raise SystemExit(f"{name} is required in .env")
    return value


def _utc_now_iso_z() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _to_float(value: Any) -> float:
    return float(str(value))


def _date_floor(value: str) -> str:
    stripped = (value or "").strip()
    if not stripped:
        return ""
    return stripped if "T" in stripped else f"{stripped}T00:00:00"


def _date_ceiling(value: str) -> str:
    stripped = (value or "").strip()
    if not stripped:
        return ""
    return stripped if "T" in stripped else f"{stripped}T99:99:99"


def issue_token() -> str:
    client_id = _require_env("TOSSINVEST_CLIENT_ID")
    client_secret = _require_env("TOSSINVEST_CLIENT_SECRET")
    response = requests.post(
        f"{TOSS_BASE_URL}/oauth2/token",
        data={
            "grant_type": "client_credentials",
            "client_id": client_id,
            "client_secret": client_secret,
        },
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        timeout=20,
    )
    if response.status_code >= 400:
        raise SystemExit(f"Token request failed: HTTP {response.status_code} {response.text[:300]}")
    payload = response.json()
    token = payload.get("access_token")
    if not token:
        raise SystemExit("Token response did not include access_token")
    return str(token)


def init_db(db_path: Path) -> None:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    try:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS market_candles (
                provider TEXT NOT NULL,
                symbol TEXT NOT NULL,
                interval TEXT NOT NULL,
                adjusted INTEGER NOT NULL,
                timestamp TEXT NOT NULL,
                open REAL NOT NULL,
                high REAL NOT NULL,
                low REAL NOT NULL,
                close REAL NOT NULL,
                volume REAL NOT NULL,
                currency TEXT NOT NULL,
                fetched_at TEXT NOT NULL,
                PRIMARY KEY (provider, symbol, interval, adjusted, timestamp)
            )
            """
        )
        conn.execute(
            """
            CREATE INDEX IF NOT EXISTS idx_market_candles_lookup
            ON market_candles(symbol, interval, adjusted, timestamp)
            """
        )
        conn.commit()
    finally:
        conn.close()


def fetch_page(
    token: str,
    *,
    symbol: str,
    interval: str,
    count: int,
    adjusted: bool,
    before: Optional[str],
) -> dict[str, Any]:
    params: dict[str, Any] = {
        "symbol": symbol,
        "interval": interval,
        "count": count,
        "adjusted": str(adjusted).lower(),
    }
    if before:
        params["before"] = before

    response = requests.get(
        f"{TOSS_BASE_URL}/api/v1/candles",
        params=params,
        headers={"Authorization": f"Bearer {token}"},
        timeout=30,
    )
    if response.status_code == 429:
        retry_after = int(response.headers.get("Retry-After", "5"))
        time.sleep(max(1, retry_after))
        return fetch_page(
            token,
            symbol=symbol,
            interval=interval,
            count=count,
            adjusted=adjusted,
            before=before,
        )
    if response.status_code >= 400:
        raise SystemExit(f"Candle request failed: HTTP {response.status_code} {response.text[:500]}")

    payload = response.json()
    result = payload.get("result") if isinstance(payload, dict) else None
    if not isinstance(result, dict):
        raise SystemExit(f"Unexpected candle response shape: {str(payload)[:500]}")
    return result


def store_candles(
    db_path: Path,
    *,
    symbol: str,
    interval: str,
    adjusted: bool,
    candles: list[dict[str, Any]],
) -> int:
    if not candles:
        return 0
    fetched_at = _utc_now_iso_z()
    rows = [
        (
            "tossinvest",
            symbol,
            interval,
            1 if adjusted else 0,
            candle["timestamp"],
            _to_float(candle["openPrice"]),
            _to_float(candle["highPrice"]),
            _to_float(candle["lowPrice"]),
            _to_float(candle["closePrice"]),
            _to_float(candle["volume"]),
            str(candle["currency"]),
            fetched_at,
        )
        for candle in candles
    ]

    conn = sqlite3.connect(db_path)
    try:
        before = conn.total_changes
        conn.executemany(
            """
            INSERT OR REPLACE INTO market_candles
            (provider, symbol, interval, adjusted, timestamp, open, high, low, close, volume, currency, fetched_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            rows,
        )
        conn.commit()
        return conn.total_changes - before
    finally:
        conn.close()


def export_csv(
    db_path: Path,
    *,
    symbol: str,
    interval: str,
    adjusted: bool,
    csv_path: Path,
    start_date: str = "",
    end_date: str = "",
) -> int:
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    try:
        conditions = ["symbol = ?", "interval = ?", "adjusted = ?"]
        params: list[Any] = [symbol, interval, 1 if adjusted else 0]
        if start_date:
            conditions.append("timestamp >= ?")
            params.append(_date_floor(start_date))
        if end_date:
            conditions.append("timestamp <= ?")
            params.append(_date_ceiling(end_date))

        rows = conn.execute(
            f"""
            SELECT timestamp, open, high, low, close, volume, currency, provider, symbol, interval, adjusted
            FROM market_candles
            WHERE {' AND '.join(conditions)}
            ORDER BY timestamp ASC
            """,
            params,
        ).fetchall()
    finally:
        conn.close()

    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["timestamp", "open", "high", "low", "close", "volume", "currency", "provider", "symbol", "interval", "adjusted"])
        for row in rows:
            writer.writerow([row[key] for key in row.keys()])
    return len(rows)


def fetch_all(args: argparse.Namespace) -> None:
    _load_env()
    sqlite_db_path = args.db_path or os.getenv("MARKET_DATA_DB_PATH", str(DEFAULT_DB_PATH))
    db_path = Path(sqlite_db_path).expanduser().resolve()
    csv_path = Path(args.csv_path).expanduser().resolve() if args.csv_path else (
        DEFAULT_EXPORT_DIR / f"{args.symbol.lower()}_{args.interval}_{'adjusted' if args.adjusted else 'raw'}.csv"
    )

    init_db(db_path)
    token = issue_token()

    before: Optional[str] = None
    seen_before: set[str] = set()
    total_pages = 0
    total_rows = 0

    while True:
        result = fetch_page(
            token,
            symbol=args.symbol,
            interval=args.interval,
            count=args.count,
            adjusted=args.adjusted,
            before=before,
        )
        candles = result.get("candles") or []
        if not isinstance(candles, list):
            raise SystemExit("Unexpected candles field in response")

        changed = store_candles(
            db_path,
            symbol=args.symbol,
            interval=args.interval,
            adjusted=args.adjusted,
            candles=candles,
        )
        total_pages += 1
        total_rows += len(candles)
        print(
            f"page={total_pages} fetched={len(candles)} stored_or_replaced={changed} "
            f"nextBefore={result.get('nextBefore')}"
        )

        next_before = result.get("nextBefore")
        if not next_before or not candles:
            break
        if next_before in seen_before:
            raise SystemExit(f"Pagination loop detected at nextBefore={next_before}")
        seen_before.add(str(next_before))
        before = str(next_before)

        if args.max_pages and total_pages >= args.max_pages:
            break
        if args.sleep_seconds > 0:
            time.sleep(args.sleep_seconds)

    exported = export_csv(
        db_path,
        symbol=args.symbol,
        interval=args.interval,
        adjusted=args.adjusted,
        csv_path=csv_path,
        start_date=args.start_date,
        end_date=args.end_date,
    )
    print(f"done pages={total_pages} fetched_rows={total_rows} exported_rows={exported}")
    print("storage=sqlite")
    print(f"db={db_path}")
    print(f"csv={csv_path}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch Toss Invest candle history into SQLite and CSV.")
    parser.add_argument("--symbol", default="SOXL")
    parser.add_argument("--interval", choices=["1d", "1m"], default="1d")
    parser.add_argument("--count", type=int, default=200)
    parser.add_argument("--adjusted", action=argparse.BooleanOptionalAction, default=True)
    parser.add_argument("--max-pages", type=int, default=0, help="0 means fetch until nextBefore is null.")
    parser.add_argument("--sleep-seconds", type=float, default=0.2)
    parser.add_argument("--db-path", default="")
    parser.add_argument("--csv-path", default="")
    parser.add_argument("--start-date", default="", help="Limit CSV export to timestamps on/after YYYY-MM-DD.")
    parser.add_argument("--end-date", default="", help="Limit CSV export to timestamps on/before YYYY-MM-DD.")
    args = parser.parse_args()

    if args.count < 1 or args.count > 200:
        raise SystemExit("--count must be between 1 and 200")

    fetch_all(args)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted", file=sys.stderr)
        raise SystemExit(130)
