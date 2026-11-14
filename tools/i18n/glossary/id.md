# Indonesian (`id`) terminology + style sheet for contentcam.app

Compiled 15 Nov 2026 for native reviewers and translation passes of `~/contentcam-web/id/`.
This is the sheet for the website. Where it disagrees with an older note, follow the order of authority below.

**Order of authority**
1. iOS store copy `~/contentcam/docs/store-descriptions/v2.8.2/desc/id.txt` (live, native-reviewed): ContentCam's feature and mode names, register, marketing phrasing.
2. Shipped in-app strings: iOS `~/contentcam/ContentCam/ContentCam/Resources/Localizable.xcstrings` (`id`) and Android `~/contentcam-android/app/src/main/res/values-in/`. Use these when a page tells the reader which on-screen label to tap.
3. Google Play listing `~/contentcam/docs/play-listings.json` key `id`: Android-only pages.
4. App glossary `~/contentcam/docs/localization-glossary-id.md`: tie-breaker for loanword-vs-native calls (it was written for the app UI, so the website follows the store copy wherever the two differ, e.g. `tap` in a marketing line).
5. Apple's Indonesian iPhone User Guide (support.apple.com/id-id) for Apple's own UI names; Samsung Indonesia support for Samsung's.

Confidence labels: **store** = in id.txt or the Play listing; **app** = shipped in-app string; **Apple-id** / **Samsung-id** = read on that vendor's Indonesian support page; **AC** = seen in Google autocomplete (hl=id, gl=id, 15 Nov 2026); **unverified** = nobody has confirmed it yet, so a native reviewer should check it first.

---

## 1. Register, person form, typography

### Register
- **Address the reader as `kamu`, with the enclitic `-mu` for possession.** Never `Anda`. The store copy is informal throughout ("Rekamanmu tetap di iPhone-mu", "scroll naskahmu") and so is the app. Current id pages: 0 × `Anda`, so this is already met.
- `-mu` is written solid on native words (`videomu`, `naskahmu`, `syutingmu`) and **hyphenated after a Latin-script proper noun or acronym**: `iPhone-mu`, `HP-mu`, `Galaxy-mu` (store: "iPhone-mu"; Play: "HP-mu"). Avoid `iPhone kamu` / `HP kamu`, and never write `iPhonemu`.
- **Author voice (Jimmy): `saya`.** Most pages use `saya` (133 × in 33 pages). A few use `aku` (see §6). `aku` is acceptable only inside quoted user reviews.
- Informal-standard, not Jakarta slang. Avoid `bikin`, `banget`, `nggak/gak`, `nih` in our own prose; use `membuat`, `sangat/sekali`, `tidak`. They are fine inside quoted reviews.
- No `silakan` / `mohon`; use bare imperatives (`Buka`, `Ketuk`, `Rekam`). The app glossary bans them, and the store copy never uses them.
- Code-mixing is the register: `take`, `syuting`, `konten`, `posting`, `upload`, `review`, `trim`, `crop`, `white balance`, `frame rate` stay as they are in the store copy. Do not "nativise" them (see §7).

### Punctuation and typography
- **Decimal comma, thousands point:** `0,5x`, `4,8`, `US$2,99`, `A$3.499`, `50.000+ unduhan`, `1.080`. This is the store convention ("tombol 0,5x, 1x, dan 2x"). Resolutions written as dimensions stay unseparated: `1080×1920`, `607×1080`.
- **Currency:** `US$2,99`, `A$`, `Rp` with no space after the symbol. Keep every price exactly as the English source gives it.
- **fps:** follow the store copy, **`60fps` solid** in ContentCam claims ("di 24, 25, 30, 50, atau 60fps", "50 dan 60fps"). Within a page, use one form. Quoted vendor specs can keep the vendor's spacing (Apple id writes "30 fps").
- **Dates:** `15 November 2026`, `4 Nov 2026` in tables. Day, month name, year; no leading zero; no comma. Month names: Januari, Februari, Maret, April, Mei, Juni, Juli, Agustus, September, Oktober, November, Desember.
- **Time:** 24-hour with a dot, e.g. `19.01`.
- **Quotes:** double quotes for quoted UI text and citations. Pages currently mix straight `"…"` with curly `“…”`; pick curly `“…”` for new work and keep one style per page. Single quotes are only for a quote inside a quote.
- **No em dashes** (brief rule). Use a comma, a colon or a new sentence. Current id pages: 0, so this is met.
- **Spacing:** no space before `:` `?` `!` `;` (unlike French). The `%` sign is solid: `31,6%`.
- **Prefix + foreign root takes a hyphen:** `meng-crop`, `di-trim`, `di-upscale`, `di-zoom`. A suffix on a foreign word: `Layout-nya`, `(Front/Back)-nya`.
- **`di-` passive is solid, `di` preposition is spaced:** `dihapus`, `diekspor` versus `di Gabungkan`, `di ekspor gratis` (= "on the free export"). Check each one: `di ekspor` is correct only when "ekspor" is a noun.
- **Capitalisation:** sentence case for headings and H2s (Indonesian does not use Title Case). Proper names and the locked mode names keep their capitals (`Lensa Ganda`, `Depan dan Belakang`). Function words inside a name stay lowercase (`Depan dan Belakang`, never `Depan Dan Belakang`). Exception: `<title>` and H1 on existing pages use Title Case ("Cara Merekam Video Portrait dan Landscape…"). That is established, so keep it consistent across the page set.
- **No reduplication after numerals:** `5 rekaman`, never `5 rekaman-rekaman`; `3 take`, not `3 takes`.

