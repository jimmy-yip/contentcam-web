# How to Record Front and Back Camera at the Same Time on Samsung Galaxy (2026)

Source: https://contentcam.app/blog/record-front-and-back-camera-samsung-galaxy/

Samsung renamed Director's View to Dual recording, and on One UI 8.5 it moved into Video mode. Which Galaxy phones have it, how to turn it on, whether it saves separate files, and the apps that do it on other Galaxy models.

By Jimmy, developer of ContentCam · 10 October 2026 · Updated 5 November 2026

To record the front and back camera at the same time on a Samsung Galaxy, use Dual recording in the Samsung Camera app: on One UI 8.5 it sits in Video mode under Quick controls, on older software under More. Dual recording is the new name for Director's View. For your face and the scene as two separate files, the Samsung Camera app only does that on the Galaxy S22 and S23; on every other Galaxy that can run both cameras at once, ContentCam's Front & Back mode records the selfie and the rear camera as two separate files in one take.

Disclosure: I build ContentCam, so I'm not neutral. Samsung claims come from Samsung's support pages, other apps' details from their Google Play listings and reviews, checked 5 November 2026. For Pixel and other Android phones, see [recording front and back at the same time on Android](https://contentcam.app/blog/record-front-and-back-camera-same-time-android/).

## What happened to Director's View on the Galaxy S24 and S25?

Samsung renamed Director's View to Dual recording. Samsung US support says "Director's View is not available on the Galaxy S24 series or S25 series," and Samsung Gulf's "Director's View Missing in Camera?" (updated 1 July 2026) explains: "The Director's view menu has been renamed to Dual recording in newer Samsung Galaxy devices."

## Which Samsung Galaxy phones have Dual recording?

Samsung lists five groups as supporting Dual recording:

- Galaxy S24 series
- Galaxy S25 series
- Galaxy Z Fold series
- Galaxy Z Flip series
- Galaxy A series (select models, which Samsung doesn't name)

Samsung lists FHD or UHD at 30fps, Front + Rear and Rear + Rear on newer models; the Galaxy S23 series was limited to FHD 30fps, Front + Rear.

## How do you turn on Dual recording on One UI 8.5?

Samsung's US support page says that from One UI 8.5, Dual rec "has been integrated into the Video menu":

1. Open the **Camera** app and tap **Video**.
2. Tap the **Quick controls** icon (the four circles).
3. Tap **Dual recordings** (a square with a smaller square in the corner) and record.

To make Dual rec its own mode again, turn it on under Additional modes in **Camera Assistant** (Samsung India labels it "Downloadable"); it then shows under **More**. Before One UI 8.5, the path is Camera, More, Dual recording (or Director's View on older models).

## Does Samsung Dual recording save two separate files?

Only on the Galaxy S22 and S23 series. Samsung's support page says S22 and S23 owners can tap the Download icon before recording to save the two videos separately, and that "this setting is not currently available on any other device besides the S22 series and S23 series." Everywhere else, Dual recording saves one video with picture-in-picture or split screen baked in, chosen before you press record.

## How do you check if a Galaxy can run both cameras in other apps?

Android 11 added the feature flag android.hardware.camera.concurrent, which Android Developers defines as "the device's main front and back cameras can stream concurrently." Google's Android Developers Blog post on CameraX 1.3 puts the two-camera ceiling at "720p or 1440p", depending on the phone.

The easy check is an app that tests the phone: ContentCam only offers Front & Back where both cameras can run, so the mode either works or isn't shown. Reviews show why a check matters: 2 of the last 39 Google Play reviews of Dual Cam: Front and Back Video (VysionApps) say it would not record both cameras, including "You cannot activate both comeras and record at the same time." (1 star, 26 September 2026). With a computer, adb shell pm list features shows android.hardware.camera.concurrent if the phone has it.

## Which apps record front and back on a Samsung Galaxy?

| Option | What it saves | Needs | Cost (per listing) |
| --- | --- | --- | --- |
| **ContentCam (Front & Back mode)** | Two separate files, HD at up to 30fps, recorded in sync. The rear camera records vertical or horizontal. Combine into PiP or split screen afterwards, originals kept. | Any Galaxy that can run both cameras at once; the app checks. Also on iPhone. | Free app, 5 free Front & Back recordings, then Premium. No ads, no watermark. |
| Samsung Dual recording | One video (PiP or split) with the layout fixed at capture; separate files on S22 and S23 only. Up to UHD 30fps on newer models. | A Galaxy on Samsung's list | Built in |
| Dual Cam: Front and Back Video (VysionApps) | One combined video | Android | Free, in-app purchases |

For most Galaxy owners who want the face and the scene as separate clips, ContentCam is the pick: two files from one take on any Galaxy that can run both cameras, a vertical or horizontal rear camera, and the same app on iPhone if you switch phones. Samsung's built-in Dual recording is already installed on listed models and saves one picture-in-picture clip. More apps are in [the best front and back camera apps](https://contentcam.app/blog/best-front-and-back-dual-camera-apps/).

## How do you record front and back on a Galaxy in ContentCam?

1. Install [ContentCam from Google Play](https://play.google.com/store/apps/details?id=app.contentcam.android&referrer=utm_source%3Dblog%26utm_campaign%3Drecord-front-and-back-camera-samsung-galaxy).
2. Switch the recording mode to Front & Back. If the mode isn't offered, your Galaxy can't run both cameras at once for apps.
3. Choose vertical or horizontal for the rear camera, then record once. The selfie and the rear camera save as two separate files, recorded in sync.

Two files means you can cut between face and scene, post them separately, or build one picture-in-picture or split-screen video in ContentCam's Combine editor (saving it is Premium). Lighting and audio tips are in the [reaction video guide](https://contentcam.app/blog/film-reaction-video-phone/).

## FAQ

### Is Director's View gone on the Galaxy S24 and S25?

Only the name. Samsung renamed Director's View to Dual recording, which Samsung lists for the Galaxy S24, S25, Z Fold, Z Flip and select Galaxy A models.

### Where is Dual recording on One UI 8.5?

From One UI 8.5, Samsung moved Dual rec into Video mode: open Camera, tap Video, tap Quick controls (four circles), then tap Dual recordings.

### Can a Samsung Galaxy save the front and back camera as two separate files?

In the Samsung Camera app, only the Galaxy S22 and S23 series, per Samsung. Other Galaxy models save Dual recording as one video. On any Galaxy that can run both cameras at once, ContentCam's Front & Back mode saves the selfie and the rear camera as two separate files.

### How do I check if my Galaxy can run the front and back camera at the same time?

The phone has to report Android's concurrent camera feature, android.hardware.camera.concurrent, added in Android 11. ContentCam checks the phone for you and only offers Front & Back where it works.

**Try ContentCam free.** Front and back in one take as two separate files, plus vertical and wide from a single shoot. Free to download on Android and iPhone.

★ Rated 4.8 by 580+ creators on the [App Store](https://apps.apple.com/app/id6765881795) and [Google Play](https://play.google.com/store/apps/details?id=app.contentcam.android). [](https://play.google.com/store/apps/details?id=app.contentcam.android&referrer=utm_source%3Dblog%26utm_campaign%3Drecord-front-and-back-camera-samsung-galaxy) [](https://apps.apple.com/app/apple-store/id6765881795?pt=128838819&ct=b-front-back-samsung-galaxy&mt=8)

Related: [front and back on any Android phone](https://contentcam.app/blog/record-front-and-back-camera-same-time-android/) · [the best front and back camera apps](https://contentcam.app/blog/best-front-and-back-dual-camera-apps/) · [the full dual camera guide](https://contentcam.app/blog/dual-camera-effect/) · [filming a reaction video on your phone](https://contentcam.app/blog/film-reaction-video-phone/)

Sources: Samsung US, "Use Director's View and Dual recording on your Galaxy phone" and "Dual recording missing in the Camera app on Galaxy phones" (samsung.com/us/support); Samsung Gulf, "Director's View Missing in Camera?" (updated 1 July 2026); Samsung India, "How to enable or run the Night, Single take & Dual rec modes" (updated 29 April 2026); Android Developers, CameraManager.getConcurrentCameraIds(), PackageManager.FEATURE_CAMERA_CONCURRENT and CameraX ConcurrentCamera; Android Developers Blog, "CameraX 1.3 is now in beta" (June 2023); Google Play listings for DuoCam, Dual Cam: Front and Back Video and DualCam Recorder, and the 39 most recent Google Play reviews of Dual Cam: Front and Back Video. Checked 5 November 2026.
