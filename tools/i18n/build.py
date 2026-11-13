#!/usr/bin/env python3
"""i18n build for contentcam.app (static, no build step otherwise).

Run from the repo root after adding or changing translations:
    python3 tools/i18n/build.py          # wire everything (idempotent)
    python3 tools/i18n/build.py --check  # list stale translations (English source changed since translated)

What it does, for every English page that has at least one translation under /<lang>/<same path>:
  1. <!-- @hreflang --> block in <head> of the English page and every translation:
     alternate links for all versions + x-default (English).
  2. <!-- @langs --> list just before </footer> and <!-- @langpick --> globe picker in the nav, on EVERY English page
     and translation: all languages, linking to this page's translation or else that language's homepage.
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
    homes = [(d, code, name) for d, code, name in LANGS if os.path.exists(os.path.join(ROOT, d, "index.html"))]
    today = date.today().isoformat()
    sm_urls = []
    # Every English page with a nav or footer gets the language picker + footer list, even when it has no
    # translations yet: languages without this page link to that language's homepage (no hreflang claim).
    english = {}
    lang_dirs = {d for d, _, _ in LANGS}
    for r, dirs, fs in os.walk(ROOT):
        relr = os.path.relpath(r, ROOT)
        top = relr.split(os.sep)[0]
        if relr != "." and (top in lang_dirs or top in ("tools", "node_modules", ".git", ".vercel") or top.startswith(".")):
            dirs[:] = []; continue
        for f in fs:
            if f.endswith(".html"):
                rel = os.path.normpath(os.path.join(relr, f)) if relr != "." else f
                english[rel] = pages.get(rel, [])
    def path_of(dd, r):
        return "/" + ((dd + "/") if dd else "") + (r[:-len("index.html")] if r.endswith("index.html") else r.replace(".html", ""))
    for rel, ls in sorted(english.items()):
        have = {d for d, _, _ in ls}
        versions = [("en", "English", rel, "")] + [(code, name, rel, d) for d, code, name in ls]
        # full list in LANGS order: translated page if it exists, else that language's homepage
        full = [("en", "English", path_of("", rel), "", True)] + [
            (code, name, path_of(d, rel) if d in have else f"/{d}/", d, d in have) for d, code, name in homes]
        hl = "\n  <!-- @hreflang -->\n" + "".join(
            f'  <link rel="alternate" hreflang="{c}" href="{url_for((d + "/" if d else "") + r)}">\n' for c, _, r, d in versions
        ) + f'  <link rel="alternate" hreflang="x-default" href="{url_for(rel)}">\n  <!-- /@hreflang -->'
        files = [(os.path.join(ROOT, rel), "")] + [(os.path.join(ROOT, d, rel), d) for d, _, _ in ls]
        for path, d in files:
            html = open(path, encoding="utf-8").read()
            if ls:
                html = put_block(html, "hreflang", hl, r"\s*</head>")
            def item(c, n, href, dd, real):
                if dd == d: return f'<strong>{n}</strong>'
                return f'<a href="{href}" hreflang="{c}" lang="{c}">{n}</a>' if real else f'<a href="{href}" lang="{c}">{n}</a>'
            sw = "\n      <!-- @langs -->\n      <div class=\"langs\" style=\"margin-top:12px;font-size:14px\">" + " · ".join(
                item(*v) for v in full) + "</div>\n      <!-- /@langs -->"
            cur = d or "en"
            pick = ("\n      <!-- @langpick -->\n      <details class=\"lang-pick\"><summary aria-label=\"Language\">"
                    "<svg viewBox=\"0 0 24 24\" width=\"17\" height=\"17\" aria-hidden=\"true\"><circle cx=\"12\" cy=\"12\" r=\"9\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"1.7\"/>"
                    "<path d=\"M3 12h18M12 3c2.5 2.7 3.8 5.7 3.8 9s-1.3 6.3-3.8 9c-2.5-2.7-3.8-5.7-3.8-9S9.5 5.7 12 3z\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"1.7\"/></svg>"
                    f"<span>{cur.split('-')[0].upper()}</span></summary><div class=\"lang-menu\">"
                    + "".join(f'<strong>{n}</strong>' if dd == d else (f'<a href="{href}" hreflang="{c}" lang="{c}">{n}</a>' if real else f'<a href="{href}" lang="{c}">{n}</a>') for c, n, href, dd, real in full)
                    + "</div></details>\n      <!-- /@langpick -->")
            if d:
                def loc(m):
                    href = m.group(2)
                    if href.startswith(f"/{d}/"): return m.group(0)
                    target = href.lstrip("/")
                    cand = target + ("index.html" if target.endswith("/") or target == "" else "")
                    if target == "" : cand = "index.html"
                    if (d, cand) in translated: return f'{m.group(1)}/{d}/{target}"'
                    return m.group(0)
                # don't localise the language lists themselves
                html = re.sub(r"\n?\s*<!-- @(langs|langpick) -->.*?<!-- /@\1 -->", "", html, flags=re.S)
                html = re.sub(r'(href=")(/[^"#?]*)"', loc, html)
                html = re.sub(r"ct=(?!" + re.escape(d) + r"-)([A-Za-z0-9_-]+)", lambda m: "ct=" + (d + "-" + m.group(1))[:40], html)
                html = re.sub(r"utm_campaign%3D(?!" + re.escape(d) + r"-)", f"utm_campaign%3D{d}-", html)
                man[f"{d}/{rel}"] = sha(os.path.join(ROOT, rel))
                sm_urls.append(url_for(d + "/" + rel))
            if re.search(r"\s*</div>\s*</footer>", html):
                html = put_block(html, "langs", sw, r"\s*</div>\s*</footer>")
            if re.search(r'<nav class="nav">\s*<a class="brand"[^>]*>.*?</a>', html, flags=re.S):
                html = put_block(html, "langpick", pick, r'<nav class="nav">\s*<a class="brand"[^>]*>.*?</a>', before=False)
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
