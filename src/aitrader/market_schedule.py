from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Any, Literal


ReportPhase = Literal["daily", "open", "close"]


@dataclass(frozen=True)
class MarketWindowResult:
    allowed: bool
    reason: str


def us_regular_market_report_window(
    calendar_payload: dict[str, Any],
    *,
    phase: ReportPhase,
    now: datetime | None = None,
    tolerance_minutes: int = 45,
) -> MarketWindowResult:
    if phase == "daily":
        return MarketWindowResult(True, "daily report does not require a market window")

    now = now or datetime.now().astimezone()
    if now.tzinfo is None:
        now = now.astimezone()
    tolerance = timedelta(minutes=tolerance_minutes)
    time_key = "startTime" if phase == "open" else "endTime"
    label = "regular market open" if phase == "open" else "regular market close"

    for day_key in ("previousBusinessDay", "today", "nextBusinessDay"):
        day = calendar_payload.get(day_key)
        if not isinstance(day, dict):
            continue
        regular = day.get("regularMarket")
        if not isinstance(regular, dict):
            continue
        target = _parse_datetime(regular.get(time_key))
        if target is None:
            continue
        if target <= now <= target + tolerance:
            return MarketWindowResult(
                True,
                f"{label} window matched {day.get('date', day_key)} at {target.isoformat()}",
            )
        if now < target <= now + tolerance:
            return MarketWindowResult(
                False,
                f"{label} has not started yet: {target.isoformat()}",
            )
    return MarketWindowResult(False, f"outside {label} window")


def _parse_datetime(value: Any) -> datetime | None:
    if not value:
        return None
    try:
        parsed = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    except ValueError:
        return None
    if parsed.tzinfo is None:
        return parsed.astimezone()
    return parsed
