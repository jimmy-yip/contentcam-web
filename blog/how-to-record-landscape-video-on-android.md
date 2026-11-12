# How to Record Landscape Video on Android (2026)

Source: https://contentcam.app/blog/how-to-record-landscape-video-on-android/

Switch to Video, turn the phone sideways, then press record. Plus auto-rotate on Pixel and Samsung, why a clip plays sideways on a computer, and how to rotate it.

By Jimmy, developer of ContentCam · 29 October 2026

Open the Camera app, switch to Video, turn the phone sideways so the long edge runs left to right, then press record. That works in Pixel Camera and Samsung Camera alike. What goes wrong is everything around it: a Samsung ratio left on 1:1, an auto-rotate lock you are not sure about, and a clip that plays upright on the phone but sideways on a laptop.

The Pixel, Samsung and Android steps below were checked against Google's and Samsung's own help pages and the Android developer documentation on 28 October 2026. Where those pages say nothing, I say so instead of guessing.

## How do you record landscape video on an Android phone?

On a Google Pixel, in Pixel Camera:

1. Open the Camera app and switch to video mode.
2. Turn the Pixel sideways, both hands on the short edges, fingers clear of the lenses.
3. Tap the record button. Tap it again to stop.

On a Samsung Galaxy, in Samsung Camera:

1. Open the Camera app and swipe to **Video**.
2. Check the aspect ratio. Samsung's support page lists 9:16 as the full screen video ratio, alongside 1:1, 3:4 and Full Screen, and notes that "available ratios may vary depending on your device's camera specifications". A 1:1 video is square whichever way you hold the phone, so set 9:16, which becomes 16:9 once the phone is sideways.
3. Turn the Galaxy sideways and tap record.

On both, turn the phone before you press record. A clip that starts upright and swings sideways has two framings in one file, and no single crop rescues both halves. If you started wrong, stop and go again.

## Does auto-rotate need to be on to record landscape video on Android?

Neither Google's nor Samsung's help pages say how the auto-rotate setting affects the camera, so treat auto-rotate as a variable to rule out rather than the answer. Here is where each one lives:

- **Pixel and stock Android.** Google's Android Accessibility Help gives the path as Settings > Display & touch > Auto-rotate screen.
- **Samsung Galaxy.** Swipe down to Quick Settings. Samsung's Australian support page lists the tile's three states as Auto Rotate, Portrait and Landscape, and says "If you choose Portrait this will lock the screen from rotating to landscape."

Why the lock may not matter: Android's CameraX documentation shows a camera app holding its own screen in a locked orientation while an OrientationEventListener keeps reading how the phone is physically held, so the saved file can still come out landscape. Whether your camera app does that is up to the app. The two second test settles it: record a short clip sideways, open it in the gallery, and turn the phone to watch it. A landscape clip fills the sideways screen.

## Why does an Android video play sideways on a computer?

