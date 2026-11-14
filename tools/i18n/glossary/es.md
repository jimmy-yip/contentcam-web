# Spanish (`es`) terminology and style sheet: contentcam.app

Neutral Spanish, Latin America first, still natural in Spain. Built 15 Nov 2026 from:

- `tools/i18n/TRANSLATE-BRIEF.md` (es row)
- Store copy `~/contentcam/docs/store-descriptions/v2.8.2/desc/es-MX.txt` (terminology authority; `es-ES.txt` read for contrast only)
- App glossary `~/contentcam/docs/localization-glossary-es.md` (locked app UI terms)
- `~/contentcam/docs/store-metadata-expansion.md` (es-MX ASO notes)
- A scan of all 45 pages under `es/` (counts below are visible text + JSON-LD, 15 Nov 2026)
- Apple, Samsung, Google and Snap Spanish pages fetched 15 Nov 2026 (sources in §4)
- Google autocomplete (`hl=es`; the endpoint returned identical lists for `gl=mx` and `gl=es`, so it is not region-split)

Where this sheet and an older page disagree, this sheet wins. Where this sheet and the store copy disagree on a ContentCam feature name, the store copy wins. Tell Jimmy if that ever happens.

---

## 1. Register, person, punctuation, typography

**Register: `tú`.** Never `usted`, never `vosotros` (0 hits on the site today, keep it that way). Imperatives: *toca, graba, desliza, mantén presionado, descarga, prueba*. Reason: the es-MX store copy uses `tú` throughout ("toca para enfocar", "organiza tus grabaciones"), and the app UI does too. The site must read like the listing a visitor just came from.

**Vocabulary base: Latin American.** `video` (no accent, 523 hits, 0 `vídeo`), `el lente`, `cuadro`, `agregar`, `tomar una foto`, `la selfie`, `Configuración`, `computadora`, `presionar`. Avoid peninsular `vídeo, objetivo, fotograma, añadir, hacer una foto, el selfie, Ajustes, ordenador, pulsar, móvil` (see §2).

**Phone noun:** `teléfono` is the default in body copy (262 hits, 42 pages). `celular` is allowed in titles, H2s and FAQ questions when the native query uses it (autocomplete: *teleprompter para celular*, *como hacer video reacciones en celular*). Not `móvil` (Spain) except fixed expressions inside a quote. When the device is clearly an iPhone, say `iPhone` / `tu iPhone`.

