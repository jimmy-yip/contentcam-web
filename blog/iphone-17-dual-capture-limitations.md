# Which iPhones Have Dual Capture? Full List + 4 Limits (2026)

Source: https://contentcam.app/blog/iphone-17-dual-capture-limitations/

Seven iPhones have Dual Capture. iPhone 16 and 17e do not. It records front and back at up to 4K 30 fps into one picture-in-picture file. The limits, and what to use instead.

By Jimmy, developer of ContentCam · 28 September 2026 · Updated 9 November 2026

**Short answer:** Apple lists seven iPhones with Dual Capture: iPhone 17, iPhone 17 Pro, iPhone 17 Pro Max, iPhone Air, iPhone 18 Pro, iPhone 18 Pro Max and iPhone Duo. iPhone 16, iPhone 16e and iPhone 17e do not have it. Dual Capture is a video mode in the Camera app, capped at 4K Dolby Vision at 30 fps, and it saves one file with your face inset in the corner. If your iPhone is not on that list, or you want the two cameras as two separate files, ContentCam's Front & Back mode records both cameras at once on any iPhone running iOS 18 (iPhone XS and later, including iPhone 15 and iPhone 16) and on Android phones whose cameras support it.

**Disclosure first:** I build ContentCam, so I am an interested party. That is why every Dual Capture figure below is tied to an Apple page, all checked on **5 November 2026**.

## What is iPhone 17 Dual Capture, and what does it record?

Dual Capture records the front and rear cameras at once in the stock Camera app. Apple's published ceiling, **"Dual Capture up to 4K Dolby Vision at 30 fps"**, appears on the [iPhone 17](https://www.apple.com/iphone-17/specs/), [iPhone Air](https://www.apple.com/iphone-air/specs/), [iPhone 18 Pro](https://www.apple.com/iphone-18-pro/specs/) and [iPhone Duo](https://www.apple.com/iphone-duo/specs/) specs pages.

Apple's iOS 27 iPhone User Guide page [Record a video with your iPhone camera](https://support.apple.com/en-au/guide/iphone/iph61f49e4bb/27/ios/27) gives the steps (Camera, Video mode, camera controls, Dual Capture) and captions its illustration "A window in the top-left of the frame displays what the front-facing camera is recording, and the rest of the frame displays what the back camera is recording." One frame, front camera inset, rear camera behind it.

