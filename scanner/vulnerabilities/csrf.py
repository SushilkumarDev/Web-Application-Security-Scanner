import requests
from bs4 import BeautifulSoup

def check(url):
    print(f"Testing CSRF on {url}")
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            forms = soup.find_all('form')
            for form in forms:
                if not form.find('input', {'name': 'csrf_token'}):
                    print(f"Possible CSRF Vulnerability found on {url}")
        else:
            print(f"Error loading {url}: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error testing CSRF on {url}: {e}")
