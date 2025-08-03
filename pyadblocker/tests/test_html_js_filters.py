# tests/test_html_js_filters.py
import unittest
from modules.html_cleaner import HTMLCleaner
from modules.js_filter import JSFilter

class TestHTMLJSFilters(unittest.TestCase):
    def setUp(self):
        self.html_cleaner = HTMLCleaner(rules=[".ad-banner", "#sponsor"])
        self.js_filter = JSFilter(block_keywords=["adsbygoogle", "googletag"])

    def test_html_cleaning(self):
        dirty_html = """
        <html><body>
            <div class='ad-banner'>Ad Here</div>
            <div>Content</div>
            <div id='sponsor'>Sponsor</div>
        </body></html>
        """
        cleaned = self.html_cleaner.clean(dirty_html)
        self.assertNotIn("ad-banner", cleaned)
        self.assertNotIn("sponsor", cleaned)
        self.assertIn("Content", cleaned)

    def test_js_blocking(self):
        js_code = """
            var adsbygoogle = window.adsbygoogle || [];
            console.log("Hello world");
            googletag.cmd.push(function() {});
        """
        cleaned_js = self.js_filter.clean(js_code)
        self.assertNotIn("adsbygoogle", cleaned_js)
        self.assertNotIn("googletag", cleaned_js)
        self.assertIn("Hello world", cleaned_js)

if __name__ == "__main__":
    unittest.main()
