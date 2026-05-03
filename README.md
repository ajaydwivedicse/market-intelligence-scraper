# Market Intelligence Scraper

A high-performance Python automation tool designed to extract structured market data from e-commerce platforms. This project demonstrates proficiency in web scraping, data cleaning with Pandas, and ethical scraping practices.

## Problem Solved
Manual market research is slow and prone to human error. This tool automates the collection of product names, pricing, and availability, transforming hours of manual work into a 5-second automated process.

## Tech Stack
* **Language:** Python 3.x
* **Libraries:** BeautifulSoup4 (Parsing), Requests (HTTP), Pandas (Data Manipulation)
* **Output:** Clean CSV reports

## Key Features
* **Multi-Page Scraping:** Capability to navigate through multiple pages of a catalog.
* **Data Sanitization:** Automatically cleans currency symbols and formats data types for analysis.
* **Ethical Design:** Includes User-Agent headers and request throttling (time delays) to respect host servers.

## How to Run
1. Clone the repo: `git clone https://github.com/ajaydwivedicse/market-intelligence-scraper.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the script: `python scraper.py`

## Sample Output
| Timestamp | Product Name | Price (GBP) | Stock Status |
| :--- | :--- | :--- | :--- |
| 2026-05-03 | A Light in the Attic | 51.77 | In stock |
