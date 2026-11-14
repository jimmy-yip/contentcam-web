# zh-hant terminology + style sheet (contentcam.app website)

Language folder `zh-hant`, `<html lang="zh-Hant">`, og:locale `zh_TW`. Written **Taiwan-first**; Hong Kong
readers get the same pages, so avoid Taiwan-only slang and note HK official names where they differ.
Never character-convert from `zh-hans` (no 視頻, 攝像頭, 豎屏, 分辨率, 幀率, 軟件, 設置, 屏幕, 保存, 文件夾).

Built 2026-11-15 from:
- Store copy (terminology authority): `~/contentcam/docs/store-descriptions/v2.8.2/desc/zh-Hant.txt` (cited `desc:N`)
  and the newer `v2.8.3/desc/zh-Hant.txt` (same terms, adds 小視窗 / 並排檢視 lines).
- Locked app glossary: `~/contentcam/docs/localization-glossary-zh-Hant.md` (cited `gloss`).
- Shipped in-app catalogue: `~/contentcam/ContentCam/ContentCam/Resources/Localizable.xcstrings`, zh-Hant column,
  608 of 734 strings translated (cited `app`). The iOS app UI is localized, so the Chinese mode names below are what
  Taiwan/HK users actually see on their buttons.
- `~/contentcam/docs/store-metadata-expansion.md` §5–6 (zh-Hant name/subtitle/keywords, gloss rules).
- `~/contentcam-web/tools/i18n/TRANSLATE-BRIEF.md` (row: zh-hant, "Taiwan vocabulary (影片, 鏡頭, 前後鏡頭)").
- Apple Taiwan and Hong Kong pages and Samsung Taiwan support pages fetched 2026-11-15 (URLs in §4).
- Google autocomplete, `hl=zh-TW&gl=tw` and `hl=zh-HK&gl=hk`, run 2026-11-15 (§5).
- A scan of all 23 pages under `~/contentcam-web/zh-hant/` (§6).

Confidence tags: **OFFICIAL** = Apple/Samsung's own localized page; **STORE** = our shipped store copy or app
strings; **AC** = Google autocomplete-verified; **CHOSEN** = editorial choice, native reviewer should attack first;
**UNVERIFIED** = could not confirm from a primary source.

---

## 1. Register, person form, typography

**Register: informal 你, never 您.** The store copy addresses the reader as 你 throughout (`desc:5`, "你的影片只會留在手機上";
`desc:30`, "整理你的每一次拍攝"), and the app catalogue does the same. The 23 existing pages use 你 197 times and 您 zero
times. Keep it. Tone is plain, friendly, spoken Taiwanese Mandarin (e.g. 一顆鏡頭吃下完整的 4:3 感光元件, 誰也不是誰的裁切版),
not formal brochure Chinese.

**Punctuation**
- Full-width punctuation in Chinese runs: ，。、：；！？（）「」『』. No half-width `, : ? ( )` touching Chinese characters.
- Quotes: 「」 for quotes and UI labels, 『』 for a quote inside a quote. **Never “ ” or " "** in Chinese prose
  (Taiwan and HK Apple both use 「」: 「相機」, 「雙向同拍」). When quoting English source text verbatim, still wrap
  it in 「」: 頁面標示「Contains Advertising」.
- UI labels and app names in 「」: 打開「相機」，選「錄影」. Store copy: 「照片」App (`desc:17`).
- Parenthetical glosses use full-width （） with no inner spaces: 前後鏡頭（Front/Back）, 使用條款（EULA）
  (store-metadata-expansion §6.3: "Traditional Chinese uses full-width （） with no spaces").
- Enumeration comma 、 between list items in a sentence: 曝光、白平衡、ISO、快門 (`desc:21`).
- Ellipsis ……, dash: avoid em dashes entirely (brief rule). Use ，or ：or rephrase. The store copy's " - " inside
  arrow lists (`desc:40`) is a list separator only; do not use it in prose.
- Range: 0.5 秒到 30 秒, 10 倍到 900 倍 (`desc:25`); in tables `24–60fps` is acceptable.

**Spacing (pangu rule, matches store copy)**
- One half-width space between Chinese and Latin letters/digits: `4K 影片`, `在 iPhone 上`, `iOS 18 或更新版本`,
  `用 ContentCam 拍` (`desc:3,20`). No space between a digit and a following full-width punctuation mark.
- No space next to full-width punctuation: `TikTok、Reels 和 YouTube` (`desc:1`).
- Units glued to digits as in store copy: `60fps`, `4:3`, `9:16`, `0.5x`, `1x` (`desc:20,27`). Existing pages also
  write `30 fps`; both occur in Apple TW copy. Prefer **`60fps`** in running text to match the store copy, but
  keep whatever a quoted source writes.
- Product names stay Latin and unspaced internally: ContentCam, iPhone 17 Pro, Galaxy S25, One UI 8.5, TikTok.

**Numbers and dates**
- Arabic numerals (half-width). No full-width digits.
- Dates: **`2026年11月12日`** (no spaces inside the date; normal pangu spacing applies only where the date
  touches a Latin word, e.g. `v2.9，2026年11月12日` or `Updated 2026年…` in a quote). 17 of 23 pages already
  use the tight form; the spaced form `2026 年 11 月 12 日` appears on 4 pages and should be normalised (§6).
