# pt-br: Brazilian Portuguese terminology + style sheet (contentcam.app)

Built 15 Nov 2026. Covers all 45 pages under `/pt-br/` as they stood that day. This sheet is for native reviewers and
translation agents. Where it conflicts with an older page, this sheet wins. Where it conflicts with the store copy on a
ContentCam feature name, the store copy wins (and this sheet should be fixed).

Sources used:
- S1 `~/contentcam/docs/store-descriptions/v2.8.2/desc/pt-BR.txt` (App Store description, current, **naming authority**)
- S2 `~/contentcam/docs/store-descriptions/v2.8.2/play/pt-BR.json` (Google Play listing, current)
- S3 `~/contentcam/ContentCam/ContentCam/Resources/Localizable.xcstrings` (shipping iOS UI, pt-BR)
- S4 `~/contentcam/docs/store-metadata-localized.md`, `store-metadata-expansion.md`, `localization-review.md`
- S5 Apple Suporte (BR), "Grave um vídeo com a câmera do iPhone": support.apple.com/pt-br/guide/iphone/iph61f49e4bb/ios
- S6 Apple Suporte (BR), "Modelos compatíveis com vídeo de Captura Dupla": support.apple.com/pt-br/guide/iphone/aside/glos3842gv5b/27/ios/27
- S7 Apple Suporte (BR), "Altere os ajustes de gravação de vídeo no iPhone": support.apple.com/pt-br/guide/iphone/iphc1827d32f/27/ios/27
- S8 Snap Newsroom pt-BR, "Faça parte de todos os momentos com a Câmera Dupla do Snapchat!" (29 ago. 2022): newsroom.snap.com/pt-BR/dual-camera
- S9 Samsung Newsroom Brasil: news.samsung.com/br/visao-do-diretor-garante-mais-versatilidade-e-controle-na-hora-de-gravar-conteudo-no-galaxy-s22-5g and the S21 FE article (Gravação Dupla)
- S10 Google autocomplete, `hl=pt-BR&gl=br`, run 15 Nov 2026 (results in section 5)
- S11 Brazilian tech press on Instagram Dual: tecnoblog.net/responde/como-filmar-reels-e-stories-do-instagram-com-duas-cameras/ and hardware.com.br (secondary, not Meta)

Confidence key: **V** = verified in an official source above. **S** = matches store copy/app. **A** = autocomplete-verified.
**U** = unverified (best knowledge; a native reviewer with the app/phone in hand should confirm).

---

## 1. Register, person, typography

### Register and person
- **você**, informal-friendly, never *tu* (zero *tu* on the site today, keep it that way) and never *o senhor / a senhora*.
  Possessives *seu/sua*, imperatives in the *você* form: *grave, toque, abra, escolha, experimente*. Matches S1/S2/S3
  ("Grave vídeo na vertical...", "Toque em...", "role seu roteiro").
- First person singular for Jimmy's voice where the English has "I" ("Eu desenvolvo o ContentCam", "testei"). S3 What's New
  uses it ("Corrigi a pré-visualização...").
- Colloquial but written Brazilian: *dá para* (not *é possível* everywhere), *pegar mais da cena*, *de graça*. Avoid
  European Portuguese entirely (see section 7).
- Device word: **celular** (generic), **iPhone** when it is an iPhone. *aparelho* only inside translated quotes of
  "device" (S4: *aparelho* appears 0 times in real BR store copy). *smartphone* / *telefone*: avoid.

### Punctuation and typography
- **No em dashes** (house rule). Use a colon, a comma or a full stop. En dash only as an empty-cell placeholder in tables
  (pricing does this; fine) and in numeric ranges is not needed: write "de 2500K a 8000K" in prose.
- **Quotes:** curly double quotes **“ ”** in visible text, single curly **‘ ’** for a quote inside a quote. Straight `"` only
  inside JSON-LD strings (escaped). Quoted English source text: “English original” (tradução em português) as the vs pages do.
- **Decimal comma, thousands dot:** 4,8 · 17,6 MB · 1.080 (but resolutions keep their name: 1080p, 4K, HD).
- **Prices:** `US$ 4,99` (space after US$, decimal comma). Never `US$4.99`. The site never shows R$ unless the source does.
  (House rule: no ContentCam price in social content; the pricing page and comparison tables are the exception.)
