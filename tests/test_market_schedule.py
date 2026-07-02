from datetime import datetime

from aitrader.market_schedule import us_regular_market_report_window


def test_us_market_open_window_matches_regular_start():
    payload = {
        "today": {
            "date": "2026-07-02",
            "regularMarket": {
                "startTime": "2026-07-02T22:30:00.000+09:00",
                "endTime": "2026-07-03T05:00:00.000+09:00",
            },
        }
    }

    result = us_regular_market_report_window(
        payload,
        phase="open",
        now=datetime.fromisoformat("2026-07-02T22:35:00+09:00"),
    )

    assert result.allowed is True
    assert "open" in result.reason


def test_us_market_close_window_matches_previous_business_day_end():
    payload = {
        "previousBusinessDay": {
            "date": "2026-07-02",
            "regularMarket": {
                "startTime": "2026-07-02T22:30:00.000+09:00",
                "endTime": "2026-07-03T05:00:00.000+09:00",
            },
        }
    }

    result = us_regular_market_report_window(
        payload,
        phase="close",
        now=datetime.fromisoformat("2026-07-03T05:05:00+09:00"),
    )

    assert result.allowed is True
    assert "close" in result.reason


def test_us_market_window_rejects_outside_window():
    payload = {
        "today": {
            "date": "2026-07-02",
            "regularMarket": {
                "startTime": "2026-07-02T22:30:00.000+09:00",
                "endTime": "2026-07-03T05:00:00.000+09:00",
            },
        }
    }

    result = us_regular_market_report_window(
        payload,
        phase="open",
        now=datetime.fromisoformat("2026-07-02T23:35:00+09:00"),
    )

    assert result.allowed is False
