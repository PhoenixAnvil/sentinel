import requests
import time

def load_test_api(url, requests_count):
    """Run a simple load test against an API by sending repeated GET requests."""
    print(f"Starting load test on {url} with {requests_count} requests...")

    success, failure = 0, 0
    start_time = time.time()

    for _ in range(requests_count):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                success += 1
            else:
                failure += 1
        except requests.RequestException:
            failure += 1

    total_time = time.time() - start_time

    print(f"\n✅ Load Test Completed")
    print(f"✔️  Successes: {success}")
    print(f"❌ Failures: {failure}")
    print(f"⏱️  Time Taken: {total_time:.2f} seconds")

    return {
        "success": success,
        "failure": failure,
        "time_taken": total_time
    }
