# pyadblock

<code>
  pyadblock/                         🔹 Unique & Modern Python AdBlocker
  ├── main.py                        ▶ CLI/test entry point
  ├── core/
  │   ├── engine.py                  ▶ Main controller: URL, HTML, script filters
  │   ├── loader.py                  ▶ Rule loader/parser (.udr format)
  │   ├── dispatcher.py              ▶ Plugin runner (URL, HTML, JS matchers)
  │   └── context.py                 ▶ Request context (URL + headers + content type)
  ├── modules/
  │   ├── url_blocker.py             ▶ Blocks URLs via .udr rules
  │   ├── html_cleaner.py            ▶ Strips ad HTML by selector
  │   ├── js_filter.py               ▶ Blocks inline JS/ad scripts
  │   └── plugin_base.py             ▶ Base class for adding more plugins
  ├── rules/
  │   └── baseline.udr               ▶ Your universal ad rules (no ABP dependency)
  ├── utils/
  │   └── logger.py                  ▶ Logging, debugging, telemetry (optional)
  ├── tests/
  │   ├── test_engine.py
  │   └── test_rules.py
  └── README.md                      ▶ Project intro, usage, rule syntax, examples
</code>code>
