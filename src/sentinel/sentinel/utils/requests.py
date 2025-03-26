import requests

def send_request(url):
    try:
        response = requests.get(url)
        print(f"Status Code: {response.status_code}")
        return {"status": response.status_code}
    except requests.RequestException as e:
        print(f"Error: {e}")
        return {"error": str(e)}
