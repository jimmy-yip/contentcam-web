# Italian (`it`) terminology and style sheet: contentcam.app

Italian for Italy (also serves Italian-speaking Switzerland). Built 15 Nov 2026 from:

- `tools/i18n/TRANSLATE-BRIEF.md` (it row: "match store copy register")
- Store copy `~/contentcam/docs/store-descriptions/v2.8.2/desc/it.txt` (terminology authority for ContentCam's own names)
- `~/contentcam/docs/store-metadata-localized.md` (Italian keyword decisions, §1 and §2 "Non-literal choices")
- `~/contentcam/docs/store-metadata-expansion.md` (Italian name/subtitle, Switzerland note)
- `~/contentcam/docs/localization-review.md` (Italian app review, device-tested; bugs such as *camera* = room)
- The live iOS app catalogue `~/contentcam/ContentCam/ContentCam/Resources/Localizable.xcstrings` (the `it` column), which gives the in-app button labels
- A scan of all 45 pages under `it/` (counts are visible text + meta/alt/JSON-LD, 15 Nov 2026)
- Apple Italia, Samsung Italia, Google and Snap Italian pages fetched 15 Nov 2026 (sources in §4)
- Google autocomplete, `hl=it&gl=it`, 15 Nov 2026

There is no `localization-glossary-it.md`; this sheet is the Italian glossary. Where this sheet and an older page disagree, this sheet wins. Where it disagrees with the store copy on a ContentCam feature name, the store copy wins; tell Jimmy if that ever happens.

---

## 1. Register, person, punctuation, typography

**Register: `tu`, informal, singular.** The store copy uses it throughout ("tocca per mettere a fuoco", "organizza i tuoi shooting", "scopri quanto puoi registrare") and so does the app ("Tocca per regolare…", "Consentilo in Impostazioni"). Never `Lei` or the plural `voi` (Samsung's manuals use *toccate*; do not copy that when quoting their steps, rewrite to *tocca*). Current pages: 0 `Lei`, 0 `voi` (the hits on *registrate* are past participles). Imperatives: *tocca, registra, apri, scegli, tieni premuto, scarica, prova*.

**Tone:** plain and direct, the store copy's voice. ContentCam is feminine (*l'app*: "Sviluppata da Jimmy", "Valutata 4,8"); never *il ContentCam*.

**Punctuation and typography**
- **No em dashes** (brief rule; current pages: 0). Use a colon, comma, parentheses or a new sentence. An en dash `–` is fine for ranges (`2500K–8000K`) and as an empty-cell marker in tables.
- **Quotation marks: caporali `«…»`** for quoted text, quoted UI strings and translated quotes; nested quotes `“…”`. This is the Italian editorial norm and what the app itself uses (`i file ora si chiamano «Front» e «Back»`). Never straight `"…"` in visible text. They need no escaping in JSON-LD.
- **UI labels the reader taps:** plain text with initial capital, no quotes, menu paths with ` > ` (Apple Italia's own style): *Impostazioni > Fotocamera > Registra video*. Exception: a multi-word Apple feature name may be quoted the way Apple does it the first time (*la modalità «Acquisizione doppia»*); after that, plain.
- **Sentence case** in titles and headings: `Come registrare con la fotocamera frontale e posteriore contemporaneamente su iPhone`, not Title Case.
- **Apostrophes:** typographic `’` or straight `'` are both acceptable; pages use straight `'`. Keep elisions correct: *un'app*, *l'app*, *un obiettivo*, *quest'anno*. Accent on capital E is `È`, not `E'`.
- **Spacing:** no space before `: ; ? !` (unlike French).

**Numbers**
- Decimal **comma**: `4,8`, `0,5x`, `29,97 fps`, `0,5s`, `31,6%`. (Store: "da 0,5s a 30s", "pulsanti 0,5x, 1x e 2x"; app: "4,8 · Amata dai creator".)
- Thousands **point**: `15.000 caratteri`, `50.000 download`, `1.999 $`. Four-digit numbers may also go without a separator (`1920`, `3840`), and always do in resolutions.
- Resolutions: `3840×2160`, `1920×1080` (multiplication sign, no spaces). Not `3840 x 2160`.
- Frame rate in running prose: `60 fps` (space; Apple Italia writes "24 fps", "a 120 fps"). Write `60fps` only when quoting the app UI or the store's Premium list verbatim.
- Zoom and speed-up: `0,5x`, `1x`, `2x`, `da 10x a 900x` (no space).
- Percent: `32%` (no space, matches the pages).
- Aspect ratios: `9:16`, `16:9`, `4:3`.

**Money**
- Amount first, comma decimal, symbol after a space: `4,99 $`, `59,99 $`, `1.999 $` (115 hits today). Use a non-breaking space between number and symbol where the HTML allows.
- Australian dollars: `3.499 A$`. Never convert prices.
- Not `$4,99`, not `4,99 US$` (see §6 #7).

**Dates:** `15 novembre 2026`; tables may use `15 nov 2026`. Months and weekdays lowercase. Byline pattern already live: *Di Jimmy, sviluppatore di ContentCam · 3 agosto 2026 · Aggiornato il 5 novembre 2026*. "As of" phrasing: *(novembre 2026)*.

**Fixed site wording (reuse verbatim):** rating line *Valutata 4,8 da 580+ creator su App Store e Google Play* (all 45 pages, consistent); CTA *Prova ContentCam gratis*; *Download gratuito su iPhone e Android*.

---

## 2. Mandated term table

| English concept | Use (it) | Avoid | Source / confidence |
|---|---|---|---|
| phone | **telefono**; **iPhone** when it is one | smartphone in prose (OK in a title if needed), cellulare, dispositivo for the reader's phone (*dispositivo* is fine in technical limits: "su questo dispositivo") | Store ("I tuoi video restano sul telefono"). Verified |
| camera (hardware) | **fotocamera** (pl. *fotocamere*) | **camera** (= *room*; the app review caught "Two bedrooms"), videocamera, telecamera (= CCTV/camcorder) | Store; localization-review bug #4. Verified. *parlare in camera* (to camera) is accepted creator jargon |
| front camera / back camera | **fotocamera frontale / fotocamera posteriore** | fotocamera davanti/dietro | Store ("la fotocamera frontale e quella posteriore"). Verified |
| front camera (Apple/Samsung wording) | **fotocamera anteriore** when describing Apple's or Samsung's own UI or quoting them; also usable in titles/H2s for search (§5) | — | Apple Italia ("dalla fotocamera anteriore"); Samsung IT manual ("Fotocamera anteriore"). Verified |
| front and back at the same time | **la fotocamera frontale e quella posteriore contemporaneamente**; *insieme* is fine in short titles | simultaneamente, allo stesso tempo (stiff, not what people type) | Store; store-metadata §2 ("contemporaneamente appears 10× in real Italian competitor copy"). Verified |
| both cameras | **entrambe le fotocamere** | tutte e due le camere | Autocomplete *registrare video con entrambe le fotocamere iphone/android*; ASO hint. Verified |
| selfie camera / a selfie | **il selfie** (masculine), *fotocamera selfie* | la selfie | Store ("passa al selfie"); 75 hits masculine, 0 feminine. Verified |
| lens | **obiettivo / obiettivi** | lente/lenti (eyeglass/contact lens; Italian for camera lens is *obiettivo*) | Store; app. Verified |
| wide / ultra wide (noun) | **grandangolo / ultra-grandangolo** | ultragrandangolo, ultra grandangolo | Store. Verified |
| wide / ultra wide (adjective) | **obiettivo grandangolare / ultra-grandangolare** | | App ("Obiettivo ultra-grandangolare"). Verified |
| portrait / landscape (orientation) | **verticale / orizzontale** (*in verticale*, *in orizzontale*) | ritratto, paesaggio (ASO notes: *paesaggio* drifts to garden apps; *Ritratto* is Apple's depth mode) | Store; store-metadata §1. Verified |
| portrait and landscape at once | **in verticale e in orizzontale contemporaneamente** | orizzontale e verticale (order flip, 0 hits; keep store order) | Store line 1. Verified |
| dual format | **i due formati / entrambi i formati**; section label **Doppio formato** | formato duale | Store ("Registra entrambi i formati"); pages. Verified |
| dual camera (generic concept) | **doppia fotocamera** | doppia camera (autocomplete = bike inner tube, double glazing, gestational sac), camera doppia, dual camera in prose | App Store name *ContentCam: Doppia Fotocamera*; autocomplete *doppia fotocamera iphone 17 / samsung / instagram*. Verified |
| take (one recording) | **il take / i take** (masculine, invariable) | la take, i takes, ripresa (collides; store-metadata §2) | Store; app ("%lld take"). Verified |
| shoot (filming session) | **shooting** (*i tuoi shooting*) | sessione | Store-metadata §2. Verified |
| clip | **la clip / le clip** (feminine, invariable) | il clip, i clip | Store ("le due clip affiancate"); 33 vs 7 hits. Verified |
| recording | **registrazione** | | Store |
| scene / project | **scena / progetto** | | Store; app |
| split screen | **schermo diviso** (*a schermo diviso*) | split screen in prose (OK only in a query-shaped heading, §5), schermo condiviso | Store; Samsung IT manual ("a schermo diviso"). Verified |
| picture in picture | **Picture in Picture** (capitalised, no hyphens) | picture-in-picture, PiP, immagine nell'immagine | Store; app; Apple Italia ("modalità Picture in Picture"). Verified |
| combine (two takes into one video) | **unire**; the feature is **Unisci** | combinare, fondere | Store ("Unisci: trasforma una registrazione…"); app. Verified |
| separate files | **file separati** (*file* invariable) | files, file distinti | Store. Verified |
| frame rate | **frame rate** (ContentCam); **frequenza dei fotogrammi** only when naming Apple's setting | velocità dei fotogrammi | Store ("Risoluzione e frame rate"); Apple Italia. Verified |
| frame (single image) | **fotogramma** (*taglia al fotogramma*) | frame (alone) | Store. Verified |
| crosshair | **crocino** (*crocino centrale*) | mirino (= viewfinder, a different thing), croce | Store; app. Verified |
| viewfinder | **mirino** | | Existing pages; correct |
| level (horizon guide) | **indicatore di livello**; in-app label **Livella** | | Store; app |
| shutter | **otturatore** | | Store |
| white balance / exposure / focus | **bilanciamento del bianco / esposizione / messa a fuoco** | | Store |
| manual controls | **controlli manuali** | | Store |
| trim | **tagliare / taglio** (*Revisione e taglio*, *Taglio in revisione*) | rifilare | Store |
| crop | **ritagliare / ritaglio** (*nessuno dei due è un ritaglio dell'altro*) | | Store. Keep trim ≠ crop |
| script (teleprompter) | **testo** (app label: *Testo*); **copione** is fine for a creator's script in prose | script | App ("Teleprompter Script" → *Testo*); pages use *copione* (13) naturally |
| teleprompter | **teleprompter** (invariable, masculine) | gobbo (TV slang, not searched for apps) | Store; autocomplete *app teleprompter gratis*. Verified |
| timelapse (ContentCam feature) | **Timelapse** | time-lapse (that is Apple's mode, §4) | Store |
| Settings | **Impostazioni** | Settings, Configurazione | App; Apple Italia. Verified |
| Photos app / library | **Foto** (app), **libreria** (*la libreria di Foto*); app label *Libreria foto* | rullino as the iPhone term (Apple retired *Rullino*; colloquial use is tolerated, see §7) | App; Apple Italia. Verified |
| Android gallery | **Galleria** | | Samsung IT manual. Verified |
| tap / press and hold / pinch | **tocca / tieni premuto / pizzica** | premi (only for physical buttons), clicca | Store. Verified |
| watermark | **filigrana** | watermark (only inside a quoted English IAP name) | Store. Verified |
| ads | **pubblicità** (*senza pubblicità*) | annunci, ads | Store; autocomplete *app senza pubblicità*. Verified |
| free | **gratis** (adverb/CTA); **gratuito/-a** as adjective (*download gratuito*, *prova gratuita*) | free | Store; app |
| free trial | **prova gratuita** (*7 giorni di prova gratuita*) | prova gratis, trial | App; pages (21, consistent). Verified |
| one-time purchase / lifetime | **acquisto unico** (noun); **paghi una volta sola**; **accesso a vita**; plan label **A vita** | pagamento unico; vitalizio | App ("acquisto unico per l'accesso a vita"); store ("una volta sola per l'accesso a vita"). *una tantum* is acceptable as a modifier (*pagamento una tantum*; autocomplete *app a pagamento una tantum*) but never as the name of our plan |
| subscription (annual / monthly / weekly) | **abbonamento annuale / mensile / settimanale** | sottoscrizione | App. Verified |
| unlock / upgrade | **sbloccare**; button **Passa a Premium** | | Store ("CON PREMIUM SBLOCCHI"); app |
| Restore purchases | **Ripristina acquisti** | | App |
| download | **scaricare**; CTA **Prova ContentCam gratis** / *Download gratuito* | | Pages |
| reaction video | **video reaction** (also *le reaction*); *video di reazione* is acceptable in body text | | Autocomplete *video reaction*, *come fare un video reaction*; *video reazione* completes to the TV quiz *Reazione a catena*. Verified |
| creator | **creator** (invariable) | creatori, creativi | App ("Amata dai creator"); pages (114) |
| indie developer | **sviluppatore indipendente** | sviluppatore solo | Store; app |
| supports (a feature) | **è compatibile con**, **funziona su**; *supporta* is tolerated (Apple Italia itself says "modelli che supportano") | | Apple Italia |

---

## 3. ContentCam mode and feature names (exactly as the it store copy writes them)

The iOS app is fully localised in Italian, and some **in-app button labels are shorter than the store names**. Use the store name in prose. When telling the reader which button to tap, give the in-app label in parentheses: *la modalità Frontale e posteriore (nell'app: Fronte/Retro)*. **Never gloss with English** (*Front/Back*, *Dual Lens*): an Italian user's app does not show those words.

| English (app/store) | Name on the website (store copy) | In-app label (it) | Notes |
|---|---|---|---|
| Single Lens | **Obiettivo singolo** | *1 obiettivo* | Capital O when it names the mode |
| Dual Lens | **Doppio obiettivo** | *2 obiettivi* | *modalità Doppio obiettivo* |
| Front/Back | **Frontale e posteriore** | *Fronte/Retro* (Premium list in app: *Fronte e retro*) | *modalità Frontale e posteriore*, capital F when it names ContentCam's mode; lowercase *frontale e posteriore* only for the generic concept or other apps |
| Front Camera | **Fotocamera frontale** | *Fotocamera frontale* | Mode name; same words as the generic noun, so capitalise when it is the mode |
| Normal Camera (ex Stock Cam) | **Fotocamera normale** | | Store-metadata §2: literal *Stock Cam* means nothing in Italian |
| Photo mode | **Modalità foto** | *Modalità Foto* | |
| Front and back photo | **Foto frontale e posteriore** | | Store |
| Shutter button next to record | **pulsante di scatto** | | Store |
| Combine | **Unisci** | *Unisci* | Premium feature; *Unisci Fronte/Retro* in app |
| Picture in Picture / split screen layouts | **Picture in Picture**, **schermo diviso** | *Picture in Picture*, *Schermo diviso* | |
| Resolution and frame rate | **Risoluzione e frame rate** | | |
| Manual controls | **Controlli manuali**: esposizione, bilanciamento del bianco, ISO, otturatore | | |
| Focus & exposure | **Messa a fuoco ed esposizione** | *Blocca fuoco ed esposizione* | |
| Teleprompter | **Teleprompter** | | Not glossed |
| Stabilisation and HDR | **Stabilizzazione e HDR** | | |
| Timelapse | **Timelapse** | *Modalità timelapse* | Not glossed |
| Guides | **Guide**: indicatore di livello, crocino centrale, indicatore audio | *Livella*, *Crocino* | |
| Zoom | **Zoom**: pulsanti 0,5x, 1x e 2x, ghiera | | |
| Projects, scenes and takes | **Progetti, scene e take** | | |
| Recording folder | **Cartella registrazioni** | *Cartella registrazioni* | |
| Review and trim | **Revisione e taglio**; Premium item **Taglio in revisione** | *Taglio in revisione* | pricing page's *Taglio prima di salvare* is a paraphrase; prefer the store name |
| Space estimate | **Stima dello spazio** | | |
| Crash protection | **Protezione dai crash** | | |
| Thermal monitoring | **Monitoraggio termico** | | |
| Unlimited projects | **Progetti illimitati** | | |
| Premium | **Premium** (capital P) | | |
| Plans | **Annuale**, **Mensile**, **A vita** | same | |

---

## 4. Platform names in Italian

| Platform / feature | it form to use | Source / status |
|---|---|---|
| Apple: Dual Capture | **Acquisizione doppia** (Apple quotes it: *la modalità «Acquisizione doppia»*). Gloss the English once per page if helpful: *Acquisizione doppia (Dual Capture)* | **Verified.** support.apple.com/it-it/guide/iphone/iph61f49e4bb/ios: "Registrare video con “Acquisizione doppia” … tocca il pulsante “Acquisizione doppia” … Per disattivare “Acquisizione doppia”". Model list: support.apple.com/it-it/guide/iphone/glos3842gv5b/ios, title "Modelli che supportano “Acquisizione doppia” per i video". Autocomplete *acquisizione doppia iphone 17/16/15* is strong; *dual capture iphone* also completes in Italy, so the gloss earns its place |
| Apple: steps | *Apri Fotocamera, seleziona la modalità Video, tocca [controlli], quindi tocca il pulsante Acquisizione doppia* | Verified (same page) |
| Apple: Camera app | **Fotocamera** (*l'app Fotocamera*) | Verified |
| Apple: Settings path | **Impostazioni > Fotocamera > Registra video** | Verified: support.apple.com/it-it/guide/iphone/iphc1827d32f/ios |
| Apple: other settings | *FPS automatico*, *Riduci FPS con luce scarsa*, *Registra suono stereo*, *Registra suono* (*Audio spaziale*, *Stereo*, *Mono*), *Video HDR*, *Blocca fotocamera*, *Stabilizzazione ottimizzata*, *Blocca il bilanciamento del bianco*, *Registra slow motion* | Verified (same page) |
| Apple: frame rate | *frequenza dei fotogrammi* | Verified (Apple Italia) |
| Apple: modes | **Video**, **Cinema** (*modalità Cinema*), **Slo-mo** (*slow motion*), **Time-lapse**, **modalità Azione**, **Ritratto** | Verified (iph61f49e4bb text: "effetto cinematografico, slow motion e time-lapse e usare la modalità Azione") |
| Apple: front camera | *fotocamera anteriore* | Verified (iphc1827d32f) |
| Apple: Photos | **Foto** (app) | Verified |
| Apple: PiP multitasking | *modalità Picture in Picture* | Verified (iPhone guide TOC: "Multitasking con la modalità Picture in Picture"). This is the video-playback feature, not a camera layout |
| Apple: Apple Account | *Apple Account* (English in Italian guide) | Verified (TOC) |
| Samsung: Dual recording | **Doppia registrazione** (*modalità Doppia registrazione*) | **Verified**: Samsung Galaxy S25 FE Italian user manual (p. 55): "Modalità Doppia registrazione … Nell'elenco delle modalità di scatto, toccate ALTRO → DOPPIA REGISTRAZIONE." Autocomplete *doppia registrazione samsung (s24 ultra)* |
| Samsung: path | **Fotocamera > Altro > Doppia registrazione** | Verified (manual). One UI 8.5 relocation to Video mode: unverified in Italian |
| Samsung: Director's View | **Vista da regista** (gloss *(Director's View)* once) | **Unverified officially.** Samsung Community IT ("seleziona vista da regista", "modalità video regista"), autocomplete *vista da regista samsung*. No Samsung Italia support page found. Write *Vista da regista (Director's View)* |
| Samsung: Camera / Gallery apps | **Fotocamera**, **Galleria** | Verified (manual) |
| Samsung: front camera | *fotocamera anteriore* | Verified (manual) |
| Google: Pixel Camera app | **Fotocamera Pixel** | **Verified**: Google Play title "Fotocamera Pixel" (hl=it); support.google.com/googlecamera title "Guida di Fotocamera Pixel" |
| Google: Android concurrent cameras | *fotocamere simultanee* (descriptive) | No UI label |
| Snapchat: Dual Camera | **la doppia fotocamera di Snapchat** (lowercase, as Snap writes it) | **Verified** for Snap's Italian newsroom: newsroom.snap.com/it-IT/dual-camera ("Oggi presentiamo la doppia fotocamera… quattro layout: verticale, orizzontale, picture in picture e ritaglio"). In-app Italian label **unverified** |
| Snapchat: Snaps, Stories, Spotlight, Memories, Lenses | *Snap*, **Storie**, *Spotlight*, *Ricordi* (unverified), *Lenti* (unverified) | Storie + Spotlight verified in the same newsroom post |
| Instagram: Dual | **Dual** (*Dual di Instagram*), describe as *la doppia fotocamera di Instagram* in headings | In-app Italian label unverified; Meta's name is "Dual". Autocomplete: *doppia fotocamera instagram*, *effetto doppia fotocamera instagram* |
| Instagram: Reels, Stories | **Reels** (product), *un reel*; **Storie** | Reels: store copy. Storie: common Italian UI, unverified here |
| TikTok: Duet / Stitch / Green Screen | **Duetto**, **Stitch**, **Green Screen** | **Unverified** (support.tiktok.com is JS-rendered). *Duetto* is the widely used Italian label and already on the site; keep *Stitch* and *Green Screen* in English until checked in the Italian app |
| YouTube: Shorts | **Shorts** | Unchanged |
| BeReal: Memories | *Memories* (BeReal does not localise it in quoted help-centre titles) | Unverified for in-app Italian |
| Stores | **App Store**, **Google Play** (*l'App Store*, *su Google Play*) | Unchanged |

---

## 5. Native search phrasing for titles and H2s (Google autocomplete, `hl=it&gl=it`, 15 Nov 2026)

**Front + back camera.** The phrase Italians type is *anteriore*, not *frontale*:
- fotocamera anteriore e posteriore contemporaneamente (+ iphone)
- video con fotocamera anteriore e posteriore (+ iphone)
- foto con fotocamera anteriore e posteriore (+ iphone / samsung)
- registrare video con entrambe le fotocamere (+ iphone / android)
- fotocamera frontale e posteriore; iphone 17 fotocamera frontale e posteriore (fewer completions)
- *registrare con fotocamera frontale e posteriore*, *registrare con due fotocamere*: no completions

Rule: body copy and the mode name stay **frontale e posteriore** (store, app). In H1/H2/meta of front+back pages, use *anteriore e posteriore* or *entrambe le fotocamere* at least once where it reads naturally, e.g. *Come fare un video con fotocamera anteriore e posteriore su iPhone*. Today the 45 pages use *anteriore* 0 times, so this is the biggest search gap.

**Dual camera**
- doppia fotocamera iphone 17 / iphone / samsung / iphone 16 / instagram / iphone 15
- come fare video con doppia fotocamera (+ iphone / samsung / iphone 16); fare video con doppia fotocamera iphone
- come attivare la doppia fotocamera (+ iphone / iphone 17)
- foto doppia fotocamera iphone; foto con doppia fotocamera samsung
- video doppia fotocamera (+ iphone); app doppia fotocamera
- dual camera iphone 17 / samsung / android / instagram / tiktok (English also completes)
- doppia fotocamera instagram; filtro / effetto doppia fotocamera instagram; doppia fotocamera tiktok (low)

**Apple / Samsung built-ins**
- acquisizione doppia iphone (+ 17 / 16 / 16 pro / 15 / 17 pro max); acquisizione doppia samsung; acquisizione doppia facetime
- dual capture iphone (+ 16 / 15 / 17 / 14)
- doppia registrazione samsung (+ s24 / s24 ultra); doppia registrazione iphone
- vista da regista samsung / iphone (low)
- iphone duo (prezzo / uscita / recensioni)

**Portrait + landscape:** no completions for any phrasing (*video verticale e orizzontale*, *registrare in verticale e orizzontale*, *… contemporaneamente*). Low-volume concept in Italian; use the store's *in verticale e in orizzontale contemporaneamente* and lean on *TikTok e YouTube* in the heading (*Come registrare per TikTok e YouTube con un solo video*). *video verticale iphone / instagram / youtube* and *come registrare video orizzontale* exist.

**Split screen / other**
- video split screen (+ app / capcut / iphone / instagram); split screen iphone; schermo diviso iphone (Apple multitasking intent)
- video con schermo diviso; video affiancati; mettere due video affiancati; capcut video affiancati
- unire due video (+ iphone / android / samsung); app per unire due video iphone
- come fare un video reaction; video reaction app; video reaction tiktok / instagram
- app teleprompter gratis (+ android / iphone); teleprompter iphone
- cambiare fotocamera durante video iphone
- time lapse iphone (+ 17 / 16 / 15)

**Heading patterns that match these:** *Come fare un video con fotocamera anteriore e posteriore su iPhone (2026)*, *Quali iPhone hanno l'Acquisizione doppia?*, *Doppia registrazione Samsung: come registrare con entrambe le fotocamere*, *Come fare video con doppia fotocamera su Instagram*, *Come mettere due video affiancati a schermo diviso*.

---

## 6. Inconsistencies found across the 45 existing `it` pages (17)

Counts are occurrences / pages on 15 Nov 2026. "Right" is what new and revised pages must use.

1. **Apple's feature name left in English.** *Dual Capture* 302 / 25 pages (heaviest: vs/apple-dual-capture 53, blog/iphone-17-dual-capture-limitations 41, iphone-duo-camera 21, record-front-and-back-camera-iphone-15-16 20, dual-camera-effect 17, doubletake-not-working-alternatives 15, switch-camera-while-recording-iphone 15). *Acquisizione doppia*: 0. Right: **Acquisizione doppia**, with *(Dual Capture)* once per page. English stays inside cited English source titles.
2. **Invented Apple name.** `vs/lookout` "Doppia ripresa" (2, in meta/alt). Right: **Acquisizione doppia**.
3. **Samsung names.** English *Dual recording* 40 / 2 (record-front-and-back-camera-samsung-galaxy 27, record-front-and-back-camera-same-time-android 13) and *Director's View* 25 / 4 (same two + snapchat-front-and-back-camera, switch-camera-while-recording-iphone), while `blog/snapchat-front-and-back-camera` already says *Doppia registrazione* (4). Right: **Doppia registrazione** (Samsung IT manual) and **Vista da regista (Director's View)**.
4. **Google Pixel camera app.** *Pixel Camera* 33 / 5 (record-front-and-back-camera-google-pixel 17, record-front-and-back-camera-same-time-android 8, record-portrait-and-landscape-video-same-time-android 6, record-portrait-and-landscape-video-same-time-iphone 1, snapchat-front-and-back-camera 1). Right: **Fotocamera Pixel**.
5. **Snapchat Dual Camera in English.** ~72 feature mentions / 13 pages (snapchat-front-and-back-camera 26, film-reaction-video-phone 10, dual-camera-effect 7, bereal-style-photo-without-bereal 5, instagram-dual-camera-missing 5, take-photo-front-and-back-camera-same-time 4, film-kid-reaction-and-what-they-see 4, split-screen-video-iphone 3, how-to-do-dual-camera-on-tiktok 2, switch-camera-while-recording-iphone 2, best-front-and-back-dual-camera-apps 2, vs/2cam 1, record-front-and-back-camera-same-time-iphone 1). Right: **la doppia fotocamera di Snapchat** (Snap's Italian newsroom). Rival app titles that contain "Dual Camera" (e.g. *Dual Camera: Shot Front & Back*) stay as published.
6. **Quote marks.** Straight `"…"` on ~25 pages (worst: dual-camera-app-without-ads 25, vs/dualcam 15, vs/dualtake 14, iphone-4k-front-and-back-camera-same-time 13, iphone-duo-camera 12, record-front-and-back-camera-samsung-galaxy 11, take-photo-front-and-back-camera-same-time 11); curly `“…”` on 7 (record-front-and-back-camera-google-pixel, vs/2cam, vs/apple-dual-capture, vs/detail, vs/dualgram, vs/lookout, vs/mixcam); caporali `«…»` on 4 (android, dual-camera-effect, film-kid-reaction-and-what-they-see, snapchat-front-and-back-camera). Right: **«…»**.
7. **Price format.** `4,99 $` 115 / 5 (dual-camera-app-one-time-purchase, phone-teleprompter-apps-compared, vs/2cam, vs/detail, dual-format-recording-apps-compared) vs `2,99 US$` 19 / 4 (dual-camera-app-without-ads 14, record-front-and-back-camera-iphone-15-16, split-screen-video-iphone, vs/dualcam) vs `$0,99` 4 / 1 (doubletake-not-working-alternatives). Right: **4,99 $**.
8. **fps spacing.** `60fps` 60 / 18 (home 7, record-front-and-back-camera-iphone-15-16 9, record-front-and-back-camera-same-time-iphone 5, android 4, features 4…) vs `60 fps` 292 / 22. Right in prose: **60 fps**; `60fps` only when quoting the app or the store list.
9. **Resolution sign.** `3840 x 2160` 26 / 8 (iphone-4k-front-and-back-camera-same-time 12, vs/dualcam 7, vs/dualgram 2, record-front-and-back-camera-google-pixel, vs/2cam, vs/dualtake, vs/lookout, vs/mixcam) vs `1080×1920` 57 / 9. Right: **3840×2160**.
10. **Mode name in lowercase.** *modalità frontale e posteriore* for ContentCam's own mode 32 / 9 (bereal-style-photo-without-bereal 12, dual-camera-app-without-ads 5, doubletake-not-working-alternatives 4, record-front-and-back-camera-iphone-15-16 3, record-front-and-back-camera-same-time-android 3, record-portrait-and-landscape-video-same-time-android 2, dual-camera-effect, record-front-and-back-camera-same-time-iphone, snapchat-front-and-back-camera) vs *modalità Frontale e posteriore* 106 / 29; *obiettivo singolo* lowercase as the mode 2 / 2 (home, record-portrait-and-landscape-video-same-time-iphone). Right: **Frontale e posteriore**, **Obiettivo singolo** capitalised when naming ContentCam's mode.
11. **English glosses on mode names.** *Frontale e posteriore (Front/Back)* 5 / 3 (vs/2cam, vs/apple-dual-capture ×3, vs/mixcam); *Doppio obiettivo (Dual Lens)* 2 / 2 (doubletake-not-working-alternatives, vs/lookout); English *Front/Back* elsewhere 6 / 4, while take-photo-front-and-back-camera-same-time correctly glosses with the Italian button *(nell'app: Fronte/Retro)*. Right: gloss only with the **in-app Italian label** (*Fronte/Retro*, *1 obiettivo*, *2 obiettivi*), never English.
12. **Picture in Picture spelling.** *picture-in-picture* 25 / 8 (vs/dualcam 7, iphone-duo-camera 6, doubletake-not-working-alternatives 3, home 2, film-kid-reaction-and-what-they-see 2, vs/detail 2, vs/dualgram 2, vs/2cam 1) vs *Picture in Picture* 114 / 30. Right: **Picture in Picture**.
13. **Clip gender.** *il clip / un clip* 7 / 3 (how-to-do-dual-camera-on-tiktok 5, vs/2cam 1, vs/apple-dual-capture 1) vs *la clip / le clip* 33 / 14. Right: **la clip** (store copy: "le due clip").
14. **One-time purchase wording.** *acquisto unico* 29 / 10, *una tantum* 42 / 8, *una volta sola* 19 / 12, and *pagamento unico* 3 / 3 (best-front-and-back-dual-camera-apps, vs/2cam, vs). Right: **acquisto unico** for our plan, *paghi una volta sola* as the verb phrase; *una tantum* only as a modifier for rivals' prices; drop *pagamento unico*.
15. **Ultra-wide spelling.** *ultragrandangolo* 1 / 1 (doubletake-not-working-alternatives) vs *ultra-grandangolo* 39 / 14. Right: **ultra-grandangolo**.
16. **"watermark" in our own prose.** `blog/split-screen-video-iphone` "niente watermark" (1). Right: **filigrana** (other *watermark* hits are inside quoted English IAP names and are fine).
17. **smartphone vs telefono.** *smartphone* 23 / 7 (vs/mixcam 6, vs/lookout 5, switch-camera-while-recording-iphone 3, vs/2cam 3, vs/apple-dual-capture 3, vs/detail 2, vs/dualgram 1) vs *telefono* 183 / 37. Right: **telefono** (store copy); soft fix, change when a page is next edited.

Consistent already (no action): `tu` register (0 `Lei`/`voi`), no em dashes, `Valutata 4,8 da 580+ creator` on all 45 pages, decimal comma (`0,5x`, `607,5`, `31,6%`), thousands point (`15.000`, `50.000`, `1.999 $`), Italian date format (303 full dates, 0 English months in visible text), `fotocamera` (no *camera* = room errors; *in camera* is the to-camera idiom), `filigrana`, `senza pubblicità`, `il selfie` (75, 0 *la selfie*), `i take` (0 *takes*), `schermo diviso`, `Unisci`, `Impostazioni`, `prova gratuita`, `contemporaneamente` (154, 0 *simultaneamente*), `Doppio obiettivo` / `Obiettivo singolo` / `Frontale e posteriore` as the store names, `il teleprompter`, `Duetto` on the TikTok page.

Gap (not an inconsistency): *fotocamera anteriore* appears 0 times, though it is Apple's and Samsung's Italian wording and the dominant autocomplete phrasing (§5).

---

## 7. False friends and calque traps for this subject

- **camera** = *room* (or *Camera dei deputati*). The hardware is always *fotocamera*. The app review caught "Two bedrooms. Two perspectives." *doppia camera* autocompletes to bike inner tubes, double glazing and a gestational sac.
- **fronte e retro / Fronte/Retro**: it is the in-app button label and an ASO keyword, but as a phrase it means **both sides of a document**: autocomplete *foto fronte retro* → *carta d'identità*, *passaporto*; *app fronte retro* → scanner and duplex printing apps. Use it only as the button label; the prose name is *Frontale e posteriore*.
- **doppia registrazione** alone also means double-entry booking in accounting (*doppia registrazione IVA / fattura / contratto di locazione*, all in autocomplete). Always anchor it: *Doppia registrazione di Samsung*, *modalità Doppia registrazione*.
- **registrare video** autocompletes almost entirely to *screen recording* (*registrare video schermo pc / android / iphone*). Headings need *fotocamera* or *doppia fotocamera* in them.
- **lente** is an eyeglass/contact/magnifying lens; a camera lens is *obiettivo*. And **obiettivo** also means *goal*: avoid "il tuo obiettivo" meaning your aim on a page about lenses; say *lo scopo* or rephrase.
- **ritratto / paesaggio** for portrait/landscape orientation: wrong sense (*paesaggio* = scenery and drifts to garden apps in App Store search; *Ritratto* is Apple's depth-of-field mode, which ContentCam does not have). Orientation is *verticale / orizzontale*.
- **scena**: ContentCam has a *Scene* entity (Progetti, scene e take). Do not use *scena* loosely for "the view in front of you" where it could read as the app object; *quello che hai davanti*, *l'inquadratura* (the store does say *la tua scena* for the back-camera view; fine when there is no project context).
- **ripresa**: means both a shot/footage and "recovery/resumption". Not the word for ContentCam's *take*; fine for generic filming (*riprese*, *riprendere*).
- **take** is masculine and invariable: *il take, i take, due take*. Never *la take*, never *takes*.
- **clip** is feminine and invariable: *la clip, le clip*.
- **selfie** is masculine in Italian: *il selfie, un selfie*.
- **video reazione** autocompletes to the TV quiz *Reazione a catena*; use *video reaction*.
- **mirino** (viewfinder) ≠ **crocino** (crosshair). The store copy's guide is *crocino centrale*.
- **frame** alone reads as English; use *fotogramma* for a single image and *frame rate* (ContentCam) or *frequenza dei fotogrammi* (Apple's setting) for the rate.
- **Rullino** (camera roll) is retired Apple wording (now *Foto* / *libreria*); the app review fixed it in the app. Fine as a colloquial word when talking about uploading from the phone to Instagram or Snapchat, but say *libreria di Foto* for iPhone instructions and *Galleria* for Samsung.
- **attualmente** = currently (not "actually" = *in realtà*); **eventualmente** = if needed (not "eventually" = *alla fine*, *prima o poi*); **realizzare** = make/carry out (to "realise" = *rendersi conto*); **libreria** = bookshop in general Italian but is Apple's term for the photo library, so keep it there; **supportare** = to support/bear; for features *è compatibile con* is cleaner.
- **contemporaneamente vs simultaneamente:** the latter is grammatical but stiff and unsearched; Italian competitor copy uses *contemporaneamente* (10×).
- **gratis vs gratuito:** *gratis* is an adverb/invariable adjective (*è gratis*, *prova gratis*), *gratuito/-a* agrees (*prova gratuita*, *download gratuito*). Do not write *prova gratis* where the app says *prova gratuita*.
- **"$" placement:** Italian puts the symbol after the amount (`4,99 $`). `$4,99` reads as an untranslated English string.
- **Billion:** Italian *bilione* is 10^12; English "billion" = *miliardo*.
- **"Gratis per sempre"** overclaims; translate exactly what the English says (free tier = *gratis, take illimitati, senza account*, single lens, HD).
- **Duo / dual SIM:** *iPhone Duo* is Apple's foldable; *dual SIM* is unrelated; *iphone dual tim* appears in autocomplete. Never shorten *Acquisizione doppia* to "Duo".
