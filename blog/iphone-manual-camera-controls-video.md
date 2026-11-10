# iPhone Manual Camera Controls for Video: ISO, Shutter & White Balance (2026)

Source: https://contentcam.app/blog/iphone-manual-camera-controls-video/

What ISO, shutter speed and white balance actually do for video, when auto fails, the 180° shutter rule, and a kelvin cheat sheet from 2500K to 8000K.

By Jimmy, developer of ContentCam · 13 July 2026

Auto mode on a phone camera is genuinely good, most of the time. This guide is about the specific moments it isn't, what each manual control does about it, and the settings that work. No photography-course padding.

## White balance: the one you'll use most

**What it is:** the camera's guess at the colour of your light, measured in kelvin. Get it wrong and white walls go orange or blue; get it inconsistent and your footage changes colour between cuts.

**How auto fails:** auto white balance re-guesses continuously. Walk from a window to a lamp mid-take and watch your skin tone slide from neutral to orange on camera. Cut two takes together where auto guessed differently, and the colour jump is visible to anyone.

**The fix:** lock it. Set a temperature that looks right and it stays there for the whole take, and the next take, and the one after.

### Kelvin cheat sheet

| Light | Set roughly |
| --- | --- |
| Candle light, very warm bulbs | 2500–2800K |
| Standard indoor bulbs ("warm white") | 2800–3200K |
| Fluorescent / cool white LED | 4000–4500K |
| Daylight, midday sun | 5200–5600K |
| Overcast sky | 6000–6500K |
| Shade on a sunny day | 7000–8000K |

ContentCam's [white balance dial runs 2500K to 8000K](https://contentcam.app/features/manual-controls/), which covers that whole table. There's a tint dial beside it on both iPhone and Android, for the green/magenta axis fluorescents mess up.

## Shutter speed: motion blur is a choice

**What it is:** how long each frame's exposure lasts. It sets how much motion blur each frame carries.

**The 180° rule:** set shutter to roughly double your frame rate. At 30fps, that's 1/60. At 24fps, 1/48. This produces the amount of motion blur people recognise from film. It's not a law, it's a default that looks right.

**How auto fails:** in bright light, auto cranks the shutter to 1/2000 to control exposure, and your footage goes strobey: every frame razor sharp, motion looking like a slideshow. That's why phone footage of moving subjects in sunlight looks "digital".

**When to break the rule:** faster shutter (1/500+) if you're capturing action you'll scrub frame-by-frame; slower if you want dreamier blur. But if you've never set it manually, start at double your frame rate and see what changes.

## ISO: control the noise floor

**What it is:** sensor gain. Low ISO, clean image, needs more light. High ISO, brighter image, visible grain.

**How auto fails:** in dim rooms, auto quietly pushes ISO way up and your dark scenes come out crawling with noise. Auto optimises for "visible", not "clean".

**The trade:** once you lock shutter with the 180° rule, ISO becomes your main brightness lever. Keep it as low as the scene allows; if the image is too dark at a clean ISO, add light rather than gain. A $20 LED panel beats ISO 3200 every time.

## EV bias: manual results without going manual

If full manual feels like too much, exposure bias is the halfway house: auto keeps doing the work, you just tell it "a bit darker" or "a bit brighter". Faces against bright windows (dial down), dark subjects on dark backgrounds (dial up). This is the control to learn first.

## Why this matters double for dual-format recording

ContentCam records [a portrait and a landscape file from every take](https://contentcam.app/features/dual-camera/). Manual settings apply to the capture itself, so both files match exactly: same colour, same exposure, same motion. Lock white balance once and your entire multi-platform edit is colour-consistent, across both timelines.

One honest note: every dial in ContentCam works live on the free tier, so you can watch what 3200K vs 5600K does to your scene before paying anything. Recording with manual controls engaged is a [premium feature](https://contentcam.app/pricing/).

## Starting recipes

| Scene | Settings |
| --- | --- |
| Talking head, indoor, window light | WB 5500K locked, 30fps, shutter 1/60, ISO to taste, EV −0.3 if the window's behind you |
| Golden hour outdoor | WB 5600K (don't let auto "correct" the gold away), shutter 1/60, low ISO |
| Indoor mixed light (window + lamps) | Kill one light source if you can; otherwise WB ~4300K as a compromise, locked |
| Night city | Shutter 1/30–1/60, ISO as low as survivable, WB ~3800K for sodium/LED mix |

**Try the dials before paying.** ContentCam's manual panel is live on the free tier, on iPhone and Android.

★ Rated 4.8 by 580+ creators on the [App Store](https://apps.apple.com/us/app/contentcam-dual-camera-video/id6765881795) and [Google Play](https://play.google.com/store/apps/details?id=app.contentcam.android). [](https://apps.apple.com/us/app/contentcam-dual-camera-video/id6765881795?pt=128838819&ct=b-iphone-manual-camera-controls-video&mt=8) [](https://play.google.com/store/apps/details?id=app.contentcam.android&referrer=utm_source%3Dblog%26utm_campaign%3Diphone-manual-camera-controls-video)

Related: [which frame rate to shoot](https://contentcam.app/blog/24fps-vs-30fps-vs-60fps-social-media/) · [why the iPhone switches lenses while recording](https://contentcam.app/blog/iphone-camera-switching-lenses-while-recording/) · [Manual controls in ContentCam](https://contentcam.app/features/manual-controls/) · [Shooting dual-format timelapses](https://contentcam.app/blog/iphone-timelapse-portrait-and-landscape/) · [Blackmagic Camera settings explained](https://contentcam.app/blog/blackmagic-camera-settings-explained/) · [Filming a talking head at home without the webcam look](https://contentcam.app/blog/talking-head-video-at-home/) · [what happened to Filmic Pro](https://contentcam.app/blog/what-happened-to-filmic-pro/) · [Android camera settings for video](https://contentcam.app/blog/android-camera-settings-for-video/)
