# Why Did My iPhone Video Stop Recording by Itself? (2026)

Source: https://contentcam.app/blog/iphone-video-stopped-recording-by-itself/

An iPhone video usually stops recording by itself for one of five reasons: you left the camera app, the phone got too hot, another app took the microphone, storage ran out, or the app crashed. How to tell which one, and how to stop it happening again.

By Jimmy, developer of ContentCam · 8 November 2026 · Updated 8 November 2026

An iPhone video that stops recording by itself almost always hit one of five things: the camera app left the screen, the iPhone got too hot, another app took the microphone, storage ran out, or the camera app crashed. Apple's camera framework, AVFoundation, names most of these as official "interruption reasons", so they are not random. Each one leaves a different clue, and each one has a fix.

I build ContentCam, an iPhone and Android camera app, and I have debugged every one of these in my own recording code. The Apple details below come from Apple's developer documentation, checked 8 November 2026.

## What are the reasons an iPhone video stops recording?

| Cause | The clue | Fix |
| --- | --- | --- |
| The camera app left the screen (lock, Home, app switch) | The video ends the moment you locked the iPhone or opened something else | Keep the camera app on screen until you tap stop |
| The iPhone got too hot | A temperature warning, a hot phone, a long take or 4K in the sun | Shade, 1080p, case off, shorter takes |
| A call, Siri or an alarm took the microphone | The video ends, or goes silent, at the moment a call rang | Airplane Mode or a Focus before long takes |
| Storage ran out | A "not enough storage" message, or the app refuses to start | Free space first; leave a few GB spare |
| The app crashed | You land back on the Home Screen, often with no video saved | Update the app; use one that writes movie fragments |

## Why does my iPhone stop recording video when I lock the screen or switch apps?

iOS does not let a camera app use the camera in the background. Apple's AVFoundation lists this as an interruption reason, videoDeviceNotAvailableInBackground: "the app being sent to the background while using a camera". Locking the iPhone, swiping to the Home Screen, or opening another app all count.

The recording does not pause and come back. It ends. What gets saved depends on the app: a well-built camera app finishes the file in the short time iOS allows after backgrounding. ContentCam does that, so the take saves up to the moment you left. The fix is simply to leave the camera app on screen. If you need the screen dark to save battery, turn the brightness down instead of locking.

## Why does my iPhone stop recording video when it gets hot?

Heat is the most common cause on long takes. iOS reports four thermal states: nominal, fair, serious and critical. At critical, Apple's own guidance to developers is: "If possible, stop using peripherals such as the camera, flash, microphone, and speaker." AVFoundation also has an interruption reason for it, videoDeviceNotAvailableDueToSystemPressure, "such as thermal duress".

