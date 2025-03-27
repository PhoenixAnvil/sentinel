from time import sleep
from sentinel.utils.requests import send_request

def monitor_api(url, interval=0, count=1):
    """Monitor an API endpoint with optional polling."
    If `interval` is 0 or negative, send a single request."
    If `count` is None, poll indefinitely."
    """
    if interval <= 0:
        return send_request(url)
    
    try:
        if count is None:
            while True:
                send_request(url)
                sleep(interval)
        else:
            for _ in range(count):
                send_request(url)
                sleep(interval)
    except KeyboardInterrupt:
        print("Monitoring stopped by user")
