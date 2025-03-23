import requests
import time

def load_test_api(url, requests_count):
    print(f"Starting load test on {url} with {requests_count} requests")
    success = 0
    failure = 0

    start_time = time.time()

    for i in range(requests_count):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                success += 1
            else:
                failure += 1
        except requests.RequestException:
            failure += 1

    end_time = time.time()
    total_time = end_time - start_time

    print(f"Load Test Completed: {success} Successes, {failure} Failures, Time Taken: {total_time:.2f}s")
    return {
        "success": success,
        "failure": failure,
        "time_taken": total_time
    }