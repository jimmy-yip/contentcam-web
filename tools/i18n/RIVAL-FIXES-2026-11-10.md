# Rival-steering fixes, 10 Nov 2026 (founder rule: never recommend/help a dual-recording rival)

Apply to the ENGLISH pages below. Exact edits; keep everything else. Where text appears in both visible HTML and JSON-LD
(FAQ/description), change both (visible uses `&amp;`, JSON-LD uses `&`). After editing, every JSON-LD block must parse.
No em dashes. Plain English. If a quoted OLD string isn't found exactly, find the equivalent sentence and apply the intent.

## blog/record-front-and-back-camera-iphone-15-16/
- Delete bullets "Free only, one finished video, already on iOS 26: SplitRig." and "Control of a RØDE wireless microphone from the camera app: RØDE Capture."; heading "Which app should you pick on an iPhone 15 or 16?" -> "How do you record front and back on an iPhone 15 or 16?"
- FAQ "What is the best free app to record front and back on iPhone 15?" -> question "What is a free way to record front and back on iPhone 15?", answer "ContentCam is free to download on iOS 18 and later, with 5 free Front & Back recordings saved as two separate files and no ads or watermark."
- Paragraph starting "Why ContentCam comes first:" -> "Why ContentCam: it runs on iOS 18, which every iPhone 15 and iPhone 16 can run, and it saves the front and back cameras as two separate files." (drop the rest of that paragraph incl. the "More apps are compared in" link)

## blog/dual-format-recording-apps-compared/
- Unlink rival links: `<a href="https://apps.apple.com/us/app/dualshot-recorder/id6761159805">DualShot Recorder</a>` -> `DualShot Recorder`; `<a href="https://ddjrproductions.com/dualshotrecorder/">developer site</a>` -> `developer site (ddjrproductions.com)`.
- Delete "DualShot Recorder suits iPhone shooters who grade Apple Log footage and don't need front and back at once."
- "Before paying for any of them, check whether the plan renews weekly and whether the landscape file is a real wide capture." -> "Check whether any plan renews weekly and whether the landscape file is a real wide capture."

## blog/index.html (cards)
- iPhone 15/16 card text -> "Neither iPhone 15 nor iPhone 16 has Apple's Dual Capture. How to record both cameras at once anyway, as two separate files."
- DoubleTake alternatives card: title -> "DoubleTake Not Working? What Still Records Two Cameras at Once (2026)", text -> "What the reviews say, and how ContentCam records two cameras at once."
- DoubleTake comparison card text -> "Two cameras at once versus two aspect ratios at once, and where each app falls short."
- Best front-and-back card text -> "How ContentCam compares with MixCam, Dualgram, DoubleTake and DualShot Recorder on front and back, and on one-take dual-format."

## vs/index.html
- `<h2>Pick the app you've already tried</h2>` -> `<h2>How ContentCam compares with other apps</h2>`
- "Closest feature match: iPhone only, 9:16 and 16:9 in one take, $24.99 lifetime." -> "iPhone only, 9:16 and 16:9 in one take." (keep the ContentCam sentence after it)

## blog/iphone-video-not-in-photos-after-recording/
- Remove the support help for DualShot users: in "If this happened to you, check iPhone Storage, check for a DualShot folder ..., don't delete the app, and contact DDJR Productions ..." keep the general checks but end with "don't delete the app." and drop the DDJR contact; same in the FAQ answer ("..., don't delete the app, and contact DDJR Productions, the developer." -> "..., and don't delete the app.").

## blog/record-front-and-back-camera-samsung-galaxy/
- FAQ: delete "; DuoCam does too" (sentence ends after "two separate files.").
- "Samsung's built-in Dual recording suits anyone on a listed model who only needs one finished picture-in-picture clip, since it is already installed." -> "Samsung's built-in Dual recording is already installed on listed models and saves one picture-in-picture clip."

## blog/instagram-dual-camera-missing/
- `<h2>Where do the other apps beat ContentCam?</h2>` -> `<h2>What do the built-in options do?</h2>`; delete the SplitRig bullet.

## vs/detail/
- Replace the "Detail is built for talking videos that come out edited: ..." paragraph with: "Detail is an AI video editor with captions, green screen, remote guests and livestreaming, on iOS 17, iPad and Mac."
- In the FAQ answer mentioning Detail's layout "can be changed after recording", append: "ContentCam's Combine editor also lets you pick picture-in-picture or split screen after recording, and keeps the originals."

## blog/splitrig-vs-contentcam/
- "If all you want is one free finished picture-in-picture clip on an iPhone running iOS 26, SplitRig suits that. Other ad-free options are in <a ...>which dual camera apps have no ads</a>." -> "ContentCam has no ads and no watermark on any plan."

