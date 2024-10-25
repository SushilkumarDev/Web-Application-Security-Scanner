import argparse
from scanner.crawler import Crawler
from scanner.scanner import Scanner
import scanner.utils as utils

def main():
    parser = argparse.ArgumentParser(description="CLI Web Application Security Scanner")
    parser.add_argument("url", help="Target URL to scan")
    args = parser.parse_args()

    # Crawl the target website
    print(f"Starting crawl on {args.url}")
    crawler = Crawler(args.url)
    urls = crawler.crawl()

    print(f"Found {len(urls)} URLs")

    # Run the security scans
    scanner = Scanner(urls)
    scanner.run_scans()

if __name__ == "__main__":
    main()
