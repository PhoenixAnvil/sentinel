from sentinel.monitor import monitor_api

def test_monitor_api():
    result = monitor_api("https://httpbin.org/get")
    assert result['status'] == 200
