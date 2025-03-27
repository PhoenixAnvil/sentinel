import requests

def send_request(url):
    """Send a GET request to the given URL and return the status or error."""
    try:
        response = requests.get(url)
        print(f"✅ Status Code: {response.status_code}")
        return {"status": response.status_code}
    except requests.RequestException as e:
        print(f"❌ Request failed: {e}")
        return {"error": str(e)}
