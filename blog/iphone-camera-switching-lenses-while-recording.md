# Why Does My iPhone Switch Lenses While Recording? How to Stop It (2026)

Source: https://contentcam.app/blog/iphone-camera-switching-lenses-while-recording/

The iPhone falls back to a wider lens when the subject is too close or the light too dim for the one you picked. How Lock Camera, Macro Control and Enhanced Stabilization change that, and what each costs.

By Jimmy, developer of ContentCam · 20 October 2026

Because the iPhone Camera app treats its rear cameras as one combined camera and keeps choosing whichever lens it thinks gives the best picture. The zoom you picked decides first. Focus distance and light come second. Move closer than the telephoto lens can focus, or into dim light, and the iPhone quietly switches to a wider lens and crops in to hold your zoom. On the recording, that shows up as a jump in sharpness, noise or colour partway through the take. Lock Camera, in Settings > Camera > Record Video, stops the switch while you record.

## Why does the iPhone camera switch lenses by itself?

Apple's developer documentation for AVFoundation, the framework every iPhone camera app is built on, explains the logic. A "virtual device" such as the Dual Camera, Dual Wide Camera or Triple Camera is made of cameras "that each have different properties like focal length, maximum light sensitivity, and minimum focus distance." When more than one of them can reach the zoom you asked for, "the virtual device chooses the best camera for the scene."

Apple says the choice is made "primarily using a camera's focal length", because the longest lens needs the least digital upscaling. Then: "Secondary conditions are focus and exposure." Apple's own example is a telephoto camera with a 40 cm minimum focus distance. It "isn't able to deliver a sharp image when the subject in the scene is closer than 40 cm", so the system switches to the wide-angle camera, which can focus closer.

In practice, the iPhone switches lenses mid-video for three reasons:

- **The subject is too close for the telephoto lens.** You're at 2x, 3x, 4x or 5x and walk towards the subject. Once it's inside the telephoto's minimum focus distance, the Main camera takes over and crops to match your zoom.
- **The light is too low for the telephoto lens.** Exposure is the other condition Apple names. In dim light a wider camera may give a cleaner image, so the iPhone falls back to it and crops, even though the screen still says 3x.
- **You're very close, and macro takes over.** On iPhone models with macro, Camera switches to the Ultra Wide camera automatically when you get close. Apple's iPhone User Guide says macro focuses "as close as 2 centimeters."

## How do you stop the iPhone switching cameras while recording?

Turn on Lock Camera. Apple's iPhone User Guide describes it like this: "the Lock Camera setting prevents switching between cameras while recording video. Lock Camera is off by default." The path is Settings > Camera > Record Video > Lock Camera.

Apple lists Lock Camera on iPhone 13, 13 mini, 13 Pro and 13 Pro Max, every iPhone 14, 15 and 16 model except iPhone 16e, iPhone 17, 17 Pro and 17 Pro Max, and iPhone 18 Pro and 18 Pro Max. iPhone 16e, iPhone Air and iPhone 17e aren't on the list.

Lock Camera works on the lens you start on. Pick the zoom before you press record, then the iPhone keeps that physical camera for the whole take.

## How do you turn off macro switching on iPhone?

Get close to the subject in Photo or Video mode. When you're within macro range, a small flower button appears on screen. Tap it to turn off automatic macro switching, and tap it again to turn it back on. That's Apple's documented method.

Two settings control the button. Settings > Camera > Macro Control decides whether the button appears at all. Settings > Camera > Preserve Settings > Macro Control keeps your last choice the next time you open Camera, instead of resetting it. Apple lists macro on iPhone 13 Pro and Pro Max, iPhone 14 Pro and Pro Max, iPhone 15 Pro and Pro Max, every iPhone 16 model except iPhone 16e, iPhone 17, iPhone 17 Pro and Pro Max, and iPhone 18 Pro and Pro Max.

If a close-up suddenly goes soft after you turn macro switching off, Apple's own tip is to back up, or tap .5x to switch to the Ultra Wide camera yourself.

## What does Lock Camera cost you?