So when the iPhone is hot enough, iOS can cut the camera off itself, whether the app likes it or not. ContentCam warns you at serious and stops and saves the take itself at critical, so you keep everything recorded up to that point. Recording at 4K, 60fps, or both cameras at once heats the iPhone fastest. The full set of cooler settings is in [how to record long videos on iPhone without overheating](https://contentcam.app/blog/record-long-video-iphone-without-overheating/).

## Does a phone call or notification stop an iPhone video recording?

A phone call, Siri or an alarm can, because each one takes the iPhone's microphone. AVFoundation calls this audioDeviceInUseByAnotherClient: "the audio hardware temporarily being made unavailable (for example, for a phone call or alarm)". If the app keeps the microphone attached, the whole capture session is interrupted, video included.

I found this the hard way. In testing, an Instagram notification sound stopped an 11-second ContentCam timelapse. ContentCam now unplugs the microphone from the session the moment audio is taken away, so the video keeps recording with a gap in the sound, and the sound comes back when iOS returns the microphone. Not every app does this. Before a take you can't redo, turn on Airplane Mode (it blocks calls) or a Focus that silences notifications.

## How much storage does iPhone video recording need?

Video bitrate decides it. One megabit per second is 0.45 GB an hour, so:

- **HD at 10 Mbps:** about 4.5 GB an hour.
- **4K at 40 Mbps:** about 18 GB an hour.
- **Two files at once** (vertical plus horizontal, or front plus back) add their bitrates together. ContentCam's HD vertical (8 Mbps) and horizontal (10 Mbps) files come to about 8 GB an hour.

Check Settings > General > iPhone Storage before a long shoot. ContentCam refuses to start a take with under 500 MB free and warns under 2 GB, because a take that runs out of space part-way is a take you probably can't repeat.

## Can I recover an iPhone video that stopped recording?

Often yes, if the app wrote movie fragments. A QuickTime movie needs a "sample table" to be playable, and that table is normally written when recording finishes. Apple's documentation explains that if recording does not complete, for example in a crash, "the file data is unusable". Movie fragments fix this by writing the table in pieces, so the file "is still usable (up to the point where the last fragment was written)".

Here is the catch. With Apple's AVCaptureMovieFileOutput, fragments are on by default every 10 seconds. With AVAssetWriter, which most advanced camera apps use, Apple "disables this feature by default". An app that never turned it on can lose an entire take to one crash. ContentCam writes a fragment every second and checks for unfinished files on the next launch, so a crash costs at most about a second of footage.

## FAQ

### Why does my iPhone stop recording when I lock the screen?

iOS does not let a camera app keep the camera running in the background. Locking the iPhone or swinging away to another app interrupts the capture session, so the recording ends there. Keep the camera app on screen until you tap stop.

### Does a phone call stop an iPhone video recording?

It can. A phone call, Siri or an alarm takes the iPhone's microphone, and Apple's AVFoundation reports that as a capture session interruption. Whether the video keeps going depends on the app. Turn on Airplane Mode or a Focus before a long take to avoid the risk.

### Can I recover an iPhone video that stopped recording?

Often, if the app wrote movie fragments. Apple's documentation says a fragmented QuickTime file stays playable up to the last fragment written, so you lose only the last few seconds. Without fragments, a recording cut off by a crash has no sample table and is unreadable.

### How much free storage do I need to record video on iPhone?

More than you think. One HD video at about 10 Mbps uses roughly 4.5 GB an hour, and 4K at 40 Mbps uses about 18 GB an hour. Check Settings > General > iPhone Storage before a long shoot and leave a few gigabytes spare.

**Try ContentCam free.** A camera app that saves the take when heat or leaving the app stops it, keeps the video rolling when a call or alarm takes the microphone, and records vertical and horizontal in one take. No ads, no watermark, iPhone and Android.

★ Rated 4.8 by 580+ creators on the [App Store](https://apps.apple.com/app/id6765881795) and [Google Play](https://play.google.com/store/apps/details?id=app.contentcam.android). [](https://apps.apple.com/app/apple-store/id6765881795?pt=128838819&ct=b-iphone-video-stopped-recording&mt=8) [](https://play.google.com/store/apps/details?id=app.contentcam.android&referrer=utm_source%3Dblog%26utm_campaign%3Diphone-video-stopped-recording-by-itself)

Related: [iPhone video with no sound](https://contentcam.app/blog/iphone-video-no-sound/) · [video not in Photos after recording](https://contentcam.app/blog/iphone-video-not-in-photos-after-recording/) · [record long videos without overheating](https://contentcam.app/blog/record-long-video-iphone-without-overheating/) · [choppy iPhone video in low light](https://contentcam.app/blog/iphone-video-choppy-low-light-auto-fps/) · [High Efficiency vs Most Compatible](https://contentcam.app/blog/iphone-high-efficiency-vs-most-compatible/)

Sources, checked 8 November 2026: Apple Developer documentation, [AVCaptureSession.InterruptionReason](https://developer.apple.com/documentation/avfoundation/avcapturesession/interruptionreason), [ProcessInfo.ThermalState.critical](https://developer.apple.com/documentation/foundation/processinfo/thermalstate-swift.enum/critical), [AVCaptureMovieFileOutput movieFragmentInterval](https://developer.apple.com/documentation/avfoundation/avcapturemoviefileoutput/moviefragmentinterval) and [AVAssetWriter movieFragmentInterval](https://developer.apple.com/documentation/avfoundation/avassetwriter/moviefragmentinterval). ContentCam behaviour checked in the iOS app's source code.
