import requests
from time import sleep

def monitor_api(url, interval=0, count=1):
    if interval == 0:
        try:
            response = requests.get(url)
            print(f"Status Code: {response.status_code}")
            return {"status": response.status_code}
        except requests.RequestException as e:
            print(f"Error: {e}")
            return {"error": str(e)}
    elif interval > 0:
        counter = 0
        while True:
            try:
                if counter < count:
                    response = requests.get(url)
                    print(f"Status Code: {response.status_code}")
                    sleep(interval)
                    counter += 1
                else:
                    break
            except requests.RequestException as e:
                print(f"Error: {e}")
                return {"error": str(e)}
            except KeyboardInterrupt:
                print("Monitoring stopped by user")
                return
