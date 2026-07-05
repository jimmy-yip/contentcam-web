# contentcam-web

Static site for [contentcam.app](https://contentcam.app) — marketing, SEO/blog,
pricing, support/FAQ, and the privacy-policy URL required by the App Store and
Google Play. No build step, no dependencies, zero JavaScript — plain HTML/CSS
on GitHub Pages.

## Structure
- `index.html` — homepage (dual-format pitch, teleprompter, features, badges)
- `features/` — hub + `teleprompter/`, `dual-camera/`, `manual-controls/`
- `android/` — Android landing page (feature parity table)
- `pricing/` — plans + free-vs-premium table (update when prices change!)
- `support/` — FAQ (this URL is the App Store "Support URL")
- `press/` — press kit + canonical facts
- `blog/` — hub + posts, one directory per post
- `privacy.html` — full privacy policy (verbatim from the iOS repo)
- `404.html` — GitHub Pages picks this up automatically
- `llms.txt` / `llms-full.txt` — AI/LLM discovery files
- `sitemap.xml`, `robots.txt`, `site.webmanifest`, `favicon.ico`
- `styles.css` — shared styles (brand cyan `#25D0E5` on near-black)
- `ios/` — Meta-ads landing page (noindexed, do not link internally)

## Editing shared nav/footer (no templating — marker blocks)

Every page carries byte-identical blocks wrapped in markers:
`<!-- @head-common -->…<!-- /@head-common -->`, `<!-- @nav -->…<!-- /@nav -->`,
`<!-- @footer -->…<!-- /@footer -->`. To change the nav or footer everywhere,
edit ONE file (e.g. `404.html`), then propagate:

```sh
# from repo root — replaces the @footer block in every page with 404.html's version
perl -0777 -ne 'print $1 if /(<!-- \@footer -->.*<!-- \/\@footer -->)/s' 404.html > /tmp/block.html
for f in $(find . -name "*.html" ! -path "./ios/*" ! -name "404.html"); do
  perl -0777 -pi -e 'BEGIN{local $/; open F,"/tmp/block.html"; $r=<F>} s/<!-- \@footer -->.*<!-- \/\@footer -->/$r/s' "$f"
done
```

Swap `footer` for `nav` or `head-common` as needed. All shared-block URLs are
root-relative (`/features/`, `/assets/...`) so blocks work at any depth.

## Preview locally
```sh
cd contentcam-web && python3 -m http.server 8000
# open http://localhost:8000
```

## Deploy
`git push` to `main` — GitHub Pages serves it. The `.app` TLD is HSTS-preloaded,
so the site MUST be served over HTTPS (GitHub Pages does this automatically).

## After content changes, remember
1. Update `sitemap.xml` `<lastmod>` for changed pages.
2. Keep `llms-full.txt` in sync with major copy changes.
3. Prices changed? Update `/pricing/` copy AND its JSON-LD `offers`, plus the
   pricing rows in `llms.txt`/`llms-full.txt` and the comparison blog post.
