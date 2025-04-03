import requests

from sentinel import logger


def send_request(url):
    """Send a GET request to the given URL and return the status or error."""
    try:
        response = requests.get(url)
        logger.info(
            f"Status Code: {response.status_code} for URL: {url}"
        )
        return {"status": response.status_code}
    except requests.RequestException as e:
        logger.error(f"Request failed for URL: {url} - {e}")
        return {"error": str(e)}