- **Zoom:** `0,5x`, `1x`, `2x` (S1). Never `0.5x`.
- **Frame rate unit:** in website prose use **`60 fps`** (space; Portuguese number-unit spacing, and 20 of 45 pages already
  do this). `60fps` without space is the store/app UI spelling: keep it only when quoting a UI label or the store list.
- **Time units in specs:** `0,5s a 30s` as in S1 is acceptable for spec lists; in prose prefer `0,5 s` / "meio segundo".
- **Dates:** prose `6 de novembro de 2026`; first of the month `1º de julho de 2026` (ordinal º). Months lower case.
  Tables may use `21 out. 2026` (abbreviation with period) or `21/10/2026` (dd/mm/aaaa), one style per table. Never
  month-first.
- **Version strings stay as published:** "iOS 18 ou posterior" (S1, not *superior*), "iOS 2.8.1", "Android 2.7.0".
- **Capitalisation:** sentence case in titles and H2s (Portuguese does not title-case): "Como gravar com a câmera frontal e
  traseira ao mesmo tempo no iPhone (2026)". Proper feature names keep their own capitals (Captura Dupla, Câmera Dupla do
  Snapchat). ContentCam mode names: capital first letter only (Frontal e traseira, Lente dupla).
- **Gender of names:** *o ContentCam*, *o app* (masculine, S1 "o ContentCam nunca envia"), *a Captura Dupla* (V, S5),
  *a Câmera Dupla do Snapchat*, *a Visão do Diretor*, *a Gravação dupla*, *o Dual do Instagram*, *o modo Frontal e traseira*.
  Competitor apps: masculine (*o DualCam, o Dualgram, o DoubleTake*).
- *app* (masc.), never *aplicativo* on this site (0 uses; S1/S2 use *app*). *aplicativo* is not wrong, just off-voice.

---

## 2. Mandated term table

