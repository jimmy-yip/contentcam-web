# German (de) terminology and style sheet for contentcam.app

Built 15 Nov 2026 for native reviewers and translation agents working on `/de/`. It covers every page under
`contentcam-web/de/` (45 pages, scanned in full).

**Order of authority.** (1) The iOS store copy, `contentcam/docs/store-descriptions/v2.8.3/desc/de-DE.txt`
(v2.8.2 is the brief's file; v2.8.3 is the live successor and uses the same terms). (2) The shipped iOS German UI,
`contentcam/ContentCam/ContentCam/Resources/Localizable.xcstrings` (de). (3) The Android glossary,
`contentcam-android/tools/localization/localization-glossary-de.md`, which is binding **for Android UI strings
only**. Where it conflicts with the store copy on the website (trimmen vs kürzen, Front/Rück vs Front und Rück,
Galerie vs Mediathek), this sheet says which one to use in which context. (4) Official Apple and Samsung German pages,
cited inline. (5) Google autocomplete (hl=de, gl=de, checked 15 Nov 2026).

Confidence labels: **verified** means checked against a source on 15 Nov 2026. **Store** means taken verbatim from
the store copy or the shipped UI. **Autocomplete** means a real German query. **Unverified** means it is not confirmed.

---

## 1. Register, person and typography

### Register
- **du, always.** That covers imperatives (*Nimm, Tippe, Wähle, Öffne*), possessives (*dein, deine*) and pronouns
  (*dich, dir*). It matches the store copy ("Nimm Videos im Hochformat und Querformat gleichzeitig auf"), the iOS UI,
  the Android glossary §1, and Apple Germany's own register ("Filme dich und deine Umgebung gleichzeitig mit Front-
  und Rückkamera", apple.com/de/iphone-17). Never use *Sie/Ihr/Ihnen* as address. All 45 pages pass: the one
  capitalised "Ihre" (`blog/iphone-4k-front-and-back-camera-same-time`) opens a sentence and means "its".
- Lowercase *du/dein* mid-sentence. Capitalised *Du/Dein* is letter style and is not used here.
- Tone: casual-competent, like a creator explaining to a creator. Use short sentences and the active voice.
  Avoid nominal style (*die Durchführung der Aufnahme*). Prefer verbs (*aufnehmen, filmen, drehen*).
- Address the founder voice in first person singular (*ich*) where the English says "I", as the existing pages do.

### Spelling
- de-DE. Write **ß** (Weißabgleich, größer, schließen), never ss. Umlauts are literal UTF-8, never ae/oe/ue.
- Capitalise every noun, including nominalised verbs (*beim Filmen, das Aufnehmen*).
- Hyphenate compounds that contain a brand, a model, a number or an acronym: *iPhone-Modelle, Galaxy-S24-Serie,
  4K-Datei, 4:3-Sensor, HD-Video, Front/Rück-Aufnahme, Dual-Kamera-App, Bild-in-Bild-Fenster*. Close native
  compounds without a hyphen: *Rückkamera, Frontkamera, Ultraweitwinkel, Splitscreen, Hochformat, Zeitraffer*.
- Suspended hyphen (Ergänzungsstrich) for shared halves: *Front- und Rückkamera, Hoch- und Querformat, Jahres- oder
  Monatsabo*. This is correct German and is the store copy's own form.

### Punctuation
- **Quotation marks: „…“** (German low-high). Every page already uses them (347 pairs, no “…” or straight quotes in
  visible text). Use them for quoted UI labels too, as Apple does: „Einstellungen“ > „Kamera“ > „Formate“.
  Nested quotes are ‚…‘.
- **No em dash (—).** None are present. In ranges, use a closed en dash only between numbers (*2500–8000 K*) or
  write *bis* (*0,5 bis 30 s*, which is the store copy's form). Don't use a spaced en dash as a sentence dash: use a
  comma, colon or full stop instead. Note `pricing` uses "–" as an empty-cell marker in its comparison table, which is
  fine.
- Only one space after a full stop. Use a comma before *dass, weil, wenn, ob* and relative clauses (German comma
  rules are not optional).
- Use a colon after a label and capitalise what follows only if it is a full sentence. The store copy does this
  (*Absturzschutz: stellt unterbrochene Aufnahmen … wieder her*).

### Numbers, units, currency, dates
- Use a decimal comma: *0,5x, 2,99, 31,6 %*. Use a thousands point: *50.000+ Downloads, 4.300 Bewertungen,
  1.999 US-Dollar*. Never write *0.5x* or *4,300* in German prose.
- Zoom: *0,5x / 1x / 2x*. That is the store copy form (no space, latin x). Pixel dimensions use *3840 x 2160*.
- Frame rate: **60 fps**, lowercase with a space (store copy: "mit 24, 25, 30, 50 oder 60 fps"). Not *60fps* or
  *60 FPS* outside verbatim quotes.
- Resolution: *1080p, 4K, HD*. They stay as written. *4K-Video* is hyphenated in compounds.
- Percent: **31,6 %** with a space (DIN 5008, as the existing pages do everywhere).
- Seconds: *0,5 bis 30 s*. Multipliers: *10- bis 900-fach*.
- Currency (USD figures from US store listings): **2,99 US$**, with the amount first, a decimal comma and a space.
  Write it out as *US-Dollar* only in running prose about a launch price. Never use *$2.99* or *2,99 $* (a bare $ is
  ambiguous for AUD/CAD readers). Use € only for real euro prices (the German App Store lists euros).
  `blog/doubletake-not-working-alternatives` uses "$0.99 bis $9.99", which is wrong (see §6).
- Dates: **3. November 2026** in prose. In dense tables, *3. Nov. 2026*. No leading zero, no English month names in
  visible text or JSON-LD text. Version stamps keep their dots (*iOS 2.9, Android 2.7.1*).

---

## 2. Mandated terms

| English concept | Use (de) | Avoid / forbidden | Source / confidence |
|---|---|---|---|
| front camera | **Frontkamera** | Vorderkamera (as body standard), vordere Kamera, Frontcam | Store; Apple DE ("Center Stage Frontkamera"); protect.json. Verified |
| back / rear camera | **Rückkamera** | Hauptkamera (that is the main *wide* lens; see §7), rückseitige Kamera, Heckkamera | Store; Apple DE ("Front- und Rückkamera"). Verified |
| front and back camera | **Front- und Rückkamera** | *Vorder- und Rückkamera* as the page's running term (see §5: allowed once as a search phrasing) | Store; Apple DE iPhone 17 page; Samsung DE. Verified |
| selfie camera | **Selfie-Kamera** (hyphenated) | Selfiekamera | Store ("Wechsle zur Selfie-Kamera"). Store |
| at the same time | **gleichzeitig** | zeitgleich (acceptable, but not in titles), zur selben Zeit (wordy) | Store; protect.json; autocomplete ("… gleichzeitig" is the head of every top query). Autocomplete |
| both cameras | **beide Kameras** | | terms.json "beide kameras gleichzeitig"; autocomplete. Autocomplete |
| portrait (orientation/format) | **Hochformat** | Porträt, Portrait (that means the Portrait *mode*), Hochkant- in compounds in prose | Store; Apple DE ("vom Hoch- ins Querformat"). Verified |
| landscape | **Querformat** | Landschaft, Landscape | Store; Apple DE. Verified |
| portrait + landscape | **Hoch- und Querformat** / *Hochformat und Querformat* | Hochformat- und Querformat (redundant; used on 2 pages) | Store. Store |
| vertical / horizontal (as format words) | **Hochformat / Querformat**. Use *vertikal/horizontal* only for "vertical feed / vertical field of view" (*vertikaler Feed, volles vertikales Bildfeld*) | *vertikales Video* as a title term | Store; autocomplete has no "vertikal und horizontal filmen" demand. Autocomplete |
| hochkant / quer (colloquial) | Allowed in prose and in one H2 for search (*Video hochkant und quer*). In-app labels are **Hochkant / Quer** (iOS UI: "PORTRAIT" = "HOCHKANT") | | iOS xcstrings de; autocomplete "video hochkant" strong. Store |
| dual camera (generic) | **Dual-Kamera** (*Dual-Kamera-App, Dual-Kamera-Video*) | Dualkamera, Dual Kamera (unhyphenated in prose). *Doppelkamera* is the iOS store title term: OK once for search, not as the running term | Play title "ContentCam: Dual-Kamera-Video"; iOS title "ContentCam: Doppelkamera"; autocomplete "dual kamera iphone/handy/samsung", "doppelkamera iphone". Autocomplete |
| take (one numbered recording) | **Take / Takes** | Aufnahme where a numbered take is meant | Store ("unbegrenzt viele Takes"); Android glossary. Store |
| in one take ("one shoot") | **in einem Dreh** / *ein Dreh* | in einer Aufnahme (ambiguous), in einem Durchgang | Store subtitle "Hochformat+Querformat, 1 Dreh". Store |
| recording (act or file) | **Aufnahme / Aufnahmen** | Take (where a generic recording is meant) | Store; Android glossary. Store |
| to record | **aufnehmen** (also *filmen*, *drehen* in creator prose) | eine Aufnahme machen, aufzeichnen (technical), recorden | Store; Android glossary. Store |
| file / two separate files | **Datei / zwei getrennte Dateien** | separate Dateien (OK but not the store form), Files | Store. Store |
| lens | **Objektiv** | Linse for the camera (see §7: *in die Linse schauen* is OK as an idiom) | Store; Android glossary. Store |
| wide / ultra wide | **Weitwinkel / Ultraweitwinkel** (one word) | Ultra-Weitwinkel. That is Apple's spelling ("Ultra-Weitwinkelkamera"), so keep it only inside a verbatim Apple quote | Store; Apple DE guide. Verified |
| telephoto | **Teleobjektiv** | Tele-Linse | iOS UI ("Teleobjektiv (Beta)"). Store |
| picture-in-picture | **Bild-in-Bild** | Picture-in-Picture, PiP, Bild-im-Bild | Store; iOS UI; Apple DE. Store |
| split screen | **Splitscreen** | Split-Screen, Split Screen, geteilter Bildschirm (*Split Screen* is fine inside a quoted search query, since autocomplete leans English: "split screen video erstellen") | Store; iOS UI ("Split" = "Splitscreen"). Store |
| side by side | **nebeneinander** (*Ansicht nebeneinander*) | Nebeneinander-Ansicht, Side-by-side | Store 2.8.3 notes. Store |
| combine (Front & Back into one video) | **kombinieren** / Button **„Kombinieren“** | zusammenfügen, mergen | Store; iOS UI. Store |
| framing / crop of the frame | **Bildausschnitt** / *Ausschnitt* | Rahmen, Framing | Store ("keines ist ein Ausschnitt des anderen"). Store |
| to crop (spatial) | **zuschneiden** / *Beschnitt* | kürzen (that is length) | iOS UI ("zugeschnitten", "stärkerer Beschnitt"). Store |
| to trim (shorten a clip) | Website prose: **kürzen** (*Kürzen im Review*, *Video kürzen*). Exact in-app label: **„Trimmen“** | zuschneiden (that is crop) | Store ("Ansehen und Kürzen", "Kürzen im Review"); iOS UI "Trimmen" / Android glossary "trimmen"; autocomplete "video kürzen iphone" (many), "video trimmen iphone" (none). Autocomplete |
| viewfinder | **Sucher** | Viewfinder, Vorschaufenster | Store; Apple DE. Store |
| preview | **Vorschau** | Preview | Android glossary; Apple. Store |
| frame rate | **Bildrate** | Framerate, Bildwiederholrate (that is the display) | Store; iOS UI. Store |
| resolution | **Auflösung** | | Store. Store |
| exposure / white balance / shutter speed | **Belichtung / Weißabgleich / Verschlusszeit** | Shutter-Speed. *ISO* stays | Store. Store |
| manual controls (ContentCam feature) | **Manuelle Steuerung** | Manuelle Kamerasteuerung, Profi-Kamerasteuerung (collides with Apple's *Kamerasteuerung*; see §7) | Store; footer label. Store |
| stabilisation | **Stabilisierung** (*Bildstabilisierung* only when quoting a spec sheet) | Stabilisation | Store. Store |
| time-lapse | **Zeitraffer**. The first mention on a page may gloss it as *Zeitraffer (Timelapse)*, as the store does | Time-Lapse, Zeitlupe (that is slow-mo) | Store; Apple DE. Store |
| teleprompter | **Teleprompter** | Prompter, Souffleur | Store. Store |
| audio level meter | **Audioanzeige** (ContentCam feature name). *Pegel* is fine in generic prose | Aussteuerung | Store ("Audioanzeige, die bei Übersteuerung rot pulsiert"). Store |
| level / crosshair | **Wasserwaage / Fadenkreuz** | | Store. Store |
| shutter button (photo) | **Auslöser** | Shutter | Store; Apple DE ("Auslösertaste"). Store |
| record button | **Aufnahmetaste** | Record-Button | Apple DE guide. Verified |
| the phone (generic) | **Smartphone** in body text; **iPhone** / **Android-Smartphone** when platform-specific | *Handy* in body text (allowed once in a title/H2/FAQ question where it matches a query, e.g. "Dual-Kamera auf dem Handy"), *Telefon* | Play copy; Android glossary; autocomplete "dual kamera handy". Autocomplete |
| photo library (iPhone) | **Mediathek** (*in deiner Mediathek in der App „Fotos“*, or simply *in der Fotos-App*) | Galerie (iPhone context), Kamerarolle (old) | Apple DE guide ("in deiner Mediathek in der App „Fotos“"). Verified |
| photo library (Android) | **Galerie** (Samsung) / **Google Fotos** | Mediathek (Android context) | Android glossary. Samsung app name high-confidence, not re-checked |
| ContentCam's own take library | **Take-Liste** | Mediathek (collides with the Apple Photos library) | Store ("in derselben Take-Liste"). Store |
| reaction video | **Reaktionsvideo** | Reaction-Video, Reaction Video | Autocomplete ("reaktionsvideo erstellen"). Autocomplete |
| creators | **Creators** | Creatorn, Ersteller, Kreative | Android glossary; footer. Store |
| watermark | **Wasserzeichen** | Watermark (except inside a quoted English IAP name) | Store. Store |
| free | **kostenlos** (main); *gratis* as rhythm variant | umsonst | Store uses both. Store |
| free trial | **kostenlose Testphase** / CTA **„Gratis testen“** | Probeabo, Probezeit, Trial | iOS UI; store 2.8.3. Store |
| one-time purchase / lifetime | **Einmalkauf** (*mit dauerhaftem Zugang*) | Lifetime-Kauf, Lifetime-Option, Lifetime-Plan, lebenslang. The App Store IAP is literally named „Premium: Lebenslang“, so quote that only when naming the store line item | Store; iOS UI ("Lifetime" = "Einmalkauf"); apps.apple.com/de IAP list. Verified |
| subscription / annual / monthly | **Abo**, *Jahresabo*, *Monatsabo*, *jährlich / monatlich* | Abonnement (OK in legal/support text only), Subscription | Store; iOS UI. Store |
| no account needed | **ohne Konto** | ohne Account, ohne Registrierung | Store. Store |
| ads | **Werbung**. The store label is **„Enthält Werbung“** | Ads, Anzeigen | Store; App Store DE. Store |
| App Store / Google Play | **App Store** (as a name); compounds *App-Store-Eintrag*. **Google Play** | Play Store (colloquial; `android` uses it once), Apple Store (that is the retail shop) | Store. Store |
| settings | **Einstellungen** (*Einstellungen > Kamera*) | Settings, Einstellungen-App | Apple DE; Android glossary. Verified |
| save | **speichern** in ContentCam and Android text. Apple's own German UI says *sichern* (*„Kameraeinstellungen sichern“*), so keep it only when quoting Apple | sichern for ContentCam | Android glossary; Apple DE guide. Verified |
| tap | **tippen** / *Fingertipp* / *mit einem Tippen* | Tipp (that means hint or tip), klicken (on touchscreens) | Store; Android glossary. Store |
| crash protection / storage calculator / thermal monitor | **Absturzschutz / Speicherplatz-Rechner / Temperaturüberwachung** | | Store. Store |

Never translated (store + Android glossary): ContentCam, Premium, Teleprompter, Timelapse (in the gloss only), 4K,
HD, HDR, ISO, fps, EV, Apple Log, Reels, Shorts, TikTok, Snapchat, BeReal, competitor app names.

---

## 3. ContentCam mode and feature names (exactly as the store copy writes them)

| Mode | First mention on a page | Later mentions | Compact / compound form | In-app label (iOS de UI) |
|---|---|---|---|---|
| Single Lens | **Ein Objektiv (Single Lens)** | *Ein Objektiv*, *im Modus Ein Objektiv* | n/a | "Ein Objektiv" |
| Dual Lens (iPhone only) | **Zwei Objektive (Dual Lens)** | *Zwei Objektive*, *im Modus Zwei Objektive* | n/a | "Zwei Objektive", chip "2 OBJEKTIVE" |
| Front & Back | **Front und Rück (Front/Back)** on iOS-only pages; Play copy writes **Front und Rück (Front & Back)**. On cross-platform web pages use *(Front/Back)* | *Front und Rück*, *der Modus Front und Rück* | **Front/Rück-** in compounds: *Front/Rück-Aufnahme, Front/Rück-Takes* | "Front/Rück", "FRONT/RÜCK", "Front/Rück kombinieren" |
| Front camera mode | **Frontkamera** | | | |
| Regular camera | **Normale Kamera** | | | |
| Combine | **Kombinieren** (*eine Front/Rück-Aufnahme zu einem Video kombinieren, als Bild-in-Bild oder Splitscreen*) | | | "Kombinieren" |
| Photo mode | **Fotomodus**; *Fotos mit Front und Rück (Front/Back)* | | | "FOTO" |
| Other features | **Teleprompter, Zeitraffer (Timelapse), Manuelle Steuerung, Auflösung und Bildrate, Fokus und Belichtung, Stabilisierung und HDR, Hilfen im Bild, Zoom, Projekte, Szenen und Takes, Aufnahmeordner, Ansehen und Kürzen, Speicherplatz-Rechner, Absturzschutz, Temperaturüberwachung, Kürzen im Review, Hintergrundunschärfe (Beta)** (Android), **Apple Log** | | | "Teleprompter", "Timelapse", "Apple Log" |
| Premium heading | **PREMIUM SCHALTET FREI** | | | |
| Builder line | *Gemacht von Jimmy, Solo-Entwickler in Sydney.* | | | |

Rules:
- Gloss the English mode name in brackets **once per page**, at first mention, then use the German name alone.
  Don't gloss in titles or H1 unless the English name is itself the search target.
- Never write *Front & Back* or *Front/Back* alone as ContentCam's mode name in German prose. Never write
  *Vorne/Hinten* as the mode name (the Android glossary rejects it). *vorne und hinten* is fine as descriptive search
  wording (*die Kameras vorne und hinten*), and protect.json requires those words on store pages.
- *Front/Rück* alone (no "und") is the UI label. In prose, it appears only in compounds and in step-by-step UI
  instructions (*tippe im Modus-Umschalter auf Front/Rück*).
- "Lifetime" in ContentCam context is always **Einmalkauf**.

---

## 4. Platform names in German

| Platform / feature | German UI name | Use on the site | Source / confidence |
|---|---|---|---|
| Apple: Dual Capture video | **„Doppelte Aufnahme“** (Kamera > Video > options icon > „Doppelte Aufnahme“) | **Dual Capture (auf deutschen iPhones „Doppelte Aufnahme“)** at first mention, then *Dual Capture* (brief: keep "Dual Capture"). In any **step-by-step instruction**, the tap target must be „Doppelte Aufnahme“, because a German iPhone never shows "Dual Capture" | support.apple.com/de-de/guide/iphone/iph61f49e4bb/ios ("Tippe auf [Symbol] und anschließend auf „Doppelte Aufnahme“"); apple.com/de/iphone-17-pro ("Videos mit Doppelter Aufnahme, um mit Front- und Rückkamera gleichzeitig zu drehen"). Autocomplete: both "dual capture iphone" and "doppelte aufnahme iphone 17" are live queries. **Verified** |
| Apple: Camera Control (hardware button, iPhone 16+) | **Kamerasteuerung** | Only for the physical button | apple.com/de ("Greif mit der Kamerasteuerung schneller auf Kameratools zu"). **Verified** |
| Apple: the icon tapped before „Doppelte Aufnahme“ | Apple's German guide shows only an icon, with no text label | Say *tippe oben auf das Symbol für die Kameraoptionen* or *tippe auf das Optionen-Symbol*, never *Taste für die Kamerasteuerung* | Apple DE guide (icon only). Label **unverified** |
| Apple: Kamera app, modes | App „Kamera“, Modus „Video“, „Slo-Mo“, „Kino“ (Kinomodus), Zeitraffer, „Porträt“ | | Apple DE guide. **Verified** |
| iOS Settings > Camera | „Einstellungen“ > „Kamera“ > „Formate“ / „Video aufnehmen“ / „Einstellungen beibehalten“ / „Zeitrafferaufnahme starten“. Also „HDR-Video“, „Auto FPS“, „Verbesserte Stabilisierung“, „Objektivkorrektur“ | Quote exactly, with German quotes and „>“ | Apple DE guides iphc1827d32f, iph62000de98, iphb362b394e. **Verified** |
| iOS Settings: mirror front camera | „Frontkamera spiegeln“ | | **Unverified** (not found on the pages fetched) |
| Apple: Photos library | Mediathek in der App „Fotos“; permission string „Fotomediathek“ | | Apple DE guide; iOS UI. **Verified** |
| Apple: Center Stage front camera | **Center Stage Frontkamera** (English "Center Stage" kept) | | apple.com/de/iphone-17. **Verified** |
| Apple: main camera | **Hauptkamera** (*48 MP Fusion Hauptkamera*) = the main wide lens, not "the back camera" | | apple.com/de/iphone-air. **Verified** |
| App Store privacy label | „Keine Daten erfasst“ (iOS) | `android` uses „Keine Daten erhoben“ for the **Play** "Data safety" section | Apple label **unverified** this pass; Play German label „Keine Daten erhoben“ **unverified** |
| Samsung: Dual recording | **„Dual-Aufnahme“** | **Dual-Aufnahme**, with *(Dual recording)* glossed once at most | samsung.com/de/support/mobile-devices/kamera-funktionen-des-galaxy-z-flip7 ("Mit der Dual-Aufnahme lassen sich Fotos mit der Front- und Hauptkamera gleichzeitig aufnehmen"); autocomplete "samsung dual aufnahme" (+ "nicht verfügbar", "s24/s25"). **Verified** |
| Samsung: Director's View (older) | **„Regieansicht“** (MEHR > REGIEANSICHT) | *Regieansicht (Director's View)* | samsung.com/de/support/mobile-devices/galaxy-s21-regieansicht-verwenden; autocomplete "samsung regieansicht". **Verified** |
| Samsung: Quick controls | **„Schnellsteuerung“** | Not *Schnelleinstellungen* (that is Android's notification-shade quick settings) | Samsung DE Flip7 support page ("Tippe auf das Schnellsteuerung-Symbol"). **Verified** |
| Samsung: More | **„Mehr“** | | Samsung DE Flip7 + S21 pages. **Verified** |
| Samsung: layout names in Dual-Aufnahme | Third-party German tutorial shows „Split-Screen (Geteilter Bildschirm)“, „Picture-in-Picture (Bild-im-Bild)“ | Describe them as *Bild-in-Bild / Splitscreen* in our prose; quote Samsung labels only if verified on a device | antwort.net tutorial (S24). **Unverified** |
| Samsung: Gallery app | **Galerie** | | High confidence, not re-checked |
| Google: Pixel camera app | *Pixel-Kamera* (app name). Pixel Fold "Dual screen" preview: German label unknown | Keep English feature names in brackets | **Unverified** |
| Google Photos | **Google Fotos** | | High confidence, not re-checked |
| Instagram: dual camera | The Instagram camera mode is shown as **„Dual“** (English word kept in German UI) | *Dual-Kamera in Instagram*; autocomplete "instagram dual kamera (weg)" | Label **unverified** |
| TikTok: dual camera / stitch / duet | *Duett*, *Stitch*; dual-camera label in German UI unknown | Autocomplete "tiktok dual kamera", "tiktok live beide kameras gleichzeitig" | Labels **unverified** |
| Snapchat: Dual Camera | **„Dual-Kamera“**-Symbol in der Werkzeugleiste (used on `bereal-style…`); Snapchat's own German string not checked | Autocomplete "snapchat dual kamera", "snapchat beide kameras gleichzeitig" | **Unverified** |
| BeReal | *BeReal* (name); German UI not relevant | | n/a |

---

## 5. Native search phrasing (autocomplete-verified, hl=de, gl=de, 15 Nov 2026)

Use these patterns for titles, H1 and H2. Keep the year in titles. The quoted text is the real suggestion.

**Front + back cameras**
- "front und rückkamera gleichzeitig iphone / android / samsung / app / iphone 15 / instagram"
- "vorder und rückkamera gleichzeitig nutzen (iphone / snapchat / instagram)", "iphone 17 (pro) vorder und rückkamera gleichzeitig"
- "frontkamera und rückkamera gleichzeitig", "iphone frontkamera und rückkamera gleichzeitig"
- "beide kameras gleichzeitig (samsung / iphone / instagram / android)", "iphone beide kameras gleichzeitig aufnehmen / filmen", "iphone mit beiden kameras gleichzeitig filmen"
- "vorne und hinten gleichzeitig filmen", "iphone vorne und hinten gleichzeitig filmen"
- → H2 pattern: *Wie filmst du mit Front- und Rückkamera gleichzeitig auf dem iPhone?* Optional single search variant per
  page: *Vorder- und Rückkamera gleichzeitig nutzen* (in an H2 or FAQ question only, not as the running body term).

**Dual camera**
- "dual kamera iphone / samsung / handy / snapchat / android / iphone 17 pro / iphone 15 pro / iphone 16 pro", "dual kamera app (android / iphone)"
- "doppelkamera iphone / instagram / snapchat / samsung / iphone 17"
- "instagram dual kamera weg", "dual kamera instagram nicht verfügbar", "snapchat dual kamera funktioniert nicht"

**Apple**
- "dual capture iphone (17 / 16 / 16 pro / 15)", "iphone dual capture (16 pro / facetime / separate videos)"
- "doppelte aufnahme iphone (17 / 17 pro / 16 / 15)", "iphone 17 doppelte aufnahme foto"
- → Titles on Apple-comparison pages should carry both: *Dual Capture („Doppelte Aufnahme“) auf dem iPhone 17: …*

**Samsung**
- "samsung dual aufnahme", "samsung dual aufnahme nicht verfügbar", "dual aufnahme samsung s25 ultra / s24"
- "samsung regieansicht", "samsung director's view" (English query also live)

**Portrait + landscape**
- "hoch und querformat gleichzeitig filmen" (exact suggestion, with no "-format" on Hoch)
- "video hochkant oder quer", "video hochkant (drehen / schneiden / format)", "querformat video (instagram)"
- No demand found for "hochformat und querformat gleichzeitig", "vertikal und horizontal filmen" or "video gleichzeitig hochkant und quer". The dominant intent is *conversion* ("video hochformat in querformat umwandeln"), which a "no conversion needed" angle can target.
- → H2 pattern: *Hoch- und Querformat gleichzeitig filmen: so geht's* / *Video hochkant oder quer? Beides in einem Dreh*

**Split screen / PiP**
- "split screen video (erstellen / app / iphone)" (English two-word spelling dominates queries), "splitscreen video erstellen (kostenlos / iphone)"
- "bild in bild video (iphone / aufnehmen / erstellen / aufnehmen iphone)"
- "zwei videos nebeneinander (legen / app / instagram)"
- → Body: *Splitscreen*. A title may use *Split-Screen-Video* only if the page targets the English-spelling query; otherwise *Splitscreen-Video*.

**Other**
- "video kürzen iphone (14…17)", "video kürzen android": use *kürzen* in search copy, not *trimmen*
- "video zuschneiden iphone": Germans also say *zuschneiden* for trimming in searches. Our prose keeps *zuschneiden* for spatial crop, so a "trim" page can mention the query once
- "reaktionsvideo (erstellen)", "teleprompter app (kostenlos / iphone / kostenlos iphone)", "zeitraffer iphone (einstellen)", "bereal alternative", "kamera app ohne abo"

---

## 6. Inconsistencies found across the existing de pages (16)

| # | Issue | Right variant | Pages using the wrong one |
|---|---|---|---|
| 1 | *Vorder- und Rückkamera* as the running term against the site-wide *Front- und Rückkamera* (store, Apple DE, protect.json) | **Front- und Rückkamera** in body. Keep at most one *Vorder-* search phrasing per page | blog/record-front-and-back-camera-google-pixel (26), blog/record-front-and-back-camera-iphone-15-16 (21), blog/record-front-and-back-camera-same-time-android (16), blog/record-front-and-back-camera-samsung-galaxy (13), blog/record-front-and-back-camera-same-time-iphone (10), blog/iphone-17-dual-capture-limitations (5), blog/iphone-duo-camera (1) |
| 2 | *Handy* vs *Smartphone* split roughly 150/153 site-wide, and mixed inside single pages | **Smartphone** in body; *Handy* once at most, in a query-shaped heading | Handy-heavy: blog/film-kid-reaction-and-what-they-see (32), blog/iphone-4k-front-and-back-camera-same-time (15), blog/snapchat-front-and-back-camera (12 vs 2), blog/instagram-dual-camera-missing (10), blog/film-reaction-video-phone (9 vs 10), vs/lookout (9), android (8), changelog (7), vs/mixcam (7), vs/dualgram (6 vs 1), blog/bereal-style-photo-without-bereal (6), vs/apple-dual-capture (5), vs/detail (5), blog/phone-teleprompter-apps-compared (4), vs/2cam (4), vs/dualtake (3), features/dual-camera, features/teleprompter (2 each), features/manual-controls, vs/dualcam, blog/doubletake-not-working-alternatives, blog/iphone-duo-camera (1 each) |
| 3 | Apple's German UI name „Doppelte Aufnahme“ never appears (0 of 295 Dual Capture mentions), and step-by-step instructions tell German users to tap "Dual Capture", a label their iPhone doesn't show | Gloss once: *Dual Capture (auf deutschen iPhones „Doppelte Aufnahme“)*. In steps, use „Doppelte Aufnahme“ | Steps: blog/record-front-and-back-camera-same-time-iphone, blog/dual-camera-effect, blog/bereal-style-photo-without-bereal, blog/switch-camera-while-recording-iphone, blog/iphone-17-dual-capture-limitations, vs/apple-dual-capture. Missing gloss: all 24 pages that mention Dual Capture |
| 4 | *„Taste für die Kamerasteuerung“* used for the on-screen options icon. *Kamerasteuerung* is Apple's name for the physical Camera Control button | *das Symbol für die Kameraoptionen* (descriptive; Apple shows an icon only) | Same 6 pages as #3 (vs/apple-dual-capture and iphone-17-dual-capture-limitations as "Modus Video, Kamerasteuerung, Dual Capture") |
| 5 | Samsung feature named in English *Dual recording* as the running term, against Samsung DE's „Dual-Aufnahme“ (used correctly on vs/lookout and blog/switch-camera-while-recording-iphone) | **Dual-Aufnahme**, with *(Dual recording)* glossed once | blog/record-front-and-back-camera-samsung-galaxy (27 vs 3), blog/record-front-and-back-camera-same-time-android (12, never glossed; also "Director's View" never given as *Regieansicht*), blog/snapchat-front-and-back-camera (1) |
| 6 | Samsung *Quick controls* rendered as *Schnelleinstellungen*. Samsung DE says „Schnellsteuerung“ | **Schnellsteuerung** | blog/record-front-and-back-camera-samsung-galaxy (3), blog/record-front-and-back-camera-same-time-android (1) |
| 7 | *Lifetime-Kauf / -Option / -Plan* against the store/UI's *Einmalkauf (mit dauerhaftem Zugang)* (used on 14 pages) | **Einmalkauf** | vs/2cam (15), vs/detail (13), vs/dualtake (5), vs/dualcam (5), vs (3), vs/mixcam (3), vs/dualgram (2), changelog (2) |
| 8 | Manual controls named three ways | **Manuelle Steuerung** (store, footer, 45 pages) | (home) and features: "Profi-Kamerasteuerung", "Manuelle Kamerasteuerung" (features breadcrumb JSON-LD); features/manual-controls: "Manuelle Kamera-Einstellungen" in title/meta |
| 9 | ContentCam's in-app library called *Mediathek* (collides with Apple's Photos Mediathek); iOS library also written *Fotomediathek* vs *Mediathek* vs *Fotos-App* | ContentCam's list = **Take-Liste** / *Projekte*; Apple's = *Mediathek (App „Fotos“)*; Android = *Galerie* | changelog ("Feinschliff bei Aufnahme und Mediathek", "Mediathek verschieben und neu sortieren"); vs/dualcam uses "Fotomediathek" 8× next to "Mediathek" 4× (OK only in the permission-string quote) |
| 10 | Trim verb: *Trimme* in prose against the store's *kürzen* | **kürzen** in prose. Use „Trimmen“ only when naming the button | blog/record-front-and-back-camera-same-time-android (1) |
| 11 | *Reaction-Video* against *Reaktionsvideo* (9 pages, 31×) | **Reaktionsvideo** | vs/detail (2), blog/record-portrait-and-landscape-video-same-time-android (2), blog/split-screen-video-iphone (1) |
| 12 | Audio meter named *Pegelanzeige* against the store feature name *Audioanzeige* | **Audioanzeige** for ContentCam's feature | vs/dualcam (3), changelog (1) |
| 13 | Currency formats mixed: *5,99 $*, *2,99 US$*, *$0.99* (English decimal point), *US-Dollar* | **2,99 US$** (*US-Dollar* only in running prose) | blog/doubletake-not-working-alternatives ("$0.99 bis $9.99", "$19.99 bis $99.99": wrong decimal separator too); "x,xx $": blog/phone-teleprompter-apps-compared (30), vs/2cam (24), vs/detail (16), blog/dual-format-recording-apps-compared (5) |
| 14 | fps casing outside quotes | **60 fps** | vs/dualcam ("29,99 FPS" in visible caption + JSON-LD caption) |
| 15 | Untranslated JSON-LD text (brief: translate JSON-LD text fields) | *"Bewertung bei Google Play, November 2026"* | (home), android: `"description": "Google Play rating, November 2026"` |
| 16 | *Hochformat- und Querformat* (redundant first half) against the store's *Hoch- und Querformat* | **Hoch- und Querformat** | blog/best-front-and-back-dual-camera-apps (2), features/dual-camera (1) |

Consistent already (no action): Splitscreen (129×, no variants), Bild-in-Bild (141×), Zeitraffer (31×; the one
"Timelapse" is the store-style gloss), Ultraweitwinkel (no hyphenated variant), *Front und Rück* (401×, English gloss
used correctly), Zwei Objektive / Ein Objektiv, du-register (0 Sie-form slips), „…“ quotes, decimal comma, "31,6 %",
German dates in visible text, nav/footer wording. (Five pages lack the "Vergleiche" and "Changelog" footer links:
those are older footer builds, not a wording conflict.)

---

## 7. False friends and calque traps for this subject

- **Kamerasteuerung** is Apple's name for the iPhone 16+ *Camera Control hardware button*. It is not "camera
  controls" in general. For ContentCam's manual settings, say *Manuelle Steuerung*. For Apple's on-screen options icon,
  say *Symbol für die Kameraoptionen*.
- **Hauptkamera** (Apple and Samsung) means the main *wide* rear lens ("48 MP Fusion Hauptkamera"; Samsung "Front- und
  Hauptkamera"). It is not "the back camera" generically. Use *Rückkamera* unless the main lens specifically is meant.
- **Porträt / Porträtmodus** is the bokeh portrait *mode*, not portrait orientation. Orientation is *Hochformat*.
  "Record in portrait" is *im Hochformat aufnehmen*, never *im Porträt aufnehmen*. (The Play copy uses *Porträtmodus*
  correctly for background blur.)
- **Landschaft** means scenery, never the orientation (*Querformat*).
- **Linse** is the glass element. The camera unit is *Objektiv*. The idiom *in die Linse / in die Kamera schauen* is
  fine (features/teleprompter uses it naturally), but never *Ultraweitwinkel-Linse* or *zwei Linsen* for the modes.
- **Tipp** means a hint or betting tip. A screen touch is *Tippen / Fingertipp*.
- **sichern vs speichern**: Apple's German UI says *sichern*. ContentCam and Android say *speichern*. Don't mix them in
  one instruction.
- **kürzen vs zuschneiden vs trimmen**: *kürzen* is length (our prose). *zuschneiden/Beschnitt* is spatial crop.
  *Trimmen* is the in-app button label only. Mixing them makes the "neither file is a crop" claim read wrong.
- **Ausschnitt** is a crop/framing. *Keines ist ein Ausschnitt des anderen* is the canonical phrasing of the
  Single Lens claim, so don't paraphrase it into *Zuschnitt* or *beschnitten*.
- **Dual-Aufnahme** is Samsung's feature, and **Doppelte Aufnahme** is Apple's. Never use either for ContentCam's
  Front und Rück mode, and don't invent *Duale Aufnahme* or *Doppelaufnahme*.
- **Schnelleinstellungen** is Android's notification-shade quick settings. Samsung's camera bar is *Schnellsteuerung*.
- **eine Aufnahme machen** is a calque of "make a recording". Write *aufnehmen*.
- **Take vs Aufnahme**: *Take* is a numbered take in the take list. *Aufnahme* is any recording. "In one take" in
  marketing copy is *in einem Dreh*, not *in einem Take* (both are understood, but the store subtitle sets *Dreh*).
- **Lifetime / lebenslang**: *lebenslang* evokes a prison sentence in German, so don't use it in copy. Write
  *Einmalkauf mit dauerhaftem Zugang*. The store IAP name „Premium: Lebenslang“ is quoted only as a store line item.
- **Mediathek** on Android or in ContentCam context reads as Apple Photos or the ARD/ZDF streaming portals. Use
  *Galerie* (Android) or *Take-Liste* (ContentCam).
- **Handy** is native, but a store-copy mismatch. It is fine in a query-shaped heading, but not as the body term
  (see #2).
- **"Ab iOS 2.9"**: German readers parse *iOS 2.9* as an operating-system version (there is none; the OS is iOS 18+).
  When the ContentCam app version is meant, write *ab Version 2.9 der iPhone-App* or *ContentCam 2.9 (iOS)*. Affected:
  blog/iphone-4k-front-and-back-camera-same-time, blog/dual-camera-effect, blog/how-to-do-dual-camera-on-tiktok,
  blog/iphone-17-dual-capture-limitations, blog/doubletake-not-working-alternatives. The changelog's "iOS 2.8 ·
  Oktober 2026" headers are fine, because there the context is clear.
- **eventuell** means "possibly", not "eventually" (*schließlich / irgendwann*). **aktuell** means "current", not
  "actual" (*tatsächlich*). **sensibel** means "sensitive", not "sensible" (*vernünftig*). **Konsequent** means
  "consistent", not "consequently". These are the classic MT slips in comparison/FAQ prose.
- **realisieren** for "realise / notice" is an anglicism. Write *merken / feststellen*.
- **Sinn machen** is common but criticised. Prefer *sinnvoll sein / Sinn ergeben*.
- **kontrollieren** means "check / inspect", not "control". Write *steuern / einstellen* for camera settings.
- **Feature** is accepted creator jargon (store: *Feature-Wunsch*), but prefer *Funktion* in UI-describing sentences
  (nav label is *Funktionen*).
