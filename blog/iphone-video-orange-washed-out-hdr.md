# Why Does iPhone Video Look Orange or Washed Out After Editing? (2026)

Source: https://contentcam.app/blog/iphone-video-orange-washed-out-hdr/

iPhone records HDR by default. When an edit keeps the HDR labels but not the HDR pixels, skin and emojis go orange; when HDR plays as standard video, it looks grey. How to check a file and fix it.

By Jimmy, developer of ContentCam · 22 October 2026

Because the iPhone records HDR video by default, and somewhere between the camera and the upload the colour labels on the file stopped matching the pixels inside it. If HDR pixels get played as ordinary video, the clip looks grey and flat. If ordinary pixels and graphics end up in a file still labelled HDR, skin, emojis and anything warm go orange. The fix is to convert every clip to standard video once, at the start of the edit, or to turn HDR off before you film.

I'm writing this because it happened to me last week. A batch of 14 reels I edited went out with orange skin, orange emojis and pink-tinged white panda fur, and the cause turned out to be one setting nobody sees.

## What does the iPhone actually record?

Apple's iPhone User Guide says that "on supported models, iPhone records video in Dolby Vision HDR for true-to-life color and contrast." It's on unless you turn it off. Dolby Vision on iPhone is built on HLG, a broadcast HDR format, so ordinary tools see it as HLG.

I checked my own clips with ffprobe, the free command-line tool that reads a video file's metadata. Every iPhone clip from the trip said the same thing: HEVC, 10-bit, transfer arib-std-b67 (that's HLG) and colour primaries bt2020. Standard video, which is what almost every editor, phone feed and laptop expects, is 8-bit, transfer bt709, primaries bt709. Those labels are what tell a player how to turn numbers into colours. They're the whole story here.

## Why does HDR footage look washed out?

Washed out means HDR pixels are being shown as if they were standard video. BT.2020 is a much wider colour space than BT.709, so the same pixel value describes a more saturated colour in BT.2020. Read those values as BT.709 and every colour shrinks back towards grey. Contrast flattens too, because the HDR brightness curve is being drawn on the wrong scale.

You usually see this when an app, a website or an older editor ignores the labels. The clip looks right on your iPhone, because the iPhone reads the labels, and dull everywhere else.

## Why does it look orange or oversaturated instead?

This is the opposite problem: the file still says HDR, but what's inside isn't clean HDR any more. That's what happened to my reels. The edit decoded each iPhone clip, added text and emojis, and encoded the result. The new file kept the HLG and BT.2020 labels, but it was only 8-bit, and the text and emojis were standard sRGB graphics laid on top with no conversion.

On screens that respect those labels, the result was:

- **Skin** went from cream to orange.
- **Emojis** went from yellow to orange, because sRGB values read as BT.2020 come out far more saturated.
- **White panda fur** picked up a red tint.

Nothing looked wrong in the editor's preview, which is why it shipped. The tell was the reel whose emojis looked fine. Its file was labelled BT.709, standard video, because it opened on a screen recording rather than iPhone camera footage.

## How do you check if a video is HDR?

Run ffprobe on the file and look at the video stream: ffprobe -v error -select_streams v:0 -show_entries stream=pix_fmt,color_transfer,color_primaries,color_space -of compact clip.mov

- color_transfer=arib-std-b67 means HLG. smpte2084 means PQ, another HDR curve. Either one is HDR.
- color_transfer=bt709 with color_primaries=bt709 is standard video.
- An HDR label next to pix_fmt=yuv420p, which is 8-bit, is the warning sign. HDR video is normally 10-bit, so an 8-bit file labelled HDR has most likely been through a tool that copied the labels without converting the pixels.

Check the file you are about to upload, not just the original. My originals were fine. The export was the broken one.

## How do you fix it?

Pick the earliest fix you can still use.

