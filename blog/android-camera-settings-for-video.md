# What Are the Best Android Camera Settings for Video in 2026?

Source: https://contentcam.app/blog/android-camera-settings-for-video/

Open Camera, Blackmagic Camera and your phone's Pro mode compared, plus the settings to change first. Why two Android phones running the same app behave differently, and what to do about it.

By Jimmy, developer of ContentCam · 21 September 2026

**Disclosure first:** ContentCam is [on Android](https://contentcam.app/android/), so I have an interest here. Every claim about another app is read from its own Play listing or its developer's own site on **21 September 2026**, and the app I would actually recommend to most people in this post is free and is not mine.

Most "best camera settings" guides are written for iPhone and then relabelled. Android has a structural difference that changes the answer, and nobody explains it: **what your phone can do depends on what its manufacturer chose to expose**, not on what the app can ask for. Two phones running the identical app will offer different settings. That is not a bug in the app.

## Why do two Android phones running the same camera app behave differently?

Because of [Camera2](https://developer.android.com/media/camera/camera2), the Android API that lets an app control the camera manually. Camera2 defines **hardware support levels**, and the manufacturer decides which one a given phone reports: LEGACY, LIMITED, FULL or LEVEL_3.

A phone reporting LEGACY gives an app almost no manual control, no matter how good the app is. A phone at FULL or LEVEL_3 exposes manual ISO, shutter, focus and more. This is why a mid-range phone can have an excellent sensor and still refuse to let any third-party app set the shutter speed, and it is why the answer to "why can't I change this setting" is usually the phone, not the software.

Open Camera's own site says the same thing plainly: several of its features, including **slow motion video and log profile video**, are listed as dependent on Camera2 support. Check what your phone reports before you go hunting for an app that will fix it.

## Which camera apps are worth having on Android in 2026?

Three, and two of them are free.

| App | Developer | Cost | Last updated | Installs | Rating |
| --- | --- | --- | --- | --- | --- |
| **Open Camera** | Mark Harman | Free, GPL v3, no ads in the app | 28 May 2026 | **100M+** | 4.0 (288K) |
| **Blackmagic Camera** | Blackmagic Design | Free, no subscription | **3 Sep 2026** | 1M+ | **4.5 (14.4K)** |
| **Your phone's Pro mode** | Samsung, Google, others | Already installed | With the system | n/a | n/a |

Google Play listings, read 21 September 2026. For contrast, [Filmic Pro's Android build has not been updated since 5 November 2025](https://contentcam.app/blog/what-happened-to-filmic-pro/), so the free options are currently better maintained than the paid incumbent.

## Which Android camera app should you install first?

**Blackmagic Camera, if your phone is supported.** It is free with no subscription and no unlock, it comes from a company that builds actual cinema cameras, and at 4.5 stars it is the best-rated serious camera app on Android. The catch is device support: Blackmagic restricts it to a named device list of recent Samsung Galaxy, Google Pixel, OnePlus, Xiaomi, Sony Xperia, Oppo and Vivo models, and its own listing warns that "some features are device dependent and may not be available on your device." Install it first and find out in thirty seconds.

**Open Camera if Blackmagic will not run.** It is free, GPL v3, written by Mark Harman, and has passed **100 million installs**. Its developer states there are no third-party ads in the app. The 4.0 rating is lower than Blackmagic's, and that is fair: it is a utility with a dense interface, not a designed product. It is also the app most likely to expose whatever your particular phone is capable of, because exposing the hardware is the entire point of it.

## What settings should you change in Open Camera for video?

In order of how much difference each one makes.

1. **Resolution to 4K, not 1080.** The extra pixels are crop room and stabilisation room, not delivery quality. Shoot big, finish small.
2. **Frame rate to 30.** 24 for a filmic cadence, 60 only for footage you will slow down. 60fps played at normal speed reads like a home camcorder.
3. **Lock exposure before the take.** The single biggest amateur tell on Android is the picture brightening and darkening every time you turn.
4. **White balance to a fixed number, not auto.** Roughly 5600K in daylight, 3200K under household bulbs. Auto white balance shifts mid-take and it is very hard to fix later.
5. **ISO as low as the light allows.** ISO is gain. Every step up adds noise that no edit removes.
6. **Shutter to about double the frame rate.** 1/60 at 30fps, 1/48 at 24fps. This is the 180 degree rule and it is why motion looks natural rather than stuttery.
7. **Video bitrate up, if your phone offers it.** Bitrate decides how much detail survives compression, and it matters more than resolution.
8. **Audio source to the best available.** Then get the phone closer to the person talking, which beats every setting on this list.

Items 3 to 6 are the ones a LEGACY phone may simply not offer. If they are greyed out, that is your answer about the hardware.

## Should you use Samsung Pro mode or Pixel's camera instead?

For a quick shot, yes. The manufacturer's own app has access to processing that third-party apps do not, which is why a Pixel's standard video often looks better than the same scene shot manually in a third-party app by someone who is not careful.

Use a third-party app when you need something the stock camera will not give you: a locked white balance that stays locked, a specific shutter, a flat profile to grade, or two framings from one take. Use the stock camera when you need to look good with no setup. Both answers are correct at different times, and the confident blanket recommendation in either direction is wrong.

## What Android video settings actually make footage look worse?

| Setting | What it costs you |
| --- | --- |
| Auto exposure left on | Brightness pumps every time you move |
| Auto white balance left on | Colour shifts mid-take, hard to fix afterwards |
| 60fps as the default | Reads like a camcorder, doubles your file size |
| Recording at 1080 | No crop room and no room to stabilise |
| Beauty or skin smoothing on | Texture is removed at capture. It does not come back |
| Ultrawide for faces | Smallest sensor, worst low light, distorted at the edges |
| Digital zoom | A crop pretending to be a lens. Step closer |
| HDR video on | Looks right on your phone, unpredictable after a platform re-encodes it |

## Where does ContentCam fit on Android?

It solves one problem and it is not "better manual controls." ContentCam records [vertical and horizontal at the same time](https://contentcam.app/blog/record-portrait-and-landscape-video-same-time-iphone/) from one take, so the widescreen version is a real wide shot rather than a crop of a tall one. It also has Front / Back mode on Android, manual white balance with temperature and tint dials, and manual ISO and shutter on phones whose cameras support it.

Two things on it are relevant to everything above. First, it checks what your camera actually exposes and only offers what it can deliver, rather than showing you a control that does nothing, which is the Camera2 problem from the top of this post handled at the app level. Second, its Play Data Safety label reads **no data collected**, because there are no accounts, no analytics and no tracking SDKs in it (the only Google libraries are Play Billing and the update check).

The honest boundaries: it does not shoot Log or ProRes, 10-bit HDR and the 0.5x ultra-wide in Front & Back are iPhone-only, and if what you want is the deepest manual control your specific phone can expose, Open Camera is more likely to surface it. Install Blackmagic Camera or Open Camera for cinema work. Install ContentCam if you are posting the same take to more than one place.

## Frequently asked questions

**Is Open Camera free?** Yes. It is released under GPL v3 and its developer, Mark Harman, states there are no third-party ads in the app.

**Does Blackmagic Camera work on Android?** Yes, and it was updated on 3 September 2026. It is restricted to specific Samsung Galaxy and Google Pixel models, so check it installs on your phone before planning around it.

**Why can't I change ISO or shutter speed in my camera app?** Because your phone reports a low Camera2 hardware support level. The manufacturer decides that, not the app, and no app can work around it.

**What frame rate should I record at on Android?** 30fps for almost everything. 24fps for a filmic cadence, 60fps only when you intend to slow the footage down in an edit.

**Should I record in 4K on Android?** Yes, if you have the storage. The benefit is crop and stabilisation room rather than delivered sharpness, since most platforms re-encode what you upload anyway.

**Is Filmic Pro still good on Android?** Its Android build was last updated 5 November 2025, while Blackmagic Camera updated 3 September 2026. The free option is better maintained.

**Try ContentCam free on Android.** One take, a vertical file and a widescreen file, no reshoot.

★ Rated 4.8 by 580+ creators on the [App Store](https://apps.apple.com/app/id6765881795) and [Google Play](https://play.google.com/store/apps/details?id=app.contentcam.android). [](https://play.google.com/store/apps/details?id=app.contentcam.android&referrer=utm_source%3Dblog%26utm_campaign%3Dandroid-camera-settings-for-video) [](https://apps.apple.com/app/apple-store/id6765881795?pt=128838819&ct=b-android-camera-settings-for-video&mt=8)

App figures were read from Google Play and [opencamera.org.uk](https://opencamera.org.uk/) on 21 September 2026. Camera2 hardware support levels are documented at [developer.android.com](https://developer.android.com/media/camera/camera2). If something here is out of date, [email me](mailto:contentcam.app@gmail.com) and I will fix it. Related: [record portrait and landscape at the same time on Android](https://contentcam.app/blog/record-portrait-and-landscape-video-same-time-android/) · [how to record landscape video on Android](https://contentcam.app/blog/how-to-record-landscape-video-on-android/) · [what happened to Filmic Pro](https://contentcam.app/blog/what-happened-to-filmic-pro/) · [iPhone manual camera controls for video](https://contentcam.app/blog/iphone-manual-camera-controls-video/) · [24 vs 30 vs 60fps for social](https://contentcam.app/blog/24fps-vs-30fps-vs-60fps-social-media/).

Related: [front and back on Google Pixel](https://contentcam.app/blog/record-front-and-back-camera-google-pixel/) · [front and back on Samsung Galaxy](https://contentcam.app/blog/record-front-and-back-camera-samsung-galaxy/)
