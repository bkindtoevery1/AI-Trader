import json
from pathlib import Path

from aitrader.cli import main
from aitrader.env import load_dotenv, mask_secret


def test_load_dotenv_sets_values_without_overriding_existing(monkeypatch, tmp_path):
    env_file = tmp_path / ".env"
    env_file.write_text(
        "\n".join(
            [
                "TOSSINVEST_CLIENT_ID=from_file",
                "TOSSINVEST_CLIENT_SECRET='secret from file'",
                "TOSSINVEST_ACCOUNT_SEQ=3",
            ]
        ),
        encoding="utf-8",
    )
    monkeypatch.setenv("TOSSINVEST_CLIENT_ID", "from_shell")
    monkeypatch.delenv("TOSSINVEST_CLIENT_SECRET", raising=False)
    monkeypatch.delenv("TOSSINVEST_ACCOUNT_SEQ", raising=False)

    result = load_dotenv(env_file)

    assert result.exists is True
    assert "TOSSINVEST_CLIENT_ID" in result.skipped
    assert "TOSSINVEST_CLIENT_SECRET" in result.loaded
    assert "TOSSINVEST_ACCOUNT_SEQ" in result.loaded
    assert result.path == env_file
    assert __import__("os").environ["TOSSINVEST_CLIENT_ID"] == "from_shell"
    assert __import__("os").environ["TOSSINVEST_CLIENT_SECRET"] == "secret from file"
    assert __import__("os").environ["TOSSINVEST_ACCOUNT_SEQ"] == "3"


def test_env_check_loads_env_file_and_masks_values(monkeypatch, tmp_path, capsys):
    repo_root = Path.cwd()
    env_file = tmp_path / ".env"
    env_file.write_text(
        "\n".join(
            [
                "TOSSINVEST_CLIENT_ID=tsck_test_123456789",
                "TOSSINVEST_CLIENT_SECRET=tssk_test_987654321",
                "TOSSINVEST_ACCOUNT_SEQ=42",
                "AI_TRADER_CONFIG=config/strategy.yaml",
            ]
        ),
        encoding="utf-8",
    )
    for key in [
        "TOSSINVEST_CLIENT_ID",
        "TOSSINVEST_CLIENT_SECRET",
        "TOSSINVEST_ACCOUNT_SEQ",
        "AI_TRADER_CONFIG",
    ]:
        monkeypatch.delenv(key, raising=False)
    monkeypatch.chdir(tmp_path)

    exit_code = main(
        [
            "--config",
            str(repo_root / "config/strategy.yaml"),
            "env-check",
            "--env-file",
            str(env_file),
        ]
    )

    assert exit_code == 0
    output = capsys.readouterr().out
    payload = json.loads(output)
    assert payload["dotenvLoaded"]["exists"] is True
    assert payload["variables"]["TOSSINVEST_CLIENT_ID"]["present"] is True
    assert payload["variables"]["TOSSINVEST_CLIENT_ID"]["masked"] == "tsck...6789"
    assert "tsck_test_123456789" not in output
    assert "tssk_test_987654321" not in output


def test_mask_secret_never_exposes_short_values():
    assert mask_secret("42") == "**"
    assert mask_secret("") == ""

