# veilblock/modules/js_filter.py
import re

class JSFilter:
    def __init__(self, rules):
        self.block_keywords = rules.get("block_js_keywords", ["adsbygoogle", "adInit"])

    def filter(self, script):
        return not any(keyword in script for keyword in self.block_keywords)
