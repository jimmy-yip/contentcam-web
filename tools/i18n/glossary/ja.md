# contentcam.app: Japanese (`ja`) terminology and style sheet

Built 2026-11-15 for native reviewers of every page under `/ja/`. Where this sheet and a page disagree, the sheet wins. Where this sheet and the shipped store copy disagree on a ContentCam feature name, the store copy wins; tell us so we can fix the sheet.

**Sources, in priority order**
1. Store copy (terminology authority for ContentCam's own names): `~/contentcam/docs/store-descriptions/v2.8.2/desc/ja.txt` (App Store) and `v2.8.2/play-2.8.2-merged.json` → `ja-JP` (Google Play).
2. The shipped app UI strings (`ContentCam/Resources/Localizable.xcstrings`, `ja`), cited below as "app UI".
3. `~/contentcam/docs/localization-glossary-ja.md` (the app glossary: register, counters, typography, traps). This sheet does not repeat all of it. Read it once.
4. `~/contentcam/docs/store-metadata-expansion.md` (ja title/subtitle and the 18-term keyword field).
5. Official local pages, fetched 2026-11-15: Apple Japan iPhone User Guide, Meta Japan newsroom, Apple iMovie JP guide, au (KDDI) Galaxy manuals for Samsung's Japanese menu names.
6. Google autocomplete with `hl=ja`, run 2026-11-15 (section 5).

Confidence labels: **verified** (seen in a source above, cited), **store** (in the shipped store copy), **app UI**, **chosen** (our decision, no external attestation), **unverified**.

---

## 1. Register, person form, typography

### Register
- **です・ます throughout body prose, FAQ answers, meta descriptions and JSON-LD text.** This matches the store copy ("同時録画できます", "必要ありません") and the app glossary. Never だ・である as a sentence style, never casual endings (〜だよ, 〜ね), never 謙譲語 chains (〜させていただきます).
  - Nominalised 「〜であること」 inside a です・ます sentence is fine (three pages use it correctly).
- **Titles, H2s, table cells, buttons, nav: noun form (体言止め) or a question.** Titles are phrased as the search query: 「〜する方法」, 「〜できる？」, 「〜は？」, 「〜アプリ比較」. No 。 at the end of a title, H2, nav item or table cell.
- **Honorifics only on the reader's side:** お使いのiPhone, ご要望, ご購入. Never on ContentCam's or Jimmy's actions.
- **Person form: drop the pronoun.** Japanese omits "you". あなた is allowed only in the store's hero construction 「あなたのリアクションと目の前の光景」 (store copy v2.5 line 8, now used on `/ja/`, `/ja/features/`, `/ja/features/dual-camera/`). Do not add あなた elsewhere. Where English says "your face", write 自分の顔 or 顔.
- **First person for the author voice (byline, disclosure boxes): 私.** Byline form already shipped: 「文：Jimmy（ContentCam開発者）· 2026年10月6日 · 2026年11月5日更新」. Disclosure box: 「お断り：私はContentCamの開発者なので、中立ではありません。」 (Pages currently use お断り and おことわり both; use **お断り**.)

### Typography (the app glossary's rules apply to web copy too)
- **Digits and Latin are half-width.** 4K, 60fps, 9:16, iPhone 17. Never ４Ｋ. (No full-width digits found on any ja page.)
- **No ASCII space between Japanese and adjacent Latin/digits:** 「iPhoneで4K録画」, 「ContentCamの前後カメラ」. Keep spaces inside a Latin run: 「iPhone 17 Pro Max」, 「ContentCam Premium」, 「One UI 8.5」.
- **Full-width punctuation:** 、。：（）「」？！. Half-width ( ) only inside an all-Latin run (none found misused).
- **Quotes:** 「」 for UI labels, app names of Apple's built-in apps and quoted Japanese. 『』 for a quote inside a quote. When quoting an English source verbatim, keep the English in 「」 followed by a Japanese gloss in （）, as the pages already do: 「Save to your device in 4K, 1080p, or 720p」（4K、1080p、720pで端末に保存）.
- **Ranges:** full-width wave dash 〜 (「0.5秒〜30秒」, 「2025年1月〜2026年9月」). Never ~ or -.
- **Lists of short items:** 中黒 ・ (「24・30・60fps」, 「iPhone 15・16」).
- **No em dash (—) and no en dash (–) in Japanese text.** Recast with 、 ： or a new sentence. In comparison tables an empty cell is 「なし」 or 「×」, not a dash.
- **Numbers:** half-width period for decimals (4.8), half-width comma for thousands (1,200万画素 / 4,300件). Japanese units after the number with no space: 30秒, 5回, 2本, 2枚, 7日間.
- **Dates:** 2026年11月15日 (no zero padding, no weekday). Month ranges 2026年6月24日〜11月1日. Already consistent across all ja pages.
- **Prices:** keep the source currency notation exactly as given (US$2.99, 22.99米ドル both appear; prefer **US$2.99** in tables and 「22.99米ドル」 in prose). Never convert to yen.
- **Counters:** 本 for video files (動画2本, ファイル2本), 枚 for photos, 件 for reviews/records (23件のレビュー), 回 for recordings allowed (5回まで無料), 機種 for phone models (全7機種), 台 for physical devices (2台目の端末).

---

## 2. Mandated term table

| English concept | Use | Avoid | Source / confidence |
|---|---|---|---|
| front camera (hardware) | **インカメラ** | フロントカメラ (that is the mode name, see §3), 前面カメラ*, 自撮りカメラ, セルフィーカメラ, 内カメ | store: 「インカメラと背面カメラを同時に録画」; app UI 'Front camera' → インカメラ. *前面カメラ only when quoting Apple or Meta JP, who use it (verified, Apple JP guide; Meta JP newsroom) |
| back / rear camera (hardware) | **背面カメラ** in body; **外カメラ** allowed in titles/H2/FAQ questions paired as 「インカメラと外カメラ」 | リアカメラ, バックカメラ (both autocomplete as car parts), アウトカメラ, 後面カメラ | store + app UI 'BACK CAMERA' → 背面カメラ; Apple JP uses 背面カメラ (verified). 外カメラ: autocomplete (§5) |
| both cameras at once | **インカメラと背面カメラを同時に** / 前後のカメラを同時に | 両側カメラ, ダブルカメラ (toy trains on autocomplete) | store |
| record front and back at the same time (search phrase) | **インカメラと外カメラを同時に録画** / 前後同時撮影 | literal 「前と後ろのカメラ」 | autocomplete (§5) |
| dual camera (generic category) | **デュアルカメラ** | ダブルカメラ, 二眼/2眼 (spec jargon, means a two-lens phone) | autocomplete: 「デュアルカメラ アプリ」, 「iphone デュアルカメラ アプリ」. Note 「デュアルカメラ」 alone also autocompletes to a car brake-assist feature, so always pair it with アプリ / iPhone / 動画 in titles |
| record (video) | **録画** | 録音 (audio), 収録 (only for broadcast/podcast sense) | store |
| shoot / film (the activity), take a photo | **撮影** / 撮る | | store 「撮影は1回、動画は2本」 |
| video | **動画** | ビデオ, except inside Apple's own labels: 「ビデオ」モード, デュアルキャプチャビデオ, HDRビデオ | store; Apple JP guide (verified) |
| photo | **写真** | | store |
| portrait video / landscape video | **縦動画 / 横動画**; as a pair 「縦と横」, chips 縦 / 横, 「縦＋横」 | ポートレート / ランドスケープ (Portrait mode and scenery), 縦型/横型, 縦長/横長 as the feature name (縦長/横長 fine for describing a frame shape) | store 「縦と横を同時に録画」; app UI 'Portrait' → 縦 |
| portrait + landscape at once | **縦と横を同時に録画** / **縦横同時撮影** (search form) | 縦横両方向同時 | store; autocomplete 「縦横同時撮影 アプリ」, 「縦動画 横動画 同時撮影」 |
| orientation of the phone (holding it) | 縦向き / 横向き | | app UI 「縦向き優先のレイアウト」 |
| aspect ratio | **比率**; アスペクト比 in technical rows; Samsung's own label 縦横比 only when citing Samsung | 画面比率 | store 「2つの比率に切り出します」 |
| file (output) | **ファイル**; 「独立した2つのファイル」, 「別々の2つのファイル」 | | store |
| picture in picture (layout) | **ワイプ（ピクチャ・イン・ピクチャ）** on first mention, then **ワイプ** | PiP, ピクチャーインピクチャー; 小窓 is fine in descriptive prose but not as the layout name | store; app UI 'Picture in picture' → ワイプ. Apple writes ピクチャインピクチャ (no dots) for iMovie; use Apple's form only when naming the iMovie feature (verified) |
| split screen (layout) | **画面分割** | 分割画面, スプリット (except iMovie's label, below) | store; app UI 'Split' → 画面分割. Autocomplete 「画面分割 動画」 is far stronger than 「分割画面 動画」 |
| combine (merge the two files into one video) | **合成** (verb 合成する; 「ひとつの動画に合成」) | マージ, 結合, 合成（Combine） | store; app UI 'Combine' → 合成, 'Combine Front & Back' → 前後カメラを合成 |
| composite editor | **合成エディタ** | | existing pages (chosen) |
| stabilisation | **手ぶれ補正** | 手ブレ補正, 手振れ補正 (Samsung's own label 「動画手振れ補正」 only when citing Samsung) | Apple JP guide 「手ぶれ補正（拡張）」 (verified); Google autocomplete rewrites 手ブレ補正 → 手ぶれ補正; app glossary locks it. NOTE: the v2.8.2 store copy and keyword field still say 手ブレ補正 (store defect, see §6) |
| level / horizon guide (ContentCam's) | **水準器** | レベル, 水平器 for ContentCam's own guide | store 「水準器、中央の十字線」. Apple's iOS setting is 「水平」 and its guide says 水平器 (verified): use those only for Apple's camera |
| grid | **グリッド** | 格子 | store (Play), Apple JP 「グリッド」 (verified) |
| preview / viewfinder | **プレビュー** | ファインダー | store; app glossary trap |
| teleprompter | **テレプロンプター**; カンペ allowed once as a search synonym (「カンペアプリ」) | プロンプター alone | store; keyword field has カンペ; autocomplete 「カンペ アプリ」 |
| script (teleprompter text) | **台本** | スクリプト | store |
| take | **テイク** | カット, ショット | store |
| trim | **トリミング** | カット編集 | store |
| crop (reframing after the fact) | **クロップ** / 切り出し / 切り取り | トリミング for crop | store keeps them separate |
| export | **書き出し** | エクスポート | store |
| lifetime / one-time purchase | **買い切り** | ライフタイム, 永久ライセンス, 永久 | store 「年額・月額・買い切り」; autocomplete 「買い切り カメラアプリ」 |
| annual / monthly / weekly plan | **年額 / 月額 / 週額** (年額プラン etc.) | 年間, 毎月 | store |
| free trial | **無料トライアル** (「7日間の無料トライアル」) | 無料体験, お試し期間 | app UI 「7日間の無料トライアル」 |
| subscription | **サブスクリプション** in prose; サブスク in titles and casual search phrasing | | app glossary; both used on pages |
| free version | **無料版** | フリー版 | store |
| ads / watermark | 広告 / **ウォーターマーク** | 透かし, ロゴ入り | store |
| the device | **iPhone** in iOS-only contexts, **スマホ** for cross-platform prose, **Androidスマホ**, 端末 only in spec/compatibility sentences (Play copy uses it that way) | デバイス in prose, スマートフォン (stiff; fine in legal/pricing text) | store (App Store and Play) |
| Apple's built-in Camera app | **「カメラ」アプリ** | カメラApp, 純正カメラアプリ, 標準カメラ (for Android, 標準カメラアプリ is fine) | Apple JP guide 「iPhoneで「カメラ」を開きます」 (verified) |
| Photos app | **「写真」アプリ** (Android: ギャラリー / Googleフォト) | 写真アプリ without brackets, カメラロール (retired; only when quoting another app's UI) | store; app glossary |
| Settings app path | 「設定」＞「カメラ」＞「ビデオ撮影」 | > (ASCII) | Apple JP guide (verified) |
| Apple's user guide | **iPhoneユーザガイド** | ユーザーガイド (when naming Apple's document) | Apple JP (verified) |
| reaction video | **リアクション動画** | | keyword field; autocomplete |
| creator | **クリエイター** | クリエーター | keyword field |
| short-form video | **ショート動画** | | keyword field |
| tested by the author | 「テスト済み」, 「〜で確認しました」 | | existing pages |

---

## 3. ContentCam mode and feature names (exactly as the store copy writes them)

The brief rule: gloss the English mode name in full-width parentheses the way the store copy does, on the **first mention per page and in titles/headers where the mode is named**; plain Japanese afterwards is fine.

| English | Website form | Notes / source |
|---|---|---|
| Front/Back (mode) | **前後カメラ（Front/Back）**, then 前後カメラ | App Store copy uses （Front/Back）. Play copy uses （Front & Back）. **Website: always （Front/Back）**, including the Android page, so all pages agree. As a mode noun: 「前後カメラ（Front/Back）モード」 |
| Single Lens | **シングルレンズ（Single Lens）** | store. (The app's switcher pill says 1レンズ; never use the pill form on the site) |
| Dual Lens | **デュアルレンズ（Dual Lens）** | store. iPhone only; requires an ultra-wide camera |
| Front Camera (mode) | **フロントカメラ** | store; no gloss. This is the only place フロントカメラ is right for ContentCam |
| Standard / portrait-only camera | **通常カメラ** | store 「通常カメラ：横をオフにすると、縦の動画1本だけを」 |
| Photo mode | **写真モード** | store |
| Combine (Premium) | **合成**; 「前後カメラ（Front/Back）の録画をひとつの動画に合成」 | store. No （Combine） gloss: it is not a mode name in the store copy |
| layouts inside Combine | **ワイプ（ピクチャ・イン・ピクチャ）** / **画面分割** | store; Play adds 「画面分割（2画面）」; site may use either |
| Timelapse | **タイムラプス** | store |
| Teleprompter | **テレプロンプター** | store |
| Manual controls | **手動コントロール**：露出、ホワイトバランス、ISO、シャッター | store |
| Background blur (Android, beta) | **背景ぼかし（ベータ版）** | Play |
| AE/AF lock | **AE/AFロック** | Play |
| Focus & exposure | フォーカスと露出 | store |
| Guides | **ガイド表示**：水準器、中央の十字線、オーディオメーター (Play adds 構図用のグリッド) | store |
| Zoom | ズーム：0.5x・1x・2xのボタン、ピンチ操作、ダイヤル | store |
| Projects, scenes, takes | **プロジェクト、シーン、テイク** | store |
| Recording folder | **録画フォルダ** | store, app UI |
| Review & trim | **確認とトリミング**; Premium row 「確認画面でのトリミング」 | store. (Pricing page currently says 「保存前のトリミング」; see §6) |
| Storage estimate | 容量の目安 | store |
| Crash recovery | クラッシュ対策 | store |
| Thermal monitor | 発熱の監視 | store |
| Premium | **Premium** (Latin, never プレミアム) | store |
| the free tier | 無料版 | store |
| "Record once, get two videos" (hero) | 「撮影は1回、動画は2本」 / 「1回の撮影で同時録画」 | store |
| "your reaction and the scene in front of you" | 「あなたのリアクションと、目の前の光景を同時に」 | store. Never シーン for the real-world scene (collides with the app's Scene); 光景 or 景色 |
| Lifetime | 買い切り | store, app UI |
| 7-day free trial | 7日間の無料トライアル | app UI |
| App name | ContentCam (store title: 「ContentCam：縦横同時撮影カメラ 1回で動画2本」; Play: 「ContentCam：縦横・前後同時録画カメラ」) | store-metadata-expansion.md, Play JSON |

---

## 4. Platform names and UI labels in Japanese

| Platform feature | Japanese name to use | Source / confidence |
|---|---|---|
| Apple Dual Capture | **デュアルキャプチャ**. First mention per page: **デュアルキャプチャ（Dual Capture）**. The video it makes: デュアルキャプチャビデオ | **verified**: Apple JP iPhone User Guide 「デュアルキャプチャビデオを撮影する」, steps 「「ビデオ」モードを選択します。〔アイコン〕をタップしてから、「デュアルキャプチャ」をタップします」 (support.apple.com/ja-jp/guide/iphone/iph61f49e4bb/ios); model list page title 「デュアルキャプチャビデオに対応しているモデル」 (…/aside/glos3842gv5b/27/ios/27). Autocomplete: 「デュアルキャプチャ iphone17」, 「デュアルキャプチャ iphone16」, 「デュアルキャプチャとは」 |
| Apple's description of Dual Capture | 「自分自身と自分の前で起きている動きを同時に撮影できます」 | verified, same page |
| Apple illustration text (if quoted) | 「フレームの左上にあるウインドウに前面カメラで撮影している映像が表示され、フレームの残りの部分に背面カメラで撮影している映像が表示されています」 | verified (image alt text, same page). Note Apple says 前面カメラ, not フロントカメラ |
| iPhone camera controls button | カメラコントロールボタン (the on-screen button); カメラコントロール (the physical iPhone 16+ control) | verified (alt text + guide) |
| iOS Camera settings | 「設定」＞「カメラ」＞「ビデオ撮影」; toggles 「グリッド」「水平」; 「手ぶれ補正（拡張）」; 「アクションモード（低照度）」 | verified (Apple JP guide iphc1827d32f, iph3dc593597) |
| Apple video mode | 「ビデオ」モード | verified |
| iMovie split screen / PiP | 「スプリットスクリーン」 / 「ピクチャインピクチャ」 | verified (Apple JP iMovie guide kna831efee4d) |
| Samsung Dual recording | **デュアル録画** | verified: au Galaxy S25 and S26 manuals list 「デュアル録画：デュアル録画の保存オプションを設定します」. Autocomplete 「デュアル録画 galaxy」 |
| Samsung Director's View | **ディレクターズビュー** | verified: au Galaxy S21 (SCG09) manual 「ディレクターズビューで撮影する」 |
| Samsung camera switch / More menu | フロントカメラ／リアカメラの切り替え; 「その他」 | verified (au manuals). Samsung JP says フロントカメラ/リアカメラ for hardware: use those only inside Samsung UI quotes |
| Samsung stabilisation label | 動画手振れ補正 | verified (au manual) |
| Samsung "selfie camera" (support page wording) | Samsung JP's own term is フロントカメラ; for our prose use インカメラ | verified (au manual); the English support page says "selfie camera" |
| Google Pixel Fold Dual Screen preview | デュアルスクリーンプレビュー（Dual screen preview） | **unverified** (Google JP label not fetched) |
| Pixel Add Me | Add Me (Google JP keeps the English name) | **unverified** |
| Instagram Dual | **「デュアル」** (Instagramのカメラの「デュアル」機能) | **verified**: Meta JP newsroom, 2022-07 「同時に前面カメラで自分のリアクションを録画することができるツール、デュアルも導入します」 (about.fb.com/ja/news/2022/07/reelsjulycreativetools/). Autocomplete 「インスタ デュアル できない」「インスタ デュアル 消えた」「インスタ デュアルカメラ」 |
| Instagram Reels / Stories | **リール** / **ストーリーズ** | verified (Meta JP newsroom uses リール); autocomplete 「インスタ リール 縦動画」 |
| YouTube Shorts | **YouTubeショート** (ショート動画 generically) | chosen; YouTube JP UI label ショート (unverified) |
| TikTok tools | TikTokのUI labels are not fetched: 「反転」 for flip camera is attested on our TikTok page; duet デュエット, stitch リミックス/つなげる are **unverified** | unverified |
| Snapchat Memories | 思い出（Memories） | unverified (existing page form) |
| BeReal | BeReal (Latin); "BeReal-style" → 「BeReal風」 | autocomplete 「bereal 風 カメラ」「bereal 風 アプリ」 |
| App Store / Google Play | App Store / Google Play (Latin) | store |

---

## 5. Native search phrasing (autocomplete-verified, `hl=ja`, 2026-11-15)

Use these shapes for titles and H2s. Keep 「（2026年）」 at the end of titles as the pages already do.

**Front + back camera at once** (the biggest cluster)
- インカメ 外カメ 同時 / 同時撮影 / 同時 アプリ / 同時 iphone / 同時 iphone17 / 同時 iphone16 / 同時 写真
- インカメラ 外カメラ 同時; iphone インカメラ 外カメラ 同時; 内カメラ 外カメラ 同時; 外カメラ 内カメラ 同時 録画
- アウトカメラ インカメラ 同時撮影; インカメラ アウトカメラ 同時 動画 / アプリ / iphone
- 前後同時撮影 アプリ / アプリ 無料 / iphone / android / カメラ; iphone17 前後同時撮影; iphone 前後カメラ 同時
- 両面カメラ / 両面カメラ アプリ / 両面カメラ iphone / iphone17 両面カメラ / インスタ 両面カメラ (new phrasing, not on any page yet; worth one H2 or FAQ mention on the dual-camera pages)
- 同時撮影 アプリ; 前後 同時撮影 アプリ iphone; 2 カメラ 同時撮影 アプリ; 内カメ 外カメ 同時撮影 アプリ
- Caution: 「前後カメラ」 alone autocompletes to dashcams (ドライブレコーダー), and 「リアカメラ」「バックカメラ」 to car cameras. Always pair 前後カメラ with iPhone/スマホ/アプリ/同時 in a title.
- Recommended title core: 「インカメラと外カメラを同時に録画する方法」 (pages already use this; keep it). Casual 「インカメと外カメ」 is a real query and is acceptable in a TikTok/Snapchat title only.

**Dual camera**
- デュアルカメラ アプリ / アプリおすすめ; iphone デュアルカメラ アプリ; デュアルカメラ iphone / android; デュアルカメラとは
- tiktok デュアルカメラ; インスタ デュアルカメラ; インスタ デュアル できない / ない / 消えた / どこ / やり方

**Portrait + landscape at once**
- 縦横同時撮影 / アプリ / アプリ android / カメラ / 写真; iphone 縦横同時撮影; スマホ 縦横 同時撮影; 縦横同時に撮れるカメラアプリ
- 縦動画 横動画 同時 / 同時撮影; 縦動画 横動画 変換 / 違い
- (縦横同時配信 is a streaming term, different intent. Do not target it.)
- YouTube: youtube ショート 横動画 / 横動画にする方法

**Apple Dual Capture**
- デュアルキャプチャ / iphone / iphone17 / iphone16 / iphone15 / iphone14 / iphone17e / iphone やり方 / とは / ビデオ / 写真; デュアルキャプチャー (long-vowel variant also typed); iphone 17 デュアルキャプチャ
- English 「dual capture iphone」 is also typed by Japanese users; the first-mention gloss デュアルキャプチャ（Dual Capture） covers both.

**Samsung**
- デュアル録画 galaxy / とは / iphone / pixel / スマホ; galaxy デュアル録画; ディレクターズビュー galaxy / とは

**Split screen / picture in picture**
- 画面分割 動画 / 動画編集 / 動画 アプリ; iphone 画面分割 動画; 動画編集 画面分割 iphone
- ワイプ 動画 / 動画編集 / 作り方 / 編集 アプリ; iphone ワイプ撮影
- ピクチャインピクチャ 動画 / 動画撮影 / 動画 保存

**Other**
- iphone 録画中 カメラ切り替え (for the switch-camera page)
- 手ぶれ補正 iphone / スマホ / 動画
- テレプロンプター アプリ / 無料 / おすすめ / iphone / android; カンペ アプリ / 無料 iphone / おすすめ
- 買い切り カメラアプリ; iphone カメラアプリ 買い切り; カメラアプリ 買い切り おすすめ
- bereal 風 カメラ / アプリ

---

## 6. Inconsistencies found across existing `/ja/` pages (21)

Counts are occurrences in visible text plus JSON-LD.

1. **Apple's feature name left in English.** Official JP name is デュアルキャプチャ. 19 pages write only 「Dual Capture」 (e.g. `blog/iphone-17-dual-capture-limitations` 43×, `vs/apple-dual-capture` 53×, `blog/iphone-duo-camera`, `blog/record-front-and-back-camera-iphone-15-16`, `blog/switch-camera-while-recording-iphone`, `blog/doubletake-not-working-alternatives`, `blog/bereal-style-photo-without-bereal`, `blog/take-photo-front-and-back-camera-same-time`, `blog/film-kid-reaction-and-what-they-see`, `blog/film-reaction-video-phone`, `blog/how-to-do-dual-camera-on-tiktok`, `blog/instagram-dual-camera-missing`, `blog/iphone-4k-front-and-back-camera-same-time`, `blog/record-front-and-back-camera-same-time-iphone`, `blog/split-screen-video-iphone`, `blog/best-front-and-back-dual-camera-apps`, `index`, `support`, `vs/lookout`). Right: デュアルキャプチャ（Dual Capture） at first mention, デュアルキャプチャ after. Right already: `blog/dual-camera-effect`, `vs/apple-dual-capture` title.
2. **Misquoted Apple page title.** 「Dual Captureビデオに対応しているモデル」 / 「Dual Captureビデオ」 in `blog/dual-camera-effect`, `blog/film-reaction-video-phone`, `blog/iphone-17-dual-capture-limitations`, `blog/take-photo-front-and-back-camera-same-time`, `vs/apple-dual-capture`. Apple JP's title is 「デュアルキャプチャビデオに対応しているモデル」.
3. **Misquoted Apple illustration text with フロントカメラ.** `blog/iphone-17-dual-capture-limitations` and `vs/apple-dual-capture` quote 「フレームの左上のウインドウにフロントカメラが…」. Apple JP says 「フレームの左上にあるウインドウに前面カメラで撮影している映像が表示され…」. Quote Apple's text exactly.
4. **リアカメラ for ContentCam's back camera.** `vs/apple-dual-capture` (3), `vs/lookout`, `vs/mixcam` (2), `vs/detail` (2). Right: 背面カメラ. リアカメラ only inside Samsung UI quotes.
5. **フロントカメラ used for hardware (not the mode).** `vs/apple-dual-capture` and `vs/lookout` 「フロントカメラとリアカメラを同時に動かせるカメラシステム」. Right: インカメラと背面カメラ. (Mode uses on `index`, `features`, `vs/dualtake` are correct. `blog/iphone-duo-camera` follows Apple marketing wording; acceptable only inside an Apple spec quote, otherwise インカメラ.)
6. **自撮りカメラ / 自撮り as the hardware noun.** `vs/mixcam` 「自撮りカメラとリアカメラ」, `vs/detail` 「自撮りとリアカメラ」, `blog/iphone-17-dual-capture-limitations` 「背面カメラと自撮りカメラの映像」. Right: インカメラと背面カメラ. (自撮り as the activity or photo is fine.)
7. **セルフィーカメラ.** `blog/record-front-and-back-camera-same-time-android` (2), `blog/record-front-and-back-camera-samsung-galaxy` (4) translate Samsung's English "selfie camera". Samsung JP's term is フロントカメラ; in our prose use インカメラ.
8. **Clipped インカメ / 外カメ in body text.** `blog/snapchat-front-and-back-camera` (20×) and `blog/how-to-do-dual-camera-on-tiktok` (9×). Allowed in the title (real query); body should be インカメラ / 外カメラ or 背面カメラ like every other page.
9. **手ブレ補正 vs 手ぶれ補正.** `index` and `features` use 手ブレ補正; `blog/iphone-duo-camera`, `changelog`, `pricing`, `vs/2cam`, `vs/dualcam`, `vs/dualgram` use 手ぶれ補正. Right: **手ぶれ補正** (Apple JP, Google autocomplete normalises to it, app glossary). Upstream note: the v2.8.2 App Store and Play copy and the ja keyword field still say 手ブレ補正; that is a store-copy defect, not a reason to follow it on the site.
10. **分割画面 vs 画面分割.** `blog/doubletake-not-working-alternatives` uses 分割画面 (2); 29 pages and the store copy use 画面分割. Right: 画面分割.
11. **合成（Combine） gloss vs plain 合成.** 14 pages gloss it (`blog/film-reaction-video-phone`, `blog/how-to-do-dual-camera-on-tiktok`, `blog/iphone-17-dual-capture-limitations`, `blog/iphone-4k-front-and-back-camera-same-time`, `blog/record-front-and-back-camera-same-time-android`, `blog/record-front-and-back-camera-same-time-iphone`, `blog/switch-camera-while-recording-iphone`, `vs/apple-dual-capture`, `vs/detail`, `vs/dualcam`, `vs/dualgram`, `vs/dualtake`, `vs/lookout`, `vs/mixcam`); the rest and the store copy write plain 合成. Right: 合成 (the app UI says 合成; the gloss is reserved for the three mode names).
12. **無料体験 vs 無料トライアル.** `index` (4) and `vs/dualcam` (4) say 無料体験; `pricing` (12), `support`, `vs/2cam`, `vs/detail`, `vs/lookout`, `vs/mixcam` say 無料トライアル. Right: **無料トライアル** (app UI). The homepage contradicts the pricing page.
13. **カメラApp vs 「カメラ」アプリ.** `vs/apple-dual-capture` (7) and `blog/iphone-duo-camera` (1) write カメラApp; 12 pages write 「カメラ」アプリ. Right: 「カメラ」アプリ (Apple JP guide).
14. **写真アプリ without brackets.** `changelog` (2), `vs/dualcam` (6), `vs/dualgram` (2). Right: 「写真」アプリ.
15. **カメラロール.** `features` (1, ContentCam's own copy) should be 「写真」アプリ. In `blog/instagram-dual-camera-missing` (3) and `blog/snapchat-front-and-back-camera` (4) it means "your gallery" when uploading; use 「写真」アプリ（Androidはギャラリー） unless quoting the other app's UI label.
16. **ファインダー.** `changelog` 「AE/AFロック：ファインダーを長押し」 and `blog/record-front-and-back-camera-google-pixel` 「両方の画面にファインダーを表示」. Right: プレビュー (store: 「画面を長押しすると、ピントと露出を固定できます」).
17. **ユーザーガイド vs ユーザガイド.** `blog/iphone-4k-front-and-back-camera-same-time` (2) and `vs/dualgram` (2) write ユーザーガイド for Apple's guide; 12 pages write ユーザガイド. Right when naming Apple's document: **iPhoneユーザガイド** (Apple's spelling).
18. **Instagram's feature name.** `blog/instagram-dual-camera-missing` calls it 「Dual」 / 「デュアルカメラ（Dual）」 throughout. Meta JP's name is 「デュアル」. Right: Instagramの「デュアル」 (keep デュアルカメラ in the title for search: 「インスタのデュアルカメラ（デュアル）がない・使えない？」).
19. **Reels / Shorts in Latin vs リール / ショート.** 11 pages write リール and 11 write Reels; 8 write ショート, 6 write Shorts (`index`, `features`, `blog/film-for-tiktok-and-youtube-at-the-same-time` etc. use Latin). Right in prose: **リール**, **YouTubeショート**. Latin "TikTok、Reels、YouTube" is acceptable only where a line mirrors the store copy's posting list.
20. **縦型 / 横型 for the video formats.** `blog/film-reaction-video-phone` (4 縦型), `blog/film-for-tiktok-and-youtube-at-the-same-time` (1), `changelog` (縦型 1, 横型 1). Right: 縦動画 / 横動画 (store, app UI).
21. **Typography slips.** (a) `pricing` uses en dash 「–」 (6) for empty table cells; use 「×」 or 「なし」. (b) ASCII space between Latin and Japanese in a label 「ContentCam 前後カメラ（Front/Back）」 on `blog/dual-camera-effect`, `blog/film-kid-reaction-and-what-they-see`, `blog/how-to-do-dual-camera-on-tiktok`, `blog/instagram-dual-camera-missing`, `blog/snapchat-front-and-back-camera`, `blog/split-screen-video-iphone`; write 「ContentCamの前後カメラ（Front/Back）」. (c) `blog/phone-teleprompter-apps-compared` 「Starter 月額 $24.99」: write 「Starter：月額US$24.99」. (d) Disclosure label varies: お断り / おことわり (`blog/record-front-and-back-camera-iphone-15-16`); use お断り.

Also worth a look (not counted): the Pricing page row 「保存前のトリミング」 vs the store's Premium row 「確認画面でのトリミング」; use the store form.

Consistent already (no action): インカメラ (41 pages), 背面カメラ in body, 前後カメラ（Front/Back） (41 pages; no page uses 前後カメラ（Front & Back）), デュアルレンズ（Dual Lens）, シングルレンズ（Single Lens）, ワイプ（ピクチャ・イン・ピクチャ）, 書き出し (no エクスポート), 台本 (no スクリプト), 買い切り, 年額/月額/週額, date format, no full-width digits, no ポートレート/ランドスケープ for orientation, no em dashes.

---

## 7. False friends and calque traps for this subject

1. **ポートレート / ランドスケープ** for orientation. ポートレート is iPhone's Portrait (bokeh) mode; ランドスケープ is scenery. Use 縦 / 横. Equally, do not write 縦横比 when you mean "portrait and landscape"; 縦横比 means aspect ratio.
2. **フロントカメラ** for the selfie hardware. Japanese users say インカメラ. フロントカメラ is ContentCam's mode name (and Samsung's menu wording).
3. **リアカメラ / バックカメラ / アウトカメラ.** Car parts on autocomplete (リアカメラ, バックカメラ) or less common; use 背面カメラ (body) or 外カメラ (search titles).
4. **前後カメラ alone in a title.** Reads as a dashcam (ドライブレコーダー). Qualify it: 「iPhoneで前後カメラを同時に録画」.
5. **デュアルカメラ alone in a title.** Also a car brake-assist term; pair with アプリ / iPhone / 動画.
6. **ダブルカメラ, 二眼 / 2眼.** ダブルカメラ is a toy-train camera; 二眼 means a phone with two rear lenses. Neither means "front + back at once".
7. **ビデオ for "video".** Use 動画, except inside Apple's own labels (「ビデオ」モード, デュアルキャプチャビデオ).
8. **録音 vs 録画.** 録音 is audio only.
9. **シーン for the real-world scene.** Collides with ContentCam's Scene entity. Use 光景 / 景色 / 目の前の様子.
10. **レビュー for the review screen.** Means a store rating. ContentCam's screen is 確認画面; star ratings are 評価 / レビュー.
11. **トリミング vs クロップ.** トリミング = cut time (trim). クロップ / 切り出し = cut the frame. "Crop a landscape out of portrait" is 切り出す / クロップ, never トリミング.
12. **ファインダー** for the on-screen preview. Use プレビュー.
13. **スクリプト** for the teleprompter text. Reads as code. Use 台本.
14. **レベル** for the horizon guide. Use 水準器 (ContentCam) / 「水平」 (Apple's setting name).
15. **Split screen as スプリット画面 or 分割画面.** Use 画面分割; 「スプリットスクリーン」 only for iMovie's label.
16. **「同時に」 placement.** Natural: 「インカメラと外カメラを同時に録画する」. Unnatural calques: 「同じ時間に録画」, 「一度に両方を記録」 (記録 is data logging).
17. **「無料で試す」 CTA phrasing.** Natural: 「無料ではじめる」 / 「無料でダウンロード」. Avoid 「フリーで」 and 「お試しください」 stacked politeness.
18. **Adding 「サブスクなし」 or price lines the English does not have.** Translate plan facts exactly where the English source states them; never add them as extra selling lines.
19. **Calque of "one-tap" / "seamless".** 「シームレスに」「ワンタップで」 read as translated ad copy; prefer 「1回押すだけで」 (store: 「1回押すだけで」).
20. **「開発者」 disclosures.** Keep 「私はContentCamの開発者なので、中立ではありません」; do not soften to 「関係者」.
21. **Counters.** 動画は本, 写真は枚, レビューは件, 機種は機種/台. 「2つの動画」 is acceptable, 「2個の動画」 is not.
22. **Rival app names.** Never translate or katakana-ise product names (DualShot, MixCam, Dualgram, DoubleTake, Snapchat, BeReal).
