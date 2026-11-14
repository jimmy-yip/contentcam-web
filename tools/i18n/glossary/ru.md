# Russian (`ru`) terminology and style sheet: contentcam.app

Built 15 Nov 2026 from:

- `tools/i18n/TRANSLATE-BRIEF.md` (ru row: "вы form unless store copy uses ты")
- Store copy `~/contentcam/docs/store-descriptions/v2.8.2/desc/ru.txt` (**terminology authority** for ContentCam's own names)
- App glossary `~/contentcam/docs/localization-glossary-ru.md` (locked app UI terms; built on v2.8.3 desc + What's New files)
- `~/contentcam/docs/store-metadata-expansion.md` (ru title `ContentCam: Двойная камера`, subtitle `Одна съемка, два формата видео`, keyword field; NFD warning; glossing rule)
- `~/contentcam/docs/store-metadata-localized.md`, `localization-review.md`: no Russian-specific content
- A scan of all **21** pages under `ru/` (visible text + JSON-LD; counts below are hits on 15 Nov 2026)
- Apple Russian support pages and Samsung Russian support pages fetched 15 Nov 2026 (sources in §4)
- Google autocomplete (`hl=ru&gl=ru`) run 15 Nov 2026 (§5)

Precedence: store copy wins on ContentCam feature names; this sheet wins over any older page; Apple/Samsung official Russian pages win on their own feature names. If the store copy and this sheet ever disagree, tell Jimmy.

---

## 1. Register, person, punctuation, typography

**Register: formal «вы», lowercase.** The store copy uses the plural imperative throughout (*«Снимайте вертикальное и горизонтальное видео»*, *«Ваши записи остаются на телефоне»*), and so does every ru page today (0 «ты»-form hits in prose). Imperatives: *снимайте, откройте, выберите, нажмите, скачайте, попробуйте*.

- **Lowercase «вы/ваш» mid-sentence.** Apple's Russian manuals capitalise «Вы» (*«то, что происходит перед Вами»*); do NOT copy that. Web/marketing copy and our store copy use lowercase; the site has 0 capitalised mid-sentence «Вы» today. Keep it.
- Tap verb: **нажмите** (site standard). Apple's manuals say *«коснитесь»*; only use that when quoting Apple step by step.

**Letter ё: do not use it. Write е everywhere** (*съемка, еще, разделенный, телесуфлер, сохраненный, ее, все*).
Reason: the v2.8.2 store description (the copy a visitor lands from) writes *съемка, еще, разделенный экран, Телесуфлер*; Apple's Russian support pages also write *«Двойная съемка»* without ё; 18 of 21 ru pages already have zero ё. Google treats е/ё as equivalent, so there is no search cost. (The in-app UI glossary does use ё; the website follows the store listing instead, as the brief requires.) Only exception: if a sentence is genuinely ambiguous (*все* vs *всё*), rephrase rather than add a single ё.

**Quotes:** «ёлочки» for app names in prose when they are UI names, mode names, menu items, button labels and quoted strings: *режим «Передняя и задняя»*, *приложение «Камера»*, *«Настройки»*, *функция «Двойная съемка»*. Nested quotes: „лапки“ (*«Модели с поддержкой функции „Двойная съемка“»*). Never straight `"…"` in visible text (current pages: 0, keep it). Brand/app product names (ContentCam, Snapchat, DualCam, Instagram) take no quotes.

**Dashes:** no em dashes (brief rule). Russian grammar wants a тире in *«X — это Y»* and *«зум — кнопка»*; rephrase instead: *«X это Y»* is acceptable in modern web prose, or use a colon (*«зум: кнопка 1x / 0,5x»*), or *«представляет собой»*. Ranges: *от 0,5 до 30 с*, *24–60 fps* only if the source has a range; an en dash in a numeric range is fine.

**Numbers**
- Decimal separator: **comma**. `4,8`, `0,5x`, `29,99 fps`, `0,5 с`, `1,78 раза`, `31,6 %`. (Store copy: *«0,5x, 1x и 2x»*, *«от 0,5 до 30 с»*.)
- Version numbers keep the dot: `iOS 18`, `iOS 26.1`, `One UI 8.5`, `ContentCam 2.9`, `версия 1.48`.
- Thousands: thin/non-breaking space: `15 000`, `1 000`; four-digit numbers may be written without a space (`1000`). Never `15,000` or `15.000`.
- Resolution: `1920 x 1080` (spaces around), `1080p`, `4K`, `HD`.
- Frame rate: **`60 fps`, with a space, lowercase**, as in the store copy (*«24, 25, 30, 50 или 60 fps»*). Do not use `60fps`, `FPS`, or `кадра/с` in our own prose. Exception: when quoting a UI string verbatim (Apple's settings show *«кадр/с»*; a rival's app shows `FPS`), copy it exactly inside «».
- Zoom/speed: `0,5x`, `1x`, `2x`, `от 10x до 900x` (Latin x, no space; store copy).
- Percent: `31,6 %` (with a non-breaking space; Russian norm).
- Aspect ratios: `9:16`, `16:9`, `4:3`.

**Money**
- Write `5,99 $` (comma decimal, sign after the number, non-breaking space), or in prose *«5,99 доллара США»*. Always say which store: *«в App Store США»*. Never `$5.99` (dot decimal reads as English) and never a converted rouble price.
- Plan names as in the store copy / glossary: *на год, на месяц, навсегда, разовая покупка*; *подписка на год*.

**Dates**
- Prose and "verified" notes: **`6 ноября 2026 года`** (months lowercase, genitive). Use this form also in parentheses (*«проверено 6 ноября 2026 года»*). It is the majority form on the site (84 hits).
- Byline/date line may use the bare form `15 ноября 2026`.
- Do not mix in `2026 г.` (currently on 3 pages, see §6). Never `ноябрь 15` or `15.11.2026` in visible text (ISO dates in JSON-LD `datePublished` stay ISO).

**Capitalisation:** sentence case in titles and headings (*«Как снимать на две камеры одновременно на iPhone»*), never Title Case. Mode names inside quotes keep their initial capital (*режим «Два объектива»*).

**Brand names in Latin:** iPhone, Samsung Galaxy, Android, Google Play, App Store, TikTok, YouTube, Instagram, Reels, Shorts. Russians type *айфон*, *самсунг*, *андроид* in search (§5), but on the page keep the Latin brand (brief rule). Do not write Cyrillic brand transliterations in visible text.

---

## 2. Mandated term table

| English concept | Use (ru) | Avoid | Source / confidence |
|---|---|---|---|
| take | **дубль** / дубля / дублей (m.) | тейк, клип (for ContentCam's unit), запись (as a countable unit) | Store: *«одним дублем»*, *«дубли без ограничений»*. Verified |
| recording (act/file) | **запись** (f.) | | Store *«Ваши записи остаются на телефоне»* |
| clip (generic / rival output) | **клип**, **ролик** | | Store uses *клипы* for clips in the takes list; fine for generic footage |
| shoot / filming | **снимать / съемка** (no ё) | снимать видео «в двух экземплярах» | Store |
| project / scene | **проект / сцена** | | Store *«Проекты, сцены и дубли»* |
| lens | **объектив** | линза (false friend, §7) | Store; glossary. Verified |
| wide / ultra wide | **широкоугольная / сверхширокоугольная камера** (or *объектив*) | ультраширокий, ultra wide | Store *«широкоугольная и сверхширокоугольная камеры»*. Verified |
| telephoto | **телеобъектив** | | Glossary (v2.9 What's New) |
| front camera | **фронтальная камера**; *селфи-камера* as a synonym | передняя камера (in search it collides with eye anatomy, §7), лицевая камера | Store *«фронтальную и основную камеры»*, *«селфи-камера»*; autocomplete *как снимать на фронтальную и заднюю камеру*. Verified |
| back / rear camera | **задняя камера** (search term) or **основная камера** (store copy wording); both fine | тыловая камера (exists in search but technical-sounding), тыльная камера | Store *«основная»*; glossary rear = *задняя*; autocomplete *фронтальную и заднюю камеру одновременно*, *фронтальную и основную камеру*. Verified |
| front and back at the same time | **фронтальная и задняя камера одновременно**; *снимать на две камеры одновременно*; *с двух камер* | в то же самое время, синхронно (stiff) | Autocomplete (§5). Verified |
| both cameras | **обе камеры / с обеих камер** | | Store-adjacent glossary (*«с обеих камер»*) |
| dual camera (generic concept) | **две камеры** / **двойная камера** | двухкамерный режим, дуал-камера, dual camera (Latin, in our own prose) | Store title `ContentCam: Двойная камера`; autocomplete *двойная камера на айфоне*, *двойная камера приложение*. Verified. Lowercase when generic |
| portrait / landscape (orientation) | **вертикальное / горизонтальное видео**; nouns **вертикаль / горизонталь** | портретное / альбомное / ландшафтное видео (§7) | Store *«отдельно для вертикали и горизонтали»*. Verified (site: 0 hits of the avoid list) |
| portrait + landscape at once | **вертикальное и горизонтальное видео одновременно** | | Store line 1. Verified |
| both formats / dual format | **оба формата**, *два формата видео* | дуал-формат, двойной формат | Store *«записью обоих форматов»*, subtitle *«Одна съемка, два формата видео»* |
| separate files | **два отдельных файла / отдельными файлами** | раздельные файлы | Store. Verified |
| picture in picture | **«картинка в картинке»** | PiP, PIP, картинка-в-картинке (Samsung's hyphenated UI form only when quoting Samsung) | Store. Verified |
| split screen | **разделенный экран** (no ё) | сплит-скрин (gaming term, §7), split screen | Store. Verified |
| combine (feature) | prose: **объединение (Combine)**; verb: **объединить**; button: **«Объединить»** | склеить, смонтировать (for this feature), редактор Combine | Store *«Объединение (Combine)»*, *«их можно объединить (Combine)»*; glossary button *Объединить* |
| teleprompter | **телесуфлер** (no ё) | телесуфлёр, суфлер, teleprompter | Store *«Телесуфлер (Teleprompter)»*; autocomplete *телесуфлер приложение*. Verified |
| timelapse | **таймлапс** | timelapse, интервальная съемка (OK as explanation only) | Store; Apple's iOS mode is also *«Таймлапс»*. Verified |
| frame rate | **частота кадров**; unit **fps** | кадровая частота, фреймрейт | Store *«Разрешение и частота кадров»* |
| resolution | **разрешение** | | Store |
| manual controls | **ручные настройки** | ручное управление | Store |
| exposure / white balance / shutter speed | **экспозиция / баланс белого / выдержка** | скорость затвора | Store |
| focus/exposure lock | **блокировка AE/AF**; *удержание фиксирует фокус и экспозицию* | лок | Store; glossary |
| crosshair / level / audio meter | **перекрестие / уровень горизонта / индикатор звука** | прицел, мушка | Store |
| stabilisation | **стабилизация** | | Store |
| shutter button (photo) | **кнопка спуска** | кнопка затвора | Store |
| watermark | **водяной знак** | вотермарк, watermark (in our prose) | Store *«нет рекламы и водяного знака»*. Verified |
| ads | **реклама** | | Store |
| free / free version | **бесплатно / бесплатная версия** | фри-версия | Store |
| Premium | **Premium** (Latin, no quotes) | премиум (Cyrillic), Премиум | Store; site 0 Cyrillic hits |
| unlock (Premium) | **открывает / открыть** | разблокировать (OK but not store wording) | Store *«PREMIUM ОТКРЫВАЕТ»* |
| one-time / lifetime | **разовая покупка навсегда** | пожизненная лицензия | Store |
| app | **приложение** | апп, аппка, прога | Store |
| phone | **телефон**; *iPhone* when it is an iPhone | смартфон (allowed, but not the default; store says *телефон*) | Store *«остаются на телефоне»* |
| creators (audience) | **авторы**; *блогеры* only in query-shaped headings | креаторы, контент-мейкеры | Glossary (chosen); site uses *авторы* 64 times |
| vlog | **влог** | видеоблог (dated) | Autocomplete; keyword field has *влог* |
| Reels / Shorts / Stories | **Reels**, **Shorts** (Latin); Stories → **истории** (Instagram's Russian UI name, unverified) or **сторис** (indeclinable colloquial) | *одной Stories* (Latin word with Russian case ending) | Store uses *Reels*; keyword field *рилс* is ASO-only, do not use *рилс* in prose |
| independent developer | **независимый разработчик** | инди-разработчик | Store |

---

## 3. ContentCam mode and feature names (exactly as the store copy writes them)

First mention on a page: Russian name in «» plus the English gloss in parentheses, as the store copy does. Later mentions: Russian name only. Never the English name alone.

| English (app UI) | Russian, first mention | Later mentions | Notes |
|---|---|---|---|
| Single Lens | режим «Один объектив» (Single Lens) | «Один объектив» | Store line 11. App chip is *1 объектив* (glossary); do not use the chip form in prose |
| Dual Lens | режим «Два объектива» (Dual Lens) | «Два объектива» | Store. *Нужен iPhone со сверхширокоугольной камерой* |
| Front & Back | режим «Передняя и задняя» (Front/Back) | «Передняя и задняя» | Store glosses as **(Front/Back)**, not *(Front & Back)*. The app's English chip reads "Front & Back"; the store gloss is the authority for this site. Switcher UI shows *Передняя/задняя* |
| Front Camera mode | «Фронтальная камера» | | Store: *«Фронтальная камера: переключение на селфи-камеру с записью обоих форматов»* |
| Standard camera | «Стандартная камера» | | Store |
| Combine | объединение (Combine); button «Объединить» | объединение | Store / glossary |
| Photo mode | режим «Фото» | | Store. Do not confuse with Apple's Photos app «Фото»: write *приложение «Фото»* or *медиатека «Фото»* for Apple's app |
| Teleprompter | Телесуфлер (Teleprompter) | телесуфлер | Store glosses it |
| Timelapse | Таймлапс (Timelapse) | таймлапс | Store glosses it |
| Projects, scenes and takes | проекты, сцены и дубли | | Store |
| Recording folder | папка для записей | | Store |
| Review and trim | просмотр и обрезка | | Store |
| Storage estimate | оценка места | | Store |
| Crash recovery | защита от сбоев | | Store |
| Thermal monitor | контроль нагрева | | Store |
| On-screen overlays | подсказки на экране | | Store |
| Section labels | СПОСОБЫ СЪЕМКИ, ФОТО, ВИДЕО, РАБОТА С МАТЕРИАЛОМ | | Store headings |
| Store title / subtitle | ContentCam: Двойная камера / Одна съемка, два формата видео | | store-metadata-expansion.md |

---

## 4. Platform names in Russian

| Platform / feature | Russian name to use | Source / confidence |
|---|---|---|
| Apple "Dual Capture" (iPhone 17 and later) | **функция «Двойная съемка»** / *режим двойной съемки*; gloss once: *«Двойная съемка» (Dual Capture)* | **Verified.** support.apple.com/ru-ru/guide/iphone/iph61f49e4bb/ios: *«Запись видео в режиме двойной съемки… коснитесь «Двойная съемка»»*. Apple writes it with е, not ё |
| Apple list "Models that support Dual Capture video" | **«Модели с поддержкой функции „Двойная съемка“»** | **Verified.** support.apple.com/ru-ru/guide/iphone/aside/glos3842gv5b/27/ios/27 (lists iPhone 17, 17 Pro, 17 Pro Max, Air, 18 Pro, 18 Pro Max, Duo) |
| iOS Camera app | приложение **«Камера»**; modes **«Видео»**, **«Фото»**, **«Таймлапс»**, **«Замедленно»**, **«Киноэффект»**, **«Экшн»** | Verified, same Apple RU guide |
| iOS Settings > Camera > Record Video | **«Настройки» > «Камера» > «Запись видео»** | Verified, Apple RU guide (*«Коснитесь «Камера», затем коснитесь «Запись видео»»*) |
| iOS: Preserve Settings / lens setup | «Сохранение настроек», «Настройка объективов основной камеры» | Verified (Apple RU guide table of contents) |
| iOS frame-rate unit | **кадр/с** (Apple UI); use only when quoting Apple | Verified |
| Apple Photos app | приложение **«Фото»**, *медиатека «Фото»* | Verified (Apple RU guide; store copy) |
| Family Sharing | **«Семейный доступ»** | Verified (Apple RU guide home) |
| Samsung Director's View (older Galaxy) | **«Режим режиссера»** (Director's View) | **Verified.** samsung.com/ru/support/mobile-devices/control-your-shots-with-directors-view-on-galaxy-s21-series/ (title *«Как включить режим режиссера на Samsung Galaxy S21»*, updated 16-12-2025). Samsung writes it without ё |
| Samsung Director's View layouts | «Картинка-в-картинке», «Сдвоенный режим», «Одиночный режим» | Verified, same Samsung RU page (older One UI) |
| Samsung "Dual recording" (One UI 8+) | **«Двойная запись»** (Dual recording) | **Partly verified.** The Samsung RU S21 page uses *«двойная запись с передней и задней камерой»* descriptively; the exact One UI 8.5 menu label in Russian is **unverified** (no samsung.com/ru page found). Autocomplete confirms people search *двойная запись самсунг*. Always pair with "Samsung" or "видео" (§7 collision) |
| Samsung camera "More" menu | «Еще» | Unverified (Samsung RU UI; consistent with Samsung's ё-less style) |
| Samsung Camera app | приложение «Камера» | Verified (Samsung RU page) |
| Google Play | **Google Play** (not *Play Маркет*, the retired name) | Verified by current store branding; site uses it 126 times |
| App Store | **App Store**; US store = *App Store США* | Site standard |
| Instagram Stories | «Истории» in the Russian Instagram UI; colloquial *сторис* | Unverified (no official source fetched) |
| Instagram Reels / YouTube Shorts | Reels / Shorts (UI keeps Latin) | Unverified for UI; matches store copy |
| Instagram "Dual" camera | **Dual** (keep Latin; Russian UI label unverified). Search phrase: *двойная камера в инстаграм* | Autocomplete verified; UI label unverified |
| Snapchat "Dual Camera" | **Dual Camera** (Latin; Russian UI label unverified) | Unverified |
| Telegram dual camera (stories / video messages) | *двойная камера в Telegram* (generic) | Autocomplete *двойная камера телеграм / в тг*; UI label unverified. Relevant competitor context for Russian readers |
| TikTok | TikTok (Russian UI labels unverified) | Unverified |

---

## 5. Native search phrasing (Google autocomplete, `hl=ru&gl=ru`, 15 Nov 2026)

Use these for titles, H1, H2 and FAQ questions. Brand words appear in Cyrillic in real queries (*айфон, самсунг, андроид*); on the page keep Latin brand names but copy the rest of the phrasing.

**Front + back at once (strongest cluster)**
- *как снимать на две камеры одновременно* (+ *айфон / андроид / самсунг / xiaomi / айфон 17 / айфон 15*)
- *как снимать с двух камер одновременно* (+ *айфон / андроид / самсунг*)
- *как снимать на фронтальную и заднюю камеру одновременно* (+ *айфон*)
- *как одновременно снимать на фронтальную и основную камеру айфон*
- *как снимать видео на фронтальную и заднюю камеру айфон*
- *запись с двух камер самсунг / айфон*; *запись видео с двух камер андроид*; *запись видео сразу с двух камер*
- *как записать видео с двух камер одновременно*; *как на айфоне записать видео с двух камер одновременно*
- *как на самсунге снимать на две камеры одновременно*
- *можно ли снимать на две камеры одновременно*
- *приложение для съемки с двух камер (одновременно)*; *приложение для съемки видео с двух камер*; *приложение которое снимает на две камеры*

**Dual camera / Apple / Samsung feature names**
- *двойная камера на айфоне*, *двойная камера на самсунг*, *двойная камера приложение*, *двойная камера на андроид*, *двойная камера на айфон 17 как включить*, *двойная камера в инстаграм*, *двойная камера телеграм*
- *двойная съемка на айфон* (+ *16 / 17 / 15 / 16 про макс / 17 про макс*), *режим двойная съемка айфон*, *как включить двойную съемку на айфоне*, *как включить двойную съемку на самсунге*
- *двойная запись самсунг*, *двойная запись видео самсунг*, *как включить двойную запись на самсунге*
- *режим двойной камеры айфон*, *как включить режим двойной камеры*
- *dual capture айфон / iphone 17* (Latin form is also searched)
- Note: people search *двойная съемка на айфон 15/16*, models Apple does NOT support. That is the opening for "how to do it on iPhone 15/16" headings.

**Vertical + horizontal**
- Autocomplete has no completions for "vertical and horizontal at the same time" phrasings (*вертикальное и горизонтальное видео одновременно* returns nothing): low-volume, so lead with the problem people do type:
- *снимать вертикально или горизонтально*, *как снимать видео на телефон вертикально или горизонтально*, *как снимать рилс вертикально или горизонтально*, *как снимать видео для инстаграм вертикально или горизонтально*
- *горизонтальное видео в вертикальное* (+ *онлайн / capcut*), *вертикальное видео в горизонтальное*, *как совместить вертикальное и горизонтальное видео*
- *как снимать reels на айфон*, *как снимать рилсы на телефон*, *как снимать видео для тик тока*

**Layouts, tools, quality**
- *картинка в картинке видео* (dominated by YouTube PiP playback intent; use only with context such as *видео с двух камер «картинка в картинке»*)
- *наложить видео на видео* (+ *capcut / inshot*): editing intent, useful for the "combine" angle
- *телесуфлер для телефона / на айфон / приложение / бесплатно*
- *лучшие приложения для съемки видео на iphone / на андроид*; *приложение для съемки видео на айфон бесплатно*
- *без водяного знака видео*; *4к 60 кадров в секунду айфон*; *селфи камера айфон 17*

Example H1s in this voice: *«Как снимать на фронтальную и заднюю камеру одновременно на iPhone (2026)»*, *«Двойная съемка на iPhone 15 и 16: как снимать на две камеры одновременно»*, *«Как на Samsung снимать на две камеры одновременно»*.

---

## 6. Inconsistencies found across the 21 ru pages (16)

Page keys: `b/` = `ru/blog/<slug>/`, `vs/` = `ru/vs/<slug>/`, `home` = `ru/index.html`.

1. **Apple Dual Capture is never given its official Russian name.** "Dual Capture" appears 141 times; Apple's Russian name «Двойная съемка» 0 times (except 2 unrelated hits in vs/lookout). Right: *функция «Двойная съемка» (Dual Capture)* at first mention, then «Двойная съемка». Pages: home, vs/index, vs/apple-dual-capture (49), b/iphone-17-dual-capture-limitations (39), b/dual-camera-effect (16), b/record-front-and-back-camera-same-time-iphone (11), b/take-photo-front-and-back-camera-same-time (9), b/best-front-and-back-dual-camera-apps (7), vs/lookout, b/record-front-and-back-camera-same-time-android, b/record-portrait-and-landscape-video-same-time-iphone, vs/dualgram. Also the Latin form misses the search phrase *двойная съемка на айфон*.
2. **Grammatical gender of "Dual Capture" flips.** Feminine (*«Dual Capture, которая»*, *«бесплатна»*, *«ее ограничения»*) on home and vs/apple-dual-capture; masculine (*«ограничен»*, *«бесплатный»*) on b/iphone-17-dual-capture-limitations and vs/apple-dual-capture. Fixing #1 resolves it: «Двойная съемка» is feminine (*функция*); if a generic noun is needed use *режим двойной съемки* (masc.).
3. **Apple's list page quoted by its English title** («Models that support Dual Capture video») on vs/apple-dual-capture (3) and b/take-photo-front-and-back-camera-same-time. Right: «Модели с поддержкой функции „Двойная съемка“» (official Apple RU title).
4. **Letter ё used on 3 pages, absent on 18.** vs/dualcam (45 ё), vs/dualgram (31, incl. *телесуфлёр* ×6, *разделённым*), b/dual-format-recording-apps-compared (*телесуфлёр* ×1). Right: no ё (§1).
5. **Rating decimal.** *«Оценка 4.8»* (dot) in the shared footer on all pages that have it, and in the CTA box on every vs/ page; *«Рейтинг 4,8»* (comma) in the CTA box on all 11 blog pages. Right: **4,8**. The footer is a shared include; fix it at source.
6. **Price format.** `$5.99`, `$49.99`, `$11.99` (dot, sign first) on vs/2cam, vs/detail, b/dual-format-recording-apps-compared; *«22,99 доллара США»* (comma) on vs/dualcam. Right: `5,99 $` / *5,99 доллара США*, always with *App Store США*.
7. **Frame-rate unit.** `60 fps` (105), `60fps` (50: vs/apple-dual-capture 21, vs/lookout 7, b/record-front-and-back-camera-same-time-iphone 5, vs/detail 4, vs/index 3, vs/dualcam 3, others), `кадра/с` (62: vs/dualcam 55, b/record-portrait-and-landscape-video-same-time-android 4, b/dual-format-recording-apps-compared 3), `FPS` (vs/dualgram 4, vs/dualcam 1). Right: `60 fps`; `кадр/с` or `FPS` only inside a verbatim quote.
8. **Front & Back gloss.** Pages gloss *«Передняя и задняя» (Front & Back)*; the store copy glosses *(Front/Back)*. Pages: b/dual-camera-effect, b/dual-format-recording-apps-compared, b/iphone-17-dual-capture-limitations, b/record-front-and-back-camera-same-time-android, b/record-front-and-back-camera-same-time-iphone, b/record-front-and-back-camera-samsung-galaxy, b/record-portrait-and-landscape-video-same-time-android, vs/dualgram. Right: (Front/Back). (Low severity; flag to Jimmy if he prefers matching the English app chip.)
9. **Combine named four ways.** *редактор объединения (Combine)* (all vs/ comparison pages), *редактор «Объединение»* (b/best-front-and-back-dual-camera-apps), *редактор «Объединить»* (b/dual-camera-effect, b/iphone-17-dual-capture-limitations, b/record-front-and-back-camera-same-time-android, b/record-front-and-back-camera-same-time-iphone, b/record-front-and-back-camera-samsung-galaxy), bare *редактор Combine* (b/record-portrait-and-landscape-video-same-time-android, vs/dualcam, vs/dualgram). Right: *объединение (Combine)* in prose, «Объединить» only for the button.
10. **Dual Lens left in English** (*«режим Dual Lens»*) on b/dual-format-recording-apps-compared, b/film-for-tiktok-and-youtube-at-the-same-time, b/record-portrait-and-landscape-video-same-time-android. Right: режим «Два объектива» (Dual Lens).
11. **Samsung «Двойная запись» quoted vs unquoted** on the same page: 4 quoted, 22 unquoted on b/record-front-and-back-camera-samsung-galaxy; 9 unquoted on b/record-front-and-back-camera-same-time-android. Right: «Двойная запись» in quotes (it is a UI name), always tied to Samsung/video.
12. **Date suffix.** `6 ноября 2026 г.` on b/best-front-and-back-dual-camera-apps (6), b/take-photo-front-and-back-camera-same-time (4), b/record-portrait-and-landscape-video-same-time-iphone (1), against `… 2026 года` everywhere else. Right: *года* (§1).
13. **Em dashes** on vs/dualgram (6, e.g. *«Just2us — приложение»*, *«зум — кнопка»*). Right: rephrase (colon or *это*).
14. **"PiP" abbreviation** on b/record-front-and-back-camera-samsung-galaxy (2). Right: «картинка в картинке».
15. **"Stories" in Latin with Russian grammar** (*«для одной Stories»*) on b/record-front-and-back-camera-same-time-android and b/dual-camera-effect. Right: *истории* / *сторис*.
16. **смартфон vs телефон.** *смартфон* used on b/dual-camera-effect (5), b/record-front-and-back-camera-same-time-android (5), b/iphone-17-dual-capture-limitations (2), b/record-front-and-back-camera-samsung-galaxy (1); the store copy and other pages say *телефон*. Low severity; prefer *телефон*.

Consistent and correct today (keep): «вы» lowercase register; *дубль*; *объектив* (0 *линза*); *вертикальное/горизонтальное* (0 *портретное/альбомное*); «картинка в картинке»; *разделенный экран* (0 *сплит*); *водяной знак*; *Premium* in Latin; *Google Play* (0 *Play Маркет*); «Передняя и задняя» (208 hits, 0 variants); «Один объектив», «Два объектива»; «ёлочки» quotes with no straight quotes in visible text.

---

## 7. False friends and calque traps

- **линза ≠ lens (camera).** A camera lens is *объектив*; *линза* is a single optical element or a contact lens.
- **портретный / альбомный / ландшафтный.** *Портретный режим* in Russian phone UIs means the background-blur portrait mode, not vertical orientation; *альбомная ориентация* is print/screen-rotation jargon; *ландшафтный* means landscape *scenery/design*. Say *вертикальное / горизонтальное видео*.
- **передняя камера** in search collides with eye anatomy (*передняя камера глаза* tops autocomplete) and car cameras. Use *фронтальная камера* for the selfie camera; *задняя камера* also pulls car/dashcam results, so pair it with *телефона/iPhone* in titles.
- **двойная запись** is also accounting's double-entry bookkeeping (top autocomplete: *двойная запись в бухгалтерии*). Never use it alone in a title; write *«Двойная запись» на Samsung* / *двойная запись видео*.
- **двойная камера** also means a CCTV dual camera (*двойная камера видеонаблюдения*) and Telegram's feature. Anchor with *на iPhone / в приложении / на телефоне*.
- **сплит-скрин** is gaming jargon (*сплит скрин игры на пк*); use *разделенный экран*.
- **картинка в картинке** searches are mostly about YouTube PiP playback; always pair with camera/recording context.
- **«Фото»** is both ContentCam's photo mode and Apple's Photos app: say *режим «Фото»* vs *приложение «Фото»*.
- **клип** alone can read as "music video" (*реакция на клип*); for ContentCam's unit use *дубль*.
- **реакция на видео** is dominated by specific celebrity reaction searches and chemistry experiments (*видео реакция*); for reaction content say *видео-реакция с двух камер* or *ролик-реакция*.
- **Calques to avoid:** *делать видео* (→ *снимать видео*), *в то же самое время* (→ *одновременно / сразу*), *два файла раздельно* (→ *два отдельных файла*), *пожизненная подписка* (→ *разовая покупка навсегда*), *креатор* (→ *автор*), *кликнуть/тапнуть* (→ *нажать*), *вотермарк* (→ *водяной знак*), *доступно в Premium-версии* is fine but *премиум* in Cyrillic is not.
- **Capitalised «Вы»** is Apple-manual style and letter-writing etiquette; on this site it reads like a bank letter. Keep lowercase.
- **Dot decimals** (`4.8`, `$5.99`) read as English; Russian uses a comma. Version numbers are the only exception.
- **Free models list:** Russian searchers expect *двойная съемка* on iPhone 15/16; Apple's Russian list excludes them. Do not imply Apple's feature works there; say ContentCam's «Передняя и задняя» does (store: iOS 18+, incl. iPhone 15 and 16).
