#!/usr/bin/env python3
"""i18n build for contentcam.app (static, no build step otherwise).

Run from the repo root after adding or changing translations:
    python3 tools/i18n/build.py          # wire everything (idempotent)
    python3 tools/i18n/build.py --check  # list stale translations (English source changed since translated)

What it does, for every English page that has at least one translation under /<lang>/<same path>:
  1. <!-- @hreflang --> block in <head> of the English page and every translation:
     alternate links for all versions + x-default (English).
  2. <!-- @langs --> language switcher just before </footer> (links to the other versions of THIS page).
  3. In translated pages: internal links /x/ -> /<lang>/x/ when that translation exists;
     App Store ct=<x> -> ct=<lang>-<x> (max 40 chars); Play utm_campaign%3D<x> -> utm_campaign%3D<lang>-<x>.
  4. sitemap.xml: one <url> per translation (lastmod = today), inside <!-- @i18n --> markers.
  5. tools/i18n/manifest.json: sha256 of the English source at the time each translation was last wired,
     so --check can flag translations whose English changed afterwards.
"""
import hashlib, json, os, re, sys
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LANGS = [  # dir, hreflang, native name
    ("de", "de", "Deutsch"), ("es", "es", "Español"), ("fr", "fr", "Français"), ("it", "it", "Italiano"),
    ("ja", "ja", "日本語"), ("pt-br", "pt-BR", "Português (Brasil)"), ("id", "id", "Bahasa Indonesia"),
    ("ko", "ko", "한국어"), ("nl", "nl", "Nederlands"), ("pl", "pl", "Polski"), ("tr", "tr", "Türkçe"),
    ("vi", "vi", "Tiếng Việt"), ("zh-hans", "zh-Hans", "简体中文"), ("zh-hant", "zh-Hant", "繁體中文"),
    ("ru", "ru", "Русский"), ("sv", "sv", "Svenska"), ("da", "da", "Dansk"), ("no", "no", "Norsk"),
    ("fi", "fi", "Suomi"), ("pt-pt", "pt-PT", "Português (Portugal)"), ("uk", "uk", "Українська"),
    ("ar", "ar", "العربية"), ("hi", "hi", "हिन्दी"), ("th", "th", "ไทย"), ("ms", "ms", "Bahasa Melayu"),
    ("fil", "fil", "Filipino"), ("bn", "bn", "বাংলা"),
    ("cs", "cs", "Čeština"), ("ro", "ro", "Română"), ("hu", "hu", "Magyar"), ("el", "el", "Ελληνικά"),
]
SITE = "https://contentcam.app"
MANIFEST = os.path.join(ROOT, "tools/i18n/manifest.json")

def url_for(rel):  # rel like "blog/x/index.html" or "index.html"
    p = rel[:-len("index.html")] if rel.endswith("index.html") else rel.replace(".html", "")
    return f"{SITE}/{p}"

def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()

def find_pages():
    out = {}
    for d, code, name in LANGS:
        base = os.path.join(ROOT, d)
        if not os.path.isdir(base): continue
        for r, _, fs in os.walk(base):
            for f in fs:
                if f.endswith(".html"):
                    rel = os.path.relpath(os.path.join(r, f), base)
                    if os.path.exists(os.path.join(ROOT, rel)):
                        out.setdefault(rel, []).append((d, code, name))
    return out

def put_block(html, tag, block, anchor_re, before=True):
    html = re.sub(rf"\n?\s*<!-- @{tag} -->.*?<!-- /@{tag} -->", "", html, flags=re.S)
    m = re.search(anchor_re, html, flags=re.S)
    if not m: raise SystemExit(f"anchor {anchor_re} missing")
    i = m.start() if before else m.end()
    return html[:i] + block + html[i:]

def main(check=False):
    pages = find_pages()
    man = json.load(open(MANIFEST)) if os.path.exists(MANIFEST) else {}
    if check:
        stale = [f"{d}/{rel}" for rel, ls in pages.items() for d, _, _ in ls
                 if man.get(f"{d}/{rel}") and man[f"{d}/{rel}"] != sha(os.path.join(ROOT, rel))]
        print("\n".join(stale) or "no stale translations"); return
    translated = {(d, rel) for rel, ls in pages.items() for d, _, _ in ls}
    today = date.today().isoformat()
    sm_urls = []
    for rel, ls in sorted(pages.items()):
        versions = [("en", "English", rel, "")] + [(code, name, rel, d) for d, code, name in ls]
        hl = "\n  <!-- @hreflang -->\n" + "".join(
            f'  <link rel="alternate" hreflang="{c}" href="{url_for((d + "/" if d else "") + r)}">\n' for c, _, r, d in versions
        ) + f'  <link rel="alternate" hreflang="x-default" href="{url_for(rel)}">\n  <!-- /@hreflang -->'
        files = [(os.path.join(ROOT, rel), "")] + [(os.path.join(ROOT, d, rel), d) for d, _, _ in ls]
        for path, d in files:
            html = open(path, encoding="utf-8").read()
            html = put_block(html, "hreflang", hl, r"\s*</head>")
            sw = "\n      <!-- @langs -->\n      <div class=\"langs\" style=\"margin-top:12px;font-size:14px\">" + " · ".join(
                (f'<strong>{n}</strong>' if dd == d else f'<a href="/{(dd + "/") if dd else ""}{r[:-len("index.html")] if r.endswith("index.html") else r.replace(".html", "")}" hreflang="{c}" lang="{c}">{n}</a>')
                for c, n, r, dd in versions) + "</div>\n      <!-- /@langs -->"
            if d:
                def loc(m):
                    href = m.group(2)
                    if href.startswith(f"/{d}/"): return m.group(0)
                    target = href.lstrip("/")
                    cand = target + ("index.html" if target.endswith("/") or target == "" else "")
                    if target == "" : cand = "index.html"
                    if (d, cand) in translated: return f'{m.group(1)}/{d}/{target}"'
                    return m.group(0)
                html = re.sub(r'(href=")(/[^"#?]*)"', loc, html)
                html = re.sub(r"ct=(?!" + re.escape(d) + r"-)([A-Za-z0-9_-]+)", lambda m: "ct=" + (d + "-" + m.group(1))[:40], html)
                html = re.sub(r"utm_campaign%3D(?!" + re.escape(d) + r"-)", f"utm_campaign%3D{d}-", html)
                man[f"{d}/{rel}"] = sha(os.path.join(ROOT, rel))
                sm_urls.append(url_for(d + "/" + rel))
            if "</footer>" in html:
                html = put_block(html, "langs", sw, r"\s*</div>\s*</footer>")
            open(path, "w", encoding="utf-8").write(html)
    sm_path = os.path.join(ROOT, "sitemap.xml")
    sm = open(sm_path, encoding="utf-8").read()
    sm = re.sub(r"\s*<!-- @i18n -->.*?<!-- /@i18n -->", "", sm, flags=re.S)
    block = "\n  <!-- @i18n -->\n" + "".join(f"  <url><loc>{u}</loc><lastmod>{today}</lastmod></url>\n" for u in sm_urls) + "  <!-- /@i18n -->"
    sm = sm.replace("</urlset>", block + "\n</urlset>")
    open(sm_path, "w", encoding="utf-8").write(sm)
    json.dump(man, open(MANIFEST, "w"), indent=1, sort_keys=True)
    print(f"wired {len(pages)} English pages, {len(sm_urls)} translations")

if __name__ == "__main__":
    main(check="--check" in sys.argv)
    if "--check" not in sys.argv:  # plain Markdown copies of English pages for AI crawlers
        import subprocess; subprocess.run([sys.executable, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "md_export.py")])
