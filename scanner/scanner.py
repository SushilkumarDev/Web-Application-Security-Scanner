from scanner.vulnerabilities import sql_injection, xss, csrf

class Scanner:
    def __init__(self, urls):
        self.urls = urls

    def run_scans(self):
        for url in self.urls:
            print(f"\n[Scanning {url}]")
            sql_injection.check(url)
            xss.check(url)
            csrf.check(url)
