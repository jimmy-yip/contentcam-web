# Why Does My iPhone Video Have No Sound? (2026)

Source: https://contentcam.app/blog/iphone-video-no-sound/

An iPhone video with no sound either recorded no audio or has audio you can't hear. How to tell which, and the six causes: microphone access off, a call taking the mic, AirPods set as the input, a covered mic, time-lapse, or a camera app bug.

By Jimmy, developer of ContentCam · 9 November 2026 · Updated 9 November 2026

An iPhone video with no sound has one of two problems. Either the file recorded no audio, or the audio is there and the iPhone isn't playing it. Work out which one first, because the fixes are different. When the file really is silent, the cause is almost always one of six: the camera app has no microphone access, a call or alarm took the microphone mid-take, the input is set to AirPods, something is covering the microphones, the video is a time-lapse, or the camera app dropped the audio.

I build ContentCam, an iPhone and Android camera app, and I spend a lot of time inside iOS recording code. The Apple details below come from Apple's iPhone User Guide, AirPods User Guide and developer documentation, checked 9 November 2026.

## How do you tell if an iPhone video has no sound or you just can't hear it?

Play the video, then press volume up while it is playing. Apple's iPhone User Guide says the volume buttons "control media volume while audio is playing; when no audio is playing, the volume buttons control ringer and alert volume." Turning the volume up before you press play changes the ringer, not the video.

Still silent? Check the sound isn't going to AirPods or a Bluetooth speaker you forgot was connected. Then play the same file on another device: AirDrop it to a Mac or send it to a friend's phone. On a Mac, QuickTime Player's Movie Inspector (Window > Show Movie Inspector) lists an audio format such as AAC when the file has a sound track. Sound on the other device means the file is fine and the problem is playback on your iPhone. Silence everywhere means the recording has no audio, and the table below covers why.

## What are the reasons an iPhone video records no sound?

| Cause | The clue | Fix |
| --- | --- | --- |
| The camera app has no microphone access | Every video from one app is silent; the iPhone Camera app records sound fine | Settings > Privacy & Security > Microphone, turn the app on |
| A call, Siri or an alarm took the microphone | The sound cuts out partway through, and may come back | Airplane Mode or a Focus before takes you can't repeat |
| The input is set to AirPods | Sound is faint, distant or muffled, and AirPods were connected | Change Input in Control Center > Camera Controls |
| Something is covering the microphones | Muffled in every app, Voice Memos included | Case off, film off, move your fingers |
| The video is a time-lapse | Only time-lapse videos are silent | Expected; add music or a voiceover in an editor |
| The camera app dropped the audio | Sound cuts out on long or 60fps takes, in one app only | Update the app; test a one-minute take first |

## Why does a camera app record video with no sound?

Usually because the app has no microphone permission, and iOS doesn't always stop it recording. Apple's developer documentation for camera and microphone permission says that until the user grants access, "the system only vends black video frames and silent audio samples." An app with camera access but no microphone access can therefore save a normal-looking video with a silent sound track.

Fix it in Settings > Privacy & Security > Microphone, where Apple lists every app that has asked and lets you switch each one on or off. Don't rely on the green dot at the top of the screen to tell you the microphone is on. Apple shows the green dot whenever an app uses the camera, with or without the microphone. The orange dot only appears when an app uses the microphone without the camera.

ContentCam is stricter about this: it won't start the camera without microphone access. It shows a "Microphone Access Required" screen with a button to Settings instead, so it can't record a silent take by accident.

## Can a phone call or Siri cut the sound out of an iPhone video?

Yes. Apple's AVFoundation lists it as a capture interruption reason: "the audio hardware temporarily being made unavailable (for example, for a phone call or alarm)". What happens next depends on the app. Some apps stop the whole recording. Others keep the video going with a silent stretch.

ContentCam does the second. When iOS takes the microphone, ContentCam disconnects it from the recording, keeps the video running, fills the gap with silence so the sound stays in sync, and reconnects the microphone when iOS gives it back. Before a take you can't repeat, turn on Airplane Mode or a Focus. The other interruptions are covered in [why an iPhone video stops recording by itself](https://contentcam.app/blog/iphone-video-stopped-recording-by-itself/).

## Why does my iPhone video sound muffled with AirPods connected?

Because the AirPods may be the microphone. Apple's AirPods User Guide says AirPods 4, AirPods 5, AirPods Pro 2, AirPods Pro 3 and AirPods Max 2 can work "as a microphone" for video in supported camera apps, "like a lapel mic", on iOS 26 or later. You choose them under Control Center > Camera Controls > Input, or Settings > Sounds & Haptics > Input. Apple notes the feature isn't available in every country or region, including the EU.

That's useful with the AirPods in your ears while you film yourself from across the room. It's not useful when they're in your pocket or in someone else's ears: the video records whatever those AirPods hear. If a video sounds distant or muffled and AirPods were connected, check Input first.

Third-party camera apps can do the same with a Bluetooth headset. Apple's allowBluetoothHFP audio option "makes Bluetooth Hands-Free Profile (HFP) devices available for audio input". ContentCam uses that option. When headphones or a Bluetooth device connect or disconnect, it shows an "Audio source" message naming the device, so you can see the switch happen.

## Is something covering the iPhone microphones?

