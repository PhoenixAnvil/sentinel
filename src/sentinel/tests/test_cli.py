import pytest
from sentinel import cli

def test_cli_monitor(monkeypatch):
    called = {}

    def mock_monitor_api(url, interval, count):
        called['url'] = url

    monkeypatch.setattr('sentinel.cli.monitor_api', mock_monitor_api)

    test_args = ['monitor', 'https://example.com']
    monkeypatch.setattr('sys.argv', ['sentinel'] + test_args)

    cli.main()
    assert called['url'] == 'https://example.com'
