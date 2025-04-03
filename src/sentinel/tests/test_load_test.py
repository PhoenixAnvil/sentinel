from unittest.mock import patch, MagicMock

import requests

from sentinel.load_test import load_test_api


# Test: All requests succeed (status 200)
def test_all_success():
    mock_response = MagicMock()
    mock_response.status_code = 200

    with patch(
        "sentinel.load_test.requests.get", return_value=mock_response
    ):
        result = load_test_api("http://test.com", requests_count=3)
        assert result["success"] == 3
        assert result["failure"] == 0


# Test: All requests fail (raises exception)
def test_all_failures():
    with patch(
        "sentinel.load_test.requests.get",
        side_effect=requests.RequestException("fail"),
    ):
        result = load_test_api("http://test.com", requests_count=3)
        assert result["success"] == 0
        assert result["failure"] == 3


# Test: Mixed success and failure
def test_mixed_results():
    mock_success = MagicMock()
    mock_success.status_code = 200

    def side_effect(*args, **kwargs):
        # first success, then failure, then success
        calls = [mock_success, Exception("fail"), mock_success]
        response = calls.pop(0)
        if isinstance(response, Exception):
            raise response
        return response

    with patch(
        "sentinel.load_test.requests.get",
        side_effect=[
            mock_success,
            requests.RequestException("fail"),
            mock_success,
        ],
    ):
        result = load_test_api("http://test.com", requests_count=3)
        assert result["success"] == 2
        assert result["failure"] == 1
        assert "time_taken" in result