1. **Turn HDR off before filming** if you don't need it. Apple's path: Settings > Camera > Record Video, then turn off HDR Video, or HDR on some models. Everything you film after that is standard video, and nothing downstream can mislabel it.
2. **Export as SDR from Apple's own editors.** Apple's support article on editing HDR video says that when you share from iMovie on iPhone or iPad you can turn HDR off, and that iMovie for Mac can share in SDR. SDR, standard dynamic range, is the opposite of HDR.
3. **Convert each clip to SDR before you edit, not after.** This is what fixed my batch. I convert every HDR clip with Apple's AVFoundation, asking for BT.709 output so the system does the tone mapping, then build the edit from those copies. Text, emojis and footage then all share one colour space, and the output is labelled BT.709. Converting at the start beats converting at the end because the graphics never meet HDR pixels at all.
4. **Label the output explicitly.** If you encode with ffmpeg, add -colorspace bt709 -color_primaries bt709 -color_trc bt709 so the file doesn't inherit stale HDR labels from a source clip.

One trap I hit: not every converter does the same job. My first attempt used a hardware-accelerated scaler and pushed bright reds too far. Apple's own conversion matched the original clips when I put them side by side, so that's the one I kept. Whatever you use, put a converted frame next to the original on the same screen and look at skin before you trust it.

## Should you film in HDR for TikTok, Reels and Shorts?

For most short-form creators, no. HDR looks great on the iPhone that shot it. After that, every editor, platform and viewer's screen gets a chance to read it differently, and you can't see most of those screens. Standard video looks the same nearly everywhere, which matters more than extra highlight range on a phone held at arm's length. Keep HDR for footage you'll grade properly and deliver as HDR on purpose.

If you've already filmed a trip in HDR, as I had, the clips aren't ruined. Convert them once, before editing, and they'll look the way they did on your phone.

## FAQ

### Why does my iPhone video look washed out on my computer?

The iPhone records Dolby Vision HDR by default, and the app on your computer is showing those HDR pixels as standard video. Colours shrink towards grey and contrast flattens. Play it in an app that supports HDR, or export an SDR version.

### Why do emojis and skin turn orange in my edited video?

The exported file is most likely still labelled HDR (HLG, BT.2020) while the pixels inside, including the text and emojis, are standard video. Players that trust the label push the colours too far. Convert the iPhone clips to SDR before editing and label the export BT.709.

### How do I turn off HDR video on iPhone?

Go to Settings > Camera > Record Video and turn off HDR Video, or HDR on some models.

### Does turning off HDR make iPhone video worse?

Only on HDR screens, where you lose some highlight range. On most social feeds and most screens, a standard video file looks more consistent than an HDR one.

**Try ContentCam free.** Records vertical and horizontal at the same time, on iPhone and Android.

★ Rated 4.8 by 580+ creators on the [App Store](https://apps.apple.com/us/app/contentcam-dual-camera-video/id6765881795) and [Google Play](https://play.google.com/store/apps/details?id=app.contentcam.android). [](https://apps.apple.com/us/app/contentcam-dual-camera-video/id6765881795?pt=128838819&ct=b-iphone-video-orange-hdr&mt=8) [](https://play.google.com/store/apps/details?id=app.contentcam.android&referrer=utm_source%3Dblog%26utm_campaign%3Diphone-video-orange-washed-out-hdr)

Related: [best iPhone video settings for Instagram Reels](https://contentcam.app/blog/iphone-video-settings-for-instagram/) · [High Efficiency vs Most Compatible on iPhone](https://contentcam.app/blog/iphone-high-efficiency-vs-most-compatible/) · [the phone video settings cheat sheet](https://contentcam.app/blog/phone-video-cheat-sheet/) · [video terms explained](https://contentcam.app/blog/video-terms-explained/) · [iPhone video settings for landscape](https://contentcam.app/blog/how-to-record-landscape-video-on-iphone/).

Sources: Apple, iPhone User Guide, "Adjust HDR camera settings on iPhone" (support.apple.com, checked 22 October 2026); Apple Support, "Edit HDR video recorded on your iPhone or iPad" (support.apple.com, published 20 March 2025, checked 22 October 2026). File measurements: ffprobe on my own iPhone clips and exported reels, October 2026.
