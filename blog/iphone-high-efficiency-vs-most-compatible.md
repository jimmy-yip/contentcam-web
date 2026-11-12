# High Efficiency vs Most Compatible on iPhone: Which for Video? (2026)

Source: https://contentcam.app/blog/iphone-high-efficiency-vs-most-compatible/

High Efficiency records HEVC, Most Compatible records H.264. In my clips 1080p took about 60 MB a minute in HEVC and 99 to 118 MB in H.264. When each makes sense, and how to convert a copy.

By Jimmy, developer of ContentCam · 24 October 2026

Use High Efficiency unless something you edit or play on can't open HEVC files. High Efficiency records video in HEVC, also called H.265, and Most Compatible records in H.264. Apple says HEVC gives the same visual quality in less space. In my own clips, a minute of 1080p at 30 fps took about 60 MB in HEVC and 99 to 118 MB in H.264. Switch to Most Compatible only if an older computer, editor or TV can't play your clips, and even then, converting a copy is usually better than changing how you record.

## What is the difference between High Efficiency and Most Compatible?

The setting lives at Settings > Camera > Formats. Apple's support article "Using HEIF or HEVC media on Apple devices" explains both choices:

- **High Efficiency** records photos as HEIF and videos as HEVC (H.265). Apple says these formats "offer better compression than JPEG and H.264, so they use less storage space on your devices and iCloud Photos, while preserving the same visual quality."
- **Most Compatible** makes "all new photos and videos" use JPEG or H.264, the older formats that Apple describes as "more broadly compatible with other devices and operating systems."

Apple recommends High Efficiency. Every iPhone from iPhone 7 onwards can record HEVC, and the setting only appears on devices that can.

## How much smaller are High Efficiency videos?

About half the size in my clips. I measured 27 of my own iPhone videos with ffprobe, all standard dynamic range at 30 fps:

- **1080p, HEVC (iPhone 16):** 58 to 62 MB per minute in 12 of 13 clips, an average bitrate of about 8 Mbps. One short clip ran at 70 MB per minute.
- **1080p, H.264 (iPhone 13):** 99 to 118 MB per minute across 4 clips, about 13 to 16 Mbps.
- **4K, HEVC (iPhone 16):** 169 to 187 MB per minute in 6 of 10 clips, about 23 to 25 Mbps. The other 4, all longer clips, ran between 211 and 275 MB per minute.

The H.264 and HEVC clips came from different iPhones, so treat the comparison as a rough guide rather than a lab test. The direction matches what Apple says, and the gap is big: a 10 minute 1080p shoot at those rates is around 600 MB in HEVC against 1 to 1.2 GB in H.264.

## Is HEVC lower quality than H.264?

No. Apple's claim is the same visual quality in less space, and that's what HEVC was designed for. The trade is work, not quality: HEVC takes more processing power to decode. That's why the problems with High Efficiency are about playback and editing on older hardware, not how the footage looks.

HDR is a separate reason to keep High Efficiency. Every HDR clip I've checked from an iPhone was 10-bit HEVC, labelled HLG. My H.264 clips from the iPhone 13 were all 8-bit standard video. If you want iPhone HDR video, expect to need High Efficiency.

## Why won't my iPhone video play on my computer or TV?

Usually because the device or app can't decode HEVC. Apple's article says support is built into iOS 11 and later and macOS High Sierra 10.13 and later. It adds that "on some older devices, support for HEVC is affected by the resolution and frame rate," and that "resolutions of 1080p or lower and frame rates of 60 fps or lower are more broadly compatible with older devices."

So if a 4K 60 fps clip won't play somewhere but a 1080p 30 fps clip does, the resolution and frame rate are the problem, not HEVC itself. You can lower both in Settings > Camera > Record Video.

## How do you convert iPhone HEVC video to H.264?

Convert a copy and keep recording in High Efficiency. Apple's article gives two built-in ways on a Mac:

