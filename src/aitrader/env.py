from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DotenvResult:
    path: Path
    exists: bool
    loaded: tuple[str, ...]
    skipped: tuple[str, ...]


def load_dotenv(path: str | Path = ".env", *, override: bool = False) -> DotenvResult:
    dotenv_path = Path(path)
    if not dotenv_path.exists():
        return DotenvResult(dotenv_path, False, (), ())

    loaded: list[str] = []
    skipped: list[str] = []
    for raw_line in dotenv_path.read_text(encoding="utf-8").splitlines():
        parsed = _parse_line(raw_line)
        if parsed is None:
            continue
        key, value = parsed
        if key in os.environ and os.environ[key] and not override:
            skipped.append(key)
            continue
        os.environ[key] = value
        loaded.append(key)

    return DotenvResult(dotenv_path, True, tuple(loaded), tuple(skipped))


def env_status(keys: list[str], *, dotenv_path: str | Path = ".env") -> dict:
    path = Path(dotenv_path)
    return {
        "dotenv": {
            "path": str(path),
            "exists": path.exists(),
        },
        "variables": {
            key: {
                "present": bool(os.environ.get(key)),
                "masked": mask_secret(os.environ.get(key, "")),
            }
            for key in keys
        },
    }


def mask_secret(value: str) -> str:
    if not value:
        return ""
    if len(value) <= 8:
        return "*" * len(value)
    return f"{value[:4]}...{value[-4:]}"


def _parse_line(line: str) -> tuple[str, str] | None:
    stripped = line.strip()
    if not stripped or stripped.startswith("#"):
        return None
    if stripped.startswith("export "):
        stripped = stripped[len("export ") :].strip()
    if "=" not in stripped:
        return None
    key, value = stripped.split("=", 1)
    key = key.strip()
    value = value.strip()
    if not key:
        return None
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        value = value[1:-1]
    return key, value

