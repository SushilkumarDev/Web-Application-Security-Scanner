# scanner/utils.py
import requests
from requests.auth import HTTPBasicAuth

def make_request_with_auth(url, username, password):
    try:
        response = requests.get(url, auth=HTTPBasicAuth(username, password))
        return response
    except requests.RequestException as e:
        print(f"Error making authenticated request to {url}: {e}")
        return None
