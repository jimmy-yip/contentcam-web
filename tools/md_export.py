#!/usr/bin/env python3
"""Write a plain Markdown copy of every indexable English page, for AI crawlers (idea from odel.dev, 10 Nov 2026).

  blog/<slug>/index.html  ->  blog/<slug>.md      (served at https://contentcam.app/blog/<slug>.md)
  index.html              ->  index.md

Also adds <link rel="alternate" type="text/markdown" href="..."> to each page's <head>, and a "Markdown copies" list
to llms.txt. Idempotent. Run from anywhere: python3 tools/md_export.py   (build.py calls it at the end).
"""
import glob, html, json, os, re
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://contentcam.app"
LANG_DIRS = {"de", "es", "fr", "it", "ja", "pt-br", "id", "ko", "nl", "pl", "tr", "vi", "zh-hans", "zh-hant", "ru", "hi",
             "sv", "th", "ms", "da", "no", "fi", "pt-pt", "uk", "fil", "bn", "cs", "ro", "hu", "el"}
SKIP_TAGS = {"script", "style", "nav", "footer", "svg", "noscript", "form", "button", "video", "picture", "source"}
SKIP_CLASSES = ("crumbs", "cta", "related", "lang-switch", "store-badges", "share")


class MD(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out, self.skip, self.href, self.lists, self.row, self.rows, self.cell = [], 0, None, [], None, None, None
        self.pre = 0

    def w(self, s):
        if self.cell is not None:
            self.cell.append(s)
        else:
            self.out.append(s)

    def handle_starttag(self, t, a):
        a = dict(a)
        cls = a.get("class") or ""
        if self.skip:
            if t not in ("br", "img", "hr", "source", "input", "meta", "link"):
                self.skip += 1
            return
        if t in SKIP_TAGS or any(c in cls.split() for c in SKIP_CLASSES) or a.get("aria-hidden") == "true":
            if t not in ("br", "img", "hr", "source", "input"):
                self.skip = 1
            return
        if t in ("h1", "h2", "h3", "h4"):
            self.w("\n\n" + "#" * int(t[1]) + " ")
        elif t == "p":
            self.w("\n\n")
        elif t in ("ul", "ol"):
            self.lists.append([t, 0]); self.w("\n")
        elif t == "li":
            l = self.lists[-1] if self.lists else ["ul", 0]
            l[1] += 1
            self.w("\n" + "  " * (len(self.lists) - 1) + ("- " if l[0] == "ul" else f"{l[1]}. "))
        elif t in ("strong", "b"):
            self.w("**")
        elif t in ("em", "i"):
            self.w("*")
        elif t == "a":
            self.href = a.get("href"); self.w("[")
        elif t == "br":
            self.w("  \n")
        elif t == "table":
            self.rows = []
        elif t == "tr":
            self.row = []
        elif t in ("td", "th"):
            self.cell = []
        elif t == "blockquote":
            self.w("\n\n> ")
        elif t == "img" and a.get("alt"):
            pass  # decorative images skipped; alt text adds noise

    def handle_endtag(self, t):
        if self.skip:
            self.skip -= 1
            return
        if t in ("strong", "b"):
            self.w("**")
        elif t in ("em", "i"):
            self.w("*")
        elif t == "a":
            h = self.href or ""
            if h.startswith("/"):
                h = SITE + h
            self.w(f"]({h})" if h and not h.startswith("#") else "]")
            self.href = None
        elif t in ("ul", "ol") and self.lists:
            self.lists.pop(); self.w("\n")
        elif t in ("td", "th") and self.cell is not None and self.row is not None:
            self.row.append(re.sub(r"\s+", " ", "".join(self.cell)).strip().replace("|", "\\|")); self.cell = None
        elif t == "tr" and self.row is not None and self.rows is not None:
            self.rows.append(self.row); self.row = None
        elif t == "table" and self.rows:
            n = max(len(r) for r in self.rows)
            lines = ["| " + " | ".join(r + [""] * (n - len(r))) + " |" for r in self.rows]
            lines.insert(1, "|" + " --- |" * n)
            self.w("\n\n" + "\n".join(lines) + "\n"); self.rows = None

    def handle_data(self, d):
        if self.skip:
            return
        d = re.sub(r"\s+", " ", d)
        if d.strip() or (self.out and not self.out[-1].endswith((" ", "\n"))):
            self.w(d)


def convert(page_html):
    m = re.search(r"<article[^>]*>(.*?)</article>", page_html, re.S) or re.search(r"<main[^>]*>(.*?)</main>", page_html, re.S)
    if not m:
        return None
    p = MD(); p.feed(m.group(1))
    md = "".join(p.out)
    md = re.sub(r"[ \t]+\n", "\n", md)
    md = re.sub(r"\n{3,}", "\n\n", md)
    md = re.sub(r"\*\*\s*\*\*", "", md)
    return md.strip()


def meta(page_html, name):
    m = re.search(rf'<meta (?:name|property)="{name}" content="([^"]*)"', page_html)
    return html.unescape(m.group(1)) if m else ""


def main():
    os.chdir(ROOT)
    written = []
    for f in sorted(glob.glob("**/index.html", recursive=True)):
        top = f.split("/")[0]
        if top in LANG_DIRS or f.startswith(("node_modules", ".")):
            continue
        s = open(f, encoding="utf-8").read()
        if re.search(r'<meta name="robots" content="[^"]*noindex', s):
            continue
        body = convert(s)
        if not body or len(body) < 400:
            continue
        rel = os.path.dirname(f)
        md_path = (rel + ".md") if rel else "index.md"
        page_url = SITE + "/" + (rel + "/" if rel else "")
        title = html.unescape(re.search(r"<title>(.*?)</title>", s, re.S).group(1).strip())
        mod = meta(s, "article:modified_time")[:10] or meta(s, "article:published_time")[:10]
        head = [f"# {title}", "", f"Source: {page_url}"]
        if mod:
            head.append(f"Updated: {mod}")
        desc = meta(s, "description")
        if desc:
            head += ["", desc]
        if body.startswith("# "):
            body = body.split("\n", 1)[1].strip() if "\n" in body else ""
        out = "\n".join(head) + "\n\n" + body + "\n"
        if not os.path.exists(md_path) or open(md_path, encoding="utf-8").read() != out:
            open(md_path, "w", encoding="utf-8").write(out)
        link = f'<link rel="alternate" type="text/markdown" href="{SITE}/{md_path}">'
        if 'type="text/markdown"' not in s:
            s2 = s.replace("</head>", f"  {link}\n</head>", 1)
            open(f, "w", encoding="utf-8").write(s2)
        written.append((md_path, title))
    # llms.txt index
    p = "llms.txt"
    if os.path.exists(p):
        t = open(p, encoding="utf-8").read()
        t = re.sub(r"\n## Markdown copies\n.*", "", t, flags=re.S).rstrip() + "\n"
        t += "\n## Markdown copies\n\nEvery page below is also available as plain Markdown:\n\n"
        t += "".join(f"- [{ti}]({SITE}/{mp})\n" for mp, ti in written)
        open(p, "w", encoding="utf-8").write(t)
    print(f"md_export: {len(written)} markdown copies")


if __name__ == "__main__":
    main()