---

## 2. Mandated term table

| English concept | Indonesian term to use | Avoid / forbidden | Source / confidence |
|---|---|---|---|
| record front and back camera at the same time | **merekam kamera depan dan belakang bersamaan** (also `sekaligus`) | `kamera muka`, `kamera depan dan kamera belakang secara simultan`, `waktu yang sama` | store ("merekam kamera depan dan kamera belakang bersamaan"); AC ("cara merekam kamera depan dan belakang bersamaan", "…sekaligus") |
| front camera | **kamera depan**; **kamera selfie** when you mean the selfie view | `kamera muka`, `kamera depan-depan` | store, app |
| back / rear camera | **kamera belakang** | `kamera utama` (that is Apple's "Main" lens), `kamera balik` | store, app |
| at the same time | **bersamaan** (two cameras running together), **sekaligus** (two outputs from one action) | `secara serentak` (stiff), `pada waktu yang sama` | store uses both in exactly this split |
| dual camera (category, generic) | **kamera ganda**, or **dual camera** in search-led titles | `kamera dual` (Instagram-page only, see §6), `dobel kamera` | store name "ContentCam: Kamera Ganda"; AC: "aplikasi kamera ganda", "aplikasi dual kamera", "dual camera" all live |
| portrait / vertical (orientation) | **vertikal** | `potret` (that is Portrait *mode*/bokeh), `tegak` for orientation, English `portrait` in body prose | store, app ("Portrait" → "Vertikal") |
| landscape / horizontal (orientation) | **horizontal** | `lanskap` (scenery), `mendatar`, English `landscape` in body prose | store, app |
| portrait + landscape at once | **video vertikal dan horizontal sekaligus** | `potret dan lanskap` | store first line. English `portrait dan landscape` is allowed only in title/H1/meta as a search phrase (AC: "video portrait dan landscape") |
| 9:16 / 16:9 | `9:16`, `16:9` (with "vertikal/horizontal" nearby) | `9x16` | store |
| two separate files | **dua file terpisah** | `dua berkas` (formal Windows-speak) | store |
| picture-in-picture | **gambar dalam gambar** | `picture-in-picture` / `PiP` in our prose (OK when quoting a rival's English UI) | store, app (iOS + Android "Gambar dalam gambar") |
| split screen | **layar terbagi** | `layar terpisah`, `layar belah`, English `split screen` in body (OK in a title as search phrase: AC "video split screen" is live, "cara membuat video layar terbagi" is not) | store, app ("Split" → "Layar terbagi") |
| side by side | **berdampingan** | `bersebelahan` (OK but not ours) | store ("putar kedua klip berdampingan"); AC "cara membuat video berdampingan" |
| layout (PiP vs split) | **tata letak** | `layout` (7 pages, see §6) | app ("Layout" → "Tata letak") |
| take (the recording unit) | **take** (no plural form) | `pengambilan`, `pengambilan gambar` | store ("dalam satu take") |
| recording (the file) | **rekaman** | `perekaman` for the file | store |
| recording (activity, mode family) | **perekaman** | | store, Play ("MODE PEREKAMAN") |
| shoot / filming session | **syuting** | `pengambilan gambar` | store |
| scene (thing in front of the lens) | **adegan**; `pemandangan` for scenery | `scene` (reserved for the app's Scene entity) | store ("Reaksi kamu dan adegannya") |
| frame (of video) / framing | **frame**; verb `membingkai` is OK for "to frame a shot" | `bingkai` as a noun for the video frame | store ("trim sampai frame yang pas"); app glossary |
| frame rate | **frame rate** | `laju bingkai` (Apple's own id term, but not ours), `kecepatan bingkai` | store. Note that Apple-id says "laju bingkai"; keep it only when quoting Apple |
| exposure | **eksposur** | English `exposure` (5 vs pages), `pencahayaan` (= lighting; that is Apple-id's term for exposure, but not ours) | store ("eksposur, white balance, ISO, shutter") |
| white balance | **white balance** | `keseimbangan putih`; `imbang putih` (Apple-id only) | store |
| manual controls | **kontrol manual** | `pengendalian manual` | store |
| shutter (manual control) / shutter button | **shutter** / **tombol rana** | `obor`-style dictionary picks | store |
| tap (UI step) | **ketuk** in step-by-step instructions; `tap` is OK as a noun in set phrases (`sekali tap`, `satu tap`) | `tap` as the verb in steps, `sentuh` for tap | app ("Ketuk…"), Apple-id ("Ketuk Video…"); store uses "satu tap" |
| press and hold | **sentuh dan tahan** (store v2.8.2) / **tekan dan tahan** (v2.5) | | store; Apple-id "sentuh dan tahan" |
| pinch | **cubit** | `jepit` (Apple-id's word, use only when quoting Apple) | store ("cubit layar") |
| preview (live tile) | **pratinjau** | `preview` (OK only inside a vendor's English feature name: "Dual screen preview", "Duo Preview") | store, app |
| review (side-by-side screen) | **review** | `pratinjau` | store |
| trim | **trim** | `potong`, `pangkas` for the Trim feature (`memotong antar-sudut` = cutting between angles is fine) | store |
| combine (the editor) | **Gabungkan** (first mention may gloss `(Combine)`) | `Gabung`, `Merge` | app (iOS/Android "Gabungkan"); store "Gabungkan kedua file…" |
| export / share | **ekspor** / **bagikan** | `bagi` | store |
| phone (generic) | **HP** in Android/generic prose; **iPhone** for Apple | `ponsel` (only in a quoted source), `handphone`, `smartphone` | Play notes ("HP… what Indonesians call a phone"); 40 pages already use HP |
| device (capability prose) | **perangkat** | | store, app glossary |
| app | **aplikasi** | `app` (Apple-id says "app Pengaturan"; quote only) | store |
| creator | **kreator** | `creator` in our prose (OK inside product names like "Creator Suite") | 45 pages use kreator |
| reaction video | **video reaksi** | `reaction video` | pages (15×). AC for "video reaksi" is polluted by chemistry results; prefer "cara membuat video reaksi" (AC live) |
| free / free to try | **gratis**; CTA `Coba gratis` | `bebas` for no-cost | store |
| unlimited | **tanpa batas** (postposed: `take tanpa batas`) | `tak terbatas` before the noun | store |
| free trial | **uji coba gratis** | `trial gratis`, `free trial` | app ("Uji coba gratis 7 hari") |
| subscription / annual / monthly | **langganan** / **tahunan** / **bulanan** | | app |
| lifetime / one-time purchase | **seumur hidup** / **sekali bayar** (app also: `beli sekali`) | `lifetime`, `selamanya` as the plan name | store ("sekali bayar untuk akses seumur hidup"), app ("Seumur hidup") |
| watermark | **watermark** | `tanda air` | store |
| no ads | **tanpa iklan** | | store |
| downloads (count) | **unduhan** (`50.000+ unduhan`) | `download` as a count noun in prose (the Apple badge keeps its own text) | pages (home, features) |
| upload / post | **upload**, **posting**; TikTok's button is **Unggah** | `mempublikasikan`, `mengunggah` in formal prose (allowed, but stiff) | store ("siap diposting"), app glossary |
| gallery (Android) / Photos (iOS) | **Galeri** / aplikasi **Foto** | `Rol Kamera`, `Photos` | Android app "Simpan ke Galeri"; iOS app "Simpan ke Foto" |
| Settings | **Pengaturan** | `Setelan`, `Settings` | app; Apple-id "Pengaturan > Kamera" |
| storage | **penyimpanan** | | store |
| crash protection / temperature monitor | **perlindungan crash** / **pemantauan suhu** | | store |
| version number of our app | **ContentCam 2.9 di iOS** / **versi iOS 2.9** | bare `iOS 2.9` (reads as Apple's iOS version) | reviewer call, see §6 #10 |

---

## 3. ContentCam mode and feature names (exactly as the store copy writes them)

**Marketing and prose name** (store id.txt and Play) and **on-screen label** (shipped app, iOS and Android identical):

| English | Website prose name (store) | On-screen label (app) | Notes |
|---|---|---|---|
| Single Lens | **Lensa Tunggal** (first mention: `Lensa Tunggal (Single Lens)`) | **1 Lensa** | mode switcher |
| Dual Lens | **Lensa Ganda** (`Lensa Ganda (Dual Lens)`) | **2 Lensa** (chip/headers: `LENSA GANDA`) | iPhone only; needs an ultra-wide |
| Front & Back / Front/Back | **Depan dan Belakang**. Gloss `(Front/Back)` on iOS or cross-platform pages (id.txt). Android-only pages may gloss `(Front & Back)` (Play listing) | **Depan/Belakang** | `mode` stays lowercase mid-sentence: `mode Depan dan Belakang` |
| Front Cam | **Kamera Depan** | | store |
| Stock Cam | **Kamera Biasa** | (app: "Mode vertikal saja") | store |
| Photo mode | **Mode Foto** | Mode Foto | store, app |
| Combine | **Gabungkan** (`editor Gabungkan`) | Gabungkan | layouts: `Gambar dalam gambar`, `Layar terbagi` |
| Teleprompter / script | **Teleprompter** / **naskah** | Teleprompter, Naskah Teleprompter | store |
| Timelapse | **Timelapse** | Timelapse | store (the Android changelog's "time-lapse" is a variant; prefer Timelapse) |
| manual controls | **Kontrol manual: eksposur, white balance, ISO, shutter** | tabs EV/Temp/Tint/ISO/Shutter stay English | store |
| AE/AF lock | **Kunci AE/AF** | Kunci AE/AF | store, app; Apple-id also "Kunci AE/AF" |
| Guides | **Panduan: indikator level, crosshair tengah, meter audio** | | store |
| Projects, scenes, takes | **Proyek, scene, dan take** | | store |
| Recording folder | **Folder rekaman** | | store |
| Storage estimate | **Estimasi penyimpanan** | | store |
| Premium unlocks | **PREMIUM MEMBUKA** | | store |
| Background blur (Android, Beta) | **Blur latar belakang (Beta)** | | Play |
| back-camera orientation row | — | **BELAKANG** (`Vertikal` / `Horizontal`) | app (`BACK CAMERA` → `BELAKANG`) |

**Rule:** prose uses the store name. Any sentence that tells the reader *what to tap* in ContentCam ("pilih … di bagian bawah layar", "ketuk … di pemilih mode") must quote the on-screen label: `1 Lensa`, `2 Lensa`, `Depan/Belakang`. Example: "Buka ContentCam, ketuk **Depan/Belakang** di pemilih mode, lalu rekam."

Store-copy phrases worth reusing verbatim:
- "Rekam video vertikal dan horizontal sekaligus, dalam satu take. Dua file terpisah, siap untuk TikTok, Reels, dan YouTube."
- "…lalu menggabungkannya jadi gambar dalam gambar atau layar terbagi kapan pun kamu mau."
- "Tanpa iklan dan watermark, baik gratis maupun Premium."
- "Bisa dipakai di semua iPhone dengan iOS 18 atau lebih baru, termasuk iPhone 16 dan 15."
- "Perlu iOS 18 atau lebih baru (iPhone XS dan XR ke atas)."

---

## 4. Platform names in Indonesian

| Platform term | Indonesian on the device | Source / confidence |
|---|---|---|
| Apple **Dual Capture** (feature name) | Apple's id **spec pages keep "Dual Capture"** ("Dual Capture hingga Dolby Vision 4K pada kecepatan 30 fps"), but the **Camera-app label and the iPhone User Guide say "Kamera Ganda"** ("Merekam video Kamera Ganda… Ketuk [ikon], lalu ketuk Kamera Ganda.") | Apple-id: support.apple.com/id-id/guide/iphone/iph61f49e4bb/ios ; support.apple.com/id-id/125091 and /125090 (tech specs). Verified 15 Nov 2026 |
| → how to write it | Name the feature **Dual Capture** (that is what people search: AC "dual capture iphone 17", "cara dual capture iphone"). In step instructions, give the on-screen label: "ketuk **Kamera Ganda**". First mention on Apple pages: `Dual Capture (di aplikasi Kamera berlabel Kamera Ganda)`. AC also shows "kamera ganda iphone 17". | |
| ⚠ collision | **Our own** store name ("ContentCam: Kamera Ganda") and nav item ("Kamera Ganda" → /id/features/dual-camera/) use the same words as Apple's label. Never write "Kamera Ganda" alone where it could mean Apple's mode; say "Kamera Ganda di aplikasi Kamera iPhone" or "Dual Capture". | |
| Apple Camera Control (the hardware button, iPhone 16+) | **Kontrol Kamera** | Apple-id ("klik Kontrol Kamera"). So "tombol kontrol kamera" in a Dual Capture step reads as the hardware button (see §6 #2, §7) |
| Apple: Camera / Photos / Settings apps | **Kamera**, **Foto**, **Pengaturan** | Apple-id ("Buka Kamera", "Buka app Pengaturan") |
| iOS Settings > Camera > Record Video | **Pengaturan > Kamera > Rekam Video** | Apple-id (iphc1827d32f) |
| Record Stereo Audio / Record Sound | **Rekam Bunyi Stereo** / **Rekam Bunyi** | Apple-id |
| Enhanced Stabilisation / Lock Camera / Lock White Balance | **Stabilisasi yang Ditingkatkan** / **Kunci Kamera** / **Kunci Imbang Putih** | Apple-id |
| Auto FPS / HDR Video | **FPS Otomatis** / **Video HDR** | Apple-id |
| Video / Cinematic / Slo-mo / Time-lapse modes | **Video**, **Sinematik**, **Slo-mo** (iOS label), **Selang Waktu** | Apple-id ("video Sinematik, gerakan lambat, dan selang waktu"; "Rekam Slo-mo") |
| Apple lens names | **Ultra Lebar**, **Utama**, **Telefoto** | Apple-id (iph3dc593597). Our own copy keeps `wide` / `ultra-wide` (store) |
| Shutter / Record button | **tombol Rana** / **tombol Rekam** | Apple-id |
| Samsung **Director's View** | **Director's View** (English kept on Samsung Indonesia's page; mode list path "LAINNYA > DIRECTOR'S VIEW") | Samsung-id: samsung.com/id/support/mobile-devices/meet-the-next-level-of-lifetime-story-maker-in-camera-of-galaxy-s21-series/ |
| Samsung **Dual recording / Dual rec** | Likely **Rekam ganda** in Indonesian One UI. AC shows "rekam ganda samsung", "cara rekam ganda samsung a55" next to "dual recording samsung a56". **Samsung-id page not found → unverified.** Write `Dual recording (Rekam ganda)` until confirmed. Not "Rekaman ganda". | AC; unverified |
| Samsung "More" | **LAINNYA** (older One UI mode list) | Samsung-id (S21 page) |
| Google Pixel **Dual screen preview** (Fold) | keep English; Indonesian label **unverified** | — |
| TikTok upload flow | **Unggah**; pages use "Tambah postingan +" for the + button | unverified (no TikTok id help page read) |
| Instagram **Dual** camera | Instagram shows **Dual**; prose "kamera Dual Instagram" or "fitur Dual". AC: "dual kamera instagram", "fitur dual kamera instagram" | label unverified; AC for phrasing |
| Snapchat **Dual Camera** | **Dual Camera** (English) | AC "dual camera snapchat" |
| App Store / Google Play badges | "Download di App Store" (current pages; Apple's official id badge text **unverified**, it may read "Unduh di App Store"), "Temukan di Google Play" | pages; unverified |
| Reels / Shorts / Stories | **Reels**, **Shorts**, **Story/Stories** (English) | store ("Reels") |

---

## 5. Native search phrasing (Google autocomplete, hl=id gl=id, 15 Nov 2026)

Use these word orders for titles, H1s, H2s and FAQ questions. All the phrases below were returned by autocomplete:

**Front + back camera**
- `cara merekam kamera depan dan belakang` (+ `iphone`, `bersamaan`, `bersamaan samsung`, `bersamaan iphone 13`)
- `cara merekam video kamera depan dan belakang`
- `rekam kamera depan belakang` (+ `samsung`, `iphone`); `aplikasi rekam kamera depan belakang`; `fitur rekam kamera depan belakang`
- `kamera depan belakang bersamaan` (+ `iphone`, `samsung`, `xiaomi`, `vivo`, `oppo`, `iphone berapa`)
- `video depan belakang` (+ `samsung`, `iphone`, model names)
- `cara merekam kamera depan dan belakang sekaligus`, `cara menggunakan kamera depan dan belakang sekaligus`
- `aplikasi kamera depan belakang` (+ `bersamaan`, `bersamaan iphone`, `bersamaan android`)
- `cara foto depan belakang iphone`, `cara foto dual kamera depan belakang iphone`
- Note: people drop `dan` in short queries (`kamera depan belakang`). Titles may do the same ("Aplikasi Kamera Depan Belakang…"), but body prose keeps `kamera depan dan belakang`.

**Dual camera**
- `aplikasi dual kamera` (+ `iphone`, `android`, `gratis`, `terbaik`, `depan belakang`), word order `dual kamera` is the typed form
- `aplikasi kamera ganda` (+ `iphone`, `samsung`), `kamera ganda iphone` (+ `17`, `16`, `15`, `berapa`)
- `dual camera` (+ `samsung`, `iphone`, `snapchat`, `artinya`, `apk`), `dual kamera iphone` (+ model)
- `dual capture iphone` (+ `15`, `17`, `air`, `18 pro`), `cara dual capture iphone`, `cara aktifkan dual capture`, `cara kamera ganda iphone 17`
- `dual kamera instagram` (+ `story`, `iphone`), `cara dual kamera instagram`, `fitur dual kamera instagram`
- `dual camera tiktok` (mostly about TikTok **LIVE**), `dual camera snapchat`, `dual camera pixel`

**Samsung**
- `dual recording samsung` (+ `a56`, `a55`, `s25 ultra`, `hilang`), `rekam ganda samsung` (+ `a56`, `a55`), `cara rekam ganda samsung`
- `director's view samsung` (+ model), `kamera ganda samsung` (+ `a56 hilang`)
- `cara merekam kamera depan dan belakang samsung`

**Vertical + horizontal**
- `video vertikal dan horizontal` (+ `perbedaan`, `contoh`, `apa itu`)
- `video portrait dan landscape` (+ `perbedaan`, `cara menggabungkan`)
- No suggestions came back for `cara merekam video vertikal dan horizontal`, `rekam video portrait dan landscape` or `…sekaligus`. Demand is low, so lead with the concept nouns ("video vertikal dan horizontal", "portrait dan landscape") rather than a long "cara rekam … sekaligus" string.

**Split screen / PiP**
- `video split screen` (+ `app`, `editor`, `template`), `cara membuat video split screen di android`, `video split screen iphone`
- `layar terbagi` returns *phone multitasking* results (vivo/samsung/infinix split-screen apps), not video. For video-editing titles, `split screen` beats `layar terbagi`; keep `layar terbagi` in body prose (store and app term)
- `cara membuat video berdampingan` (+ `di capcut`)
- `video picture in picture` (English; mostly browser PiP). `video gambar dalam gambar`: no suggestions

**Other**
- `aplikasi teleprompter` (+ `gratis`, `android`, `iphone`), `teleprompter iphone`
- `cara membuat video reaksi` (+ `di capcut`, `di youtube`)
- `cara ganti kamera saat merekam video di iphone`
- `aplikasi kamera tanpa watermark`
- `iphone duo` (+ `harga`, `harga indonesia`, `rilis kapan`)

---

## 6. Inconsistencies found across existing `/id/` pages (45 pages scanned, 18 issues)

1. **Gloss for Depan dan Belakang: `(Front/Back)` × 86 in 22 pages vs `(Front & Back)` in 6 pages.** Correct: `(Front/Back)` on iOS or cross-platform pages (id.txt); `(Front & Back)` is acceptable on Android-only pages (Play). Wrong: `blog/best-front-and-back-dual-camera-apps`, `blog/iphone-4k-front-and-back-camera-same-time`, `vs/dualtake`. Acceptable: `blog/record-front-and-back-camera-same-time-android`, `blog/record-front-and-back-camera-samsung-galaxy`. Rival app names containing "Front & Back" are untouched.
2. **Apple Dual Capture steps name the wrong UI.** Pages say "ketuk tombol kontrol kamera, lalu ketuk Dual Capture". Apple's Indonesian guide says "Pilih mode Video. Ketuk [ikon], lalu ketuk **Kamera Ganda**", and "**Kontrol Kamera**" is Apple-id's name for the hardware Camera Control button. Fix: "pilih Video, ketuk ikon kontrol di layar, lalu ketuk Kamera Ganda (Dual Capture)". Pages: `blog/bereal-style-photo-without-bereal`, `blog/dual-camera-effect` (capitalised "tombol Kontrol Kamera", the worst case), `blog/record-front-and-back-camera-same-time-iphone`, `blog/switch-camera-while-recording-iphone`.
3. **Mode-switcher instructions use prose names, not on-screen labels.** The app shows `1 Lensa / 2 Lensa / Depan/Belakang`. `blog/record-portrait-and-landscape-video-same-time-iphone` ("pilih Lensa Tunggal, Lensa Ganda, atau Depan dan Belakang di bagian bawah layar") and the `features` alt text ("pilihan Lensa Ganda dan Lensa Tunggal di bagian bawah") should name the labels. "Ganti mode ke Depan dan Belakang" steps (`record-front-and-back-camera-iphone-15-16`, `…-same-time-android`, `…-samsung-galaxy`, `take-photo-front-and-back-camera-same-time`, `dual-camera-effect`, `how-to-do-dual-camera-on-tiktok`, `bereal-style-photo-without-bereal`, `record-front-and-back-camera-same-time-iphone`) are acceptable, but are better as "ketuk Depan/Belakang".
4. **`tap` vs `ketuk` as the step verb (ketuk × 51 in 9 pages, tap × 28 in 9 pages).** Correct: `ketuk` in steps (app and Apple-id); `sekali tap` / `satu tap` as a noun idiom is fine (store). Wrong: `blog/split-screen-video-iphone` (8 × "tap" in iMovie steps), `blog/bereal-style-photo-without-bereal` (4), `blog/how-to-do-dual-camera-on-tiktok` (mixes both), `pricing` ("tap Pulihkan pembelian"), `changelog` ("tap kotak scene").
5. **English `exposure` instead of `eksposur`**: `vs/apple-dual-capture`, `vs/detail`, `vs/dualgram`, `vs/lookout`, `vs/mixcam` (shared template line "exposure, white balance, ISO, dan shutter manual"). The store says "eksposur, white balance, ISO, shutter". 17 other pages already use eksposur.
6. **`Potret dan lanskap` table row instead of `Vertikal dan horizontal`**: `vs/2cam`, `vs/apple-dual-capture`, `vs/detail`, `vs/lookout`, `vs/mixcam`. `potret` collides with Portrait (bokeh) mode, and `lanskap` means scenery. Keep the quotation of 2Cam's own wording ("Rekam dalam mode potret atau lanskap") on `vs/2cam`, since that is a quote.
7. **English `portrait`/`landscape` in body prose** (fine in title/H1/meta as a search phrase, or as a gloss after vertikal/horizontal): `blog/film-for-tiktok-and-youtube-at-the-same-time` ("versi portrait", "tile landscape"), `changelog` ("Rekam portrait saja", "Mode portrait saja"; the app says "Mode vertikal saja"), `blog/best-front-and-back-dual-camera-apps` (alt text "framing portrait dan landscape"), `blog/dual-format-recording-apps-compared` (body).
8. **Samsung Dual recording naming.** `blog/snapchat-front-and-back-camera` calls it "Rekaman ganda" (3×), while `…-samsung-galaxy`, `…-same-time-android` and `switch-camera-while-recording-iphone` say "Dual recording". Use `Dual recording (Rekam ganda)` (AC-attested, unverified), never "Rekaman ganda". `vs/lookout` "perekaman ganda" describes Lookout generically, which is fine.
9. **fps spacing mixed within a page** (`60fps` and `60 fps` on the same page): `blog/record-front-and-back-camera-same-time-iphone`, `changelog`, `support`, `vs/2cam`, `vs/apple-dual-capture`, `vs/dualcam` (74 spaced vs 3 solid), `vs/dualgram`, `vs/dualtake`, `vs/lookout`, `vs/mixcam`. Use `60fps` (store) for ContentCam claims; quoted vendor specs can keep their own spacing.
10. **"Sejak iOS 2.9" reads as Apple's iOS version** (the English source has the same ambiguity, but Indonesian readers are just as likely to misread it): `blog/doubletake-not-working-alternatives`, `blog/dual-camera-effect`, `blog/how-to-do-dual-camera-on-tiktok`, `blog/iphone-17-dual-capture-limitations`, `blog/iphone-4k-front-and-back-camera-same-time`, `blog/switch-camera-while-recording-iphone`, `blog/best-front-and-back-dual-camera-apps`, `vs/dualtake`, `blog/dual-camera-app-one-time-purchase` ("iOS 2.8.1"). Prefer "sejak ContentCam 2.9 untuk iOS". Reviewer call, since it adds words.
11. **`layout` vs `tata letak`** (app: "Tata letak"; 19 pages use tata letak): `layout` appears in `blog/dual-camera-app-one-time-purchase`, `blog/instagram-dual-camera-missing`, `blog/iphone-4k-front-and-back-camera-same-time`, `blog/split-screen-video-iphone` (7), `vs/2cam`, `vs/dualgram` (12), `vs/dualtake`. Quoted rival text ("layout tambahan" quoting Dualgram) can stay.
12. **`bingkai` for the video frame**: `features/dual-camera` mixes "frame vertikal" and "bingkai vertikal" in consecutive sentences, so use `frame`. "dalam satu bingkai" (`blog/snapchat-front-and-back-camera`, `vs/apple-dual-capture`) should read "dalam satu frame" (or "satu video"). `membingkai` (to frame a shot) elsewhere is fine.
13. **`iPhone kamu` / `HP kamu` instead of `iPhone-mu` / `HP-mu`**: `blog/switch-camera-while-recording-iphone` (2), `blog/snapchat-front-and-back-camera`, `changelog`.
14. **Decimal point**: `changelog` "ultra-wide 0.5x" (2×) should be `0,5x` (store).
15. **`ponsel` vs `HP`**: `android` uses ponsel 5× and HP 1×; the vs template pages (`vs/2cam`, `vs/apple-dual-capture`, `vs/lookout`, `vs/mixcam`, `vs/dualcam`) say "ponsel Android". The site standard is `HP` (40 pages; Play notes). `blog/dual-camera-effect`'s "ponsel" sits inside a quote from Instagram, so it stays.
16. **`creator` vs `kreator`**: `blog/dual-format-recording-apps-compared` ("bagi kebanyakan creator") should be `kreator`. "Creator Suite" (Pixel product) and "content creator" in a quoted review stay.
17. **Author pronoun `aku` vs `saya`** (saya in 33 pages): `aku` in `blog/best-front-and-back-dual-camera-apps` ("Aku yang membuat ContentCam"), `blog/dual-camera-app-without-ads`, `blog/how-to-do-dual-camera-on-tiktok` ("aplikasi yang aku buat… pilihanku"), and `home` (founder story, 6×). Standardise on `saya` / `-ku` → `saya`. If the founder story on `home` is deliberately intimate, the reviewer may keep it, but then it should be the only exception.
18. **Slang `bikin` in our own prose** (17× in 10 pages, e.g. `blog/dual-camera-app-without-ads`, `blog/dual-camera-effect`, `blog/film-for-tiktok-and-youtube-at-the-same-time`, `blog/record-front-and-back-camera-same-time-iphone`, `blog/snapchat-front-and-back-camera`, `blog/take-photo-front-and-back-camera-same-time`) is below the store's informal-standard register. Use `membuat` / `bikin` → `membuat`. (`banget`/`gak` on `home`/`features`/`vs/2cam` were checked; most are inside quoted reviews, so leave those.)

Checked and consistent (no action): `kamu` register (0 × Anda), `gambar dalam gambar` (125×) and `layar terbagi` (91×) for our features, `Lensa Ganda`/`Lensa Tunggal` always glossed correctly, `white balance` (never keseimbangan putih), `watermark`, `seumur hidup`/`sekali bayar`, `uji coba gratis`, `Pengaturan` (0 × Setelan), `Gabungkan (Combine)`, `kreator`, prices in `US$1.999` style, no em dashes, dates in `27 September 2026` format. Also fine: `tegak` on `android` and `changelog`, which means "upright" (correct use, not portrait).

---

## 7. False friends and calque traps for this subject

| Trap | Why it is wrong | Use |
|---|---|---|
| `potret` for portrait orientation | `Potret` is the bokeh **Portrait mode** (the Play listing itself says "mirip mode Potret" for background blur) | `vertikal` |
| `lanskap` for landscape orientation | means scenery or landscape painting | `horizontal` |
| `Kontrol Kamera` / "tombol kontrol kamera" | on iPhone 16+ it is Apple-id's name for the **hardware** Camera Control button | "ikon kontrol di layar" |
| `Kamera Ganda` | Apple's id label for Dual Capture **and** ContentCam's own store name and nav label | qualify it every time (§4) |
| `bingkai` for video frame | picture or photo frame | `frame` |
| `laju bingkai`, `pencahayaan`, `imbang putih`, `jepit` | Apple-id's own vocabulary. Correct on Apple's pages, but they clash with our store copy | `frame rate`, `eksposur`, `white balance`, `cubit` (quote Apple's words only inside Apple citations) |
| `keseimbangan putih` | dictionary calque nobody who shoots says | `white balance` |
| `pengambilan` / `pengambilan gambar` for take or capture | textbook or documentary register | `take`, `saat merekam`, `syuting` |
| `layar terpisah` | sounds like "separate screens" (two displays) | `layar terbagi` |
| `layar terbagi` in a title | autocomplete maps it to phone **multitasking** split-screen | title: `split screen`; body: `layar terbagi` |
| `bagi` for share | means divide | `bagikan` |
| `potong` for the Trim feature | reads as "cut out" | `trim` (`memotong antar-sudut` = cutting between angles is fine) |
| `Rekaman ganda` for Samsung's mode | not Samsung's label; AC shows `rekam ganda` | `Dual recording (Rekam ganda)` |
| `kamera muka` | archaic or odd | `kamera depan` |
| `kamera utama` for "back camera" | Apple-id `Utama` = the Main (1x) lens | `kamera belakang` |
| `dual camera` meaning "two rear lenses" | in Indonesian searches `dual kamera` also means a phone with two rear lenses (AC "kamera dual lens", "dual camera artinya") | say `kamera depan dan belakang` when that is what you mean |
| `dual camera tiktok` | autocomplete is about TikTok **LIVE** dual camera, not posting a recording | address LIVE explicitly or target "cara dual kamera di TikTok" with a post-upload angle |
| `iOS 2.9` | reads as Apple's OS version | "ContentCam 2.9 untuk iOS" |
| `scene` in prose | reserved for the app's Scene entity (project → scene → take) | `adegan` / `pemandangan` for what is filmed |
| `selfie depan` | measured as 0 search volume (store-metadata-expansion.md §selfie) | `kamera depan` / `kamera selfie` |
| `obor` (torch), `tanda air` (watermark), `bebas` (free) | dictionary-correct, contextually wrong | `lampu kilat`/`senter` (context), `watermark`, `gratis` |
| `Anda`, `silakan`, `mohon` | bank or government register; breaks parity with the store and the app | `kamu`, bare imperative |

### Sources
- Apple id: https://support.apple.com/id-id/guide/iphone/iph61f49e4bb/ios (Merekam video Kamera Ganda); https://support.apple.com/id-id/guide/iphone/iphc1827d32f/ios (Pengaturan > Kamera > Rekam Video); https://support.apple.com/id-id/guide/iphone/iph3dc593597/ios (Kunci AE/AF, Ultra Lebar/Utama/Telefoto); https://support.apple.com/id-id/125091 and https://support.apple.com/id-id/125090 (specs: "Dual Capture").
- Samsung id: https://www.samsung.com/id/support/mobile-devices/meet-the-next-level-of-lifetime-story-maker-in-camera-of-galaxy-s21-series/ (Director's View, LAINNYA). The Samsung id Dual recording page was not found (404s on the /id/ versions of the ae pages).
- Google autocomplete: `suggestqueries.google.com/complete/search?client=firefox&hl=id&gl=id`, about 60 queries on 15 Nov 2026.