Lock Camera keeps the lens you chose even when it's the wrong lens for the moment. Lock the telephoto, then move closer than its minimum focus distance, and the picture goes soft instead of switching. Lock it in a dim room and you get a noisier picture instead of a cleaner crop from the Main camera.

So lock the camera for shots where the distance and light stay put: a talking head on a tripod, an interview, a product on a table. Leave switching on for handheld shots where you're walking towards things and the light changes. If you want the telephoto look without the fallback, step back so the subject stays well beyond the telephoto's minimum focus distance, which is 40 cm in Apple's example.

## Why does my iPhone video zoom in when I start recording?

That isn't a lens switch. It's Enhanced Stabilization. Apple's iPhone User Guide says it "zooms in slightly to provide improved stabilization while recording in Video mode or Cinematic mode. Enhanced Stabilization is on by default." The crop gives the stabiliser spare picture around the edges to move into.

To turn it off, go to Settings > Camera > Record Video and turn off Enhanced Stabilization. You get the wider frame back and slightly shakier handheld footage. Apple lists it on iPhone 14 and later. If you turn it off, the techniques in [how to hold your phone steady while filming](https://contentcam.app/blog/hold-phone-steady-while-filming/) matter more.

## Do other camera apps switch lenses too?

Only if the app lets the system do it. AVFoundation gives every app a choice. An app can use the combined camera with switching set to automatic, which "places no restrictions on when a camera switch can occur". It can restrict fallback switching to conditions the app picks, or lock switching to the active camera. Or it can open one physical lens on its own, which can't switch at all.

Apple's Camera app switches automatically unless you turn on Lock Camera, which Apple describes as working while you record video. Some manual camera apps let you pick one physical lens instead, so the picture never changes underneath you. If an app keeps jumping between lenses, check its settings for a lens picker or a lock option.

## FAQ

### Why does my iPhone video go blurry when I get close?

Either the subject is closer than the telephoto lens can focus, or macro switching has kicked in or been turned off. Back up, or tap .5x to use the Ultra Wide camera, which focuses as close as 2 centimetres on macro models.

### Why does my iPhone switch from the telephoto lens to the main camera?

The telephoto lens can't focus on very close subjects and may not get a clean exposure in dim scenes, so the iPhone falls back to the Main camera and crops to match your zoom. Lock Camera stops that while you record.

### Is Lock Camera on by default?

No. Apple says Lock Camera is off by default. Turn it on in Settings > Camera > Record Video.

### Why does my iPhone video zoom in slightly when I press record?

Enhanced Stabilization crops in slightly to stabilise the picture. It's on by default on iPhone 14 and later. Turn it off in Settings > Camera > Record Video.

**Try ContentCam free.** Records vertical and horizontal at the same time, on iPhone and Android.

★ Rated 4.8 by 580+ creators on the [App Store](https://apps.apple.com/app/id6765881795) and [Google Play](https://play.google.com/store/apps/details?id=app.contentcam.android). [](https://apps.apple.com/app/apple-store/id6765881795?pt=128838819&ct=b-iphone-switching-lenses&mt=8) [](https://play.google.com/store/apps/details?id=app.contentcam.android&referrer=utm_source%3Dblog%26utm_campaign%3Diphone-camera-switching-lenses-while-recording)

Related: [iPhone video settings for landscape](https://contentcam.app/blog/how-to-record-landscape-video-on-iphone/) · [iPhone manual camera controls for video](https://contentcam.app/blog/iphone-manual-camera-controls-video/) · [why iPhone video looks choppy in low light](https://contentcam.app/blog/iphone-video-choppy-low-light-auto-fps/) · [switching between the front and back camera while recording](https://contentcam.app/blog/switch-camera-while-recording-iphone/).

Sources: Apple, iPhone User Guide, "Change video recording settings on iPhone" (iOS 27, support.apple.com, checked 22 October 2026); Apple, iPhone User Guide, "Take macro photos and videos with your iPhone camera" (checked 22 October 2026); Apple Developer Documentation, AVFoundation, AVCaptureDevice.PrimaryConstituentDeviceSwitchingBehavior (developer.apple.com, checked 22 October 2026).