- Version and model numbers unchanged: iOS 18, v2.9, iPhone XS.
- Counters: 一支影片 (video), 一顆鏡頭 (lens), 一段錄影 (recording), 兩張照片 (photo), 一個檔案 (file),
  一則評論 / 一則限時動態 (review / story), 一個 take (`gloss`).
- Currency: keep `US$` / `NT$` style exactly as the source gives it; never convert.

**Headings**
- Titles, H1, H2 phrased as the question a Taiwanese user types: `iPhone 怎麼前後鏡頭同時錄影？`,
  `Android 怎麼同時錄直式和橫式影片？`. End question headings with full-width ？. Keep the year as `（2026）`.

---

## 2. Mandated term table

| English concept | Use (zh-Hant) | Avoid / forbidden | Source, confidence |
|---|---|---|---|
| video (file) | **影片**; counter 支 | 視頻, 视频, 錄像, 片子 | STORE `desc:1`; brief |
| record (verb) / recording (act) | **錄影** / **錄**; 錄下 | 錄像, 录制; 錄製 only in formal Apple/Samsung quotes | STORE `desc:3,31`; app `Record`=錄影 |
| film / shoot | **拍**, **拍攝** | 攝製 | STORE `desc:1` 一次拍攝 |
| camera (device / app) | **相機**; Apple app = 「相機」 | 攝像頭, 攝影頭 | STORE; OFFICIAL Apple TW |
| camera (front/back unit, in prose) | **鏡頭**: 前鏡頭 / 後鏡頭 | 攝像頭, 前置攝像頭 | brief; AC (前鏡頭 後鏡頭) |
| front camera (ContentCam feature copy) | **自拍鏡頭** | — | STORE `desc:3,10` |
| back/main camera (ContentCam feature copy) | **主鏡頭** (or 後鏡頭 in search-facing text) | 後置攝像頭 | STORE `desc:3,10` |
| front / rear camera (UI, Apple context) | **前置相機 / 後置相機** | — | app `Front camera`, `BACK CAMERA`; OFFICIAL Apple TW. HK Apple uses 前置鏡頭 / 後置鏡頭 |
| front and back camera (concept, search) | **前後鏡頭** | 前後攝像頭, 前後置鏡頭, 雙向鏡頭 | STORE; AC (top suggestion) |
| record front and back at the same time | **前後鏡頭同時錄影** | 前後同步錄像, 雙重錄影 | AC (#1 suggestion for 前後鏡頭) |
| take photos front and back at once | **前後鏡頭同時拍照** | — | AC |
| portrait / vertical (video) | **直式** | 豎屏, 竖版, 直屏, 縱向; 直向 only in Apple UI names (直向鎖定) | STORE `desc:1`; app; AC (直式影片) |
| landscape / horizontal (video) | **橫式** | 橫屏, 横版; 橫向 only in Apple UI names | STORE `desc:1`; app; AC (橫式影片) |
| portrait and landscape at once | **同時錄直式和橫式影片** / 直式橫式同時錄影 | 橫豎屏同時錄製 (zh-Hans) | STORE `desc:1` 同時錄下直式和橫式影片; metadata name 直式橫式 |
| format (9:16 vs 16:9) | **格式** (兩種格式); **比例** / **畫面比例** in spec talk | 畫幅 (mainland), 雙畫面 | STORE `desc:1,11,20` |
| dual-format | **雙格式** / 兩種格式 | 雙畫面, 雙畫幅 | CHOSEN (used on 9 pages) |
| aspect ratio | **畫面比例** / 比例 | 長寬比 is OK in tech context only | CHOSEN |
| sensor | **感光元件** | 傳感器, 感測器 | STORE `desc:8` |
| crop | **裁切** / 裁出 | 裁剪, 剪裁 | STORE `desc:8` 裁出, 裁切版 |
| reframe | **重新構圖** | 二次構圖 | CHOSEN |
| frame (composition) | **構圖** | — | STORE v2.8.3 兩種構圖 |
| frame (single image) / frame rate | **影格** / **影格率** | 幀, 幀率, 帧率 | STORE `desc:20,32`; OFFICIAL Apple TW (HK Apple uses 格率) |
| resolution | **解析度** | 分辨率 (zh-Hans), 解像度 (HK Apple) | STORE `desc:20` |
| quality | **畫質** | 質素 (HK) | CHOSEN; Apple TW 高畫質格式 |
| HD / 4K | **HD / 4K** (Latin) | 高清 | STORE `desc:20` |
| picture-in-picture | **子母畫面**; the inset = **小視窗** | 畫中畫 (HK Apple + zh-Hans) | STORE `desc:3,10`; app; OFFICIAL Apple TW (使用「子母畫面」進行多工處理) |
| split screen | **分割畫面** | 分屏, 雙畫面 | STORE `desc:3`; app `Split`; AC |
| side-by-side view | **並排檢視** / 並排 | — | STORE v2.8.3, `desc:32` 並排播放 |
| two separate files | **兩個獨立檔案** | 兩個單獨文件 | STORE `desc:1,3` |
| file | **檔案** | 文件 (= document in TW) | STORE |
| folder | **資料夾** | 文件夾 | STORE `desc:31` |
| save | **存成 / 存進 / 儲存** | 保存 | STORE `desc:3,17`; app |
| export | **匯出** | 導出 | STORE `desc:30`; app |
| trim | **修剪** | 剪切, 裁剪 | STORE `desc:30,32` |
| edit (video editing) | **剪輯**; editing app = 剪輯 App / 剪輯軟體 | 編輯 (= text edit) | CHOSEN |
| post-production | **後製** | 後期 (mainland) | CHOSEN, Taiwan usage |
| combine (merge two files) | **合成**; result = 合成影片 | 合併, 拼接 | STORE `desc:3,10`; app `Combine`=合成 |
| take (the entity) | **take** (lowercase, untranslated), counter 個; "unlimited takes" = **take 不限次數** | 拍攝次數, 鏡次 | STORE `desc:17,30,37,40`; gloss |
| one take (slogan) | **一次拍攝** | — | STORE `desc:1` |
| project / scene | **專案 / 場景** | 項目 (mainland) | STORE `desc:30`; app |
| viewfinder | **觀景窗** | 取景框 (HK Apple), 取景器 | STORE `desc:22`; OFFICIAL Apple TW |
| preview | **預覽** | — | gloss (CHOSEN) |
| record button / shutter button | **錄影鍵 / 快門鈕** | 錄製鍵 | STORE `desc:15` |
| stabilisation | **防手震** | 防抖 (zh-Hans), 防震 (HK Apple) | STORE `desc:24`; app |
| teleprompter | **提詞機** | 提詞器 (zh-Hans) | STORE `desc:23`; app |
| timelapse | **縮時攝影** | 延時攝影 (zh-Hans) | STORE `desc:25`; app |
| manual controls | **手動控制** | 專業模式 | STORE `desc:21` |
| exposure / white balance / shutter / ISO | **曝光 / 白平衡 / 快門 / ISO** | — | STORE `desc:21` |
| zoom | **變焦** | 縮放 (only as Apple's 用兩指開合來縮放) | STORE `desc:27` |
| wide / ultra-wide / telephoto | **廣角 / 超廣角 / 望遠** | 長焦 (mainland) | STORE `desc:9`; app |
| overheating | **過熱** | 發燙 (informal OK in quotes) | STORE `desc:35` |
| watermark | **浮水印** | 水印 (zh-Hans) | STORE `desc:5` |
| ads | **廣告** | — | STORE `desc:5` |
| sign up / account | **註冊帳號** | 注冊, 賬號 | STORE `desc:37` |
| free / free version | **免費 / 免費版** | — | STORE `desc:5` |
| free trial | **免費試用** | — | STORE; gloss |
| Premium | **Premium** (Latin) | 高級版, 進階版, 專業版 | STORE `desc:5,52`; app |
| annual / monthly plan | **年訂閱 / 月訂閱**; verbs 按年 / 按月付費 | 年費 / 月費 in plan labels | app; STORE `desc:52` |
| lifetime | plan label **終身版**; prose **一次買斷、終身使用** | 永久會員, 一次性 (calque of one-time) | app `Lifetime`=終身版; STORE `desc:52` |
| subscription | **訂閱** | 訂購 | STORE |
| App (software) | **App** (capital A, Latin) | 應用, 應用程式 (OK only in formal Apple quotes), 軟件 | STORE `desc:17,34`; existing pages 773× |
| phone | **手機** | 手机, 電話 | STORE `desc:5` |
| creator | **創作者** | 博主 (mainland), 網紅 (only for influencer sense) | CHOSEN; store subtitle 創作者 |
| short-form video | **短影音** | 短視頻 (mainland) | STORE subtitle 短影音Vlog創作者; AC |
| Instagram Stories | **限時動態** (casual 限動) | 快拍 (mainland) | AC; widely used TW/HK |
| privacy line | 你的影片只會留在手機上 | — | STORE `desc:5` |
| iOS requirement | 需要 iOS 18 或更新版本 | iOS 18 以上 is acceptable in tables | STORE `desc:54` |

---

## 3. ContentCam mode and feature names (exact)

The iOS app UI is localized; these are the names on the buttons (app) and in the listing (STORE). Use the Chinese
name. On the **first mention per page**, you may add the English key in full-width parentheses, in exactly the
store-copy form below. Do not invent other glosses.

| English key in app | zh-Hant name (UI + store) | First-mention gloss form (store copy) | Source |
|---|---|---|---|
| Single Lens | **單鏡頭** (單鏡頭模式) | 單鏡頭（Single Lens） | `desc:8`; app |
| Dual Lens | **雙鏡頭** (雙鏡頭模式) = wide + ultra-wide, NOT front+back | 雙鏡頭（Dual Lens） | `desc:9,54`; app |
| Front & Back / Front/Back | **前後鏡頭** (前後鏡頭模式) | **前後鏡頭（Front/Back）** (not "Front & Back") | `desc:10`; app (both keys map to 前後鏡頭) |
| Front (selfie camera, dual-format) | **前鏡頭** | no gloss | `desc:11` |
| Portrait Only (landscape output off) | UI: **僅直式**; store prose: 一般相機 | no gloss | app `Portrait Only`; `desc:12` |
| Combine | **合成** (合成功能) | 合成（Combine） | `desc:10`; app |
| Photo mode / shutter | **拍照** (拍照模式), **快門鈕** | no gloss | `desc:14,15,43`; app `Photo`=照片 tab, `Take photo`=拍照 |
| Front/Back photo | **前後鏡頭拍照** | — | `desc:16` |
| Teleprompter | **提詞機** | 提詞機（Teleprompter） | `desc:23`; app |
| Timelapse | **縮時攝影** | 縮時攝影（Timelapse） | `desc:25`; app |
| Stabilisation / HDR | **防手震 / HDR** | — | `desc:24`; app |
| Overlays: level, crosshair, audio meter, grid | **輔助線**: 水平儀、中心十字線、音量表、格線 | — | `desc:26`; app |
| Zoom buttons / dial | 0.5x、1x、2x 按鈕, 雙指縮放, 轉盤 | — | `desc:27` |
| Projects, scenes and takes | **專案、場景和 take** | — | `desc:30` |
| Recording folder | **錄影資料夾** | — | `desc:31` |
| Review and trim | **檢視和修剪**, 檢視畫面 | — | `desc:32,49` |
| Storage estimate | **容量預估** | — | `desc:33` |
| Crash protection | **當機保護** | — | `desc:34` |
| Thermal monitoring | **溫度監控** | — | `desc:35` |
| Apple Log | **Apple Log** | — | v2.9 what's new; app |
| Library | **素材庫** | — | gloss (`v2.6.1`) |
| Favourite | **加入最愛** | — | `desc:30` |
| Picture-in-picture inset (Combine output) | **子母畫面**, inset **小視窗**; options 拖曳、調整大小、圓角、對調 | — | v2.8.3 `desc:10` |
| Live dual preview | 即時的子母畫面小視窗 / 並排檢視 | — | v2.8.3 |
| Premium unlock list | 升級 PREMIUM 解鎖 → … (no glosses in this list, by design) | — | `desc:39–50`; metadata §6.3 |
| App Store name / subtitle (for reference) | ContentCam：直式橫式雙鏡頭相機-前後同時錄影 / 短影音Vlog創作者必備：直向橫向兩支影片，一次搞定免重拍 | — | metadata §5 (note: the subtitle uses 直向橫向 for keyword reasons; website prose uses 直式橫式) |

Store-copy phrasings worth reusing verbatim: 一次拍攝，同時錄下直式和橫式影片 · 兩個獨立檔案 · 誰也不是誰的裁切版 ·
不論免費版或 Premium，都沒有廣告和浮水印 · 你的影片只會留在手機上 · 由獨立開發者 Jimmy 一個人打造.

---

## 4. Platform names

### Apple (iPhone, iOS)

| English | Taiwan (zh-TW) | Hong Kong (zh-HK) | Source |
|---|---|---|---|
| **Dual Capture** | **雙向同拍** | **雙向同步拍** | OFFICIAL: apple.com/tw/iphone/compare/ maps "Front Camera: Dual Capture" → 雙向同拍; support.apple.com/zh-tw/125089 (iPhone 17 tech specs) "雙向同拍，最高可達 4K 杜比視界 (30 fps)"; support.apple.com/zh-tw/guide/iphone/iph61f49e4bb/ios "錄製「雙向同拍」影片"; zh-hk equivalents say 雙向同步拍 |
| Dual Capture steps | 打開 iPhone 上的「相機」。選取「錄影」模式。點一下 [相機控制項圖像]，然後點一下「雙向同拍」。 | 選擇「錄影」模式。點一下 [圖像]，然後點一下「雙向同步拍」。 | OFFICIAL (same guide page). The icon is unlabeled in Apple's text; do NOT call it 「相機控制」 (see traps) |
| Dual Capture marketing line | 前後鏡頭同步開錄，將你自己和你所見的世界，一次盡收。 | 前後相機同步拍片，既可影自己，亦可同時錄下眼前一切。 | OFFICIAL apple.com/tw/iphone-17/, apple.com/hk/iphone-17/ |
| Center Stage (front camera) | Center Stage 前置相機; feature **人物居中** | Center Stage 前置相機; **人物置中** | OFFICIAL apple.com/tw/iphone-17/, support.apple.com/zh-tw/125089 |
| Ultra-stabilized video | 超穩定錄影 | 超防震攝錄 | OFFICIAL tech specs |
| Camera app | 「相機」 | 「相機」 | OFFICIAL |
| Video mode / Photo mode | 「錄影」 / 「拍照」 | 「錄影」 / 「影相」 | OFFICIAL guide |
| Record button | 「錄製」按鈕 | 「錄製」/「錄影」按鈕 | OFFICIAL guide |
| Cinematic / Slo-mo / Time-lapse / Action mode | 「電影級」/ 慢動作 / 縮時 / 「動作」模式 | 「電影效果」/ 慢動作 / 縮時 / 「動作」模式 | OFFICIAL guide |
| **Camera Control** (hardware button, iPhone 16+) | **「相機控制」** | 「相機控制」 | OFFICIAL guide topic 使用「相機控制」 |
| Settings > Camera > Record Video | 「設定」>「相機」>「錄影」 | 「設定」>「相機」>「錄製影片」 | OFFICIAL guide iph61f49e4bb |
| Settings > Camera > Formats | 「設定」>「相機」>「格式」 | same | OFFICIAL (guide mentions 格式); UNVERIFIED as exact menu row |
| Preserve Settings | 「保留設定」 | 「保留設定」 | OFFICIAL guide iph62000de98 |
| Mirror Front Camera | 「前置相機鏡像翻轉」 | 「鏡像前置鏡頭」 | OFFICIAL guide iph1b88429a6 |
| Record Stereo | 「錄製立體聲」 | 「錄製立體聲」 | OFFICIAL guide iphc1827d32f |
| Lens Correction | 「鏡頭校正」 | 「鏡頭校正」 | OFFICIAL guide iphb362b394e |
| Portrait Orientation Lock | 「直向鎖定」 | UNVERIFIED | used on site; Apple TW Control Center name, UNVERIFIED this session |
| Photos app / library | 「照片」 / 照片圖庫 | 「相片」 | STORE `desc:17`; HK Apple uses 相片 |
| Picture in Picture (iOS multitasking) | 「子母畫面」 | 畫中畫 | OFFICIAL guide TOC |
| Continuity Camera | 「接續互通相機」 | UNVERIFIED | used on vs/lookout; UNVERIFIED |
| Apple Account | Apple 帳號 | Apple 帳戶 (UNVERIFIED) | gloss |
| Supported models | 支援的機型 | 支援的型號 | OFFICIAL guide |

Notes: Taiwan is the default for the site. Do not write HK variants in body text; if an HK-specific clarification is
ever needed, add it once in parentheses: 雙向同拍（香港稱「雙向同步拍」）.

### Samsung (Galaxy, One UI)

| English | Taiwan (zh-TW) | Source / confidence |
|---|---|---|
| **Dual recording** | **雙鏡頭錄影** | OFFICIAL: samsung.com/tw/support/mobile-devices/how-to-use-the-dual-lens-camera-on-the-galaxy-s26-for-video-recording/ (updated 2026-03-24): "透過「雙鏡頭錄影」功能，掌鏡者可同步啟動前後鏡頭"; steps 開啟「相機」→「快速控制項」→「設定」→ 下載「Camera Assistant」→ 開啟「雙鏡頭錄影」→ 在「更多」中即會顯示 |
| **Director's View** | **最佳導演** | OFFICIAL: samsung.com/tw/support/mobile-devices/galaxy-z-fold4-camera-mode-description/ "最佳導演：預覽所有鏡頭，並透過前後鏡頭同步錄影"; news.samsung.com/tw S21 技術講座 ⑭ 最佳導演 (tagged Director's View) |
| Quick controls | **快速控制項** | OFFICIAL (S26 page above) |
| More (modes tray) | **「更多」** | OFFICIAL (S26 page above) |
| Single Take | **一鍵拍錄** | OFFICIAL (Fold4 modes page) |
| Camera Assistant | Camera Assistant (Latin) | OFFICIAL |
| Video mode | 「錄影」 | OFFICIAL |
| Hyperlapse | 縮時錄影 | OFFICIAL (Fold4 modes page) |
| Super slow-mo | 超慢動作攝影 | OFFICIAL (Fold4 modes page) |
| One UI 8.5 location of Dual recording (moved into Video mode quick controls) | UNVERIFIED in Samsung TW wording; the S26 TW page still describes the Camera Assistant → 「更多」 route | UNVERIFIED |
| Hong Kong names | UNVERIFIED (samsung.com/hk equivalents returned 404) | UNVERIFIED |

Brand: write **三星 Galaxy** or **Samsung Galaxy**; both are common in Taiwan. Headings already use 三星 Galaxy; keep it.

### Google

| English | zh-TW | Confidence |
|---|---|---|
| Pixel Camera | Pixel 相機 | UNVERIFIED |
| Google Play / Play 商店 | Google Play | Latin brand, fine |
| Android | Android | — |

### Instagram, TikTok, YouTube, Snapchat

| English | zh-TW | Confidence |
|---|---|---|
| Instagram Stories | **限時動態** (限動) | AC + common usage; in-app label UNVERIFIED this session |
| Reels | **Reels** | STORE `desc:1`; IG TW keeps Latin |
| Instagram Dual camera (Stories/Reels) | **「前後雙拍」** reported as the zh-TW in-app label | UNVERIFIED (one 2023 third-party Taiwanese tutorial, jyes.com.tw; not confirmed in-app). Until verified, write Instagram 的 Dual（前後鏡頭）功能 or Instagram 的前後鏡頭功能, not a bare invented name |
| TikTok / 抖音 | **TikTok** (Taiwan/HK app is TikTok, not 抖音) | STORE `desc:1` |
| TikTok Duet / Green Screen | 合拍 / 綠幕 | UNVERIFIED |
| YouTube Shorts | **Shorts** / YouTube Shorts | STORE-adjacent; common |
| Snapchat Dual Camera | Snapchat 的 Dual Camera（雙鏡頭） | UNVERIFIED in-app name; see trap on 雙鏡頭 collision |
| BeReal | BeReal | — |

---

## 5. Native search phrasing (autocomplete-verified 2026-11-15)

Front and back camera (the big one). `前後鏡頭` autocompletes, in order: **前後鏡頭同時錄影**, **前後鏡頭同時拍照**,
前後鏡頭, 前後鏡頭行車記錄器 (dashcam noise), 前後鏡頭一起錄影, 前後鏡頭錄影, **前後鏡頭app**, 前後鏡頭拍攝, 前後鏡頭拍照.
`前後鏡頭同時錄影` → 前後鏡頭同時錄影app · 前後鏡頭同時錄影 iphone · 前後鏡頭同時錄影 三星 · android 前後鏡頭同時錄影 ·
pixel 前後鏡頭同時錄影. Also: iphone前後鏡頭同時錄影, iphone 前後鏡頭同時拍照, iphone17 前後鏡頭同時拍照,
三星前後鏡頭同時錄影, 前後同時錄影 iphone, iphone 前後攝影, 前鏡頭 後鏡頭 (差別).
Same results under zh-HK; HK also suggests 前後相機 / iphone 前後相機.

Dual camera. `雙鏡頭` → **雙鏡頭錄影**, 雙鏡頭監視器/行車紀錄器 (noise), 雙鏡頭拍照, 雙鏡頭攝影機, **雙鏡頭錄影app**.
`雙鏡頭錄影` → 雙鏡頭錄影app · 雙鏡頭錄影iphone · 雙鏡頭錄影 三星 · 雙鏡頭錄影 手機 · 雙鏡頭錄影 ig · samsung 雙鏡頭錄影 ·
iphone17 雙鏡頭錄影 · s23u 雙鏡頭錄影. `iphone 雙鏡頭錄影` → iphone 17 / 17 pro / 16 雙鏡頭錄影. `ig 雙鏡頭` →
ig 雙鏡頭特效 · ig 雙鏡頭 濾鏡 · ig 雙鏡頭拍攝. `pixel 雙鏡頭` → pixel 雙鏡頭錄影. `三星 雙鏡頭` → 三星 雙鏡頭錄影.
**Searchers use 雙鏡頭 to mean front + back.** That is a different meaning from ContentCam's 雙鏡頭（Dual Lens） mode.
`雙拍` → iphone 雙拍, iphone17 雙拍, ig 雙拍. `雙錄` → iphone 雙錄影 (mostly insurance noise). `雙攝影` → iphone 雙攝影.

Apple Dual Capture. `雙向同拍` → **雙向同拍 iphone** · 雙向同拍錄影 · 雙向同拍 拍照 · 雙向同拍iphone16 · 雙向同拍三星 ·
雙向同拍 app · 雙向同拍 英文 · iphone17 雙向同拍 · 17pro 雙向同拍. `iphone 雙向同拍` → iphone 17 / 17 pro / 16 / 16 pro /
air 雙向同拍. The unofficial `雙重拍攝` also autocompletes (雙重拍攝 iphone, 雙重拍攝 app, i17 雙重拍攝, iphone 雙重拍攝功能)
but is polluted with Canon (canon 雙重拍攝, r5ii 雙重拍攝). `雙向同步拍` (HK official) returned no suggestions.

Portrait + landscape. No combined phrase autocompletes (同時錄直式, 直式橫式同時, 直式 橫式 同時錄影 all empty): the
need exists but people do not phrase it as one query yet. What does autocomplete: **直式影片** (尺寸, 轉橫式, 比例, 剪輯,
英文), **橫式影片** (轉直式, 尺寸, 比例, ig, reels), **橫式轉直式** / 橫式轉直式影片, 直式影片轉橫式capcut, ig 直式橫式,
iphone 直拍橫拍, reels 直式. 直向/橫向 autocomplete mostly as Word/iPad orientation, not video. **Use 直式 / 橫式 in titles**;
pair them with 影片 and a platform (TikTok、Reels、YouTube) to catch 直式影片轉橫式 intent.

Split screen / PiP. `分割畫面` → 分割畫面 手機, 分割畫面 iphone, 分割畫面 三星 (mostly multitasking intent); `分割畫面影片`
and `分割畫面 錄影` empty. `子母畫面` → settings/YouTube/Chrome (multitasking intent); `iphone 子母畫面錄影` exists.
`雙畫面` → 雙畫面設定, 雙畫面螢幕, iphone 錄影 雙畫面 (split-screen / dual monitor intent). HK: 畫中畫 and 分屏 also
autocomplete (HK/mainland-style), but stay with 子母畫面 / 分割畫面 for the Taiwan-first site.

Recommended title/H2 patterns (verified heads):
- iPhone 怎麼前後鏡頭同時錄影？ / 前後鏡頭同時錄影 App 推薦（2026）
- 三星 Galaxy 前後鏡頭怎麼同時錄影？ / 三星雙鏡頭錄影怎麼開？
- iPhone 雙向同拍怎麼用？哪些 iPhone 有雙向同拍？
- 前後鏡頭同時拍照
- iPhone 怎麼同時錄直式和橫式影片？ / 直式影片和橫式影片一次拍好
- 雙鏡頭錄影 App (only when the page is about front+back recording)

---

## 6. Inconsistencies found across the existing zh-hant pages (16)

Counts are occurrences in visible text + JSON-LD, scanned 2026-11-15. Page paths are relative to `zh-hant/`.

1. **Apple Dual Capture called 雙重拍攝 (unofficial) instead of Apple's 雙向同拍.** Right: **雙向同拍（Dual Capture）** on
   first mention, then 雙向同拍. 雙向同拍 appears 0 times on the site. 雙重拍攝 appears 89×: blog/iphone-17-dual-capture-limitations (42,
   incl. title/H1/H2s), blog/dual-camera-effect (17), blog/record-front-and-back-camera-same-time-iphone (11), vs/apple-dual-capture (9,
   incl. title/H1), index.html (3), vs/index.html (3), vs/lookout (2), vs/dualgram (1), blog/record-front-and-back-camera-same-time-android (1).
   Optional: mention once that some people call it 雙重拍攝, for the secondary search term.
2. **Apple's on-screen label quoted wrong.** Step instructions say 點「雙重拍攝」; the iPhone button reads 「雙向同拍」 (TW) / 「雙向同步拍」 (HK).
   A reader looking for 「雙重拍攝」 will not find it. Pages: blog/record-front-and-back-camera-same-time-iphone, blog/dual-camera-effect,
   blog/iphone-17-dual-capture-limitations.
3. **Bare English "Apple Dual Capture" used as the Chinese name.** vs/apple-dual-capture H2s (主要差在哪裡? etc., 53× Dual Capture),
   blog/best-front-and-back-dual-camera-apps (7), blog/take-photo-front-and-back-camera-same-time (10), blog/record-portrait-and-landscape-video-same-time-iphone (1),
   blog/record-front-and-back-camera-same-time-iphone (Dual Capture 會存成一支影片). Right: 雙向同拍, English only in the first-mention gloss.
4. **"相機控制按鈕" in the Dual Capture steps.** In Taiwan/HK iOS, 「相機控制」 is the name of the hardware **Camera Control** button
   (iPhone 16+), so "點一下相機控制按鈕" tells readers to press the wrong thing. Apple's own text says 點一下 [圖像]. Write
   點一下畫面上方的相機控制項圖示 or describe the icon. Pages: blog/record-front-and-back-camera-same-time-iphone, blog/dual-camera-effect,
   blog/iphone-17-dual-capture-limitations (相機、錄影模式、相機控制、雙重拍攝), vs/apple-dual-capture (錄影模式、相機控制、Dual Capture).
5. **Samsung Dual recording called 雙重錄影; Samsung Taiwan calls it 「雙鏡頭錄影」.** 40×: blog/record-front-and-back-camera-samsung-galaxy (29,
   incl. H2s and the FAQ step 點「雙重錄影」), blog/record-front-and-back-camera-same-time-android (11, incl. H2). It is also what Taiwanese users
   type (雙鏡頭錄影 三星 / samsung 雙鏡頭錄影 autocomplete; 雙重錄影 only gives "iphone 雙重錄影").
6. **Samsung Director's View called 導演視角; Samsung Taiwan calls it 「最佳導演」.** 16×: blog/record-front-and-back-camera-samsung-galaxy (14,
   incl. title-adjacent H2 "Galaxy S24 和 S25 的導演視角跑去哪了？"), blog/record-front-and-back-camera-same-time-android (2, incl. H2).
   Write 最佳導演（Director's View）on first mention.
