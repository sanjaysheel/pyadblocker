# veilblock/core/dispatcher.py
from modules.url_blocker import URLBlocker
from modules.html_cleaner import HTMLCleaner
from modules.js_filter import JSFilter

class PluginDispatcher:
    def __init__(self, rules):
        self.url_blocker = URLBlocker(rules)
        self.html_cleaner = HTMLCleaner(rules)
        self.js_filter = JSFilter(rules)

    def run_url_plugins(self, context):
        return self.url_blocker.match(context.url)

    def run_html_plugins(self, html):
        return self.html_cleaner.clean(html)

    def run_js_plugins(self, script):
        return self.js_filter.filter(script)
