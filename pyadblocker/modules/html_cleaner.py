# veilblock/modules/html_cleaner.py
from bs4 import BeautifulSoup

class HTMLCleaner:
    def __init__(self, rules):
        self.selectors = rules.get("block_selectors", [".ad", "[id*='ad']"])

    def clean(self, html):
        soup = BeautifulSoup(html, "html.parser")
        for selector in self.selectors:
            for tag in soup.select(selector):
                tag.decompose()
        return str(soup)
