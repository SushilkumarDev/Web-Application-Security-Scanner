import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import re

class Crawler:
    def __init__(self, base_url):
        self.base_url = base_url
        self.visited = set()
        self.to_visit = [base_url]

    def parse_robots_txt(self):
        robots_url = urljoin(self.base_url, "/robots.txt")
        try:
            response = requests.get(robots_url)
            if response.status_code == 200:
                print("Parsing robots.txt")
                return [urljoin(self.base_url, line.split(" ")[-1]) for line in response.text.splitlines() if "Allow" in line or "Disallow" in line]
        except Exception as e:
            print(f"Error parsing robots.txt: {e}")
        return []

    def parse_sitemap(self):
        sitemap_url = urljoin(self.base_url, "/sitemap.xml")
        try:
            response = requests.get(sitemap_url)
            if response.status_code == 200:
                print("Parsing sitemap.xml")
                urls = re.findall(r'<loc>(.*?)</loc>', response.text)
                return urls
        except Exception as e:
            print(f"Error parsing sitemap.xml: {e}")
        return []

    def crawl(self):
        urls_from_robots = self.parse_robots_txt()
        urls_from_sitemap = self.parse_sitemap()
        self.to_visit.extend(urls_from_robots + urls_from_sitemap)

        while self.to_visit:
            url = self.to_visit.pop(0)
            if url not in self.visited:
                self.visited.add(url)
                print(f"Crawling: {url}")
                try:
                    response = requests.get(url)
                    if response.status_code == 200:
                        soup = BeautifulSoup(response.text, 'html.parser')
                        for link in soup.find_all('a', href=True):
                            full_url = urljoin(self.base_url, link['href'])
                            if self.base_url in full_url and full_url not in self.visited:
                                self.to_visit.append(full_url)
                except requests.RequestException as e:
                    print(f"Error crawling {url}: {e}")
        return list(self.visited)
