# French (`fr`, France) terminology and style sheet for contentcam.app

Built 15 Nov 2026 for native reviewers and translation agents working on `/fr/`. It covers all 45 pages under
`contentcam-web/fr/` (visible text, meta tags and JSON-LD, scanned in full).

**Order of authority.**
1. iOS store copy `contentcam/docs/store-descriptions/v2.8.2/desc/fr-FR.txt` (the brief's file). v2.8.3 is the
   live successor and uses the same terms. The store copy decides every ContentCam mode and feature name.
2. App glossary `contentcam/docs/localization-glossary-fr.md` (locked, native-reviewed, 465 lines). It is the
   authority for in-app UI labels and for most general camera vocabulary. This sheet does not repeat all of it.
   Read its "Core nouns" and "traps" sections once.
3. Android French UI `contentcam-android/app/src/main/res/values-fr/strings.xml`, for Android screen labels only.
4. Official Apple France, Samsung France and Snap pages, cited inline (fetched 15 Nov 2026).
5. Google autocomplete (`hl=fr&gl=fr`, 15 Nov 2026).

If this sheet and the store copy disagree on a ContentCam feature name, the store copy wins. Tell Jimmy.

Confidence labels: **Store** = verbatim in the store copy or shipped UI. **Verified** = checked against an official
page on 15 Nov 2026. **Autocomplete** = real French query. **Unverified** = not confirmed. Do not present it as an
official label.

---

## 1. Register, person and typography

### Register
- **vous, always.** Imperatives take the -ez form (*Filmez, Touchez, Ouvrez, Combinez*). Possessives are *votre/vos*.
  This matches the store copy ("Vos vidéos restent sur votre téléphone", "quand vous le souhaitez"), the app glossary
  ("Register: vous, binding"), and Apple France ("Filmez-vous tout en filmant ce qui vous entoure", apple.com/fr/iphone-17).
  `vous` also works in Belgium, Switzerland, Québec and francophone Africa. All 45 pages pass: no *tu/ton/ta* found.
- Jimmy's founder voice: *je* talking to *vous* ("je suis Jimmy", "Testé moi-même"). He is a **développeur
  indépendant** (Store: "Créée par Jimmy, développeur indépendant"). Never write *développeur solo*.
- **ContentCam is feminine** (it is *l'app*, f.): *ContentCam est gratuite*, *ContentCam est-elle…?*, *Créée par
  Jimmy*, *laquelle choisir ?* (Store: "Créée par Jimmy"). See §6 for the pages that use the masculine.
- Tone: a creator talking to a creator. Short sentences, active verbs, no corporate nominal style.
- Buttons and labels quoted from an app UI: infinitive (*Enregistrer, Partager, Restaurer les achats*). Prose: vous
  imperative. Never mix them in one string (app glossary).

### Punctuation (France rules)
| Item | Rule | Example |
|---|---|---|
| `: ; ? !` | **U+00A0 no-break space before** (not a normal space, not U+202F, the store copy uses U+00A0 everywhere) | `Comment ça marche ?` |
| Guillemets | **« text »** with U+00A0 inside both marks. Never `"…"` in visible French text | `« Double capture »` |
| Quotes inside quotes | “…” (curly English quotes) inside « » | « il a dit “OK” » |
| Apostrophe | Straight `'`: the store copy and about 3,500 uses on the pages. Curly ’ appears about 86 times. Do not mix them in your own prose | `l'app` |
| Dashes | **No em dashes** (brief rule). Use a colon, a comma or a full stop. Spaced en dash ` – ` only for ranges in tables, rarely | |
| English quoted text | Keep English punctuation inside an English quote: « Who is Dual Camera available for? » (no space before `?`) | |
| Parentheses gloss | French term first, English in parentheses: *Avant et arrière (Front/Back)* | Store |
| Headings | Sentence case. Only the first word and proper nouns get a capital: *Comment filmer avec la caméra avant et arrière* | |
| Accented capitals | Keep accents in caps: VIDÉO, ARRIÈRE, ÉCRAN | Store headings |

### Numbers, units, dates, prices
- Decimal comma: `0,5x`, `4,8`, `0,5 s`. Store: "intervalles de 0,5 s à 30 s", "boutons 0,5x, 1x et 2x".
- Thousands: U+00A0 (`12 500`). Resolutions are labels, not numbers: `1080p`, `4K`, `HD`.
- U+00A0 between a number and its unit: `30 s`, `24 fps`, `12 Go`, `50 %`. Zoom factors attach: `0,5x`, `2x`.
- Units: Go/Mo, not GB/MB. **fps** for frame rate in our own voice (Store: "à 24, 25, 30, 50 ou 60 fps"). Apple France
  writes *i/s* (marketing) and *ips* (support). Use those only inside a verbatim Apple quote. See §6.
- Dates: `6 novembre 2026`. Abbreviated in tables: `21 oct. 2026`. Lowercase month. No ordinal except *1er*
  (`1er novembre 2026`). Day-month order, never `11/06`.
- Prices: amount, then U+00A0, then symbol: `5,99 $`, `19,99 €`. Say which store when quoting a US price
  ("sur l'App Store américain"), as the existing pages do.
- Aspect ratios stay `9:16`, `16:9`, `4:3` (no spaces around the colon. This is a ratio, not punctuation).

---

## 2. Mandated terms

| English concept | Use (fr-FR) | Avoid | Source / confidence |
|---|---|---|---|
| record (creator verb) | **filmer** | *enregistrer* as the record verb in UI/how-to (it also means save), *recorder* | Store ("PLUSIEURS FAÇONS DE FILMER"); app glossary §save/record collision |
| recording (noun) | **enregistrement** | *record* | Store, app glossary |
| save | **enregistrer** (*enregistrer dans Photos*) | *sauvegarder* (= back up) | App glossary trap 5 |
| take | **prise** (f.), *prises illimitées* | *take*, *prise de vue* as the countable unit, *séquence* | Store |
| shoot (a session) | **tournage** | *shoot* | Store ("organisez vos tournages") |
| front camera | **caméra avant**; *caméra selfie* fine in prose | *caméra frontale* (0 uses, keep it that way) | Store; Apple FR "caméra avant" (verified) |
| back camera | **caméra arrière** | *caméra dorsale*, *caméra principale* (that is the 1x lens) | Store; Apple FR |
| front and back camera at the same time | **la caméra avant et la caméra arrière en même temps** / *avant et arrière en même temps* | *simultanément* in titles (fine in body) | Store; autocomplete "comment filmer avec la caméra avant et arrière en même temps" |
| dual camera (generic concept, SEO) | **double caméra** (*application double caméra*, *l'effet double caméra*) | *caméra double*, *caméra duale*, *dual caméra* | Autocomplete ("double caméra iphone", "application double caméra"); ASO name "ContentCam: Double Caméra Vlog" |
| portrait / vertical output (9:16) | **vertical** / *en vertical* / *un fichier vertical* | *portrait*, *format portrait* for the output | Store; app glossary trap 3 |
| landscape / horizontal output (16:9) | **horizontal** / *en horizontal* | *paysage* (reads as scenery, and ASO showed `paysage` pulls garden apps) | Store; store-metadata-expansion.md |
| portrait + landscape at once | **en vertical et en horizontal en même temps** | *portrait et paysage* | Store first line |
| lens | **objectif** | *lentille* | Store; app glossary trap 2 |
| wide / ultra-wide | **grand-angle** / **ultra grand-angle** (no hyphen after *ultra*) | *grand angle*, *ultra-grand-angle* | Store |
| frame (one video frame) | **image** (*à l'image près*) | *trame*, *cadre* | Store |
| frame rate | **fréquence d'images**; unit **fps** | *i/s*, *ips*, *images par seconde* in our voice | Store |
| framing | **cadrage** / *cadrer* | | App glossary |
| crop / reframe | **recadrer** / *recadrage* | *rogner* for trim | Store |
| trim | **couper** / *découpe* | *rogner*, *trimmer* | Store ("Visionnage et découpe") |
| edit (in an editor) | **monter** / *montage* | *éditer* | App glossary trap 15 |
| picture-in-picture (layout) | **image dans l'image** | *PiP* alone, *picture-in-picture* untranslated | Store ("en image dans l'image ou en écran partagé") |
| inset / overlay (a fixed corner bubble in another app) | *en incrustation* is allowed as a description, never as the name of ContentCam's layout | *incrustation* for ContentCam's Combiner output | See §6 #15 |
| split screen | **écran partagé** | *écran scindé*, *écran divisé*, *split screen* (except quoting an English UI) | Store; autocomplete has "split screen vidéo" as a loan but it is English, keep it out of body text |
| side by side | **côte à côte** | | Store ("lisez les deux clips côte à côte"); autocomplete "mettre deux vidéos côte à côte" |
| layout | **disposition** (fixed layout of an overlay) or **mise en page** (Combiner layouts). Pick one per page | mixing both in one comparison table | Both used site-wide; neither in the store copy |
| watermark | **filigrane** | *watermark* (except inside an English quote) | Store ("Ni publicité ni filigrane") |
| ads | **publicité(s)**; *sans pub* only in a title/H1 that mirrors search | *pubs* in body | Store; autocomplete "application caméra sans pub" |
| subscription / one-time purchase / lifetime | **abonnement** / **achat unique** / **accès à vie** | *paiement unique*, *licence à vie* | Store |
| free trial | **essai gratuit** (*7 jours d'essai gratuit*) | | Store pricing pages |
| teleprompter | **téléprompteur** (prose, titles); *prompteur* only for the in-app chip or a hardware glass prompteur | *teleprompter* (except a product name, e.g. the app "Teleprompter") | Store; app glossary truncation table |
| timelapse (ContentCam mode) | **Timelapse** / *timelapse* | *accéléré*, *time-lapse* for ContentCam's mode | Store ("Timelapse : intervalles de 0,5 s à 30 s") |
| time-lapse (Apple's Camera mode) | **Accéléré** | | Apple FR guide ("vidéos cinématiques, ralenties et accélérées"); autocomplete "comment filmer en accéléré iphone" |
| manual controls | **commandes manuelles** | *réglages manuels*, *contrôles manuels* | Store ("Commandes manuelles : exposition, balance des blancs, ISO, vitesse d'obturation") |
| shutter speed | **vitesse d'obturation** | | Store |
| shutter button | **déclencheur** (ContentCam); Apple's own UI says *bouton Obturateur* | *obturateur* for ContentCam's button | Store; Apple FR guide (verified) |
| white balance | **balance des blancs** | *équilibre des blancs* | Store |
| focus | **mise au point** | *focus* | Store |
| audio level meter | **vumètre** | *indicateur de niveau audio* | Store; app glossary trap 11 |
| level / horizon | **indicateur de niveau** | | Store ("Repères : indicateur de niveau, réticule central…") |
| crosshair | **réticule central** | *mire*, *croix* | Store |
| stabilisation | **stabilisation** | *stabilisateur* (that is hardware) | Store |
| storage | **espace** / *espace de stockage* | *mémoire* | Store |
| device | **téléphone** (cross-platform), **votre iPhone** (iOS) | bare *appareil* (reads as camera) | Store; app glossary trap 1. Fine inside quotes from Google/Samsung docs |
| the app | **l'app** (f.) in body; **application** allowed in titles/H1 where it is the searched form | *appli* | App glossary; autocomplete ("application double caméra" is the top form, "appli" collapses into it) |
| supported | **pris en charge** / *compatible* | *supporté* | App glossary trap 13 (0 uses now) |
| settings (iOS) | **Réglages** | *Paramètres* on iOS | Apple FR (verified) |
| settings (Android) | **Paramètres** | *Réglages* on Android | ContentCam Android fr strings ("Ouvrir Paramètres"); Android OS French |
| photo library | **photothèque** (Apple's Photos library) | *pellicule* | Apple FR guide ("enregistrées dans votre photothèque dans l'app Photos") |
| reaction video | **vidéo réaction** (no *de*) | *vidéo de réaction* in titles | Autocomplete "vidéo réaction", "video reaction iphone" |
| creators | **créateurs** (*créateurs de contenu*) | *creators* | Pages |
| review (App Store rating) | **avis** | *revue*, *critique* | App glossary |

---

## 3. ContentCam mode and feature names (exactly as the store copy writes them)

| English | Store / prose form | In-app label (what the screen shows) | Notes |
|---|---|---|---|
| Single Lens | **Objectif unique (Single Lens)** | **1 objectif** | Gloss English on first mention only, as the store does |
| Dual Lens | **Double objectif (Dual Lens)**; in running prose *le mode double objectif* (lowercase, Store: "Le mode double objectif exige un iPhone doté d'un ultra grand-angle") | **2 objectifs** | |
| Front/Back | **Avant et arrière (Front/Back)**; in prose *le mode avant et arrière* | **Avant/Arrière** (pill), **AVANT/ARRIÈRE** (paywall tag) | Store also writes "Combiner un enregistrement Avant/Arrière", so the slash form is fine when naming a recording made in the mode |
| Front Camera mode | **Caméra avant** | Caméra avant | |
| Portrait Only / stock cam | **Caméra classique** | | Do not invent *mode simple* |
| Combine | **Combiner** (*Combinez-les ensuite en une seule vidéo*) | Combiner | Outputs: *image dans l'image* or *écran partagé* |
| Photo mode | **Mode photo**; *Photo Avant et arrière* | | Store |
| Shutter (photo) | **Déclencheur** | | Store |
| Library | **Bibliothèque**; list of takes = *liste de prises* | | Store |
| Resolution and frame rate | **Résolution et fréquence d'images** | | Store |
| Manual controls | **Commandes manuelles** | | Store |
| Focus and exposure | **Mise au point et exposition** | | Store |
| Teleprompter | **Téléprompteur** | chip: PROMPTEUR | Store |
| Stabilisation and HDR | **Stabilisation et HDR** | | Store |
| Timelapse | **Timelapse** | | Store |
| Guides / overlays | **Repères** (indicateur de niveau, réticule central, vumètre) | | Store |
| Zoom | **Zoom** (boutons 0,5x, 1x et 2x, pincement ou molette) | | Store |
| Projects, scenes and takes | **Projets, scènes et prises** | | Store |
| Recording folder | **Dossier d'enregistrement** | | Store |
| Review and trim | **Visionnage et découpe**; Premium line *Découpe au visionnage* | | Store. Not *découpe avant sauvegarde* (see §6) |
| Space estimate | **Estimation de l'espace** | | Store |
| Crash protection | **Protection anti-plantage** | | Store |
| Thermal monitoring | **Surveillance thermique** | | Store |
| Premium | **Premium**; heading *CE QUE PREMIUM DÉBLOQUE* | | Store |
| Plans | **abonnement annuel ou mensuel, ou achat unique pour un accès à vie** | | Store |
| Free tier | *Filmez les deux formats avec un seul objectif en HD, gratuitement, prises illimitées et sans compte* | | Store |
| App Store name / subtitle (fr-FR) | **ContentCam: Double Caméra Vlog** / **Vertical + horizontal, 1 prise** | | store-metadata-expansion.md. Store name only; in prose write *ContentCam* |

---

## 4. Platform names in French

### Apple (iOS)
| English | French | Source |
|---|---|---|
| Dual Capture | **Double capture** (capital D, lowercase c; *la Double capture*, *la fonctionnalité Double capture*, *une vidéo Double capture*) | Verified: apple.com/fr/iphone-17, /iphone-17-pro, /iphone-air, /iphone/compare; support.apple.com/fr-fr/guide/iphone/iph61f49e4bb ("Enregistrer des vidéos Double capture … touchez « Double capture »") |
| Apple spec line "Dual Capture up to 4K Dolby Vision at 30 fps" | **« Double capture (Dolby Vision jusqu'à 4K à 30 ips) »** | Verified: apple.com/fr/iphone/compare. Quote this, not the English line |
| Camera app (iOS 18 and iOS 26) | **Appareil photo** (*l'app Appareil photo*, *Réglages > Appareil photo*) | Verified: Apple FR iPhone guide, iOS 18 and iOS 26 versions |
| Camera app (iOS 27) | **Caméra** (*Ouvrez Caméra*, *l'app Caméra*, *Réglages > Caméra*) | Verified: Apple FR iPhone guide, iOS 27 version (now the default). Apple renamed it. See §6 #13 |
| Camera Control (button) | **Commande de la caméra** (iOS 27 and marketing); *commande de l'appareil photo* (iOS 26 guide) | Verified |
| Settings | **Réglages** | Verified |
| Settings > Camera > Record Video | **Réglages > Appareil photo > Enregistrer une vidéo** (iOS 26) / **Réglages > Caméra > Enregistrer une vidéo** (iOS 27) | Verified, guide iphc1827d32f |
| Formats | **Formats** | Verified, guide iphb362b394e |
| Preserve Settings | **Conserver les réglages** | Verified, guide iph62000de98 |
| Mirror Front Camera | **Mise en miroir de la caméra avant** | Verified, guide iph1b88429a6 (iOS 26 and 27) |
| Lock Camera | **Verrouiller l'appareil photo** (iOS 26) / **Verrouiller la caméra** (iOS 27) | Verified |
| Enhanced Stabilisation | **Stabilisation améliorée** | Verified |
| HDR Video | **Vidéo HDR** | Verified |
| Auto FPS | **IPS auto** | Verified |
| Lock White Balance | **Verrouiller la balance des blancs** | Verified |
| Record Slo-mo | **Enregistrer un ralenti** | Verified |
| View Outside the Frame | **Afficher les éléments hors du cadre** | Verified |
| Lens Correction | **Correction de l'objectif** | Verified |
| Record button / Shutter button | **bouton Enregistrer** / **bouton Obturateur** | Verified, guide iph61f49e4bb |
| Video / Cinematic / Slo-mo / Time-lapse / Action mode | **Vidéo / Cinématique / Ralenti / Accéléré / mode Action** | Verified (guide intro + settings pages) |
| Center Stage | **Cadre centré** (feature); hardware *caméra avant Center Stage* | Verified, apple.com/fr/iphone-17 |
| Photos app / Photos library | **Photos** / **photothèque** | Verified |
| Grid / Level (Camera settings) | **Grille** / **Niveau** | Unverified this pass (app glossary marks *Grille* as Apple's word) |
| Frame rate unit | Apple uses **i/s** (marketing) and **ips** (support). ContentCam uses **fps** | Verified |

### Samsung (Galaxy, One UI)
| English | French | Source |
|---|---|---|
| Camera app | **Appareil photo** | Samsung FR support pages ("l'application Appareil photo"), high confidence |
| Director's View | **Vue du réalisateur** (support title also says *mode Réalisateur*) | Verified: samsung.com/fr/support/mobile-devices/utiliser-le-mode-realisateur-sur-mon-galaxy-s-21-… |
| Director's View layouts | Samsung FR leaves them in English: **PIP (Picture-in-picture), Split view, Single view** | Verified, same page |
| Dual recording (S24/S25, One UI 6.1+) | **Double enregistrement** is very likely the French menu label. Write *Double enregistrement (Dual recording)* | **Unverified** on samsung.com/fr. Autocomplete: "double enregistrement samsung s25 ultra", "… s24". A third-party FR article (fr.techtribune.net) cites the label "Double enregistrement". Confirm on a French Galaxy before calling it official |
| More tab | **Plus** | Pages; matches Samsung FR UI, medium confidence |

### Google
| English | French | Source |
|---|---|---|
| Pixel Camera | Keep **Pixel Camera** (proper name) or *l'app Appareil photo du Pixel* | French Play listing name unverified |
| Google Play | **Google Play** / *le Play Store* (spoken) | Use *Google Play* |

### Social apps
| English | French | Source |
|---|---|---|
| Snapchat Dual Camera | **Double caméra** (*le mode Double caméra de Snapchat*) | Medium: Snapchat launch coverage in French (blogdumoderateur.com, 30 Aug 2022, quotes Snapchat: "une nouvelle fonctionnalité nommée Double caméra"). Not checked on help.snapchat.com/fr-FR |
| Instagram Dual | **Dual** (keep it; the pages already write *la caméra Dual d'Instagram*) | French UI label unverified. Autocomplete "double camera instagram" is what people type, so use that in the title, as `instagram-dual-camera-missing` does |
| Instagram Reels | **Reels** (plural), *un Reel* | Gender and FR UI casing unverified; pages use *Reels* |
| TikTok | **TikTok**; there is no native TikTok dual camera today. *TikTok Now* is a past feature name and stays English | Pages |
| YouTube Shorts | **Shorts** | Unverified as an FR UI label, but it is the brand name |
| BeReal | **BeReal** (brand); "BeReal-style photo" = *photo façon BeReal* | Page title + autocomplete-style phrasing |

**Collision warning:** *Double capture* (Apple), *Double caméra* (Snapchat, and also ContentCam's own nav label for
`/features/dual-camera/`), *Double enregistrement* (Samsung) and *Double objectif* (ContentCam's Dual Lens) are four
different things. Always attach the owner (*la Double capture d'Apple*, *le mode Double caméra de Snapchat*). Never
use one of these names lowercase as a generic description of a rival's feature.

---

## 5. Native search phrasing for titles and H2s (autocomplete-verified, hl=fr gl=fr, 15 Nov 2026)

Strong (appear as completions):
- **comment filmer avec la caméra avant et arrière en même temps** (top completion for several seeds)
- **filmer avec camera avant et arriere iphone**, *comment filmer avec camera avant et arriere iphone*
- **camera avant et arriere iphone 17 / 17 pro max / 13**, *video camera avant et arriere iphone*, *activer camera avant et arriere iphone*
- **filmer avec les 2 caméras samsung**, *filmer avec les 2 caméras android*, *filmer avec les deux camera iphone*
- **comment filmer en double camera**
- **double caméra iphone** (+ 15 / 16 / 17 / 17 pro), *double camera samsung* (+ s24/s25/s26), *double camera android*, *double camera pixel*
- **double capture iphone** (+ 15 / 16 / 17 / 17 pro / air / 18 pro), *double capture video iphone*, *double capture samsung*, *ios 26 double capture*
- **application double caméra**, *application double camera iphone*, *app dual camera android*
- **double camera tiktok**, *double camera instagram* (+ story), *double caméra snapchat android*
- **photo avant et arriere en meme temps (iphone)**
- **double enregistrement samsung** (+ s24 / s25 / s25 ultra), **dual recording samsung** (both forms are typed), **vue du réalisateur samsung**
- **filmer en vertical ou horizontal**, *filmer en horizontal ou vertical*, *format vertical vs horizontal*, *comment filmer en vertical*
- **convertir video horizontale en verticale** (the pain the product removes)
- **mettre deux vidéos côte à côte** (+ iphone / capcut / instagram), *fusionner deux vidéos iphone*
- **split screen video iphone / split screen video ios** (French users type the English term for split screen; use *écran partagé* in the H1 and *split screen* once in body or FAQ)
- **téléprompteur application**, *téléprompteur gratuit pour téléphone*, *application prompteur iphone gratuit*, *teleprompter iphone* (both spellings typed)
- **vidéo réaction**, *video reaction iphone*, *video reaction tiktok*
- **application caméra sans pub**, *application vidéo sans pub*, *application sans abonnement*
- **comment filmer en accéléré iphone**, *comment filmer en time lapse* (Apple mode vs generic term)
- **changer de camera en filmant iphone**

No completions (low volume or not phrased this way): *filmer en vertical et en horizontal en même temps*, *vidéo
verticale et horizontale en même temps*, *image dans l'image vidéo*, *écran divisé vidéo*, *filmer pour tiktok et youtube*,
*achat unique application*. These remain the right descriptive titles for our own concept, but pair them with a
typed form in the H2s or FAQ (*filmer en vertical ou horizontal ?*, *convertir une vidéo horizontale en verticale*).

Title patterns already used that read natively and should be kept: *Comment filmer avec la caméra avant et arrière en
même temps sur iPhone (2026)*, *Quels iPhone ont la Double capture ?*, *Quelle application double caméra sans pub ?*,
*Peut-on filmer … sur un Google Pixel ?* For comparisons, use **« ContentCam ou X : laquelle choisir ? (2026) »**.

---

## 6. Inconsistencies across the existing `fr` pages (21)

Counts are from the 15 Nov 2026 scan. "Right" is what new and revised pages must use.

1. **Frame-rate unit.** Right: **fps** (store copy, 27 pages). Wrong in our own voice: *i/s* in 14 pages (vs/dualcam 63
   uses, including the title "60 i/s"; vs/apple-dual-capture 27; blog/iphone-duo-camera 16; blog/how-to-do-dual-camera-on-tiktok 8;
   blog/record-front-and-back-camera-google-pixel 7; vs/lookout 7; blog/film-kid-reaction-and-what-they-see 6; vs/detail 4;
   blog/switch-camera-while-recording-iphone 3; blog/doubletake-not-working-alternatives 2; vs/dualgram 2; vs/mixcam 2;
   blog/record-front-and-back-camera-same-time-android 1; vs/2cam 1) and *ips* in blog/record-front-and-back-camera-same-time-iphone (5).
   Several pages mix fps and i/s. Keep *i/s*/*ips* only inside a verbatim Apple FR quote.
2. **Samsung Dual recording.** Left in English as *Dual recording* in blog/record-front-and-back-camera-samsung-galaxy (28),
   blog/record-front-and-back-camera-same-time-android (13), blog/snapchat-front-and-back-camera (1), but called
   *l'enregistrement double* in blog/switch-camera-while-recording-iphone (2). Right: *Double enregistrement (Dual recording)*
   on first mention, then *Double enregistrement* (the label is unverified, see §4). At minimum, make all pages use the same form.
3. **Director's View.** blog/switch-camera-while-recording-iphone writes *Director's View* with no French (2). Right:
   **Vue du réalisateur** (verified), with *(Director's View)* at most once, as the samsung-galaxy and android pages do.
4. **Snapchat Dual Camera.** Left in English in body text: blog/snapchat-front-and-back-camera (31), blog/film-reaction-video-phone (12),
   blog/bereal-style-photo-without-bereal (9), blog/dual-camera-effect (9), blog/film-kid-reaction-and-what-they-see (9),
   blog/instagram-dual-camera-missing (9), blog/take-photo-front-and-back-camera-same-time (8), blog/dual-camera-app-without-ads (8, mostly
   rival app names, which stay). Right: *le mode Double caméra de Snapchat* (gloss *Dual Camera* once). Source titles in
   citations stay English.
5. **Output format words.** Right: *vertical / horizontal*. Wrong: *aperçu paysage*, *fichier paysage* in changelog (5);
   table row *Portrait et paysage en une seule prise* in vs/apple-dual-capture, vs/detail, vs/dualtake, vs/lookout;
   link text *toutes les apps portrait et paysage comparées* in vs/dualtake. (Quotes of rival listings like 2Cam's
   "Record in portrait or landscape mode" stay.)
6. **Timelapse.** vs/dualcam calls the feature *accéléré* (3, "pas d'accéléré", "accéléré"). blog/iphone-duo-camera writes
   *Time-lapse* (1). Right: **Timelapse** for ContentCam's and rivals' feature; *Accéléré* only for Apple's Camera mode.
7. **Teleprompter.** vs/dualcam uses *Prompteur* / *prompteur* for the feature (table row + 4 in prose).
   features/teleprompter writes *une app de prompteur séparée*. Right: **téléprompteur** in prose and tables (store copy;
   *Téléprompteur* appears on all 45 pages via the footer). *prompteur* is fine for a physical glass prompteur
   (blog/phone-teleprompter-apps-compared) and the in-app chip.
8. **Audio meter.** vs/dualcam: *indicateur de niveau audio* (2). Right: **vumètre**.
9. **appli.** vs/2cam (5, including the title and H1), vs (3, title and H1), android (1). Every other page says *app*
   (254 uses, 42 pages). Right: *app* in body; *application* in a title when it matches search (4 blog titles already do).
   Never *appli*.
10. **Gender of ContentCam.** Masculine in vs/lookout (2, "ContentCam est gratuit"), blog/record-portrait-and-landscape-video-same-time-iphone (1),
    blog/snapchat-front-and-back-camera (1), changelog (1, "ContentCam est-il toujours mis à jour ?"), and *lequel choisir* in
    vs/apple-dual-capture (4), vs/dualgram (1), vs/lookout (1). Feminine in pricing, index, android, support, vs/2cam. Right:
    feminine (*gratuite*, *est-elle*, *laquelle choisir*).
11. **sauvegarder for save.** pricing "Découpe avant sauvegarde" (2, table and feature list: store copy says *Découpe au visionnage*),
    blog/record-front-and-back-camera-iphone-15-16 "sauvegardés en deux fichiers" (2), blog/record-front-and-back-camera-samsung-galaxy
    "pour sauvegarder" (1), blog/dual-format-recording-apps-compared "sauvegardées" (1), blog/dual-camera-app-one-time-purchase
    "avant la sauvegarde" (1). Right: *enregistré(e)s*, *enregistrement*. *Sauvegarder* means back up.
12. **Manual controls name.** features/manual-controls title "Réglages manuels en vidéo" and 6 more uses on that page, plus
    blog/dual-camera-app-one-time-purchase, changelog, vs/detail, vs/dualcam, vs/dualgram (1 each). The H1 of the same page
    and 45 pages say *commandes manuelles*. Right: **Commandes manuelles** (store copy). *réglages* is fine for a generic
    setting value.
13. **Apple's Camera app name (site-wide, currency).** 23 pages, 95 uses of *l'app Appareil photo*. Correct for iOS 18 and 26,
    but Apple France renamed the app **Caméra** in iOS 27 (guide default now). Right: on first mention, *l'app Caméra (Appareil
    photo avant iOS 27)*, then *Caméra*. For settings paths give the iOS 27 path and the iOS 26 one once. Do not change Samsung's
    *Appareil photo*.
14. **Apple spec quoted in English.** blog/iphone-17-dual-capture-limitations (2) and blog/film-kid-reaction-and-what-they-see (1)
    quote "Dual Capture up to 4K Dolby Vision at 30 fps" and back-translate it. Right: quote Apple France directly:
    « Double capture (Dolby Vision jusqu'à 4K à 30 ips) ». English Apple *source titles* in citation lists can stay, but better
    to cite the French titles: « Enregistrer une vidéo avec la caméra de l'iPhone ».
15. **PiP naming.** *image dans l'image* (store copy, 110 uses, 31 pages) vs *incrustation* (53 uses, 16 pages; vs/dualgram 11,
    vs/dualcam 7, blog/iphone-duo-camera 7). Right: name ContentCam's Combiner layout **image dans l'image**. *en incrustation* is
    acceptable only to describe a rival's fixed overlay (Apple Double capture, Instagram Dual). Low severity.
16. **Lowercase "double capture" for a rival.** vs/lookout (2): "la double capture de Lookout". It reads as Apple's feature.
    Right: *l'enregistrement avant et arrière de Lookout*.
17. **Invented term on the homepage.** index: "Comment fonctionne la capture double format". It collides with *Double capture*.
    Right: *Comment fonctionne l'enregistrement en deux formats*.
18. **Plain space before `? : ;`** in visible text: 170 cases in 18 pages. Worst: vs/dualgram 38, blog/dual-format-recording-apps-compared 28,
    blog/record-front-and-back-camera-same-time-android 26, blog/dual-camera-effect 22, blog/film-reaction-video-phone 16,
    blog/doubletake-not-working-alternatives 8. Smaller: vs/2cam 6, vs/lookout 6, vs/mixcam 5,
    blog/record-front-and-back-camera-iphone-15-16 3, vs/dualcam 3, blog/film-for-tiktok-and-youtube-at-the-same-time 2,
    blog/iphone-17-dual-capture-limitations 2, blog/iphone-4k-front-and-back-camera-same-time 2, blog/best-front-and-back-dual-camera-apps 1,
    blog/dual-camera-app-one-time-purchase 1, vs/apple-dual-capture 1. Right: U+00A0. The other 27 pages are clean.
19. **Guillemets without a no-break space inside:** 86 cases in 9 pages (vs/dualgram 40, blog/dual-format-recording-apps-compared 12,
    blog/record-front-and-back-camera-same-time-android 10, vs/dualcam 8, blog/dual-camera-effect 6, blog/film-reaction-video-phone 6, vs/2cam 6,
    vs/mixcam 4, vs/lookout 2). Right: `«` + U+00A0 … U+00A0 + `»`.
20. **grand angle.** blog/film-kid-reaction-and-what-they-see (1): "La caméra selfie est grand angle". Right: *grand-angle* (59 other uses).
21. **Comparison title pattern.** *ContentCam ou X* (vs/2cam, vs/apple-dual-capture, vs/detail, vs/dualgram, vs/lookout) vs
    *ContentCam vs X* (vs/dualcam, vs/dualtake, vs/mixcam, vs index). Both are typed in France. Pick **ContentCam ou X** in
    the H1 (more natural), and keep *vs* in the URL slug only. Low severity.

Checked and consistent (no action): *caméra avant* (362 uses, never *frontale*), *Double capture* capitalisation (295, never
*Double Capture*), *filigrane*, *achat unique*, *à vie*, *ultra grand-angle*, *écran partagé* (never *scindé/divisé*), *vous*
register, no em dashes in visible text, *supporté* absent, *lentille* absent. *Paramètres* in support refers to the Android app,
which is correct. *Avant/Arrière* (slash) in changelog and how-to steps names the on-screen pill, which is correct.

---

## 7. False friends and calque traps for this subject

1. **enregistrer = save AND record.** Use *filmer* for record, *enregistrer* for save, *enregistrement* for the recording.
   In a how-to step, "Touchez Enregistrer" is ambiguous. Apple's own button is *bouton Enregistrer* (record), so when quoting
   Apple keep it, but in ContentCam's voice say *lancez l'enregistrement* or *filmez*.
2. **sauvegarder ≠ save.** It means back up (Apple: "Sauvegarder l'iPhone"). Save = *enregistrer*.
3. **paysage / portrait.** Correct for device orientation, wrong for the output. *Paysage* also means scenery, the very thing
   people film. Use *horizontal / vertical*. Apple's *Portrait* is also a photo mode (blurred background), so *mode Portrait*
   never means 9:16.
4. **appareil photo vs caméra.** Hardware on a phone = *caméra* (*caméra avant*). Apple's app = *Appareil photo* until iOS 26,
   *Caméra* from iOS 27. Samsung's app = *Appareil photo*. A standalone camera = *appareil photo*. Bare *appareil* ≠ device.
5. **lentille ≠ lens.** *objectif*.
6. **éditer ≠ edit a video.** *monter*, *montage*. *éditer* = publish.
7. **supporter ≠ support (compatibility).** *prendre en charge*, *compatible*.
8. **digital ≠ numérique.** *zoom numérique*.
9. **capture.** French *capture* alone suggests a screenshot (*capture d'écran*). Do not coin *capture double format*,
   *capture duale*. Use *Double capture* only for Apple's feature.
10. **dual.** No French adjective *dual* in this sense. *double* before the noun: *double caméra*, *double objectif*. Avoid
    *caméra duale*, *mode dual* (except Instagram's proper name *Dual*).
11. **split screen.** People type it in English, but the French UI word is *écran partagé*. *Partage d'écran* is a false lead:
    it means screen sharing (autocomplete fills it with *vidéoprojecteur*, *WhatsApp*).
12. **simultanément vs en même temps.** Both are correct. *en même temps* is what people type in queries and what the store copy
    uses. Keep *simultanément* for body variety.
13. **réaction.** *vidéo réaction* (no *de*) is the search form; *vidéo de réaction* is grammatical but less typed.
14. **selfie.** A normal French loan (*la caméra selfie*, *un selfie*). Do not translate it as *autoportrait*.
15. **take ≠ prise de vue.** *prise* is the countable recording; *prise de vue* is the act of shooting, which is how the pages use
    it now (correct in all 11 cases).
16. **timelapse ≠ ralenti.** *Ralenti* is slow motion. ContentCam's mode is *Timelapse*; Apple's is *Accéléré*.
17. **opportunité ≠ opportunity.** Use *occasion*.
18. **réaliser ≠ realise.** In French it means "to make/direct" (*réaliser une vidéo*). "I realised" = *je me suis rendu compte*.
19. **définitivement ≠ definitely.** It means permanently (*supprimé définitivement*). "Definitely" = *sans aucun doute*.
20. **éventuellement ≠ eventually.** It means possibly. "Eventually" = *finalement*.
21. **library.** Apple's Photos library = *photothèque*; ContentCam's own list = *Bibliothèque* (store copy). *Librairie* is a bookshop.
22. **feature.** *fonctionnalité* (Apple's word) or *fonction* (store copy: "les mêmes fonctions"). Never *feature* in body text.
23. **free trial / free.** *gratuit* (price) vs *libre* (open). *Essai gratuit*, never *essai libre*.
24. **app gender.** *l'app* and *l'application* are feminine, so is ContentCam. Rival names follow the same rule
    (*Dualgram est-elle…*), unless the sentence is about *le mode* or *l'outil*.
