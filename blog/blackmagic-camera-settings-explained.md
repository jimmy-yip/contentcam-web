# Blackmagic Camera Settings Explained: A Beginner's Guide (2026)

Source: https://contentcam.app/blog/blackmagic-camera-settings-explained/

What every setting in the Blackmagic Camera app actually does: shutter angle, ISO, white balance, frame rate, ProRes vs HEVC, and which to use when. Free app, iPhone and Android.

By Jimmy, developer of ContentCam · 8 September 2026

The Blackmagic Camera app is free, it's on iPhone and Android, and it puts a proper cinema camera interface on a phone. It's made by Blackmagic Design, the company behind DaVinci Resolve and the Pocket Cinema line.

It's also the app people download, open once, and close again, because the screen is covered in numbers nobody explained. This guide explains them. No app of mine is the point here, I just think more people should be able to use this thing properly.

## Shutter angle, and the one rule worth memorising

Shutter angle controls motion blur. It's the setting that most separates footage that looks like video from footage that looks like film, and it's the one most people leave alone because the word is unfamiliar.

Blackmagic Camera lets you set anywhere from 1.1° to 360°. The number you want almost always is **180°**.

At 180°, your shutter speed is exactly half your frame rate. Shoot 24fps and you get 1/48th of a second. Shoot 30fps and you get 1/60th. Shoot 60fps and you get 1/120th. Motion blurs by roughly the amount your eye expects from cinema, and movement looks natural.

Go lower, say 45°, and each frame is a sharper, more frozen slice. Fast movement starts to stutter and look harsh. It's a deliberate effect, used for action and impact, and it's the look of the Saving Private Ryan beach sequence.

Go higher, up towards 360°, and you get heavy blur and a dreamy smear on anything that moves. Useful occasionally, distracting by default.

Set it to 180 and leave it there until you have a reason not to.

## Frame rate: decide where it's going first

On iPhone the app offers 23.98, 24, 25, 29.97, 30, 48, 59.94, 60, 100 and 120fps. On Android it goes further, up to 240fps on supported devices.

The choice is simpler than the list makes it look.

- **24fps** is the cinema standard. Use it if you want a filmic look.
- **25fps** if you're in a PAL region and the footage may end up on broadcast. Also kills flicker under 50Hz lighting.
- **30fps** is the safe default for most social video.
- **60fps and above** is for slow motion. Shoot 60, drop it onto a 30fps timeline, and you get clean half speed. Shoot 120 for quarter speed.

The mistake to avoid: shooting everything at 60fps because higher sounds better. Played back at 60, it looks like a soap opera. Shoot high only when you intend to slow it down.

## ISO: as low as the light allows

ISO is sensitivity to light. Low ISO gives a clean image, high ISO gives a noisy one, and phone sensors are small enough that noise arrives early.

The available range depends on which phone you're using. The rule doesn't: start at the lowest ISO you can and only raise it when the shot is genuinely too dark. Fix light first, raise ISO second.

Many sensors have a native ISO where they perform best, often the base value. If your phone's is documented, park there when you can.

## White balance in Kelvin

The app gives you presets and manual control from 2500K to 10,000K. Lower numbers cool the image towards blue, higher numbers warm it towards orange.

Rough starting points:

- **3200K** for warm indoor tungsten light.
- **4000K** to **4500K** for most mixed indoor lighting.
- **5600K** for daylight.
- **6500K** or higher for overcast and shade, which are bluer than they look.

Lock it manually, and don't agonise over hitting a perfect number. Auto white balance drifts mid-shot, so a wall changes colour when you pan, and no amount of grading fully undoes that. Set it, lock it, move on.

## Codec: ProRes or HEVC

On iOS you can record Apple ProRes 422 HQ, 422, 422 LT and Proxy, plus HEVC (H.265) and H.264. On Android you get HEVC and H.264, plus the APV codec on supported devices.

