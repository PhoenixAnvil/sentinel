from sentinel.utils.requests import send_request
from time import sleep

def monitor_api(url, interval=0, count=1):
    result = {}
    if interval == 0:
        return send_request(url)
    elif interval > 0:
        counter = 0
        while True:
            try:
                if counter < count:
                    result = send_request(url)
                    sleep(interval)
                    counter += 1
                else:
                    break
            except KeyboardInterrupt:
                print("Monitoring stopped by user")
                return
