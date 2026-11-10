# Recorded a Video on iPhone but It's Not in Photos? Where to Find It (2026)

Source: https://contentcam.app/blog/iphone-video-not-in-photos-after-recording/

If a video you recorded in a camera app isn't in Photos, it is usually still inside the app's own storage. How to check with iPhone Storage, find it in the Files app or on a Mac or PC, and what not to delete.

By Jimmy, developer of ContentCam · 7 November 2026 · Updated 7 November 2026

If a video you recorded in a camera app isn't in Photos, it is almost always still on the iPhone, inside that app's own storage. Most third-party camera apps write each take into a private folder first and only copy it to Photos when you export or save it. Check the app's size in Settings > General > iPhone Storage: if its Documents & Data is large, the video is there. Whatever you do next, don't delete the app.

Disclosure: I build ContentCam, a camera app that also stores takes inside the app, so I deal with this from the developer side. Apple details below come from Apple's own documentation and support pages, checked 7 November 2026.

## Why is my iPhone video not in Photos after recording?

One of three reasons:

- **The app saves to its own storage, not Photos.** Apple gives every app a private folder. Many camera apps record there, because a video can only go into Photos once the file is finished, and copy it to Photos only on export. Some never do it automatically.
- **The app has no Photos permission.** If you tapped Don't Allow, the export fails. Check Settings > Privacy & Security > Photos.
- **The recording never finished.** If the app crashed or was killed mid-take, the file may be unplayable. Why that happens, and when it can be recovered: [why an iPhone video stops recording by itself](https://contentcam.app/blog/iphone-video-stopped-recording-by-itself/).

## How do I check if the video is still on my iPhone?

Open Settings > General > iPhone Storage and tap the camera app. Two numbers show: App Size (the app itself) and Documents & Data (what the app has saved). A camera app at 5 MB with 48 GB of Documents & Data is holding about 48 GB of video. As a guide, DualShot Recorder's own settings estimate about 1,316 MB a minute for 4K at High quality saved as two files (vertical and horizontal), so a 38-minute interview lands near 50 GB.

On the same screen, iOS offers two buttons. Offload App "will free up storage used by the app, but keep its documents and data". Delete App "will delete the app and all related data from this iPhone. This action can't be undone." If the video is inside the app, Delete App deletes the video too.

## How do I find a camera app's videos in the Files app?

Open the Files app, tap Browse, then On My iPhone. Apps that share files appear there as folders with their own name. Apple's developer documentation explains why some do and some don't: an app has to switch on a setting called UIFileSharingEnabled, and "the default value is NO". If the camera app has no folder under On My iPhone, its videos can't be reached from the Files app at all.

## How do I get videos out of an iPhone app onto a Mac or PC?

Use File Sharing. On a Mac with macOS Catalina or later, connect the iPhone with a cable, open Finder, select the iPhone and click the Files tab. Apple's support page says this lists the apps "that can share files", and adds: "If you don't see a Files section, your device doesn't have any apps that can share files." On a Windows PC, Apple points to its Apple Devices app. Either way, it is the same switch as the Files app: an app that doesn't share files won't be listed.

## What if the camera app doesn't share files?

- **Keep the app installed.** The video is the Documents & Data. Deleting the app is the one step you can't undo.
- **Look inside the app.** Check for a library, gallery, export or "Save to" setting.
- **Contact the developer.** The App Store listing links to the developer's website.
- **A backup includes it, but that rarely helps.** A full iPhone backup contains the app's data, but Apple's own tools restore a backup to a phone rather than letting you pull out one file, and you need room for the whole backup on the computer.

## Why is my DualShot Recorder video not in Photos?

DualShot Recorder (DDJR Productions, version 3.1.2) has users reporting exactly this. In the app's own Telegram support group, one user recorded a 38-minute 4K interview on 23 October 2026: the video never appeared in Photos or the Files app, while iPhone Storage showed DualShot's Documents & Data at 48.46 GB. Exporting the app's data from a computer only worked through a full phone backup, which needed space they didn't have. A second user reported a recording missing from Photos on 3 November. The answers in the group came from other users, one of whom wrote that they don't work for the company. None of the replies we saw came from the developer.

DualShot Recorder was last updated on 5 June 2026 and holds 4.7 stars from about 1,900 US ratings. Settings screens that users shared show a "Save Media to" choice between Files and Photo Library; the user with the missing interview said their copy didn't show those settings. If this happened to you, check iPhone Storage, check for a DualShot folder under On My iPhone in Files and in Finder's Files tab, and don't delete the app. More on the two apps side by side: [DualShot Recorder vs ContentCam](https://contentcam.app/blog/dualshot-recorder-vs-contentcam/).

## How do I stop a recording going missing next time?

- **Test before the take that matters.** Record 30 seconds, then find that exact file in Photos or Files before you start the real one.
- **Pick an app with a Files folder.** ContentCam keeps every take in Files under On My iPhone > ContentCam the moment you stop, and in Finder's Files tab. A project can also record straight into a folder you pick. ContentCam copies to Photos only when you tap Save, so a take you haven't saved won't be in Photos, but it will be in Files.
- **Leave free space.** At over 1 GB a minute in 4K, a long take needs tens of gigabytes spare.

## FAQ

### Why is my recorded video not showing in Photos on iPhone?

Third-party camera apps often save takes inside their own storage and only copy them to Photos when you export. If the app's Documents & Data in Settings > General > iPhone Storage is large, the video is still on the iPhone, inside the app.

### Will deleting the app get my video back?

No. Deleting an app deletes its documents and data, including any video stored inside it, and iOS warns that the action can't be undone. Offload App keeps the documents and data, but it does not move the video anywhere you can open it.

### How do I get videos out of an iPhone app onto a computer?

Connect the iPhone to a Mac, open Finder, select the iPhone and click the Files tab. Apps that support File Sharing are listed there. On a Windows PC, use Apple's Apple Devices app. An app missing from the list does not share files.

### Why is my DualShot Recorder video not in Photos?

DualShot Recorder users have reported finished recordings that never appeared in Photos or the Files app while the app's Documents & Data grew by tens of gigabytes. Check iPhone Storage first, and don't delete the app.

**Try ContentCam free.** Every take lands in the Files app the moment you stop, vertical and horizontal from one recording, front and back too. No ads, no watermark, iPhone and Android.

★ Rated 4.8 by 580+ creators on the [App Store](https://apps.apple.com/us/app/contentcam-dual-camera-video/id6765881795) and [Google Play](https://play.google.com/store/apps/details?id=app.contentcam.android). [](https://apps.apple.com/us/app/contentcam-dual-camera-video/id6765881795?pt=128838819&ct=b-iphone-video-not-in-photos&mt=8) [](https://play.google.com/store/apps/details?id=app.contentcam.android&referrer=utm_source%3Dblog%26utm_campaign%3Diphone-video-not-in-photos-after-recording)

Related: [why an iPhone video stops recording by itself](https://contentcam.app/blog/iphone-video-stopped-recording-by-itself/) · [DualShot Recorder vs ContentCam](https://contentcam.app/blog/dualshot-recorder-vs-contentcam/) · [record long videos without overheating](https://contentcam.app/blog/record-long-video-iphone-without-overheating/)

Sources, checked 7 November 2026: Apple Developer, [UIFileSharingEnabled](https://developer.apple.com/documentation/bundleresources/information-property-list/uifilesharingenabled); Apple Support, [Use the Finder to share files between your Mac and your iPhone](https://support.apple.com/en-us/119585); iOS Settings > General > iPhone Storage (Offload App and Delete App wording); the App Store listing for DualShot Recorder (version, update date, ratings); user reports in the DualShot Recorder Support Telegram group, 23 October to 6 November 2026. ContentCam behaviour checked in the iOS app's source code.
