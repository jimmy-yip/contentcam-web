#!/usr/bin/env python3
"""Segment-based translation builder for one page (first used for vs/dualcam, 12 Nov 2026).

  python3 tools/i18n/section-swap/segbuild.py extract vs/dualcam      # writes seg/<page>/template.html + en.json
  python3 tools/i18n/section-swap/segbuild.py build vs/dualcam de     # reads seg/<page>/de.json (same length as en.json)

Translators only produce a JSON list of strings (same order as en.json; inline <strong>/<a> kept).
The page shell (head, nav, footer, CTA box) comes from the language's existing translation of the page,
or, if none exists, from SKELETON_FALLBACK (a sibling page in that language), with paths swapped.
Afterwards run: python3 tools/i18n/build.py   (hreflang, link localisation, sitemap).
Last two segments are always <title> and meta description.
"""
import json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
SEG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "seg")
SITE = "https://contentcam.app"
SKELETON_FALLBACK = {"vs/dualcam": "vs/dualgram"}
CRUMB = {"vs/dualcam": "DualCam"}

def rd(p): return open(p, encoding="utf-8").read()
def wr(p, s):
    os.makedirs(os.path.dirname(p), exist_ok=True); open(p, "w", encoding="utf-8").write(s)

def extract(page):
    t = rd(os.path.join(ROOT, page, "index.html"))
    a = t[t.index("      <h1>"):t.index("</article>")]
    cta = re.search(r'      <div class="post-cta">.*?\n      </div>\n', a, re.S).group(0)
    a = a.replace(cta, "@@CTA@@\n")
    segs = []
    def sub(m):
        segs.append(m.group(3)); return f"{m.group(1)}@@{len(segs)-1}@@</{m.group(2)}>"
    a = re.sub(r"(<(h1|h2|h3|p|li|td|th|figcaption)(?: [^>]*)?>)(.*?)</\2>", sub, a, flags=re.S)
    def alt(m):
        segs.append(m.group(1)); return f'alt="@@{len(segs)-1}@@"'
    a = re.sub(r'alt="([^"]+)"', alt, a)
    segs.append(re.search(r"<title>(.*?)</title>", t).group(1))
    segs.append(re.search(r'<meta name="description" content="([^"]*)"', t).group(1))
    d = os.path.join(SEG, page.replace("/", "_"))
    wr(os.path.join(d, "template.html"), a)
    wr(os.path.join(d, "en.json"), json.dumps(segs, ensure_ascii=False, indent=0))
    print(len(segs), "segments")

def clean(x):
    x = re.sub(r"<[^>]+>", "", x)
    for a, b in (("&amp;", "&"), ("&ldquo;", "“"), ("&rdquo;", "”"), ("&quot;", '"'), ("&nbsp;", " ")):
        x = x.replace(a, b)
    return " ".join(x.split())

