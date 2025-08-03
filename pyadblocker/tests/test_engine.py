# tests/test_engine.py
import unittest
from core.engine import AdBlockEngine

class TestAdBlockEngine(unittest.TestCase):
    def setUp(self):
        self.engine = AdBlockEngine("rules/baseline.udr")

    def test_blocked_urls(self):
        blocked = [
            "https://ads.google.com/banner?id=123",
            "http://partner.googleadservices.com/script.js",
            "https://doubleclick.net/tracker",
            "http://track.adform.net/pixel"
        ]
        for url in blocked:
            with self.subTest(url=url):
                self.assertTrue(self.engine.check_url(url), msg=f"Should block: {url}")

    def test_allowed_urls(self):
        allowed = [
            "https://example.com/page",
            "https://www.wikipedia.org",
            "https://openai.com/blog"
        ]
        for url in allowed:
            with self.subTest(url=url):
                self.assertFalse(self.engine.check_url(url), msg=f"Should allow: {url}")

if __name__ == '__main__':
    unittest.main()
