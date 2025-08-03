from core.engine import AdBlockEngine
import os

if __name__ == "__main__":
    rule_dir = os.path.join(os.path.dirname(__file__), "rules")
    rule_files = [
        os.path.join(rule_dir, "ads.udr"),
        os.path.join(rule_dir, "trackers.udr"),
        os.path.join(rule_dir, "malware.udr"),
        os.path.join(rule_dir, "social.udr"),
    ]

    engine = AdBlockEngine(rule_files)

    # Test a few cases
    test_urls = [
        "https://ads.google.com/banner?id=123",
        "https://partner.googleadservices.com/ad",
        "https://facebook.com/plugins/like.php",
        "http://malicious-domain.xyz/tracker",
        "https://example.com/content"
    ]

    print("\n=== Veilblock URL Test ===")
    for url in test_urls:
        result = engine.check_url(url)
        print(f"{url} -> {'BLOCKED' if result else 'ALLOWED'}")
