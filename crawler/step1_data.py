import time
import argparse
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import re
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os
from llm import ChatTranslateLLM

class ScienceDBScraper:
    def __init__(self, chrome_path="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome", headless=True):
        self.chrome_path = chrome_path
        self.headless = headless
        self.driver = self._init_driver()
        self.results = None
        self.translator = ChatTranslateLLM(temperature=0.3)

    def _init_driver(self):
        options = Options()
        options.binary_location = self.chrome_path
        if self.headless:
            options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        service = Service(ChromeDriverManager().install())
        return webdriver.Chrome(service=service, options=options)

    def extract_from_current_page(self, term, delay):
        results = []

        # 获取所有搜索结果项

        # botton = self.driver.find_elements(By.CSS_SELECTOR, ".v-input__append-inner")
        # if len(botton) > 0:
        #     botton[0].click()

        # option = WebDriverWait(self.driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Date (newest)')]"))
        # )
        # time.sleep(delay)
        # option.click()
        time.sleep(delay)

        items = self.driver.find_elements(By.CSS_SELECTOR, ".vw-searchlist-item")

        for i, item in enumerate(items):
            # 获取标题链接
            textbox = item.find_element(By.CSS_SELECTOR, ".vw-textbox")
            title_link = item.find_element(By.CSS_SELECTOR, ".vw-imgbox a")
            # 获取标题文本
            title = title_link.text.strip()
            # 滚动并点击进入详情页
            if self.results is not None and title in self.results['title']:
                continue
            # 等待跳转，确保包含 dataSetId

            # 提取DOI
            p_tags = textbox.find_elements(By.TAG_NAME, "p")
            doi = None
            for p in p_tags:
                text = p.text.strip()
                if text.startswith("DOI"):
                    doi = text.replace("DOI :", "").strip()
                    break
            
            link = f"https://doi.org/{doi}" if doi else ""
            
            # 提取作者
            author_tag = items[i].find_element(By.CSS_SELECTOR, ".vw-textbox p")
            authors = author_tag.text.strip()

            # 摘要
            abstract_tag = items[i].find_element(By.CSS_SELECTOR, ".vw-textbox div")
            abstract = abstract_tag.text.strip().replace("\xa0", " ")

            # 日期
            date_tag = items[i].find_element(By.CSS_SELECTOR, "span.vw-time")
            date_match = re.search(r"\d{4}-\d{2}-\d{2}", date_tag.text)
            publish_date = date_match.group(0)

            # 中文摘要
            ch_abstract = self.translator.translate(abstract)

            # 关键词提取
            tags =  self.translator.extract_key_words(abstract)

            results.append({
                "term": term,
                "title": title,
                "link": link,
                "authors": authors,
                "abstract": abstract,
                "ch_abstract": ch_abstract,
                "tags": tags,
                "publish_date": publish_date,
            })

        return results

    def get_max_page_number(self):
        soup = BeautifulSoup(self.driver.page_source, "html.parser")
        page_buttons = soup.select('button.v-pagination__item')
        max_page = 1
        for btn in page_buttons:
            try:
                page_text = btn.get_text(strip=True)
                if page_text.isdigit():
                    max_page = max(max_page, int(page_text))
            except:
                continue
        return max_page

    def click_next_page(self):
        try:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            wait = WebDriverWait(self.driver, 10)
            next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'button.v-pagination__navigation[aria-label="Next page"]')))
            next_button.click()
            time.sleep(2)
            return True
        except Exception as e:
            print(f"⚠️ 无法点击下一页: {e}")
            return False

    def search_and_extract(self, term, delay=5, max_pages=1, output_path="outputs/science_db_results.csv"):
        self.driver.get("https://www.scidb.cn/en/list")
        time.sleep(delay)

        input_box = self.driver.find_element(By.ID, "searchInput")
        input_box.clear()
        input_box.send_keys(term)

        search_button = self.driver.find_element(By.CSS_SELECTOR, "button[data-v-2d9f3dfa]")
        time.sleep(delay)
        search_button.click()
        time.sleep(delay)

        real_max_page = self.get_max_page_number()
        max_pages = min(max_pages, real_max_page)
        print(f"🔎 最大页数为 {real_max_page}，将抓取前 {max_pages} 页")

        is_first_page = True
        if os.path.exists(output_path):
            self.results = pd.read_csv(output_path)
            is_first_page = False

        for page_num in range(1, max_pages + 1):
            print(f"📄 抓取第 {page_num} 页")
            page_results = self.extract_from_current_page(term, delay)
            if len(page_results) > 0:
                df = pd.DataFrame(page_results)
                for col in df.columns:
                    df[col] = df[col].astype(str).apply(lambda x: x.replace('\n', '. '))
                df.to_csv(output_path, mode='a', header=is_first_page, index=False, encoding='utf-8-sig')
                

            print(f"✅ 第 {page_num} 页抓取 {len(page_results)} 条记录，已追加到 {output_path}")
            if page_num < max_pages:
                self.click_next_page()

        print(f"🎉 所有页面处理完成，共抓取 {max_pages} 页。")

    def close(self):
        self.driver.quit()


def main(args):
    scraper = ScienceDBScraper(chrome_path=args.chrome_path, headless=args.headless)
    for term in args.term.split(','):
        scraper.search_and_extract(
            term,
            delay=args.delay,
            max_pages=args.max_pages,
            output_path=args.output_path
        )

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ScienceDB term Search Scraper")
    parser.add_argument("--term", type=str, default='trade data, import export data, international trade statistics, bilateral trade, trade flows, tariff data, customs data, trade policy data, trade agreement dataset, WTO dataset, non-tariff measures, trade barriers data, trade compliance data, global trade dataset, supply chain data, trade volume, trade index, economic trade indicators, trade regulation data, cross-border trade', help="Search term for ScienceDB")
    parser.add_argument("--output_path", type=str, default="outputs/sciencedb_details.csv", help="Path to save results")
    parser.add_argument("--chrome_path", type=str, default="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome", help="Path to Chrome binary")
    parser.add_argument("--delay", type=int, default=15, help="Wait time after page loads")
    parser.add_argument("--headless", type=bool, default=True, help="Run Chrome in headless mode")
    parser.add_argument("--max_pages", type=int, default=50, help="Maximum number of pages to crawl")
    args = parser.parse_args()
    main(args)