**Pick HEVC if** you're posting more or less what you shot. It's efficient, the files are manageable, and social platforms re-compress everything you upload anyway.

**Pick ProRes if** you're grading properly, especially with 10-bit footage. It holds up to colour work far better and it edits smoothly without transcoding. Be ready for the file sizes, which are large enough to fill a phone quickly.

ProRes Proxy is the useful middle ground people forget. Small files, easy editing, and Resolve can relink to higher-quality originals later.

## Resolution

The iOS app records up to 4K. The Android app goes up to 8K on supported hardware.

4K is the sensible default. It gives you room to crop or reframe in the edit while still delivering a sharp 1080p, and it doesn't eat storage the way 8K does. Reach for 8K only when you know why you need it.

## Focus and exposure tools

The heads-up display carries lens selection, frame rate, shutter angle, timecode, ISO, white balance, tint, a histogram and audio levels.

Two things to actually use. **Focus assist** outlines what's sharp, which matters because a phone screen in daylight will lie to you about focus. And the **histogram**, where the thing to watch is the right edge: once highlights hit the wall they're gone permanently, while shadows can usually be lifted later. When in doubt, expose slightly under.

## Blackmagic Cloud and Resolve

The app records straight to Blackmagic Cloud, and the footage drops into a DaVinci Resolve project for anyone else on it. Resolve 18.6 or later is required.

If you're one person editing on the same phone or laptop, you can ignore all of this. If you're handing footage to an editor, it removes the entire business of exporting and uploading.

## What you need to run it

the App Store listing now requires iOS 18 or later (Blackmagic's own specs page still says 16.6), iPad needs iPadOS 18 or later, and Android needs Android 13 or later. Supported Android hardware covers recent Samsung Galaxy, Google Pixel, OnePlus, Xiaomi, Sony Xperia, Oppo and Vivo models, though the specific list is worth checking against your handset.

The app is free on both platforms. Blackmagic sells a ProDock accessory at $339 for ATEM control and pro connectivity, which the vast majority of people will never need.

## A sensible starting setup

If you want somewhere to begin and refine later:

- 4K, 30fps (or 24fps if you want the film look)
- Shutter angle 180°
- Lowest ISO the light allows
- White balance locked manually, near 5600K outdoors
- HEVC unless you're grading, then ProRes
- Expose for the highlights, watch the right of the histogram

That setup will look better than automatic on any phone, and every one of those settings is one you now know how to change on purpose.

One thing worth saying plainly, since this is a camera app maker's site: Blackmagic Camera is excellent and free, and if what you need is maximum image quality in a single format, it's a better tool than most paid apps. It records one format at a time, which is a different job from [recording vertical and horizontal in the same take](https://contentcam.app/blog/record-portrait-and-landscape-video-same-time-iphone/). Use whichever matches the problem you have.

Specifications are from the [Blackmagic Camera technical specifications page](https://www.blackmagicdesign.com/products/blackmagiccamera/techspecs), checked 7 September 2026, and the app updates regularly. Related: [24 vs 30 vs 60fps for social](https://contentcam.app/blog/24fps-vs-30fps-vs-60fps-social-media/) · [Blackmagic Camera vs ContentCam](https://contentcam.app/blog/blackmagic-camera-vs-contentcam/) · [iPhone manual camera controls for video](https://contentcam.app/blog/iphone-manual-camera-controls-video/) · [mobile videography tips](https://contentcam.app/blog/mobile-videography-tips/) · [what happened to Filmic Pro](https://contentcam.app/blog/what-happened-to-filmic-pro/) · [Android camera settings for video](https://contentcam.app/blog/android-camera-settings-for-video/) · [Blackmagic Camera vs Filmic Pro](https://contentcam.app/blog/blackmagic-camera-vs-filmic-pro/).

★ Rated 4.8 by 580+ creators on the [App Store](https://apps.apple.com/us/app/contentcam-dual-camera-video/id6765881795) and [Google Play](https://play.google.com/store/apps/details?id=app.contentcam.android).
