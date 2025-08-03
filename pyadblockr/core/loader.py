# veilblock/core/loader.py
class RuleLoader:
    @staticmethod
    def load_rules(path):
        rules = {"block_urls": []}
        with open(path, "r") as f:
            for line in f:
                rule = line.strip()
                if rule and not rule.startswith("#"):
                    rules["block_urls"].append(rule)
        return rules
