import requests

def get_proxied_session(proxy_url):
    session = requests.Session()
    session.proxies = {
        "http": proxy_url,
        "https": proxy_url,
    }
    return session
