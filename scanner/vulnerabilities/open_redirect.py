import requests

def check(url):
    print(f"Testing Open Redirect on {url}")
    payloads = ["https://evil.com", "//evil.com"]
    for payload in payloads:
        redirect_url = f"{url}?redirect={payload}"
        try:
            response = requests.get(redirect_url, allow_redirects=False)
            if response.status_code == 302 and "evil.com" in response.headers['Location']:
                print(f"Possible Open Redirect vulnerability found at {redirect_url}")
        except requests.RequestException as e:
            print(f"Error testing Open Redirect on {url}: {e}")