7. **Samsung "Quick controls" written 快速控制; Samsung Taiwan writes 「快速控制項」** and puts UI labels in 「」. 5×: blog/record-front-and-back-camera-samsung-galaxy (4),
   blog/record-front-and-back-camera-same-time-android (1).
8. **Mode gloss form split.** Store copy: 前後鏡頭（Front/Back）. Site: 前後鏡頭（Front & Back） 11× on 10 pages (blog/dual-format-recording-apps-compared ×2,
   blog/record-portrait-and-landscape-video-same-time-android, vs/2cam, vs/apple-dual-capture, vs/detail, vs/dualgram, vs/dualtake, vs/index, vs/lookout,
   vs/mixcam) vs （Front/Back） on 3 pages (blog/best-front-and-back-dual-camera-apps, blog/take-photo-front-and-back-camera-same-time, vs/dualcam).
   Right: （Front/Back）.
9. **Snapchat's feature glossed 雙鏡頭（Dual Camera）**, colliding with ContentCam's 雙鏡頭（Dual Lens） on the same site:
   blog/record-front-and-back-camera-same-time-iphone. Right: Snapchat 的 Dual Camera（前後鏡頭）功能.
10. **Generic 雙鏡頭 (= front+back) mixed with ContentCam's 雙鏡頭 mode (= wide+ultra-wide) without disambiguation.**
    - features/dual-camera: `<title>` "iPhone 雙鏡頭同時錄影：直式橫式一次拍" and JSON-LD name "雙格式與雙鏡頭錄影". The page is about Single Lens / Dual Lens
      dual-format recording; Taiwanese searchers read 雙鏡頭錄影 as front+back (autocomplete §5), so the title promises the wrong thing.
      Better: iPhone 同時錄直式和橫式影片：單鏡頭和雙鏡頭模式 - ContentCam.
    - vs/dualtake: "iPhone 上 5 次雙鏡頭錄影和 5 次前後鏡頭錄影" is fine only if it means Dual Lens; add 雙鏡頭（Dual Lens） or 廣角＋超廣角.
    - Titles that use 雙鏡頭相機 App for front+back apps (vs/index, vs/dualtake, blog/best-front-and-back-dual-camera-apps, internal link texts on vs/2cam,
      vs/detail, vs/dualgram) are acceptable as search phrasing, but the body must say 前後鏡頭 when it means front+back.
