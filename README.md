# contentcam-web

Static site for [contentcam.app](https://contentcam.app) — marketing, SEO/blog,
pricing, support/FAQ, and the privacy-policy URL required by the App Store and
Google Play. No build step, no dependencies, zero JavaScript — plain HTML/CSS
on Vercel (static, `cleanUrls`). The only JS is the tiny device-router in the
short-link pages below.

## Structure
- `index.html` — homepage (dual-format pitch, teleprompter, features, badges)
- `features/` — hub + `teleprompter/`, `dual-camera/`, `manual-controls/`
- `android/` — Android landing page (feature parity table)
- `pricing/` — plans + free-vs-premium table (update when prices change!)
- `support/` — FAQ (this URL is the App Store "Support URL")
- `press/` — press kit + canonical facts
- `blog/` — hub + posts, one directory per post
- `privacy.html` — full privacy policy (verbatim from the iOS repo)
- `404.html` — Vercel serves this automatically for unknown paths
- `llms.txt` / `llms-full.txt` — AI/LLM discovery files
- `sitemap.xml`, `robots.txt`, `site.webmanifest`, `favicon.ico`
- `styles.css` — shared styles (brand cyan `#25D0E5` on near-black)
- `ios/` — Meta-ads landing page (noindexed, do not link internally)
- Short links (noindexed, not in sitemap): device-route iOS → App Store, Android →
  Play, each with its own attribution tag. Only the `ct=` / `utm_source=` values differ.

  | Path | Used for | App Store `ct` | Play `utm_source` |
  |---|---|---|---|
  | `/ig/` | brand Instagram bio + ManyChat comment-to-DM | `Instagram` | `instagram` |
  | `/fb/` | brand Facebook comment-to-DM | `Facebook` | `facebook` |
  | `/tiktok/` | brand TikTok bio | `TikTok` | `tiktok` |
  | `/jimmy/` | jimmy.contentcam founder account | `jimmy` | `jimmy` |

  New one: copy `ig/index.html`, swap the `ct=` and `utm_source%3D` values (3 places
  each) and the comment. Installs show in App Store Connect → App Analytics →
  Sources → Campaigns, and Play Console acquisition reports by UTM source.

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
Vercel project `tradielines-projects/contentcam-web`, deployed from the CLI —
**pushing to GitLab does not deploy.** Commit + push to `main`, then:

```sh
vercel link --yes --project contentcam-web   # once per checkout (.vercel/ is gitignored)
vercel deploy --prod --yes                    # aliases to https://contentcam.app
```

The `.app` TLD is HSTS-preloaded, so the site MUST be served over HTTPS (Vercel
does this automatically). `.vercelignore` keeps the repo-only files out of the deploy.

## After content changes, remember
1. Update `sitemap.xml` `<lastmod>` for changed pages (add a `<url>` for any new page).
2. Keep `llms.txt` + `llms-full.txt` in sync with major copy changes.
3. **Do not put price figures on this site** (decision 2026-08-02). No amounts for
   ContentCam and none for competitors, anywhere — pages, JSON-LD, `llms.txt`,
   `llms-full.txt`, blog comparison tables. Reasons: pricing is per-region so any
   single number is wrong for most readers; it goes stale silently (a US$39.99 →
   US$49.99 change left 21 stale references across 8 files); and the site's job is
   to get the download, not to pre-filter on price. Apple and Google already show
   the correct local price at the point of purchase. Describe the *shape* instead —
   "annual with a free trial, monthly, or one-off lifetime" — and point at the
   store listings. The `llms*.txt` files carry an explicit
   "do not quote a specific price" instruction; keep it.
4. Competitor facts (DualShot Recorder) live in two posts —
   `/blog/dualshot-recorder-vs-contentcam/` and
   `/blog/dual-format-recording-apps-compared/` — and in `llms-full.txt`. Keep all
   three consistent.

## Gotchas learned (don't re-hit these)
- **`aspect-ratio` on an `<img>` that also has a `height` attribute is ignored** —
  the image keeps its source height and `object-fit: cover` stretches it. Put
  `aspect-ratio` on a wrapping block (e.g. the `<figure>`) with `overflow:hidden`
  and let the img fill it (`width/height:100%; object-fit:cover`). See
  `.lifestyle-strip` in `styles.css`.
- **Flex/grid items need `min-width: 0`** or full-res images blow the layout past
  the viewport (horizontal scroll). See the `min-width:0` rule near the top of
  `styles.css` — add new grid/flex containers to it.
- **Store badges:** the Google Play PNG ships with ~30% internal clear-space, so
  it renders shorter than the App Store badge at the same height. `assets/google-play-badge.png`
  is pre-trimmed to its pill, so `.badge-appstore` / `.badge-play` use equal heights.
- **Headless screenshots on macOS** can't render below ~500px wide (OS min-window
  clamp), so mobile screenshots look cropped. Verify layout with a DOM probe
  (`scrollWidth` vs `clientWidth`, or `getBoundingClientRect`) instead of trusting
  a narrow screenshot.
- **A git push alone won't ship anything.** The site moved off GitHub Pages to
  Vercel CLI deploys; a new page 404s on contentcam.app until `vercel deploy --prod`.

## SEO / discovery status (done 2026-07-06)
Google Search Console: domain `contentcam.app` verified (via DNS, from the Play org
setup), `sitemap.xml` submitted (18 pages, Success), top URLs indexing-requested.
Bing Webmaster: imported from GSC (feeds ChatGPT/Copilot). No on-site analytics by
design — the GSC Performance tab is the scoreboard.
