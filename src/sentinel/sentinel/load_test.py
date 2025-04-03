import time

import requests

from sentinel import logger


def load_test_api(url, requests_count):
    """Run a simple load test against an API by sending repeated GET requests."""
    logger.info(
        f"Starting load test on {url} with {requests_count} requests..."
    )

    success, failure = 0, 0
    start_time = time.time()

    for _ in range(requests_count):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                success += 1
            else:
                failure += 1
        except requests.RequestException as e:
            failure += 1
            logger.error(f"Request failed during load test: {e}")

    total_time = time.time() - start_time

    logger.info(f"Load Test Completed for {url}")
    logger.info(f"Successes: {success}")
    logger.info(f"Failures: {failure}")
    logger.info(f"Time Taken: {total_time:.2f} seconds")

    return {
        "success": success,
        "failure": failure,
        "time_taken": total_time,
    }
