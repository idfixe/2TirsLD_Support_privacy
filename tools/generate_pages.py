#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
from html import escape


LOCALES = [
    ("ar", "العربية"),
    ("ca", "Català"),
    ("cs", "Čeština"),
    ("da", "Dansk"),
    ("de", "Deutsch"),
    ("el", "Ελληνικά"),
    ("en", "English (US)"),
    ("en-GB", "English (UK)"),
    ("es", "Español (España)"),
    ("es-419", "Español (Latinoamérica)"),
    ("fi", "Suomi"),
    ("fr", "Français"),
    ("fr-CA", "Français (Canada)"),
    ("he", "עברית"),
    ("hi", "हिन्दी"),
    ("hr", "Hrvatski"),
    ("hu", "Magyar"),
    ("id", "Bahasa Indonesia"),
    ("it", "Italiano"),
    ("ja", "日本語"),
    ("ko", "한국어"),
    ("ms", "Bahasa Melayu"),
    ("nb", "Norsk Bokmål"),
    ("nl", "Nederlands"),
    ("pl", "Polski"),
    ("pt-BR", "Português (Brasil)"),
    ("pt-PT", "Português (Portugal)"),
    ("ro", "Română"),
    ("ru", "Русский"),
    ("sk", "Slovenčina"),
    ("sv", "Svenska"),
    ("th", "ไทย"),
    ("tr", "Türkçe"),
    ("uk", "Українська"),
    ("vi", "Tiếng Việt"),
    ("zh-Hans", "中文（简体）"),
    ("zh-Hant", "中文（繁體）"),
]


STYLE = """
body { font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif; margin:0; padding:0; color:#1f2937; background:#f8fafc; }
main { max-width: 860px; margin: 32px auto; background: white; border: 1px solid #e5e7eb; border-radius: 12px; padding: 24px; }
h1 { margin-top: 0; font-size: 1.8rem; }
h2 { margin-top: 1.7rem; font-size: 1.15rem; }
.muted { color:#6b7280; font-size: 0.95rem; }
.chips { display:flex; flex-wrap:wrap; gap:8px; margin: 12px 0 18px; }
.chip { border:1px solid #d1d5db; border-radius: 999px; padding: 6px 10px; text-decoration:none; color:#111827; font-size:0.9rem; }
.chip:hover { background:#f3f4f6; }
.actions { margin: 12px 0 18px; display:flex; gap:12px; flex-wrap:wrap; }
.btn { background:#111827; color:white; border-radius:8px; padding:8px 12px; text-decoration:none; }
.btn.secondary { background:#374151; }
code { background:#f3f4f6; padding:2px 5px; border-radius:5px; }
footer { margin-top: 24px; padding-top: 12px; border-top: 1px solid #e5e7eb; color:#6b7280; font-size: 0.9rem; }
"""


def locale_links(page: str) -> str:
    links = []
    for code, name in LOCALES:
        links.append(
            f'<a class="chip" href="/2TirsLD_Support_privacy/l10n/{escape(code)}/{page}.html" '
            f'hreflang="{escape(code)}" lang="{escape(code)}">{escape(name)}</a>'
        )
    return "\n".join(links)


def render_support(locale_code: str, locale_name: str) -> str:
    return f"""<!doctype html>
<html lang="{escape(locale_code)}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>2TirsLD Support</title>
  <style>{STYLE}</style>
</head>
<body>
  <main>
    <h1>2TirsLD Support</h1>
    <p class="muted">Language: {escape(locale_name)} ({escape(locale_code)})</p>
    <div class="actions">
      <a class="btn" href="/2TirsLD_Support_privacy/privacy.html">Privacy</a>
      <a class="btn secondary" href="/2TirsLD_Support_privacy/index.html">Home</a>
    </div>
    <h2>Contact</h2>
    <p>Open a GitHub issue for bug reports, support requests, or feature requests.</p>
    <p>Repository: <a href="https://github.com/idfixe/2TirsLD">https://github.com/idfixe/2TirsLD</a></p>
    <h2>Information to provide</h2>
    <ul>
      <li>App version</li>
      <li>OS version (macOS/iOS/iPadOS)</li>
      <li>Steps to reproduce</li>
      <li>Screenshots/logs when available</li>
    </ul>
    <h2>Localized versions</h2>
    <div class="chips">
      {locale_links("support")}
    </div>
    <footer>
      <p>2TirsLD Support page for App Store review. Last updated: 2026-02-07.</p>
    </footer>
  </main>
</body>
</html>
"""