| English concept | Use (pt-BR) | Avoid / forbidden | Source / confidence |
|---|---|---|---|
| front camera | câmera frontal; "a frontal" once established | câmera da frente (ok in search-phrase H2 only), câmera dianteira, câmera anterior | S1 S3 V; A ("câmera frontal e traseira" dominant) |
| back / rear camera | câmera traseira; "a traseira" | câmera de trás (only as quoted search phrase), câmera posterior, câmera principal (ambiguous) | S1 S3; A |
| selfie camera | câmera de selfie, or "a selfie" (S1: "mude para a selfie") | câmera selfie (no *de*), selfie-cam | S1; site majority (36 vs 4) |
| front and back camera at the same time | câmera frontal e traseira ao mesmo tempo / gravar com a câmera frontal e a traseira ao mesmo tempo | simultaneamente in titles (fine in body), concomitante, *simultâneo* as keyword (S4: drifts to simultaneous translation) | A (top suggestion family) |
| both cameras | as duas câmeras | ambas as câmeras (stiff), câmeras duplas | A ("gravar com as duas câmeras ao mesmo tempo") |
| dual camera (generic concept) | câmera dupla | câmera dual, dual camera (English), câmara | S4 app name "ContentCam: Câmera Dupla"; A. **Never bare "câmera dupla" as a whole title**: autocomplete drifts to CCTV (wifi, icsee, yoosee, intelbras). Pair it: "app de câmera dupla", "câmera dupla no iPhone/TikTok/Instagram", "efeito de câmera dupla" |
| portrait (orientation) | vertical / na vertical | retrato, modo retrato, em pé (colloquial; ok once), *portrait* | S1 S3 ("PORTRAIT → VERTICAL") |
| landscape (orientation) | horizontal / na horizontal | paisagem, modo paisagem, deitado, *landscape* | S1 S3 ("LANDSCAPE → HORIZONTAL"); S4 (paisagem = scenery/garden drift) |
| portrait + landscape at once | vertical e horizontal ao mesmo tempo / na vertical e na horizontal ao mesmo tempo | retrato e paisagem | S1 opening line; A ("gravar na vertical e horizontal ao mesmo tempo") |
| both formats | os dois formatos | ambos os formatos, os dois aspectos | S1 S3 |
| take | take / takes (masc., plural *takes*) | tomada, gravação when a ContentCam take is meant | S1 S3 (app UI uses take everywhere) |
| recording (noun) | gravação | filmagem (ok in prose for a shoot, not for the file) | S1 |
| to record | gravar (default); filmar ok for variety in how-to prose | capturar for video (Apple uses it for photos/modes) | S1; A (gravar >> filmar) |
| file | arquivo | ficheiro (PT-PT) | S1 |
| two separate files | dois arquivos separados | dois ficheiros, dois vídeos independentes | S1 |
| split screen | tela dividida | ecrã dividido (PT-PT), split screen, tela partida | S1 S3 ("Split → Tela dividida"); A |
| picture-in-picture | Picture in Picture (capitals, no hyphens) | picture-in-picture, PiP (except in a quote), imagem na imagem, tela sobre tela | S1 S3; A ("imagem na imagem" returns junk) |
| reaction video | vídeo de reação | react (English), vídeo react | A ("como fazer vídeo de reação") |
| watermark | marca d'água (straight apostrophe is fine, as S1) | marca de água (PT-PT) | S1 |
| ads | anúncios | propagandas (ok colloquially, not in claims), publicidade | S1 |
| free (price) | grátis; de graça (rhythm) | gratuito is fine in prose; free trial = **teste grátis** | S1 S3 ("Iniciar teste grátis", "7 dias grátis") |
| free trial | teste grátis / 7 dias grátis | avaliação gratuita, período de avaliação, trial | S3 |
| lifetime / one-time purchase | acesso vitalício; pagamento único (S1) or compra única (S3) | vitalício alone as a noun outside the plan name; licença perpétua | S1 S3. Plan label: "Vitalício" |
| subscription | assinatura; assinar o Premium | subscrição (PT-PT) | S3 |
| unlock (Premium) | liberar ("O PREMIUM LIBERA") | desbloquear (ok, but S1 uses liberar) | S1 |
| settings (iOS) | Ajustes | Configurações (that is Android), Definições (PT-PT) | V S5 S7; S3 |
| settings (Android) | Configurações | Ajustes | Android pt-BR UI (U, standard) |
| Photos app / library | app Fotos; Fototeca | rolo da câmera / Rolo da Câmera (retired Apple term, S4 bug 7), galeria for iPhone | S3; V S5 |
| gallery (Android) | galeria | rolo da câmera | U (standard Android wording) |
| frame rate | frame rate (ContentCam feature context, as S1 "Resolução e frame rate") · taxa de quadros (when describing iOS Ajustes, as Apple does) | velocidade de quadros, FPS rate | S1; V S7 ("taxa de quadros") |
| resolution | resolução; HD, 4K, 1080p unchanged | Full HD unless the source says it | S1 |
| wide / ultra-wide lens | grande-angular / ultra-angular (hyphenated) | grande angular (no hyphen), ultrawide, ultra grande-angular | S1 S3 |
| lens | lente (fem.): a lente 0,5x | objetiva | S1 |
| manual controls | controles manuais: exposição, balanço de branco, ISO, obturador | controlos (PT-PT), equilíbrio de brancos | S1 |
| white balance | balanço de branco (ContentCam) · Apple setting is "Bloquear Balanço de Brancos" | equilíbrio de brancos | S1; V S7 |
| stabilisation | estabilização | estabilizador | S1 |
| teleprompter | teleprompter (masc.) | TP, ponto eletrônico | S1; A ("app teleprompter", "teleprompter para celular") |
| script | roteiro | guião (PT-PT), script | S1 S3 |
| timelapse (ContentCam feature) | Timelapse (S1 spelling) · Apple's own is "Time-lapse" | time lapse | S1; V S7 |
| trim | cortar / corte ("Corte na revisão") | aparar, trimar | S1 |
| crop | recortar / recorte | cropar | S1 |
| scene / project | cena / projeto (ContentCam entities) | do not use *cena* loosely for "the view" in instructions; say "a cena da câmera traseira" | S1; S4 bug 5 |
| creator(s) | criador(es) de conteúdo / criadores | creators, influenciadores (different meaning) | site usage (105, consistent) |
| to post | postar; publicar (fine) | upar | S1 ("prontos para postar") |
| screenshot | print (colloquial) or captura de tela | screenshot | both used; pick per tone, one per page |
| download (verb) | baixar | fazer download (ok), descarregar (PT-PT) | site usage |
| device (generic) | celular / iPhone; aparelho only translating "device" in quotes | dispositivo (ok in technical Android API context only) | S4 |
| switch camera while recording | trocar de câmera enquanto grava | alternar câmera durante gravação (stiff) | A ("trocar de câmera enquanto grava iphone") |
| iOS 18 or later | iOS 18 ou posterior | iOS 18 ou superior, iOS 18+ in prose | S1 |
| iPhone XS or newer | iPhone XS ou mais recente(s) | ou superior | S1 |
| Apple Account | Conta Apple | ID Apple (retired) | support page usage; Apple rename (U for pt-BR string) |
| CTA "Try ContentCam free" | Experimente o ContentCam grátis / de graça | Teste grátis o ContentCam (sounds like trial) | 30 pages consistent |

