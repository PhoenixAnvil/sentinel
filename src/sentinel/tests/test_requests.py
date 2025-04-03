from unittest.mock import patch, MagicMock

import requests

from sentinel.utils.requests import send_request


# Test: Successful GET request
def test_send_request_success():
    mock_response = MagicMock()
    mock_response.status_code = 200

    with patch(
        "sentinel.utils.requests.requests.get",
        return_value=mock_response,
    ):
        result = send_request("https://example.com")
        assert result == {"status": 200}


# Test: Failed GET request (RequestException raised)
def test_send_request_exception():
    with patch(
        "sentinel.utils.requests.requests.get",
        side_effect=requests.RequestException("Network error"),
    ):
        result = send_request("https://example.com")
        assert "error" in result
        assert "Network error" in result["error"]


# Optional: Test a 404 response
def test_send_request_404():
    mock_response = MagicMock()
    mock_response.status_code = 404

    with patch(
        "sentinel.utils.requests.requests.get",
        return_value=mock_response,
    ):
        result = send_request("https://example.com")
        assert result == {"status": 404}
