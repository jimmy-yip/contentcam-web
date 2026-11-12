# Can You Record Front and Back Camera at the Same Time on a Google Pixel? (2026)

Source: https://contentcam.app/blog/record-front-and-back-camera-google-pixel/

Pixel Camera has no front and back video mode on any Pixel, including the Fold. What Dual screen preview and Add Me actually do, which Pixels let apps run both cameras, and how to check yours.

By Jimmy, developer of ContentCam · 9 October 2026 · Updated 5 November 2026

Not in Pixel Camera. Google's own camera app has no front and back video mode on any Pixel, including the Pixel Fold models. A Google Pixel can record both cameras at once only in a third-party app, and only if that Pixel's camera system reports that the front and back cameras can run together. ContentCam's Front & Back mode does this: it checks your Pixel first, then records the selfie and rear cameras from one press as two separate files.

Disclosure: I build ContentCam, so I'm not neutral. The Pixel facts below come from Google's help pages and Android developer documentation, checked 5 November 2026. For Samsung Galaxy and other Android brands, see [recording front and back on Android](https://contentcam.app/blog/record-front-and-back-camera-same-time-android/).

## Does Pixel Camera have a front and back camera mode?

No. Google's Pixel Camera Help page "Record a video on your Pixel phone" covers Video mode, Slow motion, Time Lapse, Cinematic Blur, Cinematic Pan, 10-bit HDR and video up to 4K at 60fps. None of those modes records the selfie camera and the rear camera together, and there is no picture-in-picture or split-screen option. The Pixel 11's new Creator Suite and Magic Capture don't add one either.

## Is Dual screen preview on the Pixel Fold the same thing?

No. Dual screen preview uses two screens, not two cameras. Google says it "allows your subject to see themselves while you record the video" on the Pixel Fold, Pixel 9 Pro Fold, Pixel 10 Pro Fold and Pixel 11 Pro Fold. The video still comes from one camera.

## Is Add Me on the Pixel 9 and Pixel 10 a dual camera feature?

No. Google's blog describes Add Me as a way to "combine two pictures taken during the same session and in the same scene" so the photographer ends up in the group photo. The Google Store lists it on "all Pixel 9 and Pixel 10 phones". Add Me works on still photos and never runs the front and back cameras together.

## Which Google Pixel phones can record front and back in an app?

Google doesn't publish a model list, and I won't guess one. Support depends on the phone's camera hardware, and Android tells apps about it in two ways:

- **CameraManager.getConcurrentCameraIds()**, added in Android 11 (API level 30), returns the sets of cameras that "support configuring camera device sessions concurrently".
- **The feature flag android.hardware.camera.concurrent** (FEATURE_CAMERA_CONCURRENT) means "the device's main front and back cameras can stream concurrently".

If a Pixel reports neither, no app using Android's official camera route can record both cameras on it. The Android Open Source Project explains why: the phone's image signal processor (ISP) has to split its resources between the two cameras.

## How do you check if your Pixel supports front and back recording?

1. Easiest: install ContentCam. If Front & Back appears, your Pixel supports it.
2. With a computer: turn on USB debugging, connect the Pixel and run adb shell pm list features. If the list includes android.hardware.camera.concurrent, the main front and back cameras can stream together.

## What quality do you get recording both cameras on a Pixel?

Less than a normal Pixel Camera video. Android guarantees concurrent streams up to 1440p (1920 x 1440) per camera, and Google's CameraX 1.3 announcement puts the cap at "720p or 1440p, depending on the device." ContentCam's Front & Back mode records HD at up to 30fps on Android.

| Option on a Pixel | Records front and back at once? | What you get | Which Pixels |
| --- | --- | --- | --- |
| Pixel Camera Video mode | No | One camera, up to 4K at 60fps on supported models | All |
| Dual screen preview | No | One camera, viewfinder on both screens | Pixel Fold, 9 Pro Fold, 10 Pro Fold, 11 Pro Fold |
| Add Me | No | One group photo from two shots | Pixel 9 and Pixel 10 series |
| ContentCam Front & Back | Yes | Two separate HD files, up to 30fps, combine later into picture-in-picture or split screen | Pixels that report concurrent front and back cameras |

If you only need one angle, use Pixel Camera's own Video mode, which records up to 4K at 60fps on supported models. Front and back recording through Android's concurrent camera route is capped near 1440p per camera.

## How does ContentCam's Front & Back mode work on a Pixel?

ContentCam's Front & Back mode records the selfie camera and the rear camera together from one press and saves two separate files, so you can edit your face and the scene independently. The Combine editor can later render them into one picture-in-picture or split-screen video, keeping the originals. Front & Back photos work the same way: one press saves a selfie and a rear photo as two separate pictures.

- **Checks your Pixel first:** ContentCam reads the concurrent camera report and only shows Front & Back on Pixels that support it.
- **Free to try:** 5 free Front & Back recordings, then Premium for unlimited recordings, Front & Back photos and saving Combine videos.
- **No ads and no watermark** on the free plan or Premium, no account needed, and your footage stays on your phone.

Recording one take as 9:16 and 16:9 files is free: see [recording portrait and landscape at once on Android](https://contentcam.app/blog/record-portrait-and-landscape-video-same-time-android/).

## FAQ

### Does Pixel Camera have a dual camera or front and back video mode?

No. No video mode in Google's Pixel Camera Help records the front and back cameras at the same time, on any Pixel model (checked 5 November 2026).

### Which Pixel phones can record front and back in a third-party app?

Google does not publish a list. A Pixel needs to report a front and back pair through getConcurrentCameraIds() (Android 11 and later) or the android.hardware.camera.concurrent feature.

### What app records front and back camera at the same time on a Google Pixel?

ContentCam's Front & Back mode records both cameras from one press as two separate HD files, on Pixels that support it. The first 5 Front & Back recordings are free.

### What quality is front and back recording on a Pixel?

Lower than a normal Pixel video. Android guarantees concurrent streams up to 1440p per camera, and ContentCam records HD at up to 30fps.

**Try ContentCam free.** Front and back in one take as two separate files where your phone supports it, plus vertical and wide from a single shoot. Free to download on Android and iPhone.

 Rated 4.8 by 580+ creators on the [App Store](https://apps.apple.com/us/app/contentcam-dual-camera-video/id6765881795) and [Google Play](https://play.google.com/store/apps/details?id=app.contentcam.android). [](https://apps.apple.com/us/app/contentcam-dual-camera-video/id6765881795?pt=128838819&ct=b-front-back-google-pixel&mt=8) [](https://play.google.com/store/apps/details?id=app.contentcam.android&referrer=utm_source%3Dblog%26utm_campaign%3Drecord-front-and-back-camera-google-pixel)

Related: [front and back on any Android phone](https://contentcam.app/blog/record-front-and-back-camera-same-time-android/) · [the best front and back camera apps](https://contentcam.app/blog/best-front-and-back-dual-camera-apps/) · [Android camera settings for video](https://contentcam.app/blog/android-camera-settings-for-video/) · [ContentCam for Android](https://contentcam.app/android/)

Sources: Google, Pixel Camera Help, "Record a video on your Pixel phone" (support.google.com/pixelcamera); Google, Pixel Camera Help, "Explore your Pixel Fold camera", "Use Pixel Camera Creator Suite" and "Use Magic Capture on a Pixel phone" (support.google.com/pixelcamera); Google, "How we built Pixel's Add Me feature" (blog.google) and the Google Store Add Me page (store.google.com); Android Developers, CameraManager.getConcurrentCameraIds() and PackageManager.FEATURE_CAMERA_CONCURRENT; Android Open Source Project, "Concurrent camera streaming" (source.android.com); Android Developers Blog, "CameraX 1.3 is now in beta" (June 2023). Checked 5 November 2026.