Dual Capture also works in FaceTime: flipping the camera on a call on a supported iPhone turns it on, and iOS 27.2 (released 26 October 2026) extended it to Group FaceTime calls, [MacRumors reported](https://www.macrumors.com/2026/10/26/ios-27-2-dual-capture-facetime/). It's the same one-frame picture-in-picture, streamed live rather than saved.

## Which iPhones support Dual Capture?

Seven models. Apple's guide page [Models that support Dual Capture video](https://support.apple.com/en-au/guide/iphone/aside/glos3842gv5b/27/ios/27) lists:

- iPhone 17
- iPhone 17 Pro
- iPhone 17 Pro Max
- iPhone Air
- iPhone 18 Pro
- iPhone 18 Pro Max
- iPhone Duo

The [iPhone 16](https://www.apple.com/iphone-16/specs/), [iPhone 16e](https://www.apple.com/iphone-16e/specs/) and [iPhone 17e](https://www.apple.com/iphone-17e/specs/) specs pages do not mention Dual Capture anywhere, and no iOS update adds it. Third-party apps have had Apple's [AVCaptureMultiCamSession](https://developer.apple.com/documentation/avfoundation/avcapturemulticamsession) since iOS 13.0, which is how ContentCam records both cameras on older iPhones; see [front and back on iPhone 15 and 16, without Dual Capture](https://contentcam.app/blog/record-front-and-back-camera-iphone-15-16/).

## Why is Dual Capture capped at 30 fps when the same iPhone shoots 4K60?

Apple gives no reason. The iPhone 17 specs page shows the drop:

| iPhone 17 rear camera mode | Apple's published ceiling |
| --- | --- |
| Normal video recording | 4K Dolby Vision at 24, 25, 30 or **60 fps** |
| QuickTake video | up to 4K Dolby Vision at **60 fps** |
| Action mode | up to 2.8K Dolby Vision at **60 fps** |
| Slo-mo | 1080p at 120 fps or 240 fps |
| **Dual Capture** | up to 4K Dolby Vision at **30 fps** |

[30 fps is fine for talking heads](https://contentcam.app/blog/24fps-vs-30fps-vs-60fps-social-media/), but leaves nothing to slow down. Two cameras at once are rationed by the operating system: Apple's documentation for [isMultiCamSupported](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/ismulticamsupported) says "Only this limited subset of capture formats can run sustainably in a multi-camera capture scenario", and every iPhone ContentCam has run on tops out at **1920×1440** for those formats. Inside that HD ceiling, ContentCam's Front & Back records at **up to 60 fps** on iPhones that support it (60 fps is Premium, and some older iPhones cap at 30 fps).

## Does Dual Capture give you two separate video files?

No. Everything Apple documents points to one composited recording: one spec line, one frame in the illustration, the front camera described as a window inside it. Apple publishes no statement on the file count; record five seconds and count the items in Photos.

## What can you not do with a Dual Capture video afterwards?

1. **Cut to one angle.** The inset covers the top-left of every frame, so there is no clean rear-only shot.
2. **Move, resize or swap the layout.** The inset position is baked into the pixels.
3. **Reframe for a second platform.** Cropping a 3840×2160 take to 9:16 keeps 1215×2160, about 32% of the width, and cuts off the top-left inset. See [recording vertical and horizontal at once](https://contentcam.app/blog/record-portrait-and-landscape-video-same-time-iphone/).
4. **Grade the two feeds separately.** One file, one colour pipeline.

## How does ContentCam Front & Back compare with Dual Capture?

ContentCam's Front & Back saves the front and rear cameras as **two separate video files**, never a live composite. The layout is a decision you make afterwards: the Combine editor renders the two files into a [picture-in-picture or split-screen video](https://contentcam.app/blog/split-screen-video-iphone/) and keeps the originals.

|  | Apple Dual Capture | ContentCam Front & Back |
| --- | --- | --- |
| iPhones | The 7 models listed above | Any iPhone on iOS 18 (iPhone XS, XR and later) |
| Android | No | Yes, where the phone can run both cameras at once |
| Output | One composited file | Two separate files |
| Layout | Fixed at capture | Chosen afterwards (picture-in-picture or split-screen) |
| Frame rate | 30 fps | Up to 60 fps on supported iPhones (Premium); 30 fps on Android |
| Resolution | Up to 4K | HD |

Two files means you can cut to either angle or grade each one separately. ContentCam has no ads and no watermark, the first 5 Front & Back recordings are free, then Premium makes them unlimited; saving a Combine video is Premium too.

Who Dual Capture suits: anyone on a supported iPhone who wants 4K from both cameras and will post the clip exactly as recorded. One Front & Back take in ContentCam: the rear camera and the selfie camera as two separate files, not one picture-in-picture frame.

## Frequently asked questions

**What frame rate does iPhone 17 Dual Capture record at?** Apple's specs pages list "Dual Capture up to 4K Dolby Vision at 30 fps". The same rear camera records normal video at up to 4K Dolby Vision at 60 fps, so Dual Capture halves the frame rate.

**Does Dual Capture work on iPhone 16?** No. The iPhone 16, iPhone 16e and iPhone 17e specs pages do not mention Dual Capture, and Apple's list of supported models starts at iPhone 17. ContentCam's Front & Back works on iPhone 16.

**Can you move the picture-in-picture window in Dual Capture?** Apple's published steps for the mode do not mention repositioning or resizing it. Wherever the window sits when you stop recording is where it stays in the file.

**Can third-party iPhone apps record 4K with two cameras at once?** No. Multi-camera formats on every iPhone ContentCam has run on top out at 1920×1440, so Dual Capture is the only 4K two-camera option on iOS.

**Try ContentCam free.** Front & Back records both cameras as two separate files on any iPhone running iOS 18 and on supported Android phones.

★ Rated 4.8 by 580+ creators on the [App Store](https://apps.apple.com/us/app/contentcam-dual-camera-video/id6765881795) and [Google Play](https://play.google.com/store/apps/details?id=app.contentcam.android). [](https://apps.apple.com/us/app/contentcam-dual-camera-video/id6765881795?pt=128838819&ct=b-iphone-17-dual-capture-limitations&mt=8) [](https://play.google.com/store/apps/details?id=app.contentcam.android&referrer=utm_source%3Dblog%26utm_campaign%3Diphone-17-dual-capture-limitations)

Every Dual Capture figure above was checked on 5 November 2026 against the Apple pages linked; if one is out of date, [email me](mailto:contentcam.app@gmail.com). Related: [can an iPhone record 4K from the front and back camera at once](https://contentcam.app/blog/iphone-4k-front-and-back-camera-same-time/) · [the dual camera effect on any phone](https://contentcam.app/blog/dual-camera-effect/) · [front and back dual camera apps compared](https://contentcam.app/blog/best-front-and-back-dual-camera-apps/) · [how to film a reaction video on your phone](https://contentcam.app/blog/film-reaction-video-phone/) · [recording front and back at the same time on iPhone](https://contentcam.app/blog/record-front-and-back-camera-same-time-iphone/) · [what the iPhone Duo camera can and can't do](https://contentcam.app/blog/iphone-duo-camera/).