def render_privacy(locale_code: str, locale_name: str) -> str:
    return f"""<!doctype html>
<html lang="{escape(locale_code)}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>2TirsLD Privacy Policy</title>
  <style>{STYLE}</style>
</head>
<body>
  <main>
    <h1>2TirsLD Privacy Policy</h1>
    <p class="muted">Language: {escape(locale_name)} ({escape(locale_code)})</p>
    <div class="actions">
      <a class="btn" href="/2TirsLD_Support_privacy/support.html">Support</a>
      <a class="btn secondary" href="/2TirsLD_Support_privacy/index.html">Home</a>
    </div>
    <h2>Data processed</h2>
    <p>The app stores ballistic and configuration data required for normal operation.</p>
    <h2>Storage and sync</h2>
    <ul>
      <li>Data is stored locally on your device.</li>
      <li>If iCloud is enabled, data can be synced via the user private iCloud account.</li>
      <li>No third-party analytics or ad tracking is used by the app publisher.</li>
    </ul>
    <h2>Deletion</h2>
    <p>Data can be removed from the app reset flow and by deleting app/iCloud app data.</p>
    <h2>Localized versions</h2>
    <div class="chips">
      {locale_links("privacy")}
    </div>
    <footer>
      <p>2TirsLD Privacy page for App Store review. Last updated: 2026-02-07.</p>
    </footer>
  </main>
</body>
</html>
"""


def render_root_index() -> str:
    options = "\n".join(
        [
            f'<option value="{escape(code)}">{escape(name)} ({escape(code)})</option>'
            for code, name in LOCALES
        ]
    )
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>2TirsLD Support & Privacy</title>
  <style>{STYLE}</style>
</head>
<body>
  <main>
    <h1>2TirsLD Support & Privacy</h1>
    <p>Official pages for App Store listing and review.</p>
    <div class="actions">
      <a class="btn" href="/2TirsLD_Support_privacy/support.html">Support URL</a>
      <a class="btn secondary" href="/2TirsLD_Support_privacy/privacy.html">Privacy URL</a>
    </div>
    <h2>Language selector</h2>
    <p>Choose a locale, then open dedicated Support/Privacy pages for that locale.</p>
    <label for="locale"><strong>Locale</strong></label><br>
    <select id="locale">{options}</select>
    <div class="actions">
      <a id="openSupport" class="btn">Open Support (locale)</a>
      <a id="openPrivacy" class="btn secondary">Open Privacy (locale)</a>
    </div>
    <footer>
      <p>Base URLs for App Store:</p>
      <p><code>https://idfixe.github.io/2TirsLD_Support_privacy/support.html</code></p>
      <p><code>https://idfixe.github.io/2TirsLD_Support_privacy/privacy.html</code></p>
    </footer>
  </main>
  <script>
    const known = new Set([{", ".join([f'"{code}"' for code, _ in LOCALES])}]);
    const localeSelect = document.getElementById("locale");
    const openSupport = document.getElementById("openSupport");
    const openPrivacy = document.getElementById("openPrivacy");
    function normalizeLocale(v) {{
      if (known.has(v)) return v;
      if (v.includes("-")) {{
        const base = v.split("-")[0];
        if (known.has(base)) return base;
      }}
      return "en";
    }}
    const auto = normalizeLocale(navigator.language || "en");
    localeSelect.value = auto;
    function refresh() {{
      const v = normalizeLocale(localeSelect.value);
      openSupport.href = `/2TirsLD_Support_privacy/l10n/${{v}}/support.html`;
      openPrivacy.href = `/2TirsLD_Support_privacy/l10n/${{v}}/privacy.html`;
    }}
    localeSelect.addEventListener("change", refresh);
    refresh();
  </script>
</body>
</html>
"""


def render_root_proxy(kind: str) -> str:
    title = "Support" if kind == "support" else "Privacy Policy"
    h1 = f"2TirsLD {title}"
    links = locale_links(kind)
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(h1)}</title>
  <style>{STYLE}</style>
</head>
<body>
  <main>
    <h1>{escape(h1)}</h1>
    <p>Official App Store URL. You can select language below.</p>
    <div class="chips">
      {links}
    </div>
    <div class="actions">
      <a class="btn secondary" href="/2TirsLD_Support_privacy/index.html">Home</a>
    </div>
    <footer>
      <p>Auto-redirect by device language is enabled when possible.</p>
    </footer>
  </main>
  <script>
    const known = new Set([{", ".join([f'"{code}"' for code, _ in LOCALES])}]);
    function normalizeLocale(v) {{
      if (!v) return "en";
      if (known.has(v)) return v;
      if (v.includes("-")) {{
        const base = v.split("-")[0];
        if (known.has(base)) return base;
      }}
      return "en";
    }}
    const targetLocale = normalizeLocale(navigator.language || "en");
    const target = `/2TirsLD_Support_privacy/l10n/${{targetLocale}}/{kind}.html`;
    setTimeout(() => window.location.replace(target), 150);
  </script>
</body>
</html>
"""


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    l10n = root / "l10n"
    l10n.mkdir(parents=True, exist_ok=True)

    for code, name in LOCALES:
        locale_dir = l10n / code
        locale_dir.mkdir(parents=True, exist_ok=True)
        (locale_dir / "support.html").write_text(render_support(code, name), encoding="utf-8")
        (locale_dir / "privacy.html").write_text(render_privacy(code, name), encoding="utf-8")

    (root / "index.html").write_text(render_root_index(), encoding="utf-8")
    (root / "support.html").write_text(render_root_proxy("support"), encoding="utf-8")
    (root / "privacy.html").write_text(render_root_proxy("privacy"), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
