# How to Record Vertical and Horizontal Video at the Same Time on Android: The App (2026)

Source: https://contentcam.app/blog/record-portrait-and-landscape-video-same-time-android/

Three ways to get 9:16 and 16:9 video from one Android take: crop in post, shoot 4K and reframe, or record both files at once. What each one costs.

By Jimmy, developer of ContentCam · 30 September 2026 · Updated 5 November 2026

**The short answer:** use an Android app that records both files at once from the full sensor. ContentCam does this on Android and iPhone: one take saves a 9:16 vertical file and a 16:9 horizontal file, free at 1080p, with no ads, no watermark and no account. The camera app that came with your phone can't do it, because Samsung Camera and Pixel Camera record in one shape per take. The free workarounds, cropping afterwards or shooting 4K and reframing, both lose most of the scene.

I build ContentCam, so check the maths below for yourself. The arithmetic is the same whichever tool you pick.

## Can the stock Android camera record portrait and landscape at once?

No. Stock Android camera apps record one shape per take.

- **Samsung Camera** has an aspect ratio setting; Samsung's support page lists 1:1, 3:4, 9:16 and Full Screen, noting that "available ratios may vary depending on your device's camera specifications." You choose one. The phone records one.
- **Pixel Camera**: Google's Pixel Camera help documents aspect ratios for photos only (Wide crop 16:9, Full image 4:3), none for video. A Pixel video is horizontal or vertical depending on how you hold the phone.
- **Google Photos** can crop a finished video to a different aspect ratio afterwards. That is Option 1 below, with the same cost.

## Option 1: How much do you lose cropping landscape video to portrait?

You keep 31.6% of the width and throw away 68.4% of the scene. For a 1080p landscape video:

- The landscape frame is 1920×1080.
- A 9:16 crop at full height is 1080 × 9 ÷ 16 = **607.5 pixels wide**.
- 607.5 ÷ 1920 = **0.316**, so 31.6% of the width survives.

That 607×1080 strip is then scaled up 1.78 times to 1080×1920 for TikTok, Reels or Shorts, which is why cropped verticals look soft. Avoid cropping for travel, sport, product shots, or any scene where the background matters.

## Option 2: Can you shoot 4K landscape and reframe it as vertical?

Yes, and it is the best free workaround. A 9:16 crop from a 3840×2160 frame is 2160 × 9 ÷ 16 = **1215×2160 pixels**, which is more than the 1080×1920 a vertical platform plays. The resolution problem from Option 1 goes away.

The framing problem stays: the vertical is still 31.6% of the landscape width, so the subject must sit dead centre and anything composed for the wide shot (a skyline, a second person) falls outside it. You also edit every video twice, and 4K files are four times the pixels of 1080p.

## Option 3: How do you record both formats at once on Android?

Record the sensor's full 4:3 frame, which is wider than 9:16 and taller than 16:9, and cut both shapes from it during capture. On an illustrative 4000×3000 sensor:

| Method | Vertical slice of a 4000×3000 sensor | Share of sensor area |
| --- | --- | --- |
| Record 16:9, crop 9:16 later | about 1266×2250 | 24% |
| Crop 9:16 from the full 4:3 frame | about 1688×3000 | 42% |

The full-frame vertical sees 1.78 times more of the scene, and the 16:9 landscape keeps the sensor's full width (4000×2250). Neither file is a crop of the other.

This is how [ContentCam for Android](https://contentcam.app/android/) works. One take saves a 9:16 file and a 16:9 file, on the rear and front cameras. On phones that expose an ultra-wide lens, a 0.5× option gives both crops a wider view. If you hold the phone sideways, both files are tagged with the right orientation so they play upright in CapCut or Premiere. The free tier records unlimited takes in both formats at 1080p and up to 30fps, with no ads and no watermark; [Premium](https://contentcam.app/pricing/) adds 4K and 60fps where the phone's hardware supports them.

Compared with Options 1 and 2, nothing is cropped after the fact, you frame each take once, and you don't edit every video twice.

One limit: Dual Lens mode, which records the wide and ultra-wide lenses at the same moment, is iPhone only for now.

## Which option should you use on Android?

| Your situation | Best option |
| --- | --- |
| You post both shapes regularly and want each to look framed on purpose | Record both at once (Option 3, recommended) |
| Travel, sport or product shots where the background matters | Record both at once (Option 3) |
| Selfie camera | Record both at once, it works on the front camera |
| Phone records 4K, subject stays centred, you don't mind editing twice | Shoot 4K and reframe (Option 2) |
| Talking head, face fills the frame, landscape is a one-off bonus | Crop in post (Option 1) |

## Frequently asked questions

**Can an Android phone record portrait and landscape video at the same time?** Not with the stock camera apps. Samsung Camera and Pixel Camera record in one shape per take. A third-party app that records from the full 4:3 sensor frame can save a 9:16 portrait file and a 16:9 landscape file from the same take.

**Is there an Android app for simultaneous landscape and portrait video recording?** Yes. ContentCam for Android records a 9:16 portrait file and a 16:9 landscape file from one take, on the rear and front cameras, at 1080p on the free tier, with no ads or watermark.

**How much of the picture do you lose cropping 16:9 video to 9:16?** About 68%. A 9:16 crop at the full height of a 1920x1080 frame is 607.5 pixels wide, which is 31.6% of the 1920-pixel width. The other 68.4% of the scene is discarded.

**Can I record front and back cameras at the same time on Android for reaction videos?** Yes. ContentCam's Front & Back mode records the front and rear cameras in one take on Android phones whose cameras can run together, saved as two separate HD files at up to 30fps. The Combine editor can then turn them into one picture-in-picture or split-screen video. It is a Premium feature with 5 free recordings to try.

**Does filming in 4K on Android let me crop a vertical video out of a landscape one?** Yes, with enough resolution left over. A 9:16 crop from a 3840x2160 frame is 1215x2160 pixels, which is more than a 1080x1920 vertical video needs. The framing is still a narrow slice of the landscape shot, so the subject has to be centred when you film.

**Stop filming everything twice.** ContentCam is free on Google Play; record a take and look at both files before deciding anything.

 Rated 4.8 by 580+ creators on the [App Store](https://apps.apple.com/us/app/contentcam-dual-camera-video/id6765881795) and [Google Play](https://play.google.com/store/apps/details?id=app.contentcam.android). [](https://play.google.com/store/apps/details?id=app.contentcam.android&referrer=utm_source%3Dblog%26utm_campaign%3Drecord-portrait-and-landscape-video-same-time-android) [](https://apps.apple.com/us/app/contentcam-dual-camera-video/id6765881795?pt=128838819&ct=b-portrait-landscape-android&mt=8)

Stock camera details were read from [Samsung's support page on camera ratio](https://www.samsung.com/ae/support/mobile-devices/adjusting-the-camera-ratio-on-my-samsung-phone/), [Pixel Camera Help](https://support.google.com/pixelcamera/answer/2838995?hl=en-GB) and [Google Photos Help](https://support.google.com/photos/answer/10729480?hl=en&co=GENIE.Platform%3DAndroid), checked 5 November 2026. Related: [how to record landscape video on Android](https://contentcam.app/blog/how-to-record-landscape-video-on-android/) · [the iPhone version of this guide](https://contentcam.app/blog/record-portrait-and-landscape-video-same-time-iphone/) · [best Android camera settings for video](https://contentcam.app/blog/android-camera-settings-for-video/) · [vertical vs horizontal video](https://contentcam.app/blog/why-cropping-vertical-to-horizontal-looks-wrong/)
