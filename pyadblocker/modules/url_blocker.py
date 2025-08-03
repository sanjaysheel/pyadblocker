# veilblock/modules/url_blocker.py
class URLBlocker:
    def __init__(self, rules):
        self.block_patterns = rules.get("block_urls", [])

    def match(self, url):
        return any(pattern in url for pattern in self.block_patterns)