1. **QuickTime Player:** open the video, choose File > Export As, and change the pop-up menu from Smaller File Size (HEVC) to Greater Compatibility (H.264) before you click Save. If you see an HEVC checkbox instead, deselect it.
2. **Finder:** Control-click the video, choose Services > Encode Selected Video Files, then pick an H.264 option from the Settings menu.

Apple also says that sharing by AirDrop, Messages or email to a device that doesn't support HEVC "might automatically" send a more compatible format such as H.264. Sharing through iCloud Photos keeps the original format, resolution and frame rate.

## Why did my iPhone video change format when I copied it to a PC?

Because the import converted it. Apple says that when you import HEIF or HEVC media over USB into Photos, Image Capture or a PC, "the media might be converted to JPEG or H.264." To keep the originals, go to Settings > Apps > Photos and choose Keep Originals. That matters for creators: a converted copy is bigger, and it's a second compression pass on footage you might still edit.

## Which setting should creators use?

High Efficiency, for three reasons: files about half the size, HDR when you want it, and every iPhone and Mac updated since 2017 (iOS 11 and macOS High Sierra) can play and edit HEVC. Move to Most Compatible only if your editing machine is old enough to choke on HEVC, and only until you replace it. The rest of the Reels setup is in [the best iPhone video settings for Instagram Reels](https://contentcam.app/blog/iphone-video-settings-for-instagram/).

If your footage looks orange, grey or choppy, the cause is usually a different setting: see [why iPhone video looks orange or washed out after editing](https://contentcam.app/blog/iphone-video-orange-washed-out-hdr/) and [why iPhone video looks choppy in low light](https://contentcam.app/blog/iphone-video-choppy-low-light-auto-fps/).

## FAQ

### Should I use High Efficiency or Most Compatible for iPhone video?

High Efficiency, unless a device or editor you rely on can't open HEVC. It records the same visual quality in roughly half the space, and iPhone HDR video is recorded as HEVC.

### Is Most Compatible better quality?

No. Most Compatible records H.264, an older format. Apple says HEVC preserves the same visual quality in less space.

### How do I convert an iPhone video from HEVC to H.264?

On a Mac, open it in QuickTime Player, choose File > Export As and pick Greater Compatibility (H.264), or Control-click it in Finder and use Services > Encode Selected Video Files.

### Why are my iPhone videos so big?

Resolution and format. In my clips, 4K at 30 fps in HEVC took 169 to 275 MB a minute against about 60 MB for 1080p. Recording in H.264 roughly doubles the size again.

**Try ContentCam free.** Records vertical and horizontal at the same time, on iPhone and Android.

 Rated 4.8 by 580+ creators on the [App Store](https://apps.apple.com/us/app/contentcam-dual-camera-video/id6765881795) and [Google Play](https://play.google.com/store/apps/details?id=app.contentcam.android). [](https://apps.apple.com/us/app/contentcam-dual-camera-video/id6765881795?pt=128838819&ct=b-high-efficiency-vs-most-compatible&mt=8) [](https://play.google.com/store/apps/details?id=app.contentcam.android&referrer=utm_source%3Dblog%26utm_campaign%3Diphone-high-efficiency-vs-most-compatible)

Related: [best iPhone 17 Pro video settings](https://contentcam.app/blog/best-iphone-17-pro-video-settings/) · [do you actually need to film in 4K?](https://contentcam.app/blog/do-you-need-to-film-in-4k/) · [why iPhone video looks orange or washed out](https://contentcam.app/blog/iphone-video-orange-washed-out-hdr/) · [video terms explained](https://contentcam.app/blog/video-terms-explained/) · [recording long videos on iPhone without overheating](https://contentcam.app/blog/record-long-video-iphone-without-overheating/)

Sources: Apple Support, "Using HEIF or HEVC media on Apple devices" (support.apple.com/116944, published 5 December 2025, checked 24 October 2026). File measurements: ffprobe on 27 of my own iPhone 13 and iPhone 16 clips, October 2026.
