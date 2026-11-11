# Can an iPhone Record 4K From the Front and Back Camera at the Same Time? (2026)

Source: https://contentcam.app/blog/iphone-4k-front-and-back-camera-same-time/

Apple's Dual Capture records front and back at up to 4K 30 fps on iPhone 17, Air, 18 Pro and Duo. Third-party apps are held to Apple's multi-camera formats. What rival listings claim about 4K, what Apple allows, and how to check a file.

By Jimmy, developer of ContentCam · 11 November 2026 · Updated 11 November 2026

**Short answer:** Apple's own Camera app can, on newer models. Apple lists "Dual Capture up to 4K Dolby Vision at 30 fps" for iPhone 17, iPhone Air, iPhone 18 Pro and iPhone Duo, saved as one combined video. Third-party apps are a different case. They record two cameras through Apple's AVCaptureMultiCamSession, which only accepts camera formats Apple marks as multi-camera capable. We read that list on an iPhone 18 Pro running iOS 27.0.1: 3840 x 2160 at 30 fps carries the flag, but no 4K format does at 60 fps. So 4K at 60 fps from two cameras at once isn't open to any third-party app on that phone, and 4K at 30 fps only works if the phone can run both 4K streams together.

Disclosure: I build ContentCam, an iPhone and Android camera app with a Front & Back mode. ContentCam's Front & Back records HD, not 4K, for exactly this reason. The rival quotes below are copied from each app's live store listing on 11 November 2026, and the Apple details come from Apple's developer documentation and specs pages, checked the same day.

## Which dual camera apps say they record 4K?

Five front and back camera apps mention 4K or UHD in their store listings or guides. Only Lookout's listing ties UHD to both feeds, and none of them gives a pixel size for a recording with both cameras running.

| App | Exact wording | Where |
| --- | --- | --- |
| Dualgram (Just2us) | "Support up to 4k, 60 fps" | App Store listing, version 2.5 |
| Dualgram (Just2us) | "up to 4K resolution and 60 FPS. Depending on the iPhone model, certain configurations would not be supported, so you have to try out to know." | dualgram.com user guide |
| DualCam (Mobixoft) | "Up to 4K and up to 60 fps, depending on device and mode" | App Store listing, version 1.0.5 |
| 2Cam (VISION FZ) | "Select 720p, 1080p, or 4K resolution" | App Store listing, version 1.5.2 |
| Lookout (KIDA Studios) | "Dual-Stream HD/UHD: Record both feeds in stunning clarity." | App Store listing, version 5.9 |
| MixCam (Mixcord) | "Save to your device in 4K, 1080p, or 720p" | Google Play listing; the iPhone listing names no resolution |

Read the qualifiers. DualCam's listing says "depending on device and mode" and also lists "Switch between dual-camera and single-camera shooting". 2Cam's listing adds "Some features and recording options may depend on your device capabilities." Dualgram's guide says you "have to try out to know". MixCam's Android wording is about what it saves, not what the cameras capture. Lookout's line is the only one that ties UHD to both feeds, and it gives no pixel figure.

Dualgram and DualCam both pair 4K with 60 fps. On the iPhone 18 Pro, Apple flags no 4K format at 60 fps for multi-camera use, so on that phone the 4K and the 60 fps can't both apply while two cameras are recording.

## What does Apple let third-party apps record with two cameras?

Apple limits third-party apps to a smaller set of camera formats whenever two cameras run together. Apple's documentation for AVCaptureDevice.Format.isMultiCamSupported says that with a multi-camera session "you may only set the device's format to one in which isMultiCamSupported is true. Only this limited subset of capture formats can run sustainably in a multi-camera capture scenario."

Apple's multi-camera session also keeps a running budget. Its hardwareCost property is "normalized to a range of 0.0 to 1.0", and "When the value is greater than 1.0, the capture session cannot run your configuration due to hardware constraints." A second property, systemPressureCost, covers heat and power: above 1.0 the session "cannot run sustainably, but it may be able to run briefly before stopping."

What that looks like on a real phone: ContentCam has a test build that prints every camera format and whether Apple marks it multi-camera capable. On an iPhone 18 Pro running iOS 27.0.1, on 10 November 2026:

- **4K at 30 fps:** 3840 x 2160 (16:9) carries the flag on the front camera, the rear wide and the rear ultra-wide.
- **4K at 60 fps:** no 3840 x 2160 format at 60 or 120 fps carries the flag, on any camera. Two cameras at 4K 60 is off the table on this phone.
- **4:3:** the largest flagged 4:3 format is 1920 x 1440, at 30 and 60 fps, on every camera. Apps that record from the 4:3 sensor shape so they can cut more than one frame from it are held to that size.

Being on the list isn't the same as running. Each 4K stream still counts against the hardwareCost budget, and the session refuses a set that goes over 1.0. We haven't yet recorded a two-camera 4K 30 take on the 18 Pro to see whether two 4K streams fit. Apple's own Dual Capture stopping at 4K 30 fps, not 60, matches the same ceiling.

Apple's Dual Capture is the exception. It is a mode in Apple's own Camera app on iPhone 17, iPhone 17 Pro, iPhone Air, iPhone 18 Pro and iPhone Duo (not iPhone 17e), and Apple publishes it at up to 4K at 30 fps, as one picture-in-picture video. Its limits are in [iPhone 17 Dual Capture limitations](https://contentcam.app/blog/iphone-17-dual-capture-limitations/).

## How can a dual camera app list "up to 4K"?

The App Store listings don't say which of these applies, so treat each as a possibility to check rather than a conclusion:

- **4K in a single-camera mode.** Several of these apps also record one camera at a time, where a third-party app can use the full 4K formats.
- **A 4K canvas.** A picture-in-picture or split-screen video can be saved at 3840 x 2160 while each camera feed inside it was captured smaller and scaled up. The file reports 4K; the detail is whatever the cameras captured.
- **Device dependent.** "Depending on device and mode" and "you have to try out to know" leave room for 4K on some phones and HD on others.
- **A route I haven't seen.** If an app has found two-camera 4K on a model I haven't tested, its own file will show it. The check below takes a minute.

## How do you check if a front and back video is really 4K?

Record a 10-second test with both cameras running, at the app's highest setting, then look at the file and at the detail.

1. **Read the pixel size.** Open the video in Photos and swipe up or tap the info button. A 4K file reads 3840 x 2160 (or 2160 x 3840 vertical). On a Mac, QuickTime Player's Movie Inspector (Window > Show Movie Inspector) shows the same.
2. **Check the originals, not just the combined file.** If the app also saves the front and back cameras as separate files, read their pixel sizes too. Separate originals at 1920 x 1080 under a 3840 x 2160 combined file means the combined file was scaled up.
3. **Compare the detail.** Film fine text or a brick wall from 2 metres with the app in two-camera mode, then again with the iPhone Camera app at 4K in normal video mode. Pause both on the same frame and zoom in. Real 4K keeps the edges of letters crisp; scaled-up HD goes soft at the same zoom.

A file can report 3840 x 2160 and still be HD detail. Only step 3 tells you which.

## Does 4K matter for front and back camera video?

Less than the listings suggest. Most front and back videos end up as a 9:16 post on TikTok, Instagram Reels or YouTube Shorts, where the selfie camera sits in a small picture-in-picture window. That window shows a fraction of the frame, so the front camera's resolution barely shows. The rear feed is where resolution matters, and only if you plan to crop or zoom into it in the edit. The wider trade-offs are in [do you need to film in 4K](https://contentcam.app/blog/do-you-need-to-film-in-4k/).

Frame rate is the trade people notice. Apple's Dual Capture tops out at 30 fps, while the same iPhones shoot normal video at 4K 60 fps. If you plan to slow footage down, 60 fps matters more than the extra pixels.

## What resolution does ContentCam record front and back in?

HD. ContentCam's Front & Back mode records the front and rear cameras as two separate HD files, at up to 60 fps on iPhones that support it (60 fps is Premium; some older iPhones cap at 30) and up to 30 fps on Android phones that can run both cameras. Front & Back works on every iPhone running iOS 18, from iPhone XS and XR on. The layout comes afterwards: the Combine editor turns the two files into picture-in-picture or split screen and keeps the originals. ContentCam's 4K is in its single-lens mode, which records a 9:16 vertical and a 16:9 horizontal video from one take.

## FAQ

### Can iPhone 15 or iPhone 16 record 4K with both cameras at once?

Not in the Camera app: Dual Capture is listed for iPhone 17, iPhone Air, iPhone 18 Pro and iPhone Duo, and iPhone 16 and 16e don't have it. Third-party apps can record both cameras on those phones inside Apple's multi-camera formats. To see what a given app actually gets on your phone, run the three checks above.

### Does iPhone 17 Dual Capture save two separate 4K files?

Apple's User Guide says Dual Capture records you and the action in front of you at the same time, and the specs pages list it at up to 4K Dolby Vision at 30 fps. It saves one picture-in-picture video, and Apple publishes no statement about separate front and back files. Record five seconds and count the items in Photos to see what your model saves.

### Is a 4K front and back video better than an HD one?

Only if the 4K came from the cameras. A 3840 x 2160 file built from HD feeds has the same detail as the HD file at four times the size. Check the originals' pixel size and do the detail test above.

**Try ContentCam free.** Front & Back records the selfie and rear cameras as two separate HD files on every iPhone with iOS 18 and on capable Android phones, and the layout is your choice afterwards. No ads, no watermark.

★ Rated 4.8 by 580+ creators on the [App Store](https://apps.apple.com/us/app/contentcam-dual-camera-video/id6765881795) and [Google Play](https://play.google.com/store/apps/details?id=app.contentcam.android). [](https://apps.apple.com/us/app/contentcam-dual-camera-video/id6765881795?pt=128838819&ct=b-iphone-4k-front-and-back-camera&mt=8) [](https://play.google.com/store/apps/details?id=app.contentcam.android&referrer=utm_source%3Dblog%26utm_campaign%3Diphone-4k-front-and-back-camera-same-time)

Related: [iPhone 17 Dual Capture limitations](https://contentcam.app/blog/iphone-17-dual-capture-limitations/) · [recording front and back at the same time on iPhone](https://contentcam.app/blog/record-front-and-back-camera-same-time-iphone/) · [front and back on iPhone 15 and 16](https://contentcam.app/blog/record-front-and-back-camera-iphone-15-16/) · [do you need to film in 4K](https://contentcam.app/blog/do-you-need-to-film-in-4k/)

Sources, checked 11 November 2026: US App Store listings for Dualgram (id1474345188, version 2.5), DualCam: Dual Camera Recorder (id6761523366, version 1.0.5), 2Cam Dual Shot Camera Recorder (id6444588083, version 1.5.2), Lookout Dual Camera Recorder (id6744577632, version 5.9) and MixCam (id1477390597, version 1.48); MixCam's Google Play listing (co.mixcord.mixcam); the [Dualgram user guide](https://dualgram.com/guide); Apple Developer documentation, [AVCaptureMultiCamSession](https://developer.apple.com/documentation/avfoundation/avcapturemulticamsession), [isMultiCamSupported](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/ismulticamsupported), [hardwareCost](https://developer.apple.com/documentation/avfoundation/avcapturemulticamsession/hardwarecost) and [systemPressureCost](https://developer.apple.com/documentation/avfoundation/avcapturemulticamsession/systempressurecost); Apple specs pages for [iPhone 17](https://www.apple.com/iphone-17/specs/), [iPhone Air](https://www.apple.com/iphone-air/specs/), [iPhone 18 Pro](https://www.apple.com/iphone-18-pro/specs/) and [iPhone Duo](https://www.apple.com/iphone-duo/specs/); Apple iPhone User Guide, [Record a video](https://support.apple.com/guide/iphone/record-a-video-iph61f49e4bb/ios) and [See photo and video information](https://support.apple.com/guide/iphone/see-photo-and-video-information-iph0edb9c18f/ios). ContentCam behaviour checked in the iOS app's source code; camera format list from ContentCam's test build on iPhone 18 Pro, iOS 27.0.1, 10 November 2026.
