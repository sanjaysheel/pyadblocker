# import os

# rule_content = """
# # baseline.udr - simple ad blocking rules

# ads.google.com
# partner.googleadservices.com
# doubleclick.net

# .selectors:
# #ad-banner
# .sponsored

# .js:
# adsbygoogle
# googletag
# """

# rules_dir = os.path.join(os.path.dirname(__file__), "../rules")
# os.makedirs(rules_dir, exist_ok=True)

# rule_file_path = os.path.join(rules_dir, "baseline.udr")

# with open(rule_file_path, "w") as f:
#     f.write(rule_content.strip())

# print(f"✅ Rule file created at: {rule_file_path}")
