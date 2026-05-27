# contentcam-web

Static landing page + privacy policy for [contentcam.app](https://contentcam.app).
No build step, no dependencies — plain HTML/CSS. Serves the website Google Play
(and the App Store) require, and hosts the privacy-policy URL.

## Files
- `index.html` — landing page (hero, features, privacy summary, support)
- `privacy.html` — full privacy policy (verbatim from the iOS repo)
- `styles.css` — shared styles (brand cyan `#25D0E5` on near-black)
- `assets/icon.png` — app icon
- `CNAME` — custom domain for GitHub Pages (`contentcam.app`)

## Before going live
- In `index.html`, replace the App Store `href` placeholder
  (`id0000000000`) with the real App Store URL.

## Preview locally
```sh
cd contentcam-web && python3 -m http.server 8000
# open http://localhost:8000
```

## Deploy
See the deploy + Search Console verification steps provided separately.
The `.app` TLD is HSTS-preloaded, so the site MUST be served over HTTPS
(both GitHub Pages and Cloudflare Pages do this automatically).