---

## 3. ContentCam mode and feature names (exactly as the store copy writes them)

From S1 (App Store description v2.8.2). These are the names to use on the website.

| English | pt-BR name | Notes |
|---|---|---|
| Single Lens | **Lente única** | S1 S3 |
| Dual Lens | **Lente dupla** | S1 S3. "modo Lente dupla" |
| Front & Back | **Frontal e traseira** | S1 (and S2). "o modo Frontal e traseira". Capital F when naming ContentCam's mode; lower case "um modo frontal e traseira" when generic. |
| Front camera (mode) | **Câmera frontal** | S1 |
| Normal camera / portrait only | **Câmera normal** | S1 |
| Combine | **Combinar** ("toque em Combinar") | S3. Output layouts: Picture in Picture, tela dividida |
| Photo mode | **modo Foto** in prose, **Modo Foto** at sentence/list start | S3 "Modo Foto"; S1 list "Modo foto" (list casing). Pick capital-F Foto: it is a mode name like Apple's "modo Vídeo" |
| Teleprompter | **Teleprompter** | S1 |
| Timelapse | **Timelapse** | S1 |
| Manual controls | **Controles manuais** | S1 |
| Projects, scenes and takes | **Projetos, cenas e takes** | S1 |
| Recording folder | **Pasta de gravações** | S1 |
| Review and trim | **Revisão e corte** | S1 |
| Storage estimate | **Estimativa de espaço** | S1 |
| Crash protection | **Proteção contra travamentos** | S1 |
| Thermal monitoring | **Monitoramento térmico** | S1 |
| Guides (level, crosshair, audio meter) | **Guias**: indicador de nível, mira central, medidor de áudio | S1; app also "Grade" (grid) S3 |
| AE/AF lock | **Bloqueio AE/AF** | S2 S3 |
| Background blur (Android, beta) | **Desfoque de fundo (Beta)** | S2 |
| Shutter button | **botão de disparo** | S1 |
| Premium / Lifetime | **Premium** · plan **Vitalício** · "acesso vitalício" | S1 S3 |
| Free version | **versão grátis** | S1 |

**Known source conflict (do not "fix" pages toward the app):** the shipping iOS UI (S3) still labels the mode switcher
button **"Frente/Trás"** and some strings say "Modo Frente e traseira" / "FRENTE + TRÁS" (from the V2.2 era). The v2.8.2
store copy (S1) and Play copy (S2) renamed it **Frontal e traseira**, and all 41 pages that name the mode already use
Frontal e traseira (632 uses, zero "Frente e traseira"). Keep **Frontal e traseira** on the website. Only when a page gives
a literal tap instruction for the mode switcher, it may add the on-screen label: "toque em Frente/Trás no seletor de modos".
Flag to the app owner: the app UI and the store copy disagree.

---

## 4. Platform names in pt-BR

### Apple (iPhone)
| English | pt-BR | Confidence |
|---|---|---|
| Dual Capture | **Captura Dupla** (fem.: "a Captura Dupla", "vídeos de Captura Dupla", "gravar com Captura Dupla") | **V** S5 |
| Models that support Dual Capture video | **Modelos compatíveis com vídeo de Captura Dupla** | **V** S6 (lists iPhone 17, 17 Pro, 17 Pro Max, Air, 18 Pro, 18 Pro Max, iPhone Duo) |
| Camera app / Video mode | app **Câmera** / modo **Vídeo** ("Selecione o modo Vídeo") | **V** S5 |
| Record button | botão **Gravar** | **V** S5 |
| Camera Control | **Controle da Câmera** | **V** S5 |
| Settings > Camera > Record Video | **Ajustes > Câmera > Gravar Vídeo** | **V** S7 |
| Record Sound / Stereo | **Gravar Som** · "Gravar Som em Estéreo" | **V** S7 |
| Enhanced Stabilisation | **Estabilização Aprimorada** | **V** S7 |
| Lock Camera / Lock White Balance | **Bloquear Câmera** / **Bloquear Balanço de Brancos** | **V** S7 |
| Action mode | **modo Ação** / **modo de Ação** (Apple uses both) | **V** S5 |
| Slow motion / Time-lapse / Cinematic | **Câmera Lenta** / **Time‑lapse** / **modo Cinema** | **V** S5 S7 |
| frame rate (Apple) | **taxa de quadros** | **V** S5 S7 |
| Photos app / Library | app **Fotos** / **Fototeca** | **V** S5 (Fototeca) |
| User Guide | **Manual de Uso do iPhone** (current page title) | **V** S6. Pages write "Manual do Usuário do iPhone": acceptable paraphrase, prefer the official title when citing |
| Mirror Front Camera, Grid, Formats, Preserve Settings | Espelhar Câmera Frontal, Grade, Formatos, Preservar Ajustes | **U** (not reached on Apple BR this pass) |
| Apple Account | Conta Apple | **U** (renamed globally 2024; pt-BR string not checked) |