11. **Instagram's feature named three ways:** Instagram 的 Dual (blog/dual-camera-effect, blog/take-photo-front-and-back-camera-same-time),
    Instagram 的雙鏡頭 / 雙鏡頭功能 (blog/dual-camera-effect H2, blog/record-front-and-back-camera-same-time-android). Pick one:
    Instagram 的 Dual（前後鏡頭）功能 until the zh-TW in-app label (reportedly 前後雙拍) is verified.
12. **take translated as 拍攝次數** where the store copy keeps take: blog/dual-format-recording-apps-compared (專案、場景、拍攝次數、自動檔名; 拍攝次數不限 ×2),
    blog/record-portrait-and-landscape-video-same-time-android (拍攝次數不限). Right: 專案、場景和 take; take 不限次數 (`desc:30,37`).
13. **雙畫面 used to mean "two aspect ratios".** blog/dual-format-recording-apps-compared (11×: 雙畫面比例錄影 App, breadcrumb, JSON-LD, H2
    "關於雙畫面比例 App"), blog/film-for-tiktok-and-youtube-at-the-same-time (1×). In Taiwan 雙畫面 means split screen / dual display (autocomplete:
    雙畫面設定, 雙畫面螢幕). Right: 雙格式 / 直式橫式同時錄影 App.
