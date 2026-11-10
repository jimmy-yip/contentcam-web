#!/usr/bin/env python3
"""Mechanical check of translations vs the English source.
Usage: python3 tools/i18n/check_tr.py <path e.g. blog/x/index.html> <lang dir> [<lang dir> ...]
       python3 tools/i18n/check_tr.py --all   (every translated page in the manifest + any new ones)
"""
import json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CODES = {"de": "de", "es": "es", "fr": "fr", "it": "it", "ja": "ja", "pt-br": "pt-BR", "id": "id", "ko": "ko",
         "nl": "nl", "pl": "pl", "tr": "tr", "vi": "vi", "zh-hans": "zh-Hans", "zh-hant": "zh-Hant", "ru": "ru",
         "hi": "hi", "sv": "sv", "th": "th", "ms": "ms", "da": "da", "no": "no", "fi": "fi", "pt-pt": "pt-PT", "uk": "uk"}


def count(tag, html):
    return len(re.findall(rf"<{tag}[\s>]", html))


def visible_faq(html):
    return [re.sub(r"\s+", " ", re.sub("<[^>]+>", "", q)).strip() for q in re.findall(r"<h3[^>]*>(.*?)</h3>", html, re.S)]


def strip_blocks(h):
    return re.sub(r"<!-- @(hreflang|langs) -->.*?<!-- /@\1 -->", "", h, flags=re.S)


def check(rel, d):
    src = strip_blocks(open(os.path.join(ROOT, rel), encoding="utf-8").read())
    p = os.path.join(ROOT, d, rel)
    if not os.path.exists(p):
        return [f"MISSING {d}/{rel}"]
    t = strip_blocks(open(p, encoding="utf-8").read())
    errs = []
    url = f"https://contentcam.app/{d}/" + (rel[: -len("index.html")] if rel.endswith("index.html") else rel)
    if f'<html lang="{CODES[d]}"' not in t:
        errs.append("html lang wrong")
    if f'rel="canonical" href="{url}"' not in t:
        errs.append(f"canonical != {url}")
    if f'og:url" content="{url}"' not in t and 'og:url' in src:
        errs.append("og:url wrong")
    for tag in ("h2", "table", "tr", "li", "a", "img", "script"):
        a, b = count(tag, src), count(tag, t)
        if a != b and not (tag == "a" and abs(a - b) <= 2):
            errs.append(f"<{tag}> {a} vs {b}")
    for m in ("@nav", "/@nav"):
        if f"<!-- {m} -->" in src and f"<!-- {m} -->" not in t:
            errs.append(f"marker {m} lost")
    srch = sorted(set(re.findall(r'href="(/[^"]*)"', src)))
    trh = sorted(set(re.findall(r'href="(/[^"]*)"', t)))
    # build.py localises hrefs; compare with the /<d>/ prefix stripped
    trh_n = sorted(set(re.sub(rf"^/{d}/", "/", h) for h in trh))
    if srch != trh_n:
        errs.append(f"internal hrefs differ: missing {sorted(set(srch)-set(trh_n))[:5]} extra {sorted(set(trh_n)-set(srch))[:5]}")
    for blk in re.findall(r'<script type="application/ld\+json">(.*?)</script>', t, re.S):
        try:
            j = json.loads(blk)
        except Exception as e:
            errs.append(f"JSON-LD invalid: {e}")
            continue
        s = json.dumps(j, ensure_ascii=False)
        for node in (j.get("@graph") or [j]):
            if node.get("@type") == "FAQPage":
                qs = [q["name"].strip() for q in node["mainEntity"]]
                vis = re.sub(r"\s+", " ", re.sub("<[^>]+>", " ", re.sub(r"<script.*?</script>", "", t, flags=re.S)))
                vis = vis.replace("&amp;", "&").replace("&nbsp;", " ").replace("\u00a0", " ")
                for q in qs:
                    if q.replace("\u00a0", " ") not in vis:
                        errs.append(f"FAQ JSON-LD question not in visible text: {q[:60]}")
        if "contentcam.app/blog/" in s and f"contentcam.app/{d}/" not in s and '"BreadcrumbList"' in s:
            pass
    if "—" in t and "—" not in src:
        errs.append("em dash added")
    # leftover English: long ASCII-only sentences in <p>/<li>/<h2> (skip for Latin langs: check common English words)
    body = re.sub(r"<(script|style)[^>]*>.*?</\1>", "", t, flags=re.S)
    eng = re.findall(r">([^<]{40,})<", body)
    common = re.compile(r"\b(the|and|with|you|your|this|that|which|because|recording)\b", re.I)
    left = [e.strip() for e in eng if len(common.findall(e)) >= 4]
    if left:
        errs.append(f"WARN (ok if quoted source titles) possible English left ({len(left)}): {left[0][:80]}")
    return errs


def main():
    a = sys.argv[1:]
    if not a:
        print(__doc__); sys.exit(1)
    pairs = []
    if a[0] == "--all":
        for d in CODES:
            base = os.path.join(ROOT, d)
            if not os.path.isdir(base):
                continue
            for r, _, fs in os.walk(base):
                for f in fs:
                    if f.endswith(".html"):
                        rel = os.path.relpath(os.path.join(r, f), base)
                        if os.path.exists(os.path.join(ROOT, rel)):
                            pairs.append((rel, d))
    else:
        pairs = [(a[0], d) for d in a[1:]]
    bad = 0
    for rel, d in pairs:
        e = check(rel, d)
        if e:
            bad += 1
            print(f"✗ {d}/{rel}")
            for x in e:
                print("   ", x)
    print(f"{len(pairs) - bad}/{len(pairs)} OK")


if __name__ == "__main__":
    main()