**Punctuation**
- Inverted marks are mandatory: `¿…?` and `¡…!`, opening at the start of the question, not the sentence (`Si no te aparece, ¿qué haces?`). Current pages pass.
- No em dashes (brief rule). Use a colon, comma, or parentheses. Current pages: 0.
- Quotation marks: use curly double quotes `“…”` for quoted text and UI strings quoted in prose. They are typographic, need no escaping inside JSON-LD, and the most recent `vs/` pages already use them. Not straight `"…"` in visible text, not `«…»`. Nested: `‘…’`.
- UI labels the reader taps: write them as plain text with initial capital, no quotes, as Apple does: *toca Captura dual*, *Configuración > Cámara > Grabar video*. Menu paths use ` > ` (Apple's own style; the support page currently uses `→`, which is acceptable but `>` is preferred for new text).
- Sentence case in titles and headings. Spanish does not capitalise every word: `Cómo grabar con la cámara frontal y trasera al mismo tiempo`, not `Cómo Grabar Con…`.
- Periods are never placed after `?` or `!`; a closing quote goes before the period: `…dice “sí”.`

**Numbers (LatAm convention, matches the app glossary)**
- Decimal separator is a **period**: `4.8`, `0.5x`, `29.99 fps`, `0.5 s`. This is a deliberate LatAm choice (glossary: "it and pt render the rating as 4,8; a LatAm-leaning es uses 4.8").
- Thousands separator is a **comma**: `15,000 caracteres`, `50,000 descargas`, `1,000`. Four-digit numbers may also go without a separator (`1000`), but never `15.000` (that would read as fifteen in a period-decimal document).
- Resolutions: `1920 x 1080` (or `1920 × 1080`), spaces around the sign, as the pages already do.
- Frame rate in prose: `60 fps`, with a space, lowercase, matching the store copy (`a 24, 25, 30, 50 o 60 fps`). App UI chips may show `60fps`; when quoting a rival's UI string, copy it exactly.
- Zoom: `0.5x`, `1x`, `2x`, no space. Speed-up: `de 10x a 900x`.
- Percent: `31.6 %` or `31.6%`; pick the no-space form to match the existing pages.

**Money**
- Always mark USD explicitly: `US$4.99`, `US$59.99`, prefix, no space. A bare `$` reads as pesos in Mexico, Argentina, Chile, Colombia. Never `22,99 US$` (Spain order and comma).
- Other currencies by ISO-style prefix as the English source has them (`A$`), never converted.

**Dates:** `15 de noviembre de 2026`; short form in tables `15 nov 2026`. Months lowercase. Never `noviembre 15`. Day of week lowercase (`lunes`).

**Accents worth checking:** `guion` (no accent, RAE 2010; 0 `guión` today), `solo` (no accent, also as adverb), `este/ese` (no accent), `ícono` (LatAm, 9 hits, consistent), `video` (no accent).

---

## 2. Mandated term table

| English concept | Use (es) | Avoid | Source / confidence |
|---|---|---|---|
| video | **video** | vídeo | Store es-MX; app glossary. Verified |
| phone | **teléfono**; `celular` in query-shaped titles/H2s | móvil, smartphone (in prose) | Brief; autocomplete. Verified |
| take (one recording) | **toma / tomas** (feminine: *guardada, eliminada*) | clip (for ContentCam's unit), grabación (as countable unit) | Store; app glossary. Verified. `clip` is fine for rival output and generic footage |
| recording (act/result, uncountable) | **grabación** | | Store |
| scene / project | **escena / proyecto** | | Store |
| lens | **el lente / los lentes** (masculine) | objetivo, la lente | Store es-MX; glossary ("clearest Mexico-vs-Spain marker"). Verified |
| wide / ultra wide | **gran angular / ultra gran angular** | ultra angular, ultrawide | Store. Verified |
| front camera / back camera | **cámara frontal / cámara trasera** | cámara delantera, cámara posterior, frente/atrás | Store; glossary (§Front/Back); autocomplete. Verified |
| front and back at the same time | **la cámara frontal y la trasera al mismo tiempo** (or *a la vez*) | simultáneamente (stiff; OK inside a quote) | Autocomplete: *grabar con camara frontal y trasera al mismo tiempo* is the top completion. Verified |
| both cameras | **las dos cámaras** | ambas cámaras (OK but rarer), dual cámaras | Autocomplete: *grabar con las dos camaras al mismo tiempo / a la vez*. Verified |
| selfie camera | **cámara selfie**; *la selfie* (feminine) | el selfie (Spain) | Store es-MX "cámara selfie"; Apple es-MX "Tomar una selfie". Verified |
| take a photo | **tomar una foto** | hacer una foto (Spain), sacar una foto (OK colloquial, avoid in UI-like text) | Apple es-MX TOC. Verified |
| portrait / landscape (orientation) | **vertical / horizontal** | retrato, apaisado, paisaje (paisaje = scenery, and the ASO notes record `landscape`-type drift) | Store; glossary. Verified |
| portrait and landscape at once | **vertical y horizontal al mismo tiempo / a la vez** | | Store line 1; autocomplete *grabar en vertical y horizontal a la vez*. Verified |
| dual format (both orientations) | **los dos formatos**; section label **Doble formato** | formato dual | Store ("graba los dos formatos"). Verified |
| dual camera (generic concept) | **doble cámara** (preferred, also for titles) or **cámara dual** | cámara doble | Both are real queries (*doble camara iphone 17*, *camara dual samsung*). es-MX ASO chose `doble cámara` (8 of 14 Mexican competitor names). Lowercase when generic. Verified |
| split screen | **pantalla dividida** | split screen | Store; autocomplete *video en pantalla dividida*. Verified |
| picture in picture | **imagen en imagen** | imagen dentro de imagen (Apple's name for the iOS multitasking feature only), PiP, picture-in-picture | Store es-MX. Verified |
| combine (two takes into one video) | **combinar**; the feature is **Combinar** | fusionar, unir | Store ("Combinar una grabación de Frontal y trasera"). Verified |
| separate files | **archivos separados** | archivos independientes (es-ES store wording) | Store es-MX. Verified |
| frame (of video) | **cuadro**; frame rate = **cuadros por segundo (fps)** | fotograma, velocidad de fotogramas | Store es-MX; glossary. Note: Apple es-MX itself says *frecuencia de fotogramas* in iOS Settings; use Apple's wording only when naming that iOS setting |
| crosshair | **mira** (*mira central*) | cruz central, retícula | Store es-MX; glossary. Verified |
| shutter | **obturador** | obturación | Store es-MX |
| white balance | **balance de blancos** | | Store |
| manual controls | **controles manuales** | | Store |
| preview | **vista previa** | | Glossary |
| trim / cut in review | **recortar / corte** (*Revisión y corte*) | | Store; glossary |
| crop (reframing) | **recorte** in prose about cropping a 16:9 into 9:16 | | Store ("Ninguno de los dos es un recorte del otro") |
| framing | **encuadre / encuadrar** | | Existing pages, natural |
| script (teleprompter) | **guion** | guión, libreto | Glossary; store |
| teleprompter | **teleprompter** | apuntador, prompter | Store; autocomplete *app teleprompter*. Verified |
| timelapse (ContentCam feature) | **Timelapse** | time-lapse, cámara rápida (Apple's mode name, see §4) | Store |
| Settings (app or iOS) | **Configuración** | Ajustes | Apple es-MX "Configuración > Cámara"; glossary. Verified. Lowercase *ajustes* stays fine for setting values |
| photo library / Photos app | **Fotos** (app), **fototeca** (library) | carrete (Spain colloquial), galería (OK for Android only) | Apple es-MX "Explorar tu fototeca". Verified. On Android, *galería* is correct |
| add | **agregar** | añadir | LatAm; Apple es-MX "Agregar". Verified |
| tap / press and hold | **tocar / mantener presionado** | pulsar, mantener pulsado | Store es-MX ("mantén presionado"). Verified |
| watermark | **marca de agua** | | Store |
| ads | **anuncios** | publicidad (OK in prose) | Store |
| free | **gratis** | gratuito (fine as adjective, but CTA is *gratis*) | Store; ASO keyword `gratis` |
| free trial | **prueba gratis** (*7 días de prueba gratis*) | prueba gratuita | Existing pages (19 hits, 0 alternative) |
| one-time purchase / lifetime | **pago único**, **acceso de por vida** | compra única, un solo pago, vitalicio | Store ("pago único con acceso de por vida"). Verified |
| subscription (annual / monthly / weekly) | **suscripción anual / mensual / semanal** | | Store |
| unlock (Premium) | **desbloquear** | | Store ("CON PREMIUM DESBLOQUEAS") |
| Restore purchases / Upgrade | **Restaurar compras**, **Pasar a Premium** (app button labels) | | Support page; app UI |
| download | **descargar**; CTA **Descarga gratis** | bajar | Existing pages |
| reaction video | **video de reacción** | video reacción (OK in titles if the query needs it) | Autocomplete *como hacer un video de reaccion*. Verified |
| indie developer (byline) | **desarrollador independiente** | | Store |
| rating line | **Valorada con 4.8 por 580+ creadores** (footer CTA) and **Calificada con ★ 4.8 por más de 580 creadores** (hero) are both live; see §6 #4 for the single form | | |

---

## 3. ContentCam mode and feature names (exactly as the es-MX store copy writes them)

| English (app/store) | es on the website | Notes |
|---|---|---|
| Single Lens | **Un solo lente** | Store form. The in-app button is shorter: **Un lente** (glossary amendment 25 Aug 2026, width). Use *Un solo lente* in prose; write *Un lente* only when telling the reader which button to tap |
| Dual Lens | **Doble lente** | Lowercase inside "modo doble lente" in the store's Premium list; on the site write **modo Doble lente** (capital D = it is a name). Never *Doble objetivo*, *Lente dual* |
| Front/Back | **Frontal y trasera** | In-app label **Frontal/Trasera**. Never *Frente/Atrás* (glossary: calque from pt-BR, *la frente* = forehead), never *Delantera/Trasera*. Write **modo Frontal y trasera** for ContentCam's mode; lowercase *un modo frontal y trasera* only for the generic concept in other apps |
| Front Camera | **Cámara frontal** | Store mode list |
| Normal Camera | **Cámara normal** | Store mode list |
| Photo mode / Photo in Front/Back | **Modo foto**, **Foto en Frontal y trasera** | Store |
| shutter button next to record | **Disparador** | Store |
| Combine | **Combinar** | Premium feature |
| Picture in picture / Split screen layouts | **imagen en imagen**, **pantalla dividida** | Store |
| Manual controls | **Controles manuales**: exposición, balance de blancos, ISO, obturador | The in-app tab labels stay English (`EV, Temp, Tint, ISO, Shutter`) in every language (glossary). If you must name the tab, write *Shutter* and gloss: *Shutter (obturador)* |
| Teleprompter | **Teleprompter** | Not glossed |
| Timelapse | **Timelapse** | Not glossed |
| Focus & exposure | **Enfoque y exposición** | Store |
| Stabilization and HDR | **Estabilización y HDR** | Store |
| Guides | **Guías**: indicador de nivel, mira central, medidor de audio | Store. Not *cruz central* |
| Projects, scenes and takes | **Proyectos, escenas y tomas** | Store |
| Recording folder | **Carpeta de grabaciones** | Store |
| Review and trim | **Revisión y corte** | Store |
| Space estimate | **Estimación de espacio** | Store |
| Crash protection | **Protección contra cierres inesperados** | Store |
| Thermal monitoring | **Monitoreo térmico** | Store es-MX (es-ES says *monitorización*; not here) |
| Premium | **Premium** | Unchanged |
| HD, 4K, HDR, ISO, fps | unchanged | |

**English gloss rule (store-metadata-expansion §gloss):** the store glosses a mode once in parentheses where the Spanish differs from the English, e.g. *Frontal y trasera (Front/Back)*, *Doble lente (Dual Lens)*, *Un solo lente (Single Lens)*. On the website, gloss at most **once per page**, at first mention, and only for these three modes. Never gloss Teleprompter or Timelapse. Since the app UI is now localized, the gloss is optional; if used, use it consistently for all three.

---

## 4. Platform names in Spanish

| Platform / feature | es form to use | Source / status |
|---|---|---|
| Apple: Dual Capture | **Captura dual** (lowercase *d*); in running prose *la captura dual* or *video de captura dual* is also Apple's own usage | **Verified.** support.apple.com/es-mx/guide/iphone/iph61f49e4bb/ios: "Grabar videos de captura dual … toca el Captura dual … Para desactivar la captura dual". Glossary aside es-mx/…/glos3842gv5b: "Modelos compatibles con video de captura dual". es-es: "Captura dual" too. The brief's "Captura Dual" (capital D) does not match Apple; this sheet supersedes it |
| Apple: Camera app | **Cámara** (*la app Cámara*) | Verified (Apple es-MX) |
| Apple: Settings path | **Configuración > Cámara > Grabar video** | Verified: support.apple.com/es-mx/guide/iphone/iphc1827d32f/ios ("Ve a Configuración > Cámara > Grabar video"). es-ES uses *Ajustes*, do not use |
| Apple: Record stereo / sound | *Grabar sonido estéreo*, *Grabar sonido* (Audio espacial, Estéreo, Mono) | Verified (same page) |
| Apple: Auto FPS | *Frecuencia automática*; *FPS para poca luz* | Verified (same page) |
| Apple: frame rate (iOS wording) | *frecuencia de fotogramas* | Verified (Apple es-MX). Use only when naming the iOS setting; ContentCam copy says *cuadros por segundo* |
| Apple: time-lapse camera mode | **Cámara rápida** | Verified (es-MX "cámara lenta, cámara rápida o Cine") |
| Apple: Cinematic / Action / Slo-mo | **Cine**, **modo Acción**, **cámara lenta** | Verified (es-MX) |
| Apple: Photos / library | **Fotos**, **fototeca** | Verified (es-MX TOC) |
| Apple: Apple Account | **Cuenta de Apple** | Verified (es-MX TOC) |
| Apple: PiP multitasking | *Imagen dentro de imagen* | Verified only in es-ES TOC ("Multitarea con Imagen dentro de imagen"). This is the video-playback feature, not a camera layout. Do not use it for Captura dual's inset; say *un recuadro* or *imagen en imagen* |
| Apple: crop/rotate tools | *Recortar, girar, voltear, enderezar* | Verified: support.apple.com/es-mx/guide/iphone/iph0f3ebb1dd/ios |
| Apple: selfie | *Tomar una selfie* | Verified (es-MX TOC) |
| Samsung: Dual recording | **Grabación dual** | Verified (LatAm community, Samsung's own staff tip, r1.community.samsung.com, Oct 2025: "seleccionar “Vista del Director” (o “Grabación dual”)"); autocomplete *grabacion dual samsung s24 ultra*. Samsung LatAm support page not found; treat as high confidence |
| Samsung: Director's View | **Vista del director** | Verified: samsung.com/cl/support/mobile-devices/camera-options-directors-view (title "Opciones de cámara: Vista del director"); Samsung CO/AR pages "Vista del Director". Samsung Spain (ushl.samsung.com/es) keeps **Director's View** in English. Use *Vista del director*, optionally gloss *(Director's View)* once |
| Samsung: path | **Cámara > Más > Grabación dual** | Verified (community tip above). One UI 8.5 relocation to the Video mode: unverified in Spanish |
| Samsung: Camera app | **Cámara** | Verified |
| Google: Pixel Camera app | **Cámara Pixel** | Verified: Google Play title "Cámara Pixel" (hl=es-419 and es); support.google.com/googlecamera "Ayuda de Cámara Pixel". Not *Pixel Camera*, not *Pixel Cámara* |
| Google: Android concurrent cameras | *cámaras simultáneas* (descriptive) | Descriptive, no official UI label |
| Snapchat: Dual Camera | **Doble cámara** (*la Doble cámara de Snapchat*) | Verified for es-ES: newsroom.snap.com/es-ES/dual-camera ("Hoy presentamos la Doble cámara"). In-app es-419 label **unverified**. Never *Cámara Dual* |
| Snapchat: Snaps, Stories, Memories, Lenses, Spotlight | *Snaps*, *Historias*, *Recuerdos* (unverified; pages keep *Memories*), *Lentes*, *Spotlight* | Historias + Lentes: verified in the same Snap newsroom post. Recuerdos: unverified, keep *Memories* until checked |
| Instagram: Dual | **Dual** (*Dual de Instagram*) | In-app label unverified for Spanish; Meta's English name is "Dual". Autocomplete shows users call it *cámara dual instagram* / *doble camara instagram*; use those in titles and H2s, *Dual* for the tool name |
| Instagram: Reels, Stories | **Reels**, **Historias** | Reels unchanged (verified in store copy). Historias: common Spanish UI, unverified here |
| TikTok: Duet / Stitch / Green Screen | **Dúo**, **Pegar** (Stitch), **Pantalla verde** | **Unverified** (support.tiktok.com/es is JS-rendered, could not fetch). Dúo and Pantalla verde already on the site; the TikTok page says *Stitch* in English. Check against the TikTok app in Spanish before changing |
| YouTube: Shorts | **Shorts** | Unchanged |
| Store names | **App Store**, **Google Play** | Unchanged (*el App Store*, masculine, as the pages use) |

---

## 5. Native search phrasing for titles and H2s (Google autocomplete, 15 Nov 2026)

Autocomplete strips accents; restore them in copy (*cámara*, *cómo*, *aplicación*).

**Front + back camera**
- grabar con cámara frontal y trasera al mismo tiempo (+ iphone / samsung / android / xiaomi)
- cómo grabar con la cámara frontal y trasera al mismo tiempo
- cómo grabar con las dos cámaras (+ en samsung / del iphone); *a la vez* variant also tops in Spain
- grabar con las dos cámaras al mismo tiempo; se puede grabar con las dos cámaras al mismo tiempo; aplicación para grabar con las dos cámaras al mismo tiempo
- cámara frontal y trasera al mismo tiempo (+ android / iphone / samsung); usar / activar cámara frontal y trasera al mismo tiempo
- cámara frontal y trasera iphone 17 / 16 / 15
- grabar video con cámara frontal y trasera
- tomar foto con cámara frontal y trasera (+ iphone / samsung); cómo tomar una foto frontal y trasera al mismo tiempo
- cómo cambiar de cámara frontal a trasera mientras grabas iphone

**Dual camera**
- doble cámara iphone / iphone 17 / samsung / xiaomi; doble cámara en samsung
- cámara dual / cámara dual samsung / cámara dual iphone 17 / cámara dual instagram
- cómo hacer doble cámara en (samsung / iphone / iphone 17 / instagram / tiktok)
- app doble cámara (+ android / iphone); app para grabar doble cámara; app cámara doble lente
- doble cámara instagram / efecto doble cámara instagram; cámara dual instagram no sale
- doble cámara tiktok (low volume)
- *dual camera samsung / iphone* also completes in English: keep English only inside app names

**Portrait + landscape**
- grabar en vertical y horizontal a la vez
- cómo grabar en horizontal y vertical al mismo tiempo iphone 17
- app para grabar en vertical y horizontal
- video vertical y horizontal; formato de video vertical y horizontal
- "grabar video vertical y horizontal al mismo tiempo" returned no completion; prefer *grabar en vertical y horizontal a la vez* for H1/H2

**Apple / Samsung built-ins**
- captura dual iphone / iphone 17 / iphone 16 / iphone 15 (users search it on models that do not have it: good H2 material)
- grabación dual samsung (+ s24 ultra / s25 ultra / a55 / a56)
- vista del director samsung (low volume, still completes)

**Split screen / other**
- video en pantalla dividida; cómo hacer un video con pantalla dividida (+ en tiktok / capcut)
- cómo hacer un video de reacción (+ en tiktok / instagram / celular)
- app teleprompter gratis; teleprompter para celular
- imagen en imagen video (weak; do not build headings on it)

**Heading pattern that matches these:** `Cómo grabar con la cámara frontal y trasera al mismo tiempo en iPhone (2026)`, `¿Se puede grabar con las dos cámaras al mismo tiempo en Samsung?`, `¿Qué iPhone tienen captura dual?`, `Cómo grabar en vertical y horizontal a la vez`.

---

## 6. Inconsistencies found across the 45 existing `es` pages (18)

Counts are occurrences / pages on 15 Nov 2026. "Right" is what new and revised pages must use.

1. **Apple feature capitalisation.** *Captura Dual* (270 / 23 pages) vs Apple's own **Captura dual** (es-MX and es-ES support pages). Only `vs/lookout` uses the lowercase form. Right: *Captura dual*. Affects every page that names it (all `blog/` Apple pages, `vs/apple-dual-capture`, `vs/`, home). The brief row ("Captura Dual") should be updated to match.
2. **English "Dual Capture" in Spanish prose.** `support` ("que no tienen el modo Dual Capture de Apple"). Right: *Captura dual*. (English in cited source titles, e.g. "Models that support Dual Capture video", is fine.)
3. **Rating decimal.** Footer CTA "Valorada con **4,8** por 580+ creadores" on all 45 pages vs "★ **4.8**" on home, features, pricing, android, vs/dualtake, blog/phone-teleprompter-apps-compared. Right: **4.8** (glossary mandates period decimal for LatAm es).
4. **Rating line wording.** "Valorada con 4,8 por 580+ creadores" (footer, 45 pages) vs "Calificada con ★ 4.8 por más de 580 creadores" (hero: home, features, pricing) and "más de 580" in vs/dualtake. Right: one form, **Calificada con 4.8 por más de 580 creadores** (LatAm *calificación*, words not "+"). Footer is shared markup, so fix it once in the template/build step.
5. **Other decimal commas.** `changelog` and `vs/dualgram` "0,5x"; `vs/dualcam` "29,99 fps" (×9) and "22,99 US$"; `vs/dualgram` "58,91 fps". Right: `0.5x`, `29.99 fps`, `US$22.99`, `58.91 fps`.
6. **Thousands separator.** `changelog` "15.000 caracteres" vs `features` "15,000 caracteres" (same fact). `blog/record-portrait-and-landscape-video-same-time-android` is correct (607.5 decimal). Right: **15,000**.
7. **Currency format.** Prefix `US$4.99` (6 pages: dual-camera-app-without-ads, iphone-duo-camera, record-front-and-back-camera-iphone-15-16, split-screen-video-iphone, vs/2cam, vs/detail) vs bare `$` (81 hits: dual-camera-app-one-time-purchase 43, phone-teleprompter-apps-compared 29, dual-format-recording-apps-compared 5, doubletake-not-working-alternatives 4) vs suffix `22,99 US$` (vs/dualcam). Right: **US$** prefix everywhere; bare `$` reads as local pesos in LatAm.
8. **fps spacing.** `60fps` (49 hits / 14 pages, incl. home 7, record-front-and-back-camera-iphone-15-16 9) vs `60 fps` (265 / 25 pages). Right in prose: **60 fps** (store copy). Keep `60fps` only when quoting a UI string.
9. **Quote marks.** Straight `"…"` (25 pages), curly `“…”` (9 pages: the vs/ set, iphone-4k-…, record-front-and-back-camera-google-pixel), angled `«…»` (android, blog/film-kid-reaction-and-what-they-see). Right: **“…”**.
10. **Snapchat Dual Camera.** English *Dual Camera* / *la Dual Camera* (most Snapchat mentions; e.g. snapchat-front-and-back-camera, film-reaction-video-phone, bereal-style-photo-without-bereal, dual-camera-effect) vs *Cámara Dual* (best-front-and-back-dual-camera-apps ×3, take-photo-front-and-back-camera-same-time ×6). Right: **Doble cámara de Snapchat** (Snap's own Spanish name); *Cámara Dual* is wrong in any case. If the es-419 in-app label turns out to be English, fall back to *Dual Camera* everywhere, never mixed.
11. **Google Pixel camera app.** *Pixel Camera* (27: record-front-and-back-camera-google-pixel 14, record-front-and-back-camera-same-time-android 6, record-portrait-and-landscape-video-same-time-android 6, record-portrait-and-landscape-video-same-time-iphone 1) and *Pixel Cámara* (snapchat-front-and-back-camera 1). Right: **Cámara Pixel** (Google Play + Google Help titles in Spanish).
12. **Settings.** *Ajustes* for ContentCam's own settings in `features/manual-controls` ("una opción en Ajustes") and in screenshot alt text on `vs/dualcam`, `vs/dualgram` vs *Configuración* (changelog, pricing, support). Right: **Configuración**.
13. **Frame.** *fotograma* (bereal-style-photo-without-bereal ×4, switch-camera-while-recording-iphone ×1, vs/dualcam "velocidad(es) de fotogramas" ×3) vs *cuadro* (108 / 27 pages). Right: **cuadro**, **cuadros por segundo**.
14. **Crosshair.** `changelog` "Cruz central que se ilumina en cian" vs store/pages *mira central*. Right: **mira central**.
15. **One-time purchase.** *pago único* (47 / 13) vs *compra única* (19 / 9: home ×4, changelog, pricing, vs/detail, vs/dualgram, vs/lookout, vs/mixcam, best-front-and-back-dual-camera-apps, dual-format-recording-apps-compared) vs *un solo pago* (7 / 4). Right: **pago único** (store). *se paga una sola vez* is fine as a verb phrase.
16. **Picture in picture.** `blog/iphone-duo-camera` uses *imagen dentro de imagen* (×5) vs *imagen en imagen* (128 / 33 pages). Right: **imagen en imagen**.
17. **Add.** *añadir/añadió* (4 pages: bereal-style-photo-without-bereal, iphone-duo-camera, vs/dualgram, vs/lookout) vs *agregar* (42 / 24). Right: **agregar** (one of the bereal hits is a verb of saying, "y añade:"; use *y agrega:*).
18. **Mode glosses.** *Frontal y trasera (Front/Back)* glossed on 9 pages, *Doble lente (Dual Lens)* on 3, *Un solo lente (Single Lens)* on none. Right: either gloss all three once per page at first mention, or none (§3).

Consistent already (no action): `video` (0 `vídeo`), `el lente` (0 `objetivo`, 0 `la lente`), `Frontal y trasera` (0 `Frente/Atrás`), `tú` (0 `usted`/`vosotros`), `guion` (0 `guión`), `la selfie` (0 `el selfie`), `ícono`, `archivos separados` (0 `independientes`), `prueba gratis`, inverted `¿¡`, no em dashes, `tomar una foto` (0 `hacer una foto`), `Grabación dual` / `Vista del director` usage on the Samsung pages.

---

## 7. False friends and calque traps for this subject

- **Frente/Atrás** for Front/Back: pt-BR calque; *la frente* = forehead; *atrás* pairs with *adelante*. Use *Frontal y trasera*.
- **Cámara dual vs doble cámara:** both are real, but *cámara doble* (word order flipped) reads as "a double camera" object. Never invent *Cámara Dual* as a product name for someone else's feature.
- **Paisaje / retrato** for landscape / portrait orientation: wrong sense (*paisaje* = scenery, *retrato* = a portrait photo or Apple's Portrait *mode*). Orientation is *horizontal / vertical*. Careful: Apple's camera **mode** *Retrato* exists; do not confuse it with vertical video.
- **Grabar (record) vs grabar (engrave)** is fine; but **"tomar" a video** is not used: *grabar un video*, *tomar una foto*.
- **Toma** (ContentCam's take) vs **tomar** (verb): avoid "toma una toma"; write *graba una toma*.
- **Clip** is not ContentCam's unit: the unit is *toma*. A *clip* is a generic piece of footage or a rival's output.
- **Recortar** means both crop and trim. ContentCam has no crop control, so *recortar/recorte* = trim in the review screen, but in dual-format explanations *recorte* = crop (a 9:16 cut from a 16:9). Make the sense clear from context: *corta al cuadro exacto* (trim) vs *no es un recorte del 16:9* (crop).
- **Tinte** (Tint): in LatAm reads as hair dye. Use *matiz* if ever needed (glossary).
- **Actualmente** = currently (not "actually"); **eventualmente** = possibly (not "eventually"; use *con el tiempo / al final*); **soportar** = to endure (for "supports" use *es compatible con / admite*); **aplicar** ≠ "apply for"; **librería** = bookshop (library = *biblioteca*, photo library = *fototeca*); **resolver** fine, but **realizar** ≠ "realize" (= carry out; "realize" = *darse cuenta*); **editar** ≠ publish (*editar* = edit video, fine).
- **Simultáneo/simultáneamente:** grammatical but stiff and rarely searched; the queries say *al mismo tiempo* / *a la vez*. Also the ASO notes record Portuguese *simultaneo* drifting to simultaneous translation.
- **Atrás** as a keyword drifted to countdown timers in App Store search (ASO notes); irrelevant to prose, but do not use *atrás* for the back camera.
- **Formato** in Spanish covers both aspect ratio and file format; when the meaning is orientation, prefer *vertical y horizontal* over *los dos formatos* in headings, and keep *los dos formatos* in body text where the store uses it.
- **Selfie gender:** LatAm *la selfie*, Spain *el selfie*. Use *la*.
- **Pantalla dividida** also completes to *videojuegos* (split-screen gaming): headings should add *video* (*video en pantalla dividida*).
- **Imagen en imagen vs Imagen dentro de imagen:** the latter is Apple's floating-video multitasking feature, not a camera layout.
- **Configuración vs Ajustes:** Apple Spain says *Ajustes*, Apple LatAm *Configuración*. Mixing them signals a Spain/LatAm switch mid-page.
- **$ alone** means pesos to a Mexican, Argentine, Chilean or Colombian reader. Always *US$*.
- **Billón** = 10^12 in Spanish. If an English source says "billion", write *mil millones*.
- **"Gratis para siempre"** risks overclaiming; translate exactly what the English says (free tier = *gratis, tomas ilimitadas, sin crear cuenta*).
