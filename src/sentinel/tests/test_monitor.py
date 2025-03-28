from sentinel.monitor import monitor_api
from unittest.mock import patch, MagicMock
import pytest

# Test: monitor_api sends single request if interval is 0
def test_monitor_single_request(monkeypatch):
    called = {}

    def mock_send_request(url):
        called["url"] = url
        return {"status": 200}
    
    monkeypatch.setattr("sentinel.monitor.send_request", mock_send_request)
    result = monitor_api("https://example.com", interval=0)
    assert result["status"] == 200
    assert called["url"] == "https://example.com"

# Test: monitor_api sends request 'count' times with interval
def test_monitor_with_count(monkeypatch):
    calls = []

    def mock_send_request(url):
        calls.append(url)
    
    monkeypatch.setattr("sentinel.monitor.send_request", mock_send_request)
    monkeypatch.setattr("time.sleep", lambda x: None)  # Skip delay
    monitor_api("https://example.com", interval=1, count=3)

    assert len(calls) == 3
    assert all(url == "https://example.com" for url in calls)

# Test: monitor_api runs until KeyboardInterrupt when count is None
def test_monitor_infinite_with_interrupt(monkeypatch):
    call_count = {"count": 0}

    def mock_send_request(url):
        call_count["count"] += 1
        if call_count["count"] == 3:
            raise KeyboardInterrupt()
        return {"status": 200}
    
    monkeypatch.setattr("sentinel.monitor.send_request", mock_send_request)
    monkeypatch.setattr("time.sleep", lambda x: None)

    monitor_api("https://example.com", interval=1, count=None)
    assert call_count["count"] == 3

# Test: monitor_api prints message on KeyboardInterrupt
def test_monitor_interrupt_prints(monkeypatch, capsys):
    def mock_send_request(url):
        raise KeyboardInterrupt()
    
    monkeypatch.setattr("sentinel.monitor.send_request", mock_send_request)
    monkeypatch.setattr("time.sleep", lambda x: None)

    monitor_api("https://example.com", interval=1, count=None)
    captured = capsys.readouterr()
    assert "Monitoring stopped by user" in captured.out
