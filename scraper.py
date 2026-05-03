import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from datetime import datetime


class MarketScraper:
    def __init__(self, base_url):
        self.base_url = base_url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        self.results = []

    def fetch_page(self, url):
        """Fetch HTML content with error handling."""
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            return response.text
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            return None

    def scrape_books(self, page_count=1):
        """Scrapes book titles and prices from multiple pages."""
        print(f"Initializing Scraper at {datetime.now().strftime('%H:%M:%S')}...")

        for page in range(1, page_count + 1):
            url = f"{self.base_url}catalogue/page-{page}.html"
            print(f"Scraping Page {page}...")

            html = self.fetch_page(url)
            if not html:
                continue

            soup = BeautifulSoup(html, "html.parser")
            products = soup.find_all("article", class_="product_pod")

            for product in products:
                title = product.h3.a["title"]
                price = product.find("p", class_="price_color").text
                # Remove currency symbols and convert to float
                clean_price = float(price.replace('£', '').replace('Â', ''))

                self.results.append({
                    "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
                    "Product Name": title,
                    "Price (GBP)": clean_price,
                    "Stock Status": product.find("p", class_="instock availability").text.strip()
                })

            time.sleep(1)  # Ethical scraping delay

    def export_data(self, filename="market_data.csv"):
        """Saves scraped data to a CSV using Pandas."""
        if not self.results:
            print("No data to export.")
            return

        df = pd.DataFrame(self.results)
        df.to_csv(filename, index=False)
        print(f"Success! {len(df)} items exported to {filename}")


if __name__ == "__main__":
    # We use a legal practice site specifically for scrapers
    TARGET_URL = "http://books.toscrape.com/"

    scraper = MarketScraper(TARGET_URL)
    scraper.scrape_books(page_count=2)  # Scraping first 2 pages
    scraper.export_data()