### Samsung (Galaxy)
| English | pt-BR | Confidence |
|---|---|---|
| Director's View | **Visão do Diretor** | **V** S9 (Samsung Newsroom Brasil; one older article says "Visão de Diretor"); A ("visão do diretor samsung") |
| Dual recording | **Gravação dupla** (menu casing U; Newsroom writes "Gravação Dupla") | **V** S9 for the name; A ("gravação dupla samsung", with "sumiu" a frequent suffix) |
| Camera app | app **Câmera** | U (standard One UI) |
| More (modes menu) | **Mais** | U (S9 describes "toque em 'mais'") |
| Settings | **Configurações** | U (One UI standard) |

Write "a Visão do Diretor (Director's View)" only on first mention if the page cites an English Samsung source; never the
bare English name in prose.

### Google
| English | pt-BR | Confidence |
|---|---|---|
| Google Play / Play Store | Google Play | brand, unchanged |
| Pixel Camera | Pixel Camera (pages use "Ajuda da Pixel Camera") | U whether the pt-BR app is titled "Câmera Pixel"; keep as is |

### Snapchat
| English | pt-BR | Confidence |
|---|---|---|
| Dual Camera | **Câmera Dupla** ("a Câmera Dupla do Snapchat") | **V** S8 |
| layouts: vertical, horizontal, picture-in-picture, cutout | vertical, horizontal, picture-in-picture, recorte | **V** S8 (Snap writes it lower case; on our site keep "Picture in Picture" house style) |
| Lenses / Stories / Spotlight / Memories | **Lentes** / **Histórias** / **Holofote** / **Memórias** | **V** S8 for Lentes, Histórias, Holofote; Memórias **U** |
| Camera Roll (tab in Memories) | Rolo da Câmera | **U** (only acceptable when naming Snapchat's own tab) |

### Instagram (Meta)
| English | pt-BR | Confidence |
|---|---|---|
| Dual (Reels/Stories camera tool) | Meta's name: **Dual**. In the pt-BR app the button reportedly reads **"Duplo"** | Dual **V** (Meta global); "Duplo" **U** (S11 secondary press only) |
| Reels / Stories | **Reels** / **Stories** (Instagram pt-BR keeps the English) | U (standard; site consistent) |
| Edits (app) | Edits | brand |

Rule: name it **"o Dual do Instagram"** in prose (78 uses, 15 pages already). In titles/H2s lead with the search phrase
**"câmera dupla do Instagram"** (A, much stronger than "dual instagram", whose suggestions are English "dual app" clones).
Optionally on first mention: "o Dual (no app em português pode aparecer como “Duplo”)". Do not alternate Dual/Duplo.

### TikTok
| English | pt-BR | Confidence |
|---|---|---|
| Duet / Stitch / Green Screen | Dueto / Costurar / Tela verde | U |
| TikTok has no native dual camera | say "o TikTok não tem câmera dupla nativa" | site claim, keep per source |

---

## 5. Native search phrasing (Google autocomplete, hl=pt-BR, gl=br, 15 Nov 2026)

Users type without accents (camera, tras, video); write accented, Google folds them. Strongest families first.

**Front + back at the same time (core):**
- como gravar com a camera frontal e traseira ao mesmo tempo (+ iphone, samsung, instagram, xiaomi, android, motorola, s24)
- câmera frontal e traseira ao mesmo tempo (+ iphone, iphone 17); usar câmera frontal e traseira ao mesmo tempo android / iphone / instagram
- gravar com as duas câmeras do celular ao mesmo tempo (+ iphone, android, instagram); gravar duas cameras ao mesmo tempo (+ iphone, samsung); app gravar duas cameras ao mesmo tempo
- como gravar as duas cameras ao mesmo tempo iphone 15 / 16 / 17; como usar duas cameras ao mesmo tempo iphone
- app para gravar camera frontal e traseira (ao mesmo tempo); aplicativo para gravar com duas câmeras ao mesmo tempo
- como fazer video com duas cameras (iphone, instagram, iphone 17); como fazer vídeo usando as duas câmeras do celular
- **camera frente e verso** (iphone, instagram, samsung, iphone 17, ao mesmo tempo), como gravar video frente e verso: real BR phrasing, see section 7 before using
- camera da frente e de tras do iphone (thin)

**Dual camera:**
- câmera dupla iphone (15, 16, 17, 17 pro max); app camera dupla (iphone, android); app de camera dupla
- câmera dupla instagram (2026, sumiu, iphone, android), efeito camera dupla (instagram, iphone), modo camera dupla instagram, como gravar camera dupla instagram
- camera dupla tiktok (thin)
- bare "camera dupla" = security cameras (wifi, icsee, yoosee, intelbras). Always qualify.

**Apple Dual Capture:**
- captura dupla iphone (15, 16, 17, 13, 14, 16 pro max): people search it for phones that do not have it, which is the angle of the iPhone 15/16 pages
- "captura dupla" alone also returns "captura dupla starship" (noise)

**Samsung:**
- gravação dupla samsung (a56, s24 ultra, sumiu, s24, a55, s25 ultra, s23, s25 fe); visão do diretor samsung (s23, s23 ultra, sumiu, s25 ultra, s24 ultra, s26 ultra); "dual recording samsung" also typed in English

**Vertical + horizontal:**
- gravar na vertical e horizontal ao mesmo tempo (the only on-target completion)
- "vídeo horizontal e vertical" drifts to conversion (horizontal para vertical, capcut); "gravar vídeo na horizontal ou vertical" is a "which is better" query
- "retrato e paisagem" returns nothing: confirms vertical/horizontal

**Split screen / PiP:**
- vídeo com tela dividida (capcut, instagram, tiktok, edits), como fazer vídeo com tela dividida no celular, como gravar video com tela dividida, tela dividida iphone (+ model numbers, but that is mostly multitasking intent)
- picture in picture: English only and streaming-intent (netflix, youtube); "imagem na imagem" is junk

**Other:**
- como fazer vídeo de reação (no capcut, no instagram, pelo celular); "vídeo de reação" alone drifts to chemistry
- trocar de camera enquanto grava (iphone, instagram)
- foto: como tirar foto com a camera frontal e traseira ao mesmo tempo (iphone, samsung)
- teleprompter para celular (gratuito, app, iphone); app teleprompter gratuito (android, iphone)
- app camera sem anúncio (thin)

Title/H2 patterns that fit: "Como gravar com a câmera frontal e traseira ao mesmo tempo no iPhone (2026)", "Como gravar com as
duas câmeras do celular ao mesmo tempo", "Como gravar na vertical e na horizontal ao mesmo tempo", "Câmera dupla do Instagram
sumiu?", "Gravação dupla da Samsung sumiu?", "Como fazer vídeo com tela dividida no celular". Existing titles already follow
these; keep the year.

---

## 6. Inconsistencies found across existing pt-br pages (18)

Counts are visible text + JSON-LD, 15 Nov 2026. "Right" = what to normalise to on the next pass.

1. **Snapchat feature name.** "Dual Camera (do Snapchat)" in English: 58 uses on 9 pages (snapchat-front-and-back-camera 20,
   film-reaction-video-phone 10, dual-camera-effect 7, bereal-style-photo-without-bereal 6, take-photo-front-and-back-camera-same-time 6,
   film-kid-reaction-and-what-they-see 4, how-to-do-dual-camera-on-tiktok 2, switch-camera-while-recording-iphone 2,
   dual-camera-app-without-ads 1). **Right: "a Câmera Dupla do Snapchat"** (S8), already used on best-front-and-back-dual-camera-apps,
   instagram-dual-camera-missing, record-front-and-back-camera-same-time-iphone, split-screen-video-iphone. bereal page also uses
   masculine "o Dual Camera": wrong gender either way. Keep English only inside cited help-article titles.
2. **Instagram Dual: "Dual" vs "Duplo".** dual-camera-effect uses "o Duplo do Instagram" (6); 15 other pages use "o Dual do
   Instagram". **Right: Dual** (section 4), with optional one-time gloss.
3. **Samsung Director's View.** switch-camera-while-recording-iphone says "a Director's View com gravação dupla" (2, English name,
   lower-case feature). **Right: "a Visão do Diretor" / "a Gravação dupla"**, as record-front-and-back-camera-samsung-galaxy and
   record-front-and-back-camera-same-time-android do. Those two pages may keep "(Director's View)" once as a gloss.
4. **Apple Dual Capture in English.** dual-camera-app-without-ads: "que não têm o Dual Capture da Apple" (1). **Right: "a Captura
   Dupla da Apple"** (297 uses, 24 pages). English "Dual Capture" otherwise appears only in cited English source titles/quotes (ok).
5. **take vs tomada.** vs/dualcam uses "tomada(s)" 15 times (plus "Tomadas seguras"); vs/lookout once inside a translated quote.
   **Right: take/takes** (S1/S3, 205 uses on 41 pages). In vs/lookout's quote gloss, "um único take perfeitamente sincronizado".
6. **Orientation as "Retrato e paisagem".** Comparison-table row labels on vs/apple-dual-capture, vs/detail, vs/lookout, vs/mixcam,
   vs/2cam ("Retrato e paisagem em um só take / na mesma gravação"). **Right: "Vertical e horizontal..."**. vs/2cam's quotes of 2Cam's
   own page ("modo retrato ou paisagem") may stay as quotes.
7. **"rolo da câmera".** instagram-dual-camera-missing (3: "envie para o Reels pelo rolo da câmera") and snapchat-front-and-back-camera (4).
   **Right: "pela galeria do celular" / "a partir do app Fotos"** for iPhone/Instagram. On the Snapchat page, only where it names
   Snapchat's own Memórias tab, "Rolo da Câmera" (U) may stay, capitalised.
