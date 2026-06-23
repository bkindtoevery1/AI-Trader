from __future__ import annotations

import argparse
import math
import sqlite3
from dataclasses import dataclass
from pathlib import Path
from statistics import median
from typing import Optional


ROOT_DIR = Path(__file__).resolve().parents[3]
DEFAULT_DB_PATH = ROOT_DIR / "service" / "server" / "data" / "market_data.db"


@dataclass(frozen=True)
class Candle:
    date: str
    close: float
    volume: float


@dataclass(frozen=True)
class Match:
    distance: float
    similarity: float
    end_index: int
    start_date: str
    end_date: str
    path_return: float
    future_end_date: str
    future_return: float


def load_candles(db_path: Path, symbol: str) -> list[Candle]:
    conn = sqlite3.connect(db_path)
    try:
        rows = conn.execute(
            """
            SELECT substr(timestamp, 1, 10) AS date, close, volume
            FROM market_candles
            WHERE symbol = ? AND interval = '1d' AND adjusted = 1
            ORDER BY timestamp ASC
            """,
            (symbol,),
        ).fetchall()
    finally:
        conn.close()
    return [Candle(date=row[0], close=float(row[1]), volume=float(row[2])) for row in rows]


def find_as_of_index(candles: list[Candle], as_of: Optional[str]) -> int:
    if not candles:
        raise SystemExit("No candles found")
    if not as_of:
        return len(candles) - 1

    candidate = -1
    for idx, candle in enumerate(candles):
        if candle.date <= as_of:
            candidate = idx
        else:
            break
    if candidate < 0:
        raise SystemExit(f"No candle on or before {as_of}")
    return candidate


def log_returns(candles: list[Candle], start: int, end: int) -> list[float]:
    return [
        math.log(candles[idx].close / candles[idx - 1].close)
        for idx in range(start + 1, end + 1)
    ]


def zscore(values: list[float]) -> list[float]:
    mean = sum(values) / len(values)
    variance = sum((value - mean) ** 2 for value in values) / max(1, len(values) - 1)
    std = math.sqrt(variance)
    if std == 0:
        return [0.0 for _ in values]
    return [(value - mean) / std for value in values]


def cosine_distance(a: list[float], b: list[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(y * y for y in b))
    if norm_a == 0 or norm_b == 0:
        return 1.0
    corr = dot / (norm_a * norm_b)
    return 1.0 - max(-1.0, min(1.0, corr))


def euclidean(values_a: list[float], values_b: list[float]) -> float:
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(values_a, values_b)) / len(values_a))


def realized_vol(returns: list[float]) -> float:
    if len(returns) < 2:
        return 0.0
    mean = sum(returns) / len(returns)
    return math.sqrt(sum((value - mean) ** 2 for value in returns) / (len(returns) - 1))


def max_drawdown(candles: list[Candle], start: int, end: int) -> float:
    peak = candles[start].close
    worst = 0.0
    for idx in range(start, end + 1):
        peak = max(peak, candles[idx].close)
        drawdown = candles[idx].close / peak - 1.0
        worst = min(worst, drawdown)
    return worst


def path_return(candles: list[Candle], start: int, end: int) -> float:
    return candles[end].close / candles[start].close - 1.0


def volume_z(candles: list[Candle], start: int, end: int) -> float:
    vols = [math.log(max(1.0, candles[idx].volume)) for idx in range(start, end + 1)]
    if len(vols) < 2:
        return 0.0
    mean = sum(vols) / len(vols)
    std = math.sqrt(sum((value - mean) ** 2 for value in vols) / (len(vols) - 1))
    if std == 0:
        return 0.0
    return (vols[-1] - mean) / std


def regime_vector(candles: list[Candle], start: int, end: int, returns: list[float]) -> list[float]:
    return [
        path_return(candles, start, end),
        realized_vol(returns),
        max_drawdown(candles, start, end),
        volume_z(candles, start, end),
    ]


