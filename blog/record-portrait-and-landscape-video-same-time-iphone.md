# How to Record Portrait and Landscape at the Same Time (iPhone)

Source: https://contentcam.app/blog/record-portrait-and-landscape-video-same-time-iphone/

One take, two files: a 9:16 vertical and a 16:9 landscape of the same moment. Three ways to do it on iPhone, what cropping in post costs you, and a real example.

By Jimmy, developer of ContentCam · 25 July 2026 · Updated 5 November 2026

To record portrait and landscape video at the same time on iPhone, use a camera app that saves a 9:16 vertical file and a 16:9 horizontal file from the same take, because the iPhone Camera app records one shape per take. ContentCam, which I build, does this free at 1080p and up to 30fps on iPhone and Android, taking both files from the full 4:3 sensor so neither is a crop of the other; Premium adds 4K and 60fps. Without an app like that, you either film the piece twice or shoot horizontal in 4K and crop the vertical out afterwards, which keeps about 32% of the frame.

TikTok, Reels and Shorts want 9:16 vertical. YouTube wants 16:9 horizontal. Same content, incompatible shapes, so most creators film the piece twice or butcher the second version in an editor.

There are three real ways to get both formats out of one shoot. I build ContentCam, so read this with that in mind: it does options 2 and 3 below, the two that record both files at capture. Option 1 needs only an editor, and the maths shows what it costs. One take on a travel creator's trip, walking through a tunnel of mossy branches: the portrait and landscape files ContentCam saved, playing in sync. Neither one is a crop of the other.

## Option 1: Film portrait, crop landscape in post

The default workflow. Record vertical, drop the clip into CapCut or Premiere, set a 16:9 sequence, and scale the portrait clip until it fills the frame.

Here's the maths problem. A 1080×1920 portrait clip cropped to 16:9 gives you a 1080×607 strip, stretched to 1920×1080: about three times the pixel area, upscaled. The result is soft, and the framing is whatever survived the chop, usually a face with no room around it.

It's fine for talking heads where the landscape version is a bonus. It hurts anywhere the wide shot matters: travel, vlogs, sport, product shots.

## Option 2: Record the full sensor, crop both ways at capture

Your iPhone's camera sensor isn't portrait or landscape. It's 4:3: wider than a 9:16 frame and taller than a 16:9 frame. Standard camera apps throw part of it away the moment you pick an orientation.

The smarter approach is to record the whole 4:3 frame and cut both deliverables from it at capture time:

- The 9:16 portrait crop keeps the sensor's **full vertical** field of view.
- The 16:9 landscape crop keeps the sensor's **full horizontal** field of view.

Neither file is a crop of the other. The landscape version actually shows more of the scene left and right than your portrait does, because that's what the sensor saw. This is how [ContentCam's Single Lens mode](https://contentcam.app/features/dual-camera/) works, and both files encode independently: 1080×1920 and 1920×1080 HEVC, or 4K equivalents. No upscaling anywhere in the chain. Recording in ContentCam: you see both framings before you press record.

## Option 3: Record two cameras at once

An iPhone 11 or later with an ultra-wide camera (so not iPhone SE or iPhone 16e) can run two rear cameras simultaneously. ContentCam's Dual Lens mode uses this: the wide lens records your portrait while the ultra-wide records landscape, at the same instant.

The difference from option 2 is framing. With two lenses, your portrait can be a tight shot while your landscape is a genuinely wide establishing shot: two different shots from one take. Dual Lens mode: the live view while recording (left), then the review screen (right). The portrait stays tight on the walk while the landscape takes in the whole tunnel.

The limits: it runs at 1080p (third-party apps can only run two cameras at once in Apple's multi-camera formats, which top out at 1920×1440 on every iPhone ContentCam has run on except the iPhone 18 Pro), and running two cameras uses more battery. Apple's own Camera app has [iPhone Dual Capture](https://contentcam.app/blog/iphone-17-dual-capture-limitations/) at up to 4K30, but it pairs the front and rear cameras, not two rear framings, and saves one picture-in-picture video. It gives you no 9:16 and 16:9 pair at all.

## How do you record landscape video on an iPhone?

Turn the phone sideways and the Camera app records 16:9 landscape. That covers one format. Rotating gives you one or the other, and cropping a vertical out of that landscape afterwards keeps only about 32% of the width. Lock Rotation and fixing a clip filmed the wrong way are in [how to record landscape video on iPhone](https://contentcam.app/blog/how-to-record-landscape-video-on-iphone/).

If you need both, record the full sensor once in ContentCam and take both framings out of it at capture (Option 2 above). The landscape file stays a real 16:9 recording, and the portrait one keeps its full height.

## Which one should you use?

| Your situation | Best option |
| --- | --- |
| Talking head, face fills frame, landscape is secondary | Crop in post is fine |
| Both versions need to look intentional | ContentCam full-sensor capture (option 2), free in HD |
| You want different framing per platform | ContentCam Dual Lens (option 3) |
| You need 4K in both formats | ContentCam full-sensor capture (Premium), the only one of the three that can |
| Front camera | ContentCam full-sensor capture (works on the selfie cam) |

If you post the same take to TikTok and YouTube more than once a week, record it in ContentCam. Cropping in post only makes sense when the landscape version barely matters.

## Step by step in ContentCam

1. Open ContentCam and pick Single Lens, Dual Lens or Front & Back at the bottom of the record screen.
2. Frame your shot. The landscape preview tile shows what the 16:9 version sees, so check both before rolling. Grid, crosshair and level overlays help here.
3. Record. One button, both files.
4. Stop, and the review screen shows portrait and landscape side by side. Save both, or delete the take and go again.
5. Files are auto-named (my_project_scene_001_Portrait.mov and _Landscape.mov) so you can't mix them up in the edit.

The free tier does all of this at 1080p with the single lens: unlimited takes, no account, no ads and no watermark. [Premium](https://contentcam.app/pricing/) adds Dual Lens, 4K and 60fps.

## On Android?

Same problem, same fix. [ContentCam for Android](https://contentcam.app/android/) records both formats from the full sensor too, with manual white balance, ISO and shutter on phones that support them. The [Android version of this guide](https://contentcam.app/blog/record-portrait-and-landscape-video-same-time-android/) covers what Samsung Camera and Pixel Camera can and can't do here.

**Stop filming everything twice.** ContentCam is free on both stores; record a take and look at both files before deciding anything.

★ Rated 4.8 by 580+ creators on the [App Store](https://apps.apple.com/us/app/contentcam-dual-camera-video/id6765881795) and [Google Play](https://play.google.com/store/apps/details?id=app.contentcam.android). [](https://apps.apple.com/us/app/contentcam-dual-camera-video/id6765881795?pt=128838819&ct=b-portrait-landscape-iphone&mt=8) [](https://play.google.com/store/apps/details?id=app.contentcam.android&referrer=utm_source%3Dblog%26utm_campaign%3Drecord-portrait-and-landscape-video-same-time-iphone)

Related: [Vertical vs horizontal video: which should you shoot?](https://contentcam.app/blog/why-cropping-vertical-to-horizontal-looks-wrong/) · [How to film for TikTok and YouTube at the same time](https://contentcam.app/blog/film-for-tiktok-and-youtube-at-the-same-time/) · [Dual-format recording apps compared](https://contentcam.app/blog/dual-format-recording-apps-compared/) · [How to record landscape video on iPhone](https://contentcam.app/blog/how-to-record-landscape-video-on-iphone/) · [ReFrame vs ContentCam](https://contentcam.app/blog/reframe-vs-contentcam/)