14. **Date format split.** Tight 2026年11月5日 on 17 pages; spaced 2026 年 11 月 5 日 on android (1), blog/record-front-and-back-camera-same-time-iphone (4, byline),
    vs/dualcam (12), vs/dualgram (11, mixed with 9 tight). Right: tight form (§1).
15. **Curly quotes in Chinese prose:** blog/dual-format-recording-apps-compared (“Front or back camera, your call”, “Contains Advertising”). Right: 「」.
16. **Lifetime plan named inconsistently:** 終身 (57×), 買斷 (61×), 一次性買斷 / 一次性價格 (blog/dual-format-recording-apps-compared, 3×). Right: plan label 終身版,
    prose 一次買斷、終身使用 (app + `desc:52`); drop 一次性 (calque). Minor; rival pricing may keep the rival's own wording in quotes.

Also noted, not counted as errors: one missing CJK/Latin space on vs/dualcam (步驟在iPhone); 自拍鏡頭/主鏡頭 (store copy) and 前鏡頭/後鏡頭 (search
phrasing) coexist, which is fine (feature copy vs search copy); 直向 appears once, inside Apple's own name 「直向鎖定」, which is correct; 前置相機 on
vs/apple-dual-capture is Apple's own term, correct.

---

## 7. False friends and calque traps

