# filename: ssrn_scraper.py

import time
import argparse
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os

class SSRNScraper:
    def __init__(self, chrome_path="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome", headless=True):
        self.chrome_path = chrome_path
        self.headless = headless
        self.driver = self._init_driver()

    def _init_driver(self):
        options = Options()
        options.binary_location = self.chrome_path
        if self.headless:
            options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        return driver

    def search_and_extract(self, keyword, delay=10):
        url = f"https://papers.ssrn.com/searchresults.cfm?term={keyword}"
        self.driver.get(url)
        time.sleep(delay)

        soup = BeautifulSoup(self.driver.page_source, "html.parser")
        results = []

        for item in soup.find_all("div", class_="result-item"):
            h3 = item.find("h3")
            if h3 and h3.a:
                title = h3.get_text(strip=True)
                link = h3.a["href"]
                results.append({"term":keyword, "title": title, "link": link})

        return results

    def close(self):
        self.driver.quit()


def main(args):
    scraper = SSRNScraper(chrome_path=args.chrome_path, headless=args.headless)
    current_results = pd.read_csv(args.output_path)
    term_list = pd.read_csv(args.term_file, header=None)[0].tolist()
    try:
        for term in term_list:
            if term in current_results['term']:
                continue
            results = scraper.search_and_extract(keyword=term, delay=args.delay)
            df = pd.DataFrame(results)
            df.to_csv(args.output_path, mode='a', index=False, header=not os.path.exists(args.output_path))
            print(f"✅ Saved {len(results)} results to {args.output_path}")
    finally:
        scraper.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SSRN Paper Search Scraper")
    parser.add_argument("--term_file", type=str, default='dataset/trade.list', help="Search term for SSRN")
    parser.add_argument("--output_path", type=str, default="outputs/ssrn_search_results.csv", help="Path to save results")
    parser.add_argument("--chrome_path", type=str, default="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome", help="Path to Chrome binary")
    parser.add_argument("--delay", type=int, default=10, help="Time to wait for page to load")
    parser.add_argument("--headless", type=bool, default=False, help="Run browser in headless mode")

    args = parser.parse_args()
    main(args)