Android's recording API can save a sideways clip with an orientation flag rather than turning the picture itself, and some players ignore the flag. Android's MediaRecorder.setOrientationHint() documentation says it "will not trigger the source video frame to rotate during video recording", but adds "a composition matrix containing the rotation angle in the output video" for MP4 and 3GP files, and warns that "some video players may choose to ignore the compostion matrix" (Google's typo, not mine).

That is why the same file plays upright in the phone's gallery and on its side in an older desktop player or editor. The fix is to rotate the clip on the phone, save the rotated copy, and test that copy in the player that got it wrong.

## How do you rotate a video on Android?

In Google Photos, per Google Photos Help:

1. Open the video in the Google Photos app.
2. Tap **Crop**.
3. Tap **Rotate**. Each tap turns the video 90 degrees.
4. Tap **Save** at the top. Google Photos saves a copy, so the original stays untouched.

Google lists the limits: crop and straighten need at least 1 GB of RAM and Android 6.0 or later, and "Non-pixel Android devices running on Android 9 do not support or have access to video editing."

In Samsung Gallery: open the video, tap the Edit (pencil) icon, tap Transform, then Rotate. Samsung says its built-in Video editor is on the Galaxy S20 and later.

## What if the video was filmed upright and you needed it wide?

Then rotating will not help, because the picture really is vertical. Cropping a 1080×1920 vertical clip to 16:9 leaves a 1080×607 strip, about 32% of the height, which then gets stretched to 1920×1080. It works for a face that fills the frame and fails for any scene where the width mattered. [Converting vertical video to horizontal](https://contentcam.app/blog/convert-vertical-video-to-horizontal/) compares cropping with a blurred background fill.

## Where are the video resolution settings on Android?

In Pixel Camera, switch to video mode and tap Settings at the bottom left, where Google's help page shows the Resolution option. A landscape clip at 1080p is 1920×1080, and at 4K it is 3840×2160. The [Android camera settings guide](https://contentcam.app/blog/android-camera-settings-for-video/) explains why some phones offer far fewer options than others.

## What if you need the landscape and the vertical version?

Turning the phone sideways gets you a 16:9 clip for YouTube and nothing for TikTok. Cropping a 9:16 vertical out of that 1920×1080 frame keeps 607 of its 1920 pixels of width, which is 31.6%.

When the same moment has to go to both, record both at once. ContentCam for Android does this: one take saves a 9:16 file and a 16:9 file, cut from the sensor's full 4:3 frame so neither is a crop of the other. If you hold the phone rotated, both files are tagged with the right orientation and play upright in the gallery, CapCut or Premiere. [Recording portrait and landscape at the same time on Android](https://contentcam.app/blog/record-portrait-and-landscape-video-same-time-android/) has the full arithmetic. One ContentCam take, two files: the vertical keeps the walker and the red ceiling, the wide keeps the river and the walls.

## Common questions

**How do I record video in landscape mode on Android?** Open the Camera app, switch to Video, turn the phone sideways, then tap record. On Samsung, check the ratio is 9:16 and not 1:1 first.

**Do I need auto-rotate on to film landscape?** Google's and Samsung's pages do not say. Turn auto-rotate on to remove the variable, record a two second sideways test, and play it back in the gallery.

**Why is my Android video sideways on my PC?** Most likely the file carries its rotation as a flag, and Android's own documentation warns that some players ignore it. Rotate the clip in Google Photos or Samsung Gallery, which saves a rotated copy, and use that copy.

**How do I rotate a video on a Samsung phone?** Open it in Gallery, tap Edit, then Transform, then Rotate. Samsung lists the Video editor for the Galaxy S20 and later.

**Can Android record landscape and portrait at the same time?** Not in Pixel Camera or Samsung Camera, which record one shape per take. Apps like ContentCam save a 9:16 file and a 16:9 file from the same take.

Sources, checked 28 October 2026: [Pixel Camera Help](https://support.google.com/pixelcamera/answer/2838995?hl=en-GB); [Android Accessibility Help on auto-rotate](https://support.google.com/accessibility/android/answer/6006961?hl=en); [Google Photos Help, edit your videos](https://support.google.com/photos/answer/10729480?hl=en&co=GENIE.Platform%3DAndroid); Samsung's support pages on [camera ratio](https://www.samsung.com/ae/support/mobile-devices/adjusting-the-camera-ratio-on-my-samsung-phone/), [screen rotation](https://www.samsung.com/au/support/mobile-devices/screen-rotate) and the [Samsung Video editor](https://www.samsung.com/au/support/mobile-devices/how-to-use-samsung-video-editor); Android Developers, [CameraX rotation](https://developer.android.com/media/camera/camerax/orientation-rotation) and [MediaRecorder](https://developer.android.com/reference/android/media/MediaRecorder).

**Need the vertical cut too?** ContentCam records 9:16 and 16:9 in one take, free to try on Android and iPhone.

 Rated 4.8 by 580+ creators on the [App Store](https://apps.apple.com/us/app/contentcam-dual-camera-video/id6765881795) and [Google Play](https://play.google.com/store/apps/details?id=app.contentcam.android). [](https://apps.apple.com/us/app/contentcam-dual-camera-video/id6765881795?pt=128838819&ct=b-landscape-video-android&mt=8) [](https://play.google.com/store/apps/details?id=app.contentcam.android&referrer=utm_source%3Dblog%26utm_campaign%3Dhow-to-record-landscape-video-on-android)

Related: [How to record landscape video on iPhone](https://contentcam.app/blog/how-to-record-landscape-video-on-iphone/) · [How to record portrait and landscape at the same time on Android](https://contentcam.app/blog/record-portrait-and-landscape-video-same-time-android/) · [Android camera settings for video](https://contentcam.app/blog/android-camera-settings-for-video/) · [Vertical vs horizontal video](https://contentcam.app/blog/why-cropping-vertical-to-horizontal-looks-wrong/)
