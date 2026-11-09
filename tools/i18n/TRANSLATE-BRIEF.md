# Translating a contentcam.app page (brief for translation agents)

Single pass, no separate review agent, so self-check carefully before finishing.

## Languages
| dir | html lang | Language | Store copy (terminology source) | Notes |
|---|---|---|---|---|
| de | de | German | de-DE.txt | du form (match store copy). Glossary ~/contentcam-android/tools/localization/localization-glossary-de.md. Keep "Dual Capture" |
| es | es | Spanish, neutral (LatAm first, natural in Spain) | es-MX.txt | tú. teléfono (celular only where natural). Glossary ~/contentcam/docs/localization-glossary-es.md. Apple: "Captura Dual" |
| fr | fr | French (France) | fr-FR.txt | vous unless store copy uses tu. Non-breaking space before : ? ! ; Glossary ~/contentcam/docs/localization-glossary-fr.md. Apple: "Double capture" |
| it | it | Italian | it.txt | match store copy register |
| ja | ja | Japanese | ja.txt | です/ます. Glossary ~/contentcam/docs/localization-glossary-ja.md. Gloss English mode names like 前後カメラ（Front/Back） as the store copy does |
| pt-br | pt-BR | Portuguese (Brazil) | pt-BR.txt | você. celular, câmera. Apple: "Captura Dupla" |
| id | id | Indonesian | id.txt | casual-polite, kamu. Glossary ~/contentcam/docs/localization-glossary-id.md |
| ko | ko | Korean | ko.txt | 해요체 unless the store copy uses 합니다체; match it. Natural Korean search phrasing (e.g. 가로세로 동시촬영, 전후면 카메라 동시 촬영, 듀얼카메라) |

Store copy files: ~/contentcam/docs/store-descriptions/v2.8.2/desc/<file>. Use its names for ContentCam's modes and
features exactly. Existing translated pages in ~/contentcam-web/<dir>/ show the established nav/footer wording and
style: open ONE of them (e.g. <dir>/blog/record-front-and-back-camera-same-time-iphone/index.html) and reuse its
nav, footer, CTA box and byline wording verbatim.

## Rules
- Source: ~/contentcam-web/<path>. Output: ~/contentcam-web/<dir>/<path> (create dirs).
  Public URL: https://contentcam.app/<dir>/<path without index.html>.
- Translate ALL human-visible text, <title>, meta description, og/twitter title+description, image alt text, and text
  fields inside JSON-LD (headline, description, name, FAQ question/answer, breadcrumb names). FAQ JSON-LD text must
  equal the visible FAQ text exactly.
- Keep HTML structure, classes, ids, marker comments (<!-- @nav --> etc.), scripts, images, and every number, price,
  date and fact. Do not add, drop or soften any claim. Never add anything negative about ContentCam.
- Set <html lang="...">, canonical, og:url and JSON-LD url/@id/mainEntityOfPage to the public URL. Add
  <meta property="og:locale" content="xx_YY"> if absent. Do NOT add hreflang or the language switcher (a script does it;
  if the source contains <!-- @hreflang --> or <!-- @langs --> blocks, drop those blocks entirely).
- Leave internal links (href="/...") and store links exactly as they are; a script localises them.
- Title, H1 and H2s: phrase them as the question a native speaker would really type into Google/an AI assistant, not
  a literal translation. Keep the year. If unsure, check Google autocomplete:
  `curl -s "https://suggestqueries.google.com/complete/search?client=firefox&hl=<lang>&q=<url-encoded phrase>"`.
- Product/app names stay as is (ContentCam, ReFrame, Snapchat, BeReal, etc.).
- Dates in local format. Natural native prose, no em dashes.
- Write the whole file with one write per language (do not write in pieces).

## Self-check (run after writing, fix anything it flags)
```
python3 ~/contentcam-web/tools/i18n/check_tr.py <path> <dir> [<dir> ...]
```