Check this when every app sounds muffled. Apple says the iPhone "uses multiple microphones to achieve stereo sound". The microphones sit at different points on the body, including the bottom edge and next to the rear cameras. A thick case, the edge of a screen protector, pocket lint, or a hand wrapped around the bottom while you hold the phone sideways can block one or more of them.

Test outside the camera app. Record 10 seconds in Voice Memos with the case on, then 10 seconds with it off, and compare. If Voice Memos is muffled both times, the problem is the microphones themselves, not the camera app, and Apple Support is the next step.

## Which iPhone video modes record no sound?

Time-lapse. Apple's User Guide describes it as footage captured "at selected intervals", so there is no continuous sound to keep, and a time-lapse plays back silent. ContentCam's time-lapse doesn't connect the microphone at all. Add music or a voiceover in your editor afterwards.

## Can a camera app bug drop the sound from a video?

Yes, and the app may not notice. In Apple's camera framework, the video output has a callback that reports dropped frames, captureOutput(_:didDrop:from:). The audio output has no equivalent. Audio that never arrives is simply missing, with no error raised.

It usually shows up on long takes at high frame rates, where the phone is working hardest. A dropout can also turn into a lip-sync problem: if an app doesn't fill the missing stretch with silence, the rest of the sound slides earlier and drifts out of sync with the picture. ContentCam fills any gap with silence, so the sound stays lined up. On an older iPhone, recording long takes at 30fps instead of 60fps takes load off the phone.

If one app loses sound on long takes and other apps don't, update that app. Then record a one-minute test at the exact settings you plan to use and listen back before the real take. A level meter helps too. ContentCam has an optional Audio level meter in Settings that moves while the microphone is live and pulses red when the sound is clipping.

## FAQ

### Why is there no sound when I play a video on my iPhone?

Press volume up while the video is playing. Apple says the iPhone volume buttons only change media volume while audio is playing; otherwise they change the ringer. Then check the sound isn't going to connected AirPods or a Bluetooth speaker, and play the file on another device to see whether it has audio at all.

### Does Spatial Audio cause no sound on iPhone 16 videos?

iPhone 16 and later record Spatial Audio by default, and you can switch to Stereo or Mono in Settings > Camera > Record Sound. If Photos plays the sound but another app or computer doesn't, the file has audio and that app is the problem. Record a short Stereo test and compare.

### Can I get the sound back on a silent iPhone video?

Not if the file recorded no audio, because there is nothing in it to recover. You can add music or a voiceover in an editor such as iMovie or CapCut. If the sound is only quiet, an editor can raise the volume.

**Try ContentCam free.** A camera app that won't start recording without microphone access, keeps the video rolling with a silent gap when a call takes the microphone, and records vertical and horizontal in one take. No ads, no watermark, iPhone and Android.

 Rated 4.8 by 580+ creators on the [App Store](https://apps.apple.com/us/app/contentcam-dual-camera-video/id6765881795) and [Google Play](https://play.google.com/store/apps/details?id=app.contentcam.android). [](https://apps.apple.com/us/app/contentcam-dual-camera-video/id6765881795?pt=128838819&ct=b-iphone-video-no-sound&mt=8) [](https://play.google.com/store/apps/details?id=app.contentcam.android&referrer=utm_source%3Dblog%26utm_campaign%3Diphone-video-no-sound)

Related: [why phone video audio sounds bad](https://contentcam.app/blog/why-phone-video-audio-sounds-bad/) · [iPhone video stopped recording by itself](https://contentcam.app/blog/iphone-video-stopped-recording-by-itself/) · [lavalier vs shotgun mic](https://contentcam.app/blog/lavalier-vs-shotgun-mic-phone/) · [video not in Photos after recording](https://contentcam.app/blog/iphone-video-not-in-photos-after-recording/)

Sources, checked 9 November 2026: Apple iPhone User Guide, [Adjust the volume](https://support.apple.com/guide/iphone/adjust-the-volume-iphb71f9b54d/ios), [Control access to hardware features](https://support.apple.com/guide/iphone/control-access-to-hardware-features-iph168c4bbd5/ios), [Change sound recording options](https://support.apple.com/guide/iphone/change-sound-recording-options-iph31c1ca6c7/ios), [Change video recording settings](https://support.apple.com/guide/iphone/change-video-recording-settings-iphc1827d32f/ios) and [Record a video](https://support.apple.com/guide/iphone/record-a-video-iph61f49e4bb/ios); Apple AirPods User Guide, [Use AirPods with supported camera apps](https://support.apple.com/guide/airpods/use-airpods-with-camera-apps-dev8e2a2ba2e/web); Apple Developer documentation, [AVCaptureDevice requestAccess](https://developer.apple.com/documentation/avfoundation/avcapturedevice/requestaccess(for:completionhandler:)), [audioDeviceInUseByAnotherClient](https://developer.apple.com/documentation/avfoundation/avcapturesession/interruptionreason/audiodeviceinusebyanotherclient), [allowBluetoothHFP](https://developer.apple.com/documentation/avfaudio/avaudiosession/categoryoptions-swift.struct/allowbluetoothhfp), [AVCaptureVideoDataOutputSampleBufferDelegate](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutputsamplebufferdelegate) and [AVCaptureAudioDataOutputSampleBufferDelegate](https://developer.apple.com/documentation/avfoundation/avcaptureaudiodataoutputsamplebufferdelegate). ContentCam behaviour checked in the iOS app's source code.
