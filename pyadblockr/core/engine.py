from core.loader import RuleLoader
from core.dispatcher import PluginDispatcher
from core.context import RequestContext
import os

class AdBlockEngine:
    def __init__(self, rule_files):
        self.rules = self._merge_rules(rule_files)
        self.dispatcher = PluginDispatcher(self.rules)

    def _merge_rules(self, file_paths):
        merged = {
            "block_urls": [],
            "selectors": [],
            "js_patterns": []
        }
        for path in file_paths:
            if not os.path.exists(path):
                raise FileNotFoundError(f"UDR rule file missing: {path}")
            rules = RuleLoader.load_rules(path)
            merged["block_urls"] += rules.get("block_urls", [])
            merged["selectors"] += rules.get("selectors", [])
            merged["js_patterns"] += rules.get("js_patterns", [])
        return merged

    def check_url(self, url):
        context = RequestContext(url=url, headers={}, content_type="text/html")
        return self.dispatcher.run_url_plugins(context)

    def clean_html(self, html):
        return self.dispatcher.run_html_plugins(html)

    def filter_js(self, script):
        return self.dispatcher.run_js_plugins(script)