- **雙鏡頭 has two meanings.** In search and on Samsung (雙鏡頭錄影) and Instagram, 雙鏡頭 = front + back. In ContentCam, 雙鏡頭（Dual Lens） =
  wide + ultra-wide on the back. Never write "ContentCam 的雙鏡頭模式" in a sentence about front+back recording. Front+back = 前後鏡頭.
- **Dual Capture ≠ 雙重拍攝.** 雙重 = "double/duplicate" (雙重曝光 = double exposure, 雙重國籍). Apple TW chose 雙向同拍 ("two-direction
  simultaneous shooting"). 雙重拍攝 also collides with Canon's dual-shooting feature in search.
- **Dual recording ≠ 雙重錄影.** Samsung TW: 雙鏡頭錄影. Same calque problem.
- **Director's View ≠ 導演視角.** Samsung TW: 最佳導演. 導演視角 is a literal translation readers will not find in the camera.
- **「相機控制」 is a button name** (Camera Control hardware button). Do not use it for "camera controls" UI icons; for ContentCam's manual
  controls say 手動控制 (store copy), not 相機控制.
- **文件 ≠ file.** In Taiwan 文件 = document (Apple 說明文件, 參考文件 are fine). A video file is 檔案. Folder is 資料夾, not 文件夾.
- **直向/橫向 vs 直式/橫式.** 直向/橫向 is device orientation (Word, iPad, Apple's 直向鎖定). Video format is 直式/橫式 (store copy, app UI,
  autocomplete 直式影片 / 橫式影片). The App Store subtitle's 直向橫向 is a keyword choice, not a website style.
- **豎屏/橫屏/竖版** are mainland; they read as Simplified-converted text in Taiwan. Same for 視頻, 攝像頭, 分辨率, 幀率, 防抖, 提詞器, 延時攝影,
  水印, 導出, 保存, 設置, 屏幕, 軟件, 博主, 後期, 長焦.
- **畫中畫 vs 子母畫面.** 畫中畫 is mainland and HK; Taiwan Apple uses 子母畫面. Use 子母畫面.
- **雙畫面** = split screen / dual monitor, not "two formats".
- **分割畫面** in searches mostly means phone multitasking split screen; when you mean the video layout, say 分割畫面的影片 / 上下分割的影片.
- **錄製 vs 錄影.** 錄製 is formal/written (Apple's 「錄製」按鈕, Samsung quotes). Default to 錄影 / 錄 in our voice.
- **一次性** (calque of "one-time") reads as "disposable". Use 一次買斷.
- **Take** is not 鏡次 (film-set jargon) or 拍攝次數 ("number of shoots"). Keep take (store copy, app).
- **主鏡頭** in store copy = the back camera. In Apple TW marketing 融合主相機 = the 1x main lens. In Apple-specific spec sentences say 後置相機
  or 廣角 to avoid implying the 1x lens only.
- **前置/後置** are fine but stiff in prose; 前鏡頭/後鏡頭 is how people search. Use 前置相機/後置相機 only in Apple/UI contexts.
- **影片 vs 視訊.** 視訊 = video call (Apple 視訊通話). A recording is 影片.
- **相片 vs 照片.** 相片 is HK Apple. Taiwan: 照片 (store copy 「照片」App).
- **免費 vs 免費試用.** 免費 = free tier (forever). 免費試用 = Premium trial. Do not mix.
- **Premium** stays Latin; 高級版 / 專業版 imply a different product tier.
- **抖音** is the mainland app; TikTok in Taiwan/HK is TikTok.
- **Literal heading calques to avoid:** "如何…" chains (如何如何同時錄製…) and "…的終極指南". Taiwanese users type 怎麼…？ and …推薦.
