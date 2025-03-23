from sentinel.load_test import load_test_api

def test_load_test_api():
    report = load_test_api("https://httpbin.org/get", requests_count=3)
    assert report['success'] + report['failure'] == 3