def find_matches(
    candles: list[Candle],
    *,
    as_of_index: int,
    lookback: int,
    horizon: int,
    top: int,
    min_gap: int,
) -> tuple[int, int, list[Match]]:
    target_start = as_of_index - lookback + 1
    target_end = as_of_index
    if target_start <= 0:
        raise SystemExit(f"Need at least {lookback} candles before as-of date")

    target_returns = log_returns(candles, target_start, target_end)
    target_shape = zscore(target_returns)
    target_regime = regime_vector(candles, target_start, target_end, target_returns)

    matches: list[Match] = []
    latest_candidate_end = as_of_index - min_gap - horizon
    for candidate_end in range(lookback - 1, latest_candidate_end + 1):
        candidate_start = candidate_end - lookback + 1
        future_end = candidate_end + horizon
        if future_end >= len(candles):
            continue

        candidate_returns = log_returns(candles, candidate_start, candidate_end)
        candidate_shape = zscore(candidate_returns)
        candidate_regime = regime_vector(candles, candidate_start, candidate_end, candidate_returns)

        shape_distance = cosine_distance(target_shape, candidate_shape)
        return_distance = euclidean(target_shape, candidate_shape)
        regime_distance = euclidean(zscore(target_regime), zscore(candidate_regime))
        distance = 0.60 * shape_distance + 0.25 * return_distance + 0.15 * regime_distance

        future_return = candles[future_end].close / candles[candidate_end].close - 1.0
        matches.append(
            Match(
                distance=distance,
                similarity=1.0 / (1.0 + distance),
                end_index=candidate_end,
                start_date=candles[candidate_start].date,
                end_date=candles[candidate_end].date,
                path_return=path_return(candles, candidate_start, candidate_end),
                future_end_date=candles[future_end].date,
                future_return=future_return,
            )
        )

    return target_start, target_end, sorted(matches, key=lambda item: item.distance)[:top]


def pct(value: float) -> str:
    return f"{value * 100:.2f}%"


def print_report(candles: list[Candle], target_start: int, target_end: int, matches: list[Match], horizon: int) -> None:
    target_path_return = path_return(candles, target_start, target_end)
    target_returns = log_returns(candles, target_start, target_end)
    print(f"Target window: {candles[target_start].date} -> {candles[target_end].date}")
    print(f"Target path return: {pct(target_path_return)}")
    print(f"Target realized vol(daily): {pct(realized_vol(target_returns))}")
    print(f"Forecast horizon: {horizon} trading days")
    print()

    if not matches:
        print("No historical matches found.")
        return

    print("Top matches:")
    for rank, match in enumerate(matches, start=1):
        print(
            f"{rank}. {match.start_date} -> {match.end_date} "
            f"similarity={match.similarity:.4f} "
            f"path={pct(match.path_return)} "
            f"next_{horizon}d({match.end_date}->{match.future_end_date})={pct(match.future_return)}"
        )

    future_returns = [match.future_return for match in matches]
    wins = sum(1 for value in future_returns if value > 0)
    avg_return = sum(future_returns) / len(future_returns)
    med_return = median(future_returns)
    downside = min(future_returns)
    upside = max(future_returns)

    print()
    print("Forecast from analogs:")
    print(f"avg_next_{horizon}d_return={pct(avg_return)}")
    print(f"median_next_{horizon}d_return={pct(med_return)}")
    print(f"win_rate={wins / len(future_returns) * 100:.1f}%")
    print(f"best={pct(upside)} worst={pct(downside)}")

    if med_return > 0.03 and wins / len(future_returns) >= 0.6:
        signal = "SOXL bias"
    elif med_return < -0.03 and wins / len(future_returns) <= 0.4:
        signal = "SOXS/CASH defensive bias"
    else:
        signal = "CASH/neutral"
    print(f"signal={signal}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Find historical SOXL analogs and forecast next-week move.")
    parser.add_argument("--symbol", default="SOXL")
    parser.add_argument("--as-of", default="", help="Use the last candle on or before YYYY-MM-DD. Defaults to latest.")
    parser.add_argument("--lookback", type=int, default=20)
    parser.add_argument("--horizon", type=int, default=5)
    parser.add_argument("--top", type=int, default=5)
    parser.add_argument("--min-gap", type=int, default=5, help="Exclude candidates too close to target window.")
    parser.add_argument("--db-path", default=str(DEFAULT_DB_PATH))
    args = parser.parse_args()

    candles = load_candles(Path(args.db_path).expanduser().resolve(), args.symbol)
    as_of_index = find_as_of_index(candles, args.as_of or None)
    target_start, target_end, matches = find_matches(
        candles,
        as_of_index=as_of_index,
        lookback=args.lookback,
        horizon=args.horizon,
        top=args.top,
        min_gap=args.min_gap,
    )
    print_report(candles, target_start, target_end, matches, args.horizon)


if __name__ == "__main__":
    main()
