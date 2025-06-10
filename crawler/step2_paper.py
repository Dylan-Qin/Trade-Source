# filename: step2_get_information.py

import time
import argparse
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os
from llm import ChatTranslateLLM
from datetime import datetime

def convert_date(date_str):
    """
    将 "11 Mar 2013" 格式的日期字符串转换为 "2013-03-11"
    """
    dt = datetime.strptime(date_str, "%d %b %Y")
    return dt.strftime("%Y-%m-%d")

class SSRNDetailScraper:
    def __init__(self, chrome_path, headless, output_path):
        self.chrome_path = chrome_path
        self.headless = headless
        self.output_path = output_path
        self.driver = self._init_driver()
        self.done_links = self._load_done_links()
        self.translator = ChatTranslateLLM(temperature=0.3)

    def _init_driver(self):
        options = Options()
        options.binary_location = self.chrome_path
        if self.headless:
            options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def _load_done_links(self):
        if os.path.exists(self.output_path):
            df = pd.read_csv(self.output_path)
            print(f"🔁 已加载 {len(df)} 条已保存记录")
            return set(df['link'].dropna().tolist())
        else:
            return set()

    def extract_detail(self, url, delay=5):
        self.driver.get(url)
        time.sleep(delay)

        soup = BeautifulSoup(self.driver.page_source, "html.parser")

        # 摘要
        abstract_div = soup.find("div", class_="abstract-text")
        abstract_en = " ".join(p.get_text(strip=True) for p in abstract_div.find_all("p")) if abstract_div else ""

        # 关键词
        keyword_p = soup.find("p", string=lambda x: x and "Keywords:" in x)
        if not keyword_p:
            strong = soup.find("strong", string="Keywords:")
            keyword_p = strong.parent if strong else None
        keywords = keyword_p.get_text(strip=True).replace("Keywords:", "").strip() if keyword_p else ""

        # 作者与机构
        author_div = soup.find("div", class_="authors authors-full-width")
        author_name = author_div.find("h2").get_text(strip=True) if author_div and author_div.find("h2") else ""
        affiliation = author_div.find("p").get_text(strip=True) if author_div and author_div.find("p") else ""

        # 发布与修订时间
        note_div = soup.find("p", class_="note note-list")
        posted_date = ""
        if note_div:
            spans = note_div.find_all("span")
            for span in spans:
                text = span.get_text(strip=True)
                if text.startswith("Posted:"):
                    posted_date = text.replace("Posted:", "").strip()


        abstract_zh = self.translator.translate(abstract_en)

        return {
            "authors": author_name,
            "abstract": abstract_en,
            "ch_abstract": abstract_zh,
            "tags": keywords,
            "publish_date": convert_date(posted_date)
        }

    def save_detail(self, data):
        df = pd.DataFrame([data])
        for col in df.columns:
            df[col] = df[col].apply(lambda x: x.replace('\n', '. ').strip(' '))
        df.to_csv(self.output_path, mode='a', index=False, header=not os.path.exists(self.output_path))

    def process(self, input_df, delay=5):
        for idx, row in input_df.iterrows():
            term = row['term']
            title = row['title']
            link = row['link']

            if link in self.done_links:
                print(f"✅ [{idx+1}] 已跳过: {title}")
                continue

            print(f"🔍 [{idx+1}] 正在爬取: {title}")
            try:
                detail = self.extract_detail(link, delay=delay)
                result = {
                    "term": term,
                    "title": title,
                    "link": link,
                    **detail
                }
                self.save_detail(result)
                self.done_links.add(link)
                print(f"💾 已保存: {title}")
            except Exception as e:
                print(f"❌ 错误: {title} - {e}")

    def close(self):
        self.driver.quit()


def main(args):
    input_df = pd.read_csv(args.input_path)
    scraper = SSRNDetailScraper(
        chrome_path=args.chrome_path,
        headless=args.headless,
        output_path=args.output_path
    )
    try:
        scraper.process(input_df, delay=args.delay)
    finally:
        scraper.close()
        print("🔚 浏览器已关闭")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SSRN Paper Detail Scraper with Save & Resume")
    parser.add_argument("--input_path", type=str, default="outputs/ssrn_search_results.csv", help="CSV containing paper links")
    parser.add_argument("--output_path", type=str, default="outputs/ssrn_details.csv", help="Output CSV for enriched info")
    parser.add_argument("--chrome_path", type=str, default="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome", help="Chrome binary path")
    parser.add_argument("--delay", type=int, default=10, help="Seconds to wait after loading each page")
    parser.add_argument("--headless", type=bool, default=True, help="Use headless browser")

    args = parser.parse_args()
    main(args)