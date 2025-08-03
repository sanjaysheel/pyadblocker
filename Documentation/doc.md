# 🧱 PyAdBlock — Module-Level Technical Documentation

> Version: `v0.1.0`
> Maintainer: `@sanjaysheel`

---

## 🔧 Core Components

---

### 🔹 `main.py` — Entry Point

| Purpose | CLI runner for testing ad-blocking logic |
| ------- | ---------------------------------------- |
| Input   | Hardcoded list of test URLs              |
| Output  | Console output: `BLOCKED` or `ALLOWED`   |

Useful for quickly validating rule matching without integrating into larger systems.

---

### 🔹 `init_rules.py`

| Purpose | Initializes rule files on first run                                       |
| ------- | ------------------------------------------------------------------------- |
| Logic   | Checks if `rules/baseline.udr` exists, if not creates with default values |

Prevents users from forgetting to add rule files before testing.

---

## 🧠 Core Engine

---

### 📁 `core/engine.py`

| Purpose | Central controller — takes a context (URL, headers, type) and runs filters |
| ------- | -------------------------------------------------------------------------- |
| Input   | `Context` object (URL, headers, content type)                              |
| Output  | `True` or `False` → Block decision                                         |

Centralizes filtering logic, decoupled from CLI and rule parsing.

---

### 📁 `core/loader.py`

| Purpose | Loads `.udr` files and parses into structured dict |
| ------- | -------------------------------------------------- |
| Input   | Filepath to `.udr`                                 |
| Output  | Dict with keys: `urls`, `selectors`, `js_keywords` |

```python
{
  'urls': ['ads.google.com', 'doubleclick.net'],
  'selectors': ['#ad-banner', '.sponsored'],
  'js_keywords': ['googletag', 'adsbygoogle']
}
```

---

### 📁 `core/dispatcher.py`

| Purpose | Dispatches filtering to plugins dynamically         |
| ------- | --------------------------------------------------- |
| Logic   | Runs `.match()` for each plugin and returns verdict |

Makes plugin orchestration clean and extensible.

---

### 📁 `core/context.py`

| Purpose | Encapsulates a web request (URL + optional content type & headers) |
| ------- | ------------------------------------------------------------------ |
| Usage   | Every filtering decision runs against a `Context()` object         |

Abstracts away raw values, supports clean interface.

---

## 🥉 Filtering Plugins (`modules/`)

---

### 🔹 `url_blocker.py`

\| Filters | URLs based on simple match against rule list |
\| Input   | `context.url`                                |
\| Match   | Substring or full match                      |

```python
context.url = "https://ads.google.com/banner?id=123"
﹀ matches rule: "ads.google.com"
```

---

### 🔹 `html_cleaner.py`

\| Filters | Ad-related HTML using CSS selectors |
\| Match   | `context.html` content (if available) |
\| Behavior | Removes nodes matching `.selectors:` section of `.udr` |

---

### 🔹 `js_filter.py`

\| Filters | Inline JavaScript content               |
\| Match   | Looks for presence of `adsbygoogle`, `googletag`, etc. |
\| Input   | `context.script` or `<script>` contents |

---

### 🔹 `plugin_base.py`

\| Purpose | Abstract base class for plugin structure |
\| Defines | `match(self, context)`                   |

Guarantees that all plugins conform to a consistent interface.

---

## 📆 Rule Files (`rules/`)

---

### `baseline.udr`

\| Purpose | General blocking — common ad URLs, CSS, and JS |
\| Status  | Auto-generated via `init_rules.py` on first run |

---

### `trackers.udr`

\| Purpose | Focused on known trackers like Facebook Pixel, GTM |
\| Structure | Same `.udr` format |

---

## 🧪 Tests (`tests/`)

---

### `test_engine.py`

\| Tests | Full engine logic, given mock context and mock rules |
\| Tools | `unittest` or `pytest`                              |

---

### `test_rules.py`

\| Tests | Rule loader correctness, edge cases in parsing |
\| Example | Incorrect section ordering, empty values     |

---

## 📁 `utils/logger.py`

\| Purpose | (Optional) Structured logging for debug or telemetry |
\| Usage  | Use for future extension into Web UI or logs          |

---

## 🛠️ Design Decisions

| Design Area          | Reason / Justification           |
| -------------------- | -------------------------------- |
| `.udr` format        | Lightweight, editable, readable  |
| Plugin architecture  | Easy to extend, decouple logic   |
| No ABP/EasyList      | Avoids bloat, better performance |
| CLI + tests included | Developer friendly               |

---

## 🔮 Future Module Ideas

| File Name          | Purpose                                      |
| ------------------ | -------------------------------------------- |
| `video_blocker.py` | Strip YouTube or embedded ads                |
| `cookie_banner.py` | Auto-dismiss GDPR overlays                   |
| `ml_filter.py`     | Use transformer to detect "sponsored" blocks |