def build(page, lang):
    d = os.path.join(SEG, page.replace("/", "_"))
    en = json.load(open(os.path.join(d, "en.json")))
    tr = json.load(open(os.path.join(d, f"{lang}.json")))
    assert len(tr) == len(en), f"{lang}: {len(tr)} segments, expected {len(en)}"
    if lang == "fr":
        tr = [re.sub(r" ([:?!;»])", "\u00a0\\1", x).replace("« ", "«\u00a0") for x in tr]
    for i, (e, x) in enumerate(zip(en, tr)):
        for tag in ("<strong>", "<a ", "</a>"):
            assert e.count(tag) == x.count(tag), f"{lang} seg {i}: {tag} count differs"
        assert "—" not in x, f"{lang} seg {i}: em dash"
    out = os.path.join(ROOT, lang, page, "index.html")
    src = out if os.path.exists(out) else os.path.join(ROOT, lang, SKELETON_FALLBACK[page], "index.html")
    sk = rd(src)
    if src != out:
        old = SKELETON_FALLBACK[page]
        sk = sk.replace(f"/{old}/", f"/{page}/").replace(f"/{old}.md", f"/{page}.md").replace(f"vs-{old.split('/')[-1]}", f"vs-{page.split('/')[-1]}")
    url = f"{SITE}/{lang}/{page}/"
    cta = re.search(r'      <div class="post-cta">.*?\n      </div>\n', sk, re.S).group(0)
    body = rd(os.path.join(d, "template.html"))
    body = re.sub(r"@@(\d+)@@", lambda m: tr[int(m.group(1))].replace('"', "&quot;") if f'alt="@@{m.group(1)}@@"' in m.string[max(0, m.start()-5):m.end()+2] else tr[int(m.group(1))], body)
    body = body.replace("@@CTA@@\n", cta)
    s = sk.index("      <h1>"); e = sk.index("</article>")
    t = sk[:s] + body + sk[e:]
    title, desc = clean(tr[-2]), tr[-1]
    t = re.sub(r"<title>.*?</title>", lambda m: f"<title>{title}</title>", t, count=1)
    for k in ("name", "property"):
        for f, v in (("description", desc), ("og:title", title), ("og:description", desc), ("twitter:title", title), ("twitter:description", desc)):
            if (k == "name") == (f in ("description",) or f.startswith("twitter")):
                t = re.sub(rf'<meta {k}="{f}" content="[^"]*">', lambda m: f'<meta {k}="{f}" content="{v}">', t)
    t = re.sub(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{url}">', t)
    t = re.sub(r'<meta property="og:url" content="[^"]*">', f'<meta property="og:url" content="{url}">', t)
    t = re.sub(r'(<div class="crumbs">.*?›[^›]*›\s*)[^<]*(</div>)', lambda m: m.group(1) + CRUMB[page] + m.group(2), t, count=1, flags=re.S)
    # JSON-LD
    art = t[t.index("      <h1>"):t.index("</article>")]
    qa = []
    m4 = re.search(r"<h2>([^<]*4K[^<]*)</h2>\s*<p>(.*?)</p>", art, re.S)
    if m4: qa.append((clean(m4.group(1)), clean(m4.group(2))))
    faq = art[art.index("<h3>"):]
    qa += [(clean(q), clean(a)) for q, a in re.findall(r"<h3>(.*?)</h3>\s*<p>(.*?)</p>", faq, re.S)]
    imgs = re.findall(r'<img src="(/assets/[^"]+)" alt="([^"]+)"[^>]*>\s*<figcaption>(.*?)</figcaption>', art)
    m = re.search(r'(<script type="application/ld\+json">)(.*?)(</script>)', t, re.S)
    o = json.loads(m.group(2))
    g = o.get("@graph", [o])
    g = [n for n in g if n.get("@type") != "FAQPage"]
    for n in g:
        if n.get("@type") == "WebPage":
            n.update({"@id": url, "url": url, "name": title, "description": clean(desc), "dateModified": "2026-11-12",
                      "image": [f"{SITE}/assets/og/og-blog.jpg"] + [{"@type": "ImageObject", "contentUrl": SITE + u, "description": clean(a), "caption": clean(c)} for u, a, c in imgs]})
            n.pop("mainEntityOfPage", None)
        if n.get("@type") == "BreadcrumbList":
            last = n["itemListElement"][-1]; last["name"] = CRUMB[page]; last["item"] = url
    g.append({"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in qa]})
    o = {"@context": "https://schema.org", "@graph": g}
    t = t[:m.start()] + m.group(1) + "\n" + json.dumps(o, ensure_ascii=False, indent=2) + "\n  " + m.group(3) + t[m.end():]
    wr(out, t)
    left = [x for x in re.findall(r"[Dd]ualgram", t)]
    print(lang, "ok", "(new page)" if src != out else "(updated)", f"faq={len(qa)} imgs={len(imgs)}", "LEFTOVER dualgram!" if left else "")

if __name__ == "__main__":
    if sys.argv[1] == "extract": extract(sys.argv[2])
    else:
        for l in sys.argv[3:]: build(sys.argv[2], l)