8. **Price format.** "US$8.99", "US$29.99", "US$2.99", "US$5.99" with no space and decimal point: dual-camera-app-without-ads (14) and
   iphone-duo-camera (7). **Right: "US$ 8,99"** (133 uses on 10 pages).
9. **Zoom decimal.** changelog "0.5x" (2). **Right: "0,5x"** (S1).
10. **fps spacing.** "60fps" on 23 pages (71) vs "60 fps" on 20 pages (261); several pages mix (e.g. record-front-and-back-camera-iphone-15-16,
    home, changelog, android, vs index). **Right: "60 fps"** in prose; "60fps" only when quoting the store/app UI.
11. **Quote marks.** Curly “ ” on 11 pages (all vs/* except dualcam, plus iphone-4k..., google-pixel, film-kid-reaction), straight " " in
    visible text on 22 pages, mixed on android and vs/dualgram. **Right: curly “ ”.**
12. **picture-in-picture casing.** Lower-case hyphenated "picture-in-picture" 31 uses on 9 pages (vs/dualgram 10, vs/dualcam 7,
    iphone-duo-camera 6, record-front-and-back-camera-samsung-galaxy 3, others 1 each) and "PiP" twice on the Samsung page. **Right: "Picture in
    Picture"** (S1/S3; 107 uses on 30 pages) unless quoting.
13. **"câmera selfie" vs "câmera de selfie".** "câmera selfie" on doubletake-not-working-alternatives (2), film-reaction-video-phone (1),
    changelog (1). **Right: "câmera de selfie"** (36 uses) or "câmera frontal".
14. **Photo mode casing.** "Modo Foto" (changelog) vs "modo foto" (take-photo-front-and-back-camera-same-time 10+, features). **Right: "modo Foto"**
    in prose, "Modo Foto" at list/sentence start.
15. **frame rate vs taxa de quadros.** "frame rate" on 5 pages, "taxa de quadros" on 5 pages (vs/lookout, vs/dualcam, vs/detail, vs/mixcam,
    iphone-4k...). **Right:** "frame rate" for ContentCam settings, "taxa de quadros" when describing Apple/iOS settings; do not mix both for
    the same thing on one page.
16. **Table date styles.** doubletake-not-working-alternatives "10 mar 2025" (no period) while dual-camera-app-one-time-purchase uses "21 out. 2026"
    and phone-teleprompter-apps-compared uses "04/11/2026". **Right:** "10 mar. 2025" (abbreviation with period) or dd/mm/aaaa, one style per table.
17. **Apple guide title.** Pages cite "Manual do Usuário do iPhone"; Apple BR's current title is "Manual de Uso do iPhone" (S6). And
    iphone-17-dual-capture-limitations glosses the model list as "Modelos compatíveis com vídeo em Captura Dupla"; official is "...vídeo **de**
    Captura Dupla". **Right:** the official titles when citing.
18. **"aparelho" outside quotes.** 23 uses on 12 pages; most are fine (translations of "device" inside quotes on iphone-4k-front-and-back-camera-same-time),
    but plain-prose uses on features/teleprompter (2), features/manual-controls (1), index (1), vs/2cam (1), vs/mixcam (1), vs/dualgram (2),
    doubletake-not-working-alternatives (1), instagram-dual-camera-missing (2) should be **"celular" / "iPhone"** (S4).

Consistent already (no action): Frontal e traseira (632, no variants), Lente dupla / Lente única, Captura Dupla, tela dividida,
celular, arquivo, marca d'água, você (no *tu*), Ajustes (iOS) vs Configurações (Android) on support, "iOS 18 ou posterior", "Experimente o
ContentCam" CTA, no em dashes, no PT-PT forms (ecrã/telemóvel/ficheiro: 0).

---

## 7. False friends and calque traps (this subject, pt-BR)

- **paisagem** = scenery/landscape view, not landscape orientation. "Grave o seu rosto e a paisagem" (switch-camera page) is correct
  Portuguese for the view; "vídeo em paisagem" for orientation is a calque. Use horizontal. Same for **retrato** = a portrait photo, and
  Apple's **modo Retrato** is the depth-effect photo mode (S4 notes the clash). Never say ContentCam records "em retrato".
- **frente e verso** = two sides of a sheet/document. Brazilians do type "camera frente e verso" (A), so it may appear once as a recognised
  search phrase in body text or an FAQ question ("também chamado de câmera frente e verso"), never as the mode name or in a heading on its own.
- **frente e trás**: "câmera frente e trás" autocompletes to **dashcams** (carro, veicular, automotiva). Do not use as a heading keyword.
  It is also the older in-app label (section 3).
- **câmera dupla** bare = CCTV / security cameras (A). Qualify it.
- **simultâneo** as a keyword drifts to *tradução simultânea* (S4). "ao mesmo tempo" is what people type.
- **gravar** vs **filmar**: both fine; **capturar** is Apple's verb for photos/modes and reads translated for video in our prose.
- **take** is the creator word in BR and in the app; **tomada** reads European/dubbed, and *tomada* is also the electrical socket.
- **cena** is a ContentCam entity (Projetos, cenas e takes). Avoid "toque na cena" ambiguity: say "toque na imagem da câmera traseira".
- **câmera / câmara**: Brazilian is **câmera**. *Câmara* is PT-PT (and in BR means a chamber/legislature).
- PT-PT leakage to block: ecrã (tela), telemóvel (celular), ficheiro (arquivo), descarregar (baixar), definições (Ajustes/Configurações),
  guião (roteiro), subscrição (assinatura), controlos (controles), utilizador (usuário), registar (gravar), *estás a gravar* (você está gravando).
- **realizar** ≠ "realise" (use *perceber*); **atualmente** ≠ "actually" (use *na verdade*); **eventualmente** ≠ "eventually" (use *no fim*,
  *com o tempo*); **pretender** ≠ "pretend"; **suportar** for device support is common but prefer **ser compatível com / funcionar em**
  (S3: "não é compatível com este iPhone").
- **app nativo / câmera nativa**: fine for the built-in Câmera app; S1 "estabilização de nível nativo" is store wording, keep it.
- **lifetime** ≠ *tempo de vida*; use **vitalício / acesso vitalício**.
- **free** ≠ *livre*; use grátis / de graça.
- **review** (App Store rating) = **avaliação**; product review video = **review** (S2 "Reviews de produtos") or análise.
- **feature** = **recurso** (S1 "pedido de recurso"), not *funcionalidade* (PT-PT-leaning) or *feature*.
- **upgrade** = assinar o Premium / liberar; not *fazer upgrade* in UI-style copy.
- **Picture in Picture** stays in English (S1); a literal *imagem na imagem* is not used by people (A).
- Gender traps: *a* Captura Dupla, *a* Câmera Dupla, *a* Visão do Diretor, *a* Gravação dupla, *o* Dual, *o* ContentCam, *o* app, *a* lente,
  *o* take, *o* teleprompter.
