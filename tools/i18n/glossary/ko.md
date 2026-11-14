# Korean (`ko`) terminology + style sheet for contentcam.app

Built 2026-11-15. Applies to every page under `contentcam-web/ko/`, now and in later passes.

Sources, in order of authority:
1. **Store copy**: `~/contentcam/docs/store-descriptions/v2.8.2/desc/ko.txt` (native-reviewed, shipped). Cited as `store`.
2. **App glossary**: `~/contentcam/docs/localization-glossary-ko.md` (built from the v2.8.3 store copy + What's New files). Cited as `app-gl`. Rows it marks "(chosen, unattested)" are flagged here too.
3. **Apple Korea**: apple.com/kr product pages and the Korean iPhone User Guide (support.apple.com/ko-kr/guide/iphone/...), fetched 2026-11-15.
4. **Samsung Korea**: samsungsvc.co.kr solution pages 89629 (Galaxy S21 디렉터스 뷰, updated 2026-10-28) and 1083256 (Z Fold4 디렉터스뷰, updated 2026-10-05) and 37685 (듀얼 카메라 = rear dual lens, 2020).
5. **Google autocomplete** (`hl=ko&gl=kr`), run 2026-11-15. Cited as `AC`.

Confidence labels: **verified** (seen in a source above), **AC-only** (real search behaviour, no official UI source), **unverified** (our best guess; a native reviewer should check).

---

## 1. Register, person form, typography

### Register
- **해요체 in every sentence** of body copy, FAQ answers, captions, CTA sentences: `촬영해요`, `올릴 수 있어요`, `돼요`. This is what the store copy uses all the way through (`store` line 1: "촬영해요", "올릴 수 있어요"), and the brief says to follow the store copy.
- Instructions to the reader: `~하세요` (`앱을 여세요`, `녹화 버튼을 누르세요`). Polite requests: `~해 주세요`.
- **Never 합쇼체** (`~합니다`, `~습니다`, `~하십시오`) in our own voice. The only allowed 합니다체 is inside a **verbatim quote** of Apple/Samsung/Meta text (Apple KR support and Samsung svc both write 합니다체; the ko pages currently quote them correctly, e.g. "...제공되지 않습니다").
- Headings, table cells, chips, badges, and nav labels are **noun-style**, with no verb ending: `가로 세로 동시 촬영`, `광고 없음`, `워터마크 없음`, `계정 필요 없음`, `수동 조작`.
- Titles/H1/H2 may end in a question (`~될까?`, `~나요?`) or a `~하는 법` / `~방법` noun phrase. Both match how people search (section 5).
- Person: talk to the reader without a pronoun (Korean drops 당신/여러분). Use `내 폰`, `내 얼굴` for "your phone/face" as the store copy does ("내 폰에만 남아요"). Jimmy speaks as `저` in disclosure lines ("저는 ContentCam을 만드는 사람이라..."). **Never `당신`.**

### Spacing (띄어쓰기)
- Korean words are spaced. Particles attach (`iPhone에서`, `ContentCam은/을`). After a Latin brand name, pick the particle by how the name is **pronounced**: `ContentCam을` (캠 ends in a consonant), `iPhone에서`, `TikTok에`, `Android에서`, `Pixel은`.
- Loanword compounds: write them spaced in prose: `듀얼 카메라`, `듀얼 렌즈`, `분할 화면`, `화면 속 화면`, `프레임 레이트`, `화이트 밸런스`, `손떨림 보정`. The closed search forms (`듀얼카메라`, `동시촬영`, `가로세로`) are allowed **only in the title/H1/H2/meta/breadcrumb** of a page that targets that exact query (section 5). Don't switch forms inside one page's body.
- `가로 세로` (spaced) or `가로세로` (closed, search form). Both are fine. Never `세로 가로` in a title or link anchor (section 6, #10).
- Counters: `5번`, `파일 두 개`, `사진 두 장`, `iPhone 7개 모델` (native numerals + counter for small counts, as in the store copy "파일 두 개", "사진 두 장").

### Punctuation
- **No em dashes** (site rule). Join with a comma, a period, or `:`. An en dash `–` is allowed only as an empty table cell meaning "not included" (pricing table).
- Middle dot `·` (U+00B7) for the mode name `전면·후면` and for short lists of equal items: `24·25·30·50·60fps`, `iPhone XS·XR`, `0.5x·1x·2x`, `아이폰 15·16`. That is the store copy's style.
- Range: `0.5초~30초`, `10배~900배속` (tilde, no spaces), as in the store copy.
- Quotes: the site mostly uses straight `"..."` for quotations. Pick **one** style per page and stick to it. Recommended going forward: `"..."` for quoted sentences and `‘...’` for UI labels you name (Apple KR style: `‘듀얼 캡처’`). Don't mix `"` and `“”` in one page (section 6, #13).
- Parenthetical English gloss right after the Korean, no space: `합치기(Combine)`, `PIP(화면 속 화면)`, `싱글 렌즈(Single Lens)`. Gloss on first use per page only.
- Question marks and exclamation marks as in English. Sentences end with `.`; noun-style table cells and headings take no period.

### Numbers, units, dates, prices
- Dates: **`2026년 11월 5일`** (all pages already do this; never `2026. 11. 5.` or `11/5`). Month only: `2026년 5월`.
- Byline: `글: Jimmy, ContentCam 개발자 · 2026년 10월 9일 · 2026년 11월 5일 업데이트` (majority format; section 6, #2).
- fps: no space, `30fps`, `60fps`, `24·25·30·50·60fps` (`store`). Resolution: `4K`, `HD`, `1080p`, `FHD`. Ratios: `9:16`, `16:9`, `4:3`. Zoom: `0.5x·1x·2x` (`store`).
- Percent: `50%` (no space).
- Prices: copy the source format exactly (brief: keep every price). The site uses `$19.99` form. Don't convert to `19.99달러` or `US$` mid-site (section 6, #15).
- Thousands separator: `50,000회 이상`.
- Counts of free takes: **`5번`** (`전면·후면 녹화 5번 무료`), not `5회` (section 6, #16).

---

## 2. Mandated term table

| English concept | Use (Korean) | Avoid / forbidden | Source / confidence |
|---|---|---|---|
| record front and back camera at the same time (the generic concept, titles) | **전후면 카메라 동시 촬영**; prose: `전면 카메라와 후면 카메라로 동시에 녹화` | `앞뒤 카메라` in prose (OK only as a secondary search keyword), `양면 카메라`, `이중 카메라` | AC: "전후면 카메라 동시 촬영", "아이폰 전후면 동시촬영", "갤럭시 전후면 동시 촬영"; Apple KR iPhone 17/Air: "전후면 동시 동영상 촬영"; iPhone 17 Pro: "전후면 카메라로 동시에 녹화". **verified** |
| front camera / rear camera | **전면 카메라 / 후면 카메라**; selfie camera **셀카 카메라** | `뒷면 카메라`, `뒤 카메라`, `셀피 카메라`, `메인 카메라` (= Apple's main rear lens) for "rear camera" | `store`, Apple KR guide. **verified** |
| selfie | **셀카** | `셀피` | `store` ("셀카 카메라", "셀카 사진"). **verified** |
| dual camera (search term) | **듀얼 카메라** (prose); `듀얼카메라` in a title that targets that query | using it alone where it could mean a dual **rear** lens (section 7) | AC: both "듀얼카메라 앱" and "듀얼 카메라 앱". **verified** |
| portrait / vertical | **세로** (`세로 영상`, `세로 9:16`) | `세로형`, `포트레이트`, `인물 사진` (= Apple Portrait photo mode) | `store`. **verified** |
| landscape / horizontal | **가로** (`가로 영상`, `가로 16:9`) | `가로형`, `랜드스케이프`, `풍경` | `store`. **verified** |
| portrait + landscape at once (concept, titles) | **가로 세로 동시 촬영** / **가로세로 동시촬영**; prose: `세로 영상과 가로 영상을 동시에` | `세로 가로` in titles/anchors; `두 포맷`; `듀얼 포맷` | AC: "가로세로 동시 촬영", "가로 세로 동시 촬영 앱", "아이폰 가로 세로 동시 촬영"; `store` line 1 for prose. **verified** |
| both formats / dual-format | **두 비율** (`두 비율 녹화`) | `두 형식`, `두 포맷`, `두 화면비`, `듀얼 포맷` | `store` ("두 비율을 HD로 녹화"). **verified** |
| video (general noun) | **영상** (default); `동영상` OK when naming a camera mode or in titles that mirror searches ("아이폰 동영상 촬영 중 카메라 전환") | `비디오` in our own prose (Apple's **support guide** uses 비디오; quote it only when naming Apple's mode/page) | `store` uses only 영상. Apple KR marketing: "듀얼 캡처 동영상"; Apple KR guide: "비디오 모드". **verified** |
| record (video) / shoot | **녹화하다** (recording), **촬영하다/찍다** (shooting). Both fine | `레코딩` (except inside Samsung's name 듀얼 레코딩) | `store`, `app-gl`. **verified** |
| file / two separate files | **파일 두 개로 따로 저장** | `2개의 파일`, `두 파일로 분리` | `store`. **verified** |
| picture-in-picture | **PIP(화면 속 화면)** on first use, then `PIP` | `PiP`, `픽처 인 픽처`, `픽인픽` | `store` "PIP(화면 속 화면)"; Apple KR "‘화면 속 화면’"; Samsung KR "PIP 화면 (화면 속 화면)". **verified** |
| PiP inset (the small tile) | **작은 창** | `작은 화면` (one occurrence; drift), `썸네일` | `app-gl` (desc v2.8.3). **verified** |
| split screen (video layout) | **분할 화면** (`분할 화면 영상`) | `분할화면` (closed) in prose | `store`; Samsung KR "분할 화면". **verified** |
| split-screen video (search title) | **화면 분할 영상** is OK in a title that targets "아이폰 화면 분할 영상" | `스플릿 스크린` | AC: "화면 분할 영상", "분할 화면 영상". **verified** |
| Combine (ContentCam feature) | **합치기(Combine)** on first use, then `합치기` | `결합`, `병합`, `컴바인`, `합성` | `store`. **verified** |
| take / scene / project | **테이크 / 씬 / 프로젝트** | `촬영본` for take, `장면` for the app's Scene entity | `store`, `app-gl`. **verified** |
| scene in front of the lens | **눈앞의 장면** / `앞의 장면` | `씬` in that sense | `app-gl` (chosen, unattested); Apple KR "눈앞의 광경". **verified-ish** |
| trim | **자르기** | `트리밍`, `컷 편집` | `store` ("리뷰와 자르기"). **verified** |
| review screen | **리뷰 화면** | `검토` | `store`. **verified** |
| crop | **크롭** | `잘라내기` | `store` ("크롭해요"). **verified** |
| teleprompter / script | **텔레프롬프터 / 대본** | `프롬프터` alone, `스크립트` | `store`. **verified** |
| stabilisation | **손떨림 보정** (ContentCam); `흔들림 보정` only when quoting Apple specs ("광학 이미지 흔들림 보정") | `안정화` in our voice (Apple Settings label is "안정화 향상"; quote only) | `store`; Apple KR. **verified** |
| timelapse | **타임랩스** | `타임 랩스`, `저속 촬영` | `store`. **verified** |
| frame rate | **프레임 레이트** | `프레임률` (Apple's term; quote only), `초당 프레임 수` | `store`; Apple KR uses "프레임률". **verified** |
| resolution | **해상도** | | `store`. **verified** |
| manual controls | **수동 조작** | `수동 컨트롤`, `매뉴얼` | `store`. **verified** |
| white balance / exposure / focus | **화이트 밸런스 / 노출 / 초점** | `화이트밸런스` (closed) | `store`. **verified** |
| wide / ultra-wide | **광각 / 초광각** (ContentCam copy); Apple calls the ultra-wide `울트라 와이드` (quote/spec tables only) | `울트라 와이드` in our own feature copy | `store`; Apple KR guide "울트라 와이드 카메라". **verified** |
| record button / shutter button | **녹화 버튼 / 셔터 버튼** | `촬영 버튼` for ContentCam | `store`; Apple KR guide. **verified** |
| storage | **저장 공간** | `스토리지`, `용량` | `store`. **verified** |
| Photos app / photo library | **사진 앱 / 사진 보관함** | `갤러리` (that is Samsung's app; use only for Android/Samsung) | `store` "사진 앱"; Apple KR "사진 앱의 보관함", "사진 보관함". **verified** |
| Files app | **파일 앱** | | `app-gl` (chosen, unattested; iOS name). **unverified** |
| phone | **폰** (default, matches store "내 폰"); `기기` for device lists/specs | `휴대폰`, `핸드폰`, `스마트폰` in body (allowed only where Samsung/Apple are quoted) | `store`. **verified** |
| third-party app | **서드파티 앱** | `타사 앱`, `외부 앱` | site usage (18 pages). Site convention |
| built-in camera app | **기본 카메라 앱** | `순정 카메라` (slang), `내장 카메라` | site usage; store "기본 카메라 수준". Site convention |
| app | **앱** | `어플`, `어플리케이션` (people type 어플 in search, but don't write it) | `store`. **verified** |
| Premium | **프리미엄** | `Premium` in Latin letters | `store`. **verified** |
| lifetime purchase | **평생 이용권** (`한 번 결제하는 평생 이용권`) | `평생 구매`, `평생 플랜`, `평생 라이선스` (for ContentCam) | `store`. **verified** |
| annual / monthly subscription | **연간 구독 / 월간 구독** | `연 구독`, `월 정기 결제` | `store`. **verified** |
| plan (pricing tier) | **요금제** (`연간 요금제`) is fine for a plan name | | site usage. Site convention |
| free trial | **무료 체험** (`7일 무료 체험`) | `무료 평가판`, `체험판` | `app-gl`. **verified** |
| no ads / no watermark / no account | **광고 없음 / 워터마크 없음 / 계정 필요 없음** (badges); prose `광고도 워터마크도 없어요` | | `store`, home/pricing. **verified** |
| free to try (CTA) | **ContentCam을 무료로 써 보세요.** | `ContentCam 무료로 써 보기.` (minority variant) | majority site usage (20 pages). Site convention |
| solo developer | **1인 개발자** | `인디 개발자`, `개인 개발자` | `store`. **verified** |

---

## 3. ContentCam mode and feature names (exactly as the store copy writes them)

| English | Korean (use verbatim) | Notes |
|---|---|---|
| Single Lens | **싱글 렌즈** (first use may add `(Single Lens)`) | never `단일 렌즈`, `싱글렌즈` |
| Dual Lens | **듀얼 렌즈** (`(Dual Lens)` gloss optional) | It means wide + ultra-wide, **not** front + back. Never `듀얼 카메라` for this mode |
| Front & Back / Front/Back | **전면·후면** (middle dot U+00B7), `전면·후면 모드` | Never `전후면 모드`, `전면/후면`, `전·후면` for **our** mode. In a store-style gloss: `전면·후면(Front/Back)` |
| Front camera (mode) | **전면 카메라** | store: "셀카 카메라로 전환해도 두 비율 녹화는 그대로예요" |
| Normal camera / Portrait only | **일반 카메라** (store) / **세로만** (`app-gl`, chosen, unattested) | |
| Combine | **합치기(Combine)** → `합치기` | "녹화가 끝난 뒤 합치기(Combine)로 두 파일을 PIP(화면 속 화면)나 분할 화면 영상 하나로" |
| Photo mode / shutter button | **사진 모드 / 셔터 버튼** | `전면·후면 사진` = Front/Back photo |
| Resolution & frame rate | **해상도와 프레임 레이트** | |
| Manual controls | **수동 조작** (노출, 화이트 밸런스, ISO, 셔터) | |
| Focus & exposure (tap / long-press lock) | **초점과 노출**; "AE/AF 잠금", in prose `고정` | |
| Teleprompter | **텔레프롬프터** | |
| Stabilisation & HDR | **손떨림 보정과 HDR** | |
| Timelapse | **타임랩스** | |
| Guides: level, crosshair, audio meter | **가이드: 수평계, 중앙 십자선, 오디오 미터** | |
| Zoom | **줌** (0.5x·1x·2x 버튼, 핀치, 다이얼) | |
| Projects, scenes, takes | **프로젝트, 씬, 테이크** | |
| Recording folder | **녹화 폴더** | |
| Review & trim | **리뷰와 자르기** / `리뷰 화면에서 자르기` | not `검토와 트리밍` |
| Storage calculator | **저장 공간 계산** | |
| Crash recovery | **예기치 않은 종료 대비** | |
| Thermal management | **발열 관리** | |
| Premium unlock list header | **프리미엄으로 열리는 기능** | |
| Lifetime / annual / monthly | **평생 이용권 / 연간 구독 / 월간 구독** | |
| Requirements line | **iOS 18 이상이 필요해요(iPhone XS·XR 이후 모델)** | |

---

## 4. Platform names and their Korean UI labels

| Platform / feature | Korean to use | Source / confidence |
|---|---|---|
| Apple "Dual Capture" | **듀얼 캡처** (`Apple 듀얼 캡처`, `아이폰 듀얼 캡처`, `듀얼 캡처 동영상`) | apple.com/kr/iphone-17-pro ("‘듀얼 캡처’ 기능을 사용해 전후면 카메라로 동시에 녹화"), apple.com/kr/iphone-17 and /iphone-air ("듀얼 캡처 동영상"), Korean iPhone User Guide iph61f49e4bb ("듀얼 캡처 비디오 녹화하기"). **verified**. Never `듀얼캡처`, `듀얼 캡쳐`, `Dual Capture` untranslated |
| Apple Camera app steps for Dual Capture | Camera **카메라** → **비디오** mode → **카메라 제어 항목 버튼** → **듀얼 캡처** → **녹화 버튼**; turn off with **듀얼 캡처 버튼** | Korean iPhone User Guide iph61f49e4bb. **verified**. Note: **카메라 컨트롤** is the *hardware* Camera Control button, not the on-screen control (section 6, #5) |
| Apple "Models that support Dual Capture video" page title | **듀얼 캡처 비디오를 지원하는 모델** | used on 7 ko pages, matches Apple KR guide wording. **verified (title form)** |
| Apple "Record videos with your iPhone camera" | **iPhone 카메라로 비디오 녹화하기** | Korean guide page title. **verified** |
| iOS Settings > Camera | **설정 > 카메라 > 비디오 녹화**; **포맷**; **카메라 잠금**; **안정화 향상**; **화이트 밸런스 잠금**; **HDR 비디오**; **자동 FPS**; **소리 녹음**; **스테레오 사운드 녹음**; **프레임 영역 밖 보기**; **렌즈 수정**; **‘사진 보관함에 캡처 저장’** | Korean iPhone User Guide iphc1827d32f, iphb362b394e. **verified** |
| Apple Picture in Picture (system) | **‘화면 속 화면’** | Korean guide TOC "‘화면 속 화면’ 기능으로 멀티태스킹하기". **verified** |
| Apple Center Stage | **센터 스테이지** (Apple KR mixes in `Center Stage 전면 카메라` on the 17 Pro page) | apple.com/kr/iphone-air. **verified** |
| Apple Camera Control (hardware) | **카메라 컨트롤** | Korean guide TOC "카메라 컨트롤 사용하기". **verified** |
| iPhone Duo | **iPhone Duo** in prose; **아이폰 듀오** in titles | Apple KR guide writes "iPhone Duo"; AC: "아이폰 듀오" (가격, 사전예약...). **verified** |
| iPhone (brand) | **iPhone** in prose; **아이폰** in title/H1/H2/meta/breadcrumb (search form) | `store` writes iPhone (one 아이폰); Apple KR writes iPhone; AC is all 아이폰. **verified** |
| Samsung Galaxy | **갤럭시** (Korean script; Samsung Korea's own form) | samsungsvc.co.kr ("갤럭시 S21", "갤럭시 Z 폴드4"). **verified** |
| Samsung Director's View | **디렉터스 뷰** (Samsung KR writes both `디렉터스 뷰` and `디렉터스뷰`; use spaced) | samsungsvc.co.kr 89629, 1083256. **verified** |
| Samsung Dual recording | **듀얼 레코딩** | AC: "듀얼 레코딩 갤럭시", "듀얼 레코딩 설정", "삼성 듀얼 레코딩", "s26 듀얼레코딩"; Samsung Members community posts. Official Korean One UI label **unverified** (no samsung.com/sec page found). High confidence |
| Samsung camera menu "More" | **더보기** | samsungsvc.co.kr ("카메라 > 더보기 > 디렉터스뷰"). **verified** |
| Samsung layouts | **PIP 화면(화면 속 화면) / 분할 화면 / 싱글 화면** | samsungsvc.co.kr 89629. **verified** |
| Samsung camera video mode / gallery | **동영상** / **갤러리** | samsungsvc.co.kr. **verified** |
| Samsung One UI 8.5 "Quick controls" | Korean label **unverified**. Don't print the English "Quick controls" as if it were the Korean UI; describe it (`동영상 모드 화면의 빠른 설정 아이콘(동그라미 네 개)`) and mark as checked-in-English if needed | **unverified** |
| Google Pixel | **구글 픽셀** in titles; **Pixel** in prose (model names stay Latin: `Pixel 9 Pro Fold`) | Pixel is not officially sold in Korea; Korean UI labels for Pixel Camera can't be checked from a KR source. AC: "구글 픽셀". Pixel "Dual Screen" = `듀얼 스크린` **unverified** |
| Android | **안드로이드** in titles; **Android** in prose and requirement lines | `store` style (Latin in specs). Site convention |
| TikTok | **틱톡** | `store` ("틱톡, 릴스, 유튜브에 바로 올릴 수 있어요"); AC. **verified**. Keep Latin only for the product names `TikTok Now`, `TikTok Newsroom` |
| Instagram | **인스타그램** in prose, **인스타** in titles (search form) | AC: "인스타 듀얼 카메라". Site convention. Latin `Instagram` only inside cited English page titles |
| Instagram Reels / Dual | **릴스** / **듀얼** (Instagram camera tool) | `store` "릴스". Instagram's Korean label for the Dual tool **unverified** (pages use `듀얼`) |
| YouTube / Shorts | **유튜브 / 쇼츠** | `store` "유튜브". **verified** for 유튜브; 쇼츠 = site convention |
| Snapchat / BeReal | **스냅챗 / 비리얼** in titles; **Snapchat / BeReal** in prose | AC: "비리얼". Snapchat's Korean "듀얼 카메라" label **unverified** |
| App Store / Google Play | **App Store / Google Play** (Latin, always) | site + Apple KR usage. **verified** |

---

## 5. Native search phrasing (autocomplete-verified, `hl=ko&gl=kr`, 2026-11-15)

Use these for titles, H1s, H2s and FAQ questions. Keep the year `(2026)`.

**Front + back at once**
- 전후면 카메라 동시 촬영 · 전후면 카메라 동시 촬영 앱 · 전후면 동시촬영
- 아이폰 전후면 카메라 동시 촬영 · 아이폰 전후면 동시촬영 · 아이폰 17 전후면 동시 촬영
- 갤럭시 전후면 동시 촬영 · 갤럭시 전면 후면 동시 촬영
- 전면 후면 동시 촬영 · 전면 후면 동시 촬영 어플 · 아이폰 전면 후면 동시 촬영
- 앞뒤 동시 촬영 · 아이폰 앞뒤 동시 촬영 · 아이폰 카메라 앞뒤 동시 촬영 (secondary keyword only; fine in an FAQ question)
- 셀카 후면 동시에 · 아이폰 셀카 후면 동시

**Dual camera**
- 듀얼카메라 / 듀얼 카메라 · 듀얼카메라 아이폰 · 듀얼카메라 앱 · 듀얼카메라 갤럭시 · 듀얼 카메라 하는법 · 아이폰17 듀얼카메라 · 인스타 듀얼카메라 / 인스타 듀얼 카메라 · 아이폰 16 듀얼 카메라

**Apple Dual Capture**
- 듀얼 캡처 · 아이폰 듀얼 캡처 · 아이폰 17 듀얼 캡처 · 아이폰 16 듀얼 캡처 · 17프로 듀얼 캡처 (searchers also type the misspelling `캡쳐`; never write it)

**Samsung**
- 듀얼 레코딩 · 듀얼 레코딩 갤럭시 · 듀얼 레코딩 설정 · 삼성 듀얼 레코딩 · 갤럭시 카메라 듀얼 레코딩 · 폴드 8 듀얼 레코딩 · 갤럭시 26 듀얼 레코딩
- 디렉터스 뷰 · 갤럭시 디렉터스 뷰 · 갤럭시 카메라 디렉터스 뷰

**Portrait + landscape at once**
- 가로세로 동시 촬영 · 가로 세로 동시 촬영 · 가로 세로 동시 촬영 앱 · 아이폰 가로세로 동시 촬영 · 아이폰 가로 세로 동시 촬영 · 인스타 가로 세로 동시에
- 세로 영상 가로로 (변환/만들기): a different intent (converting), useful as an H2 contrast
- Not our intent: `가로세로 동시송출` (live simulcast), `갤럭시 가로세로` (screen rotation)

**Split screen / PIP**
- 화면 분할 영상 · 화면 분할 영상 편집 · 분할 화면 영상 · 아이폰 영상 분할
- pip 영상 · pip 영상 편집 · 아이폰 pip (mostly about YouTube's floating window; see section 7)

**Switching camera while recording**
- 아이폰 동영상 촬영 중 카메라 전환 · 동영상 촬영 중 카메라 전환

**Other**
- 텔레프롬프터 앱 · 텔레프롬프터 앱 추천 · 무료 텔레프롬프터 앱
- 비리얼 · 비리얼 찍는법 · 비리얼 앱
- 아이폰 듀오 (가격 / 출시 / 사전예약)
- 틱톡 듀얼: no camera intent (returns 듀얼넘버/듀얼앱). Title the TikTok page around `틱톡 듀얼카메라 하는 법` + `전후면 동시 촬영`, as it does now
- No autocomplete for: 스냅챗 듀얼, 픽셀 전후면, 안드로이드 전후면, 리액션 영상 촬영. Use the generic `전후면 카메라 동시 촬영` pattern with the brand in front

---

## 6. Inconsistencies found across the existing ko pages (17)

Scanned all 39 pages under `contentcam-web/ko/` (visible text + JSON-LD). Page paths are relative to `ko/`.

1. **Breadcrumb left in English (`Home`, `Blog`)**. Right: `홈 › 블로그` (33 pages). Wrong, in both visible breadcrumb and BreadcrumbList JSON-LD: `blog/best-front-and-back-dual-camera-apps`, `blog/record-front-and-back-camera-iphone-15-16`, `blog/record-portrait-and-landscape-video-same-time-iphone`, `blog/record-portrait-and-landscape-video-same-time-android`.
2. **Byline format.** Right (17 pages): `글: Jimmy, ContentCam 개발자 · …`. Wrong (`Jimmy (ContentCam 개발자)`): `blog/best-front-and-back-dual-camera-apps`, `blog/dual-format-recording-apps-compared`, `blog/film-for-tiktok-and-youtube-at-the-same-time`, `blog/record-front-and-back-camera-iphone-15-16`, `blog/record-portrait-and-landscape-video-same-time-android`, `blog/record-portrait-and-landscape-video-same-time-iphone`.
3. **CTA box sentence.** Right (20 pages): `ContentCam을 무료로 써 보세요.` Minority variant `ContentCam 무료로 써 보기.`: `blog/best-front-and-back-dual-camera-apps`, `blog/record-front-and-back-camera-iphone-15-16`, `vs/2cam`, `vs/detail`, `vs/dualgram`, `vs/lookout`.
4. **Samsung UI labels left in English.** `blog/record-front-and-back-camera-samsung-galaxy` uses `Dual recording(듀얼 레코딩)`, `Quick controls`, `More(더보기)`, `Dual recordings`, `Dual rec`, `Director's View(디렉터스 뷰)` as the main labels (22× "Dual recording"). `blog/record-front-and-back-camera-same-time-android` already uses `듀얼 레코딩` and `디렉터스 뷰`. Right: Korean labels first (`듀얼 레코딩`, `더보기`, `디렉터스 뷰`). English only in a gloss, or when quoting an English Samsung page. `blog/snapchat-front-and-back-camera` cites a Samsung page by its English title, which is fine.
5. **Apple's on-screen control called `카메라 컨트롤 버튼`.** Apple KR: tap the **카메라 제어 항목 버튼**, then 듀얼 캡처. `카메라 컨트롤` is the hardware button. Right: `blog/dual-camera-effect`, `blog/iphone-17-dual-capture-limitations`. Wrong: `blog/bereal-style-photo-without-bereal`, `blog/record-front-and-back-camera-same-time-iphone`, `blog/switch-camera-while-recording-iphone`, `vs/apple-dual-capture`.
6. **Lifetime naming for ContentCam.** Right: `평생 이용권` (14 pages, `store`). Wrong: `vs/dualcam` writes ContentCam's plans as `연간, 월간, 평생 구매` (the comparison-table row). `평생 구매` for DualCam and `평생 플랜` for Detail (`vs/detail`) describe competitors, which is acceptable.
7. **`Premium` in Latin letters for ContentCam.** Right: `프리미엄`. Wrong: `vs/dualcam` (`광고 없음(무료, Premium 모두)`, `워터마크 없음(무료, Premium 모두)`, `HD 60(Premium)`), `blog/dual-format-recording-apps-compared` (`Premium은 월간, 연간…`). `vs/dualtake`'s `Premium Weekly` is DualTake's own plan name, which is fine.
8. **Changelog drifts from store terms.** `changelog`: `두 형식` → `두 비율`; `트리밍` (2×) → `자르기`; `검토와 트리밍` → `리뷰와 자르기`; `휴대폰` (7×) → `폰` (all other pages use 폰; store says "내 폰").
9. **Platform names in mixed scripts.** Store: `틱톡, 릴스, 유튜브`. Wrong: `vs/2cam`, `vs/detail`, `vs/lookout` (`TikTok, 릴스, 쇼츠용 … YouTube용`: Latin and Hangul in one list); `vs/dualgram` (`TikTok, Reels, Shorts용 … YouTube용`, all Latin). Right: `틱톡, 릴스, 쇼츠용 9:16 파일과 유튜브용 16:9 파일`. (`home`'s platform logo strip in Latin is fine, since those are logo labels.)
10. **Portrait/landscape keyword order and spacing.** In titles and link anchors, `세로 가로` (not a search form) appears in: `blog/film-for-tiktok-and-youtube-at-the-same-time` (title "세로 가로 한 번에"), `blog/record-front-and-back-camera-google-pixel` and `blog/record-front-and-back-camera-same-time-android` (anchor "안드로이드 세로 가로 영상 동시 촬영", while the target page's own title is "안드로이드·갤럭시 가로세로 동시촬영"), `blog/record-front-and-back-camera-same-time-iphone` (anchor "세로 가로 영상 동시 촬영"), `vs` (3× "세로 가로 (동시) 녹화"), `vs/dualtake` (anchor "세로 가로 동시 촬영 앱 전체 비교"). `pricing` writes `세로·가로 동시 녹화`. Right: `가로 세로` / `가로세로` in titles and anchors; prose follows the store (`세로와 가로`, `세로 영상과 가로 영상`). Also, anchors pointing to the same comparison page vary three ways ("가로세로 동시촬영 앱 전체 비교" / "…전부 비교" / "세로 가로 동시 촬영 앱 전체 비교"). Use one anchor.
11. **Pixel / 픽셀 mixed in body text** (Pixel 80× in 7 pages, 픽셀 55× in 15 pages, often in the same page, e.g. `blog/record-front-and-back-camera-google-pixel`). Right: `구글 픽셀` in title/H1/H2/meta; `Pixel` in body text and model names.
12. **Apple source titles left in English when Apple has a Korean page.** `blog/bereal-style-photo-without-bereal` ("Models that support Dual Capture video", "Record a video with your iPhone camera") and `blog/how-to-do-dual-camera-on-tiktok` ("Models that support Dual Capture video"). Seven other pages cite the Korean titles `듀얼 캡처 비디오를 지원하는 모델` / `iPhone 카메라로 비디오 녹화하기`, and those are right. (English titles of Snapchat/Meta/TikTok pages with no Korean version are fine.)
13. **Quote style mixed.** Curly `“ ”` in `vs/lookout`, `vs/mixcam`, `vs/dualtake`, `vs/2cam`, `vs/detail`, `blog/iphone-4k-front-and-back-camera-same-time`, `android`; straight `"` everywhere else; `vs/dualgram` and `android` mix both within the page; `vs/detail` also uses `‘ ’`. Right: one style per page (section 1).
14. **ContentCam's mode called by the generic name.** `vs/dualcam` says ContentCam's free tier includes `전후면 카메라 5회` (4×). Right: `전면·후면 5번`. Opposite drift: `vs/dualgram` uses our mode name `전면·후면` for Dualgram's feature ("Dualgram PRO로 열리는 것: 전면·후면 파일 따로 저장") and for iPad support. Use `전후면` / `전면과 후면` for anything that isn't ContentCam's mode.
15. **Price format.** `vs/dualcam` writes `연간(22.99달러, …)`; every other price on the site is `$22.99` style. Right: `$22.99` (keep the source format).
16. **Free-take counter.** Right: `5번` (21 pages, incl. pricing). Wrong `5회`: `blog/dual-camera-effect` (3×), `blog/iphone-17-dual-capture-limitations`, `blog/record-front-and-back-camera-samsung-galaxy`, `vs/dualcam` (8×).
17. **`듀얼카메라` / `듀얼 카메라` switching inside one page body.** `blog/dual-camera-effect` (14 closed / 2 spaced) and `blog/how-to-do-dual-camera-on-tiktok` (15 / 3). The closed form is fine in the title/H1/meta that targets "듀얼카메라 …". Body text should use one form, preferably `듀얼 카메라`. Low severity.

Not counted, but checked and OK: dates (all `2026년 11월 5일` style); no em dashes (only table `–` in `pricing`); `합니다/습니다` appears only inside verbatim quotes; `전면·후면` as our mode name is consistent on 37 pages; `PIP(화면 속 화면)` gloss consistent; `합치기(Combine)` consistent; `App Store` / `Google Play` never transliterated; `울트라 와이드` / `흔들림 보정` appear only in `blog/iphone-duo-camera` Apple spec context (allowed).

---

## 7. False friends and calque traps (this subject, Korean)

- **듀얼 카메라 ≠ front + back.** In Korean tech usage, 듀얼 카메라 very often means a phone's **two rear lenses** (Samsung KR svc 37685: "듀얼 카메라 기능: 2배 광학줌… 라이브 포커스"; AC: "듀얼카메라 광각렌즈", "듀얼 카메라 모듈", "듀얼 카메라 블랙 박스", "듀얼 카메라 스트랩"). Whenever you use 듀얼 카메라 for our concept, pair it with `전후면` / `전면과 후면` in the same title or first sentence.
- **듀얼 렌즈 (our mode) ≠ 듀얼 카메라.** ContentCam's 듀얼 렌즈 is wide + ultra-wide. Never translate "Dual Lens mode" as 듀얼 카메라, and never call 전면·후면 "듀얼 렌즈".
- **캡처 = screenshot** in everyday Korean (`듀얼모니터 캡처`, `캡처 도구`). Always write `Apple 듀얼 캡처` / `아이폰 듀얼 캡처` with `동영상` or `녹화` nearby so it reads as video. Spell it `캡처` (Apple + standard orthography), never `캡쳐`.
- **듀얼 alone** autocompletes to 듀얼심, 듀얼앱, 듀얼메신저, 듀얼넘버, 듀얼스크린. Never use bare `듀얼` except as Instagram's tool name.
- **PIP / 화면 속 화면** in search mostly means the **floating video window** (YouTube/Netflix PiP, "아이폰 pip 안됨"). For our layout, write `PIP 영상` / `PIP(화면 속 화면) 영상` or `작은 창`.
- **화면 분할** ("아이폰 화면 분할", "분할화면 종료") usually means split-screen **multitasking**. For video write `분할 화면 영상` / `화면 분할 영상` with 영상.
- **가로세로** alone = screen rotation / aspect setting (`갤럭시 가로세로 전환`, `가로세로 고정`) or, in Excel, freezing panes. Always add `동시 촬영` / `동시에 녹화`. **동시송출** = live simulcast streaming. That's not us; don't use it.
- **녹화 alone** often means **screen recording** (화면 녹화). In titles prefer `촬영` or `동영상 촬영` for camera recording ("아이폰 동영상 촬영 중 카메라 전환" is the real query).
- **포맷 ≠ aspect ratio.** Apple KR uses 포맷 for resolution/codec (HD, 4K, HEVC: "비디오 녹화 포맷"). Dual-format = `두 비율`, not `두 포맷` / `두 형식` / `듀얼 포맷`.
- **인물 사진** is Apple's Portrait photo mode (bokeh), not "portrait orientation". Portrait video = `세로 영상`.
- **메인 카메라** in Apple KR is the main rear lens (48MP Fusion). Don't use it for "rear camera" in general.
- **리뷰** also means app-store reviews. On pages that discuss store reviews, write `리뷰 화면` for ContentCam's Review screen so the two don't blur.
- **셀카 vs 셀피**: Koreans say 셀카. **어플**: commonly typed but reads informal. Write `앱`.
- **비디오 vs 영상 vs 동영상**: Apple KR's support guide uses 비디오 (mode name), Apple KR marketing and Samsung use 동영상, and our store copy uses 영상. Mirror Apple's label only when naming Apple's UI ("비디오 모드"); otherwise use 영상.
- **Combine → 합성** is a trap: 합성 implies compositing/photo manipulation (and 합성 사진 = faked photo). Use `합치기`.
- **Premium → 유료 버전**: OK as a plain description, but the feature tier name is `프리미엄`.
- **Lifetime → 영구 / 평생 소장**: avoid. Use `평생 이용권` (store).
- **Free trial → 무료 평가판** is Microsoft-style software wording. Use `무료 체험`.
- **Samsung naming changed**: 디렉터스 뷰 (older Galaxy) → 듀얼 레코딩 (newer). Both are real Korean search terms. Mention both on Samsung pages, with 듀얼 레코딩 first for current models.
- **"Front camera" vs 전면 카메라 mode**: ContentCam also has a mode literally named 전면 카메라 (single front camera, both ratios). When you mean front + back, don't shorten 전면·후면 to 전면.
