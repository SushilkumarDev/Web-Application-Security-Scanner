import requests

def check_api(url, method="GET", data=None):
    print(f"Testing API endpoint: {url}")
    try:
        response = requests.request(method, url, json=data)
        if response.status_code == 200:
            print(f"API {url} is reachable")
        else:
            print(f"API {url} returned status code {response.status_code}")
    except requests.RequestException as e:
        print(f"Error testing API {url}: {e}")
