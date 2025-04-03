import sys

import pytest

from sentinel import cli


# Test: Monitor command basic usage
def test_cli_monitor(monkeypatch):
    called = {}

    def mock_monitor_api(url, interval, count):
        called["url"] = url
        called["interval"] = interval
        called["count"] = count

    monkeypatch.setattr("sentinel.cli.monitor_api", mock_monitor_api)

    test_args = [
        "monitor",
        "https://example.com",
        "--interval",
        "5",
        "--count",
        "3",
    ]
    monkeypatch.setattr(sys, "argv", ["sentinel"] + test_args)

    cli.main()
    assert called["url"] == "https://example.com"
    assert called["interval"] == 5
    assert called["count"] == 3


# Test: Loadtest command with requests
def test_cli_loadtest(monkeypatch):
    called = {}

    def mock_load_test_api(url, requests_count):
        called["url"] = url
        called["requests"] = requests_count

    monkeypatch.setattr(
        "sentinel.cli.load_test_api", mock_load_test_api
    )

    test_args = ["loadtest", "https://example.com", "--requests", "20"]
    monkeypatch.setattr(sys, "argv", ["sentinel"] + test_args)

    cli.main()
    assert called["url"] == "https://example.com"
    assert called["requests"] == 20


# Test: parse_count handles "None"
def test_parse_count_none():
    assert cli.parse_count("None") is None


# Test: parse_count handles integers
def test_parse_count_int():
    assert cli.parse_count("5") == 5


# Test: Missing command should exit with error
def test_cli_missing_command(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["sentinel"])  # No command
    with pytest.raises(SystemExit):
        cli.main()