## blog/doubletake-not-working-alternatives/
- title/h1/og:title/headline -> "DoubleTake Not Working? What Still Records Two Cameras at Once (2026)"; twitter:title -> "DoubleTake Not Working? Two Cameras at Once (2026)"
- descriptions: "Common causes, and the apps that still record two cameras at once." -> "Common causes, and what still records two cameras at once."; "Why it may not be working for you, and which apps still record front and back at the same time." -> "Why it may not be working for you, and how ContentCam and Apple's Dual Capture record front and back at the same time."
- h2 "Which apps record two cameras at once instead of DoubleTake?" -> "How does DoubleTake compare with ContentCam and Apple's Dual Capture?"; delete table rows for RØDE Capture, SplitRig, Dualgram.
- "RØDE Capture and Dualgram also list separate files, though Dualgram's listing is marked Contains Advertising. SplitRig and Dual Capture save one combined video, so there are no separate angles to re-cut." -> "Apple's Dual Capture saves one combined video, so there are no separate angles to re-cut."
- "Which DoubleTake alternative should you pick?" -> "Which option fits you?"; delete the RØDE Capture bullet.
- FAQ: delete "RØDE Capture lists a Separate Files option, and Dualgram says it saves both originals plus the combined video."; question "Which DoubleTake alternative saves the front and back camera as separate files?" -> "Which app saves the front and back camera as separate files on iPhone?"

## vs/dualgram/
- "Dualgram suits someone on iPhone or iPad who wants a finished picture-in-picture or side-by-side clip straight out of the camera with the two originals saved too:" -> "Dualgram's listing describes a finished picture-in-picture or side-by-side clip straight out of the camera, with the two originals saved too:"

## blog/dual-camera-app-one-time-purchase/
- "If you only want a free front and back recorder on iOS 26, SplitRig costs nothing. More apps, including free ones, are in <a ...>the best front and back camera apps</a>, and Android phones are covered in" -> "Android phones are covered in"
- lede "CamDuo ($4.99), Twofold ($6.99) and Dualgram ($29.99 one-time PRO, or the paid Dualgram Pro app) also sell a one-time option, SplitRig is free with nothing to buy, and DoubleTake and MixCam list weekly plans." -> "Other apps list one-time options or weekly plans on their US App Store pages; the table below has the facts."
- FAQ answer starting "Yes. SplitRig's App Store listing says it is free" -> "Yes. ContentCam sells a one-time lifetime purchase next to its monthly and yearly plans, so you never have to subscribe."

## blog/dual-camera-app-without-internet/
- delete "SplitRig is the free option if your iPhone runs iOS 26."
- h2 "When is SplitRig or Lookout the better offline app?" -> "When is ContentCam the better offline app?"; delete the SplitRig bullet and the Lookout bullet (keep the ContentCam bullet).
- FAQ: drop the leading SplitRig sentence so the answer starts "ContentCam is free to download with 5 free Front & Back recordings, then Premium, and records offline on iOS 18 or later and Android." (keep any following ContentCam text)

## blog/reframe-vs-contentcam/
- "If ads are the deciding factor, <a ...>dual camera apps without ads</a> covers the other options." -> "If ads are the deciding factor, ContentCam shows none on any plan."

## blog/dual-camera-app-without-ads/
- lede: delete "SplitRig and MixCam: Front and Back Camera (iPhone) and PairTake, DualCam and DuoCamera (Android) also show no ads." 
- delete "SplitRig (iOS 26 or later) and DualCam by Rajesh Hadiya (Android) list no in-app purchases at all."
- FAQ: delete the sentences listing SplitRig/MixCam/PairTake/DualCam/DuoCamera as ad-free; keep "Checked 5 November 2026."

## blog/dualshot-recorder-vs-contentcam/
- unlink: `<a href="https://apps.apple.com/us/app/dualshot-recorder/id6761159805">App Store listing</a>` -> `App Store listing`; `<a href="https://ddjrproductions.com/dualshotrecorder/">DDJR Productions' DualShot page</a>` -> `DDJR Productions' DualShot page`
- delete table row "Grade in Apple Log on an iPhone 15 Pro or later, or want the cheapest yearly plan | DualShot Recorder"
- "Whichever you try, compare the two <em>landscape</em> files" -> "When you try ContentCam, compare the two <em>landscape</em> files"
- Related list: remove the link "DualShot video not in Photos: where to find it".

## blog/doubletake-vs-contentcam/
- unlink `<a href="https://apps.apple.com/us/app/doubletake-multicam-video/id1478041592">App Store listing</a>` -> `App Store listing`
- "DoubleTake still suits one case: filming on an iPad, or on an iPhone too old for iOS 18, provided it opens on your device." -> "DoubleTake's listing covers iPad and older iPhones; ContentCam needs iOS 18 or later on iPhone."

## blog/best-front-and-back-dual-camera-apps/
- "Which front and back camera apps are worth installing?" -> "How do front and back camera apps compare?"
- "DualShot Recorder suits iPhone-only creators who want Apple Log and 4K." -> "DualShot Recorder's listing mentions Apple Log and 4K."
- delete rows "One free combined video on iOS 26 | SplitRig" and "Free, one merged clip, on Android | TwinLens"
- FAQ "Is there a free way...": drop "SplitRig (iOS 26 or later) is free on iPhone and TwinLens is free on Android." 
- FAQ "Which front and back camera apps run on Android?": answer -> "ContentCam runs on both iPhone and Android, and it only offers Front & Back on Android phones that can run both cameras at once." (keep any remainder that is about ContentCam)
