import pytest
import sys
from sentinel import cli
from sentinel.monitor import monitor_api

def test_monitor_api():
    result = monitor_api("https://httpbin.org/get")
    assert result['status'] == 200

def test_monitor_with_interval_and_count(monkeypatch):
    called_urls = []

    # Mock monitor_api to track calls
    def mock_monitor_api(url, interval=0, count=1):
        for _ in range(count):
            called_urls.append(url)

    # Mock time.sleep to skip actual delay
    monkeypatch.setattr("time.sleep", lambda x: None)

    # Replace the real function with mock
    monkeypatch.setattr("sentinel.cli.monitor_api", mock_monitor_api)

    # Simulate CLI args: sentinel monitor <url> --interval 1 --count 3
    test_args = ['sentinel', 'monitor', 'https://example.com', '--interval', '2', '--count', '3']
    monkeypatch.setattr(sys, 'argv', test_args)

    # Run the CLI
    cli.main()

    # Assert the API was called 3 times
    assert len(called_urls) == 3
    assert all(url == 'https://example.com' for url in called_urls)
