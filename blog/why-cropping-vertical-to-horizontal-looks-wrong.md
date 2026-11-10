# Why Does Cropping Vertical Video to Horizontal Look Wrong? (2026)

Source: https://contentcam.app/blog/why-cropping-vertical-to-horizontal-looks-wrong/

A 9:16 crop to 16:9 keeps 31.6% of the picture, and a centred crop starts 16 pixels below a correctly framed eyeline. The arithmetic, the three workarounds and their costs, and how to frame so both versions survive.

By Jimmy, developer of ContentCam · 14 October 2026

Cropping a 9:16 vertical clip to 16:9 keeps 31.6% of the picture and throws away 68.4%, and what the crop throws away is the top and the bottom of the frame, which is where a vertical composition puts everything worth seeing. That is the whole problem. Here is the arithmetic, the three ways out, and what each one costs.

## What happens to the pixels when you crop 9:16 to 16:9?

A 1080×1920 vertical recording cropped to 16:9 at full width becomes 1080×607. The surviving fraction is (9/16) divided by (16/9), or 81/256, which is 31.6%. Delivering that strip as a 1920×1080 file means scaling it up 1.78 times in each direction, so every recorded pixel is smeared across 3.16 output pixels. A 1080×607 strip is already below 720p before the upscale begins, and scaling up adds no detail, only a second generation of compression.

Film the vertical take in 4K and the arithmetic changes. A 2160×3840 recording cropped to 16:9 at full width is 2160×1215, larger than 1920×1080 in both directions with 12.5% to spare, so that crop downscales into a genuine 1080p horizontal file. Shooting resolution is the choice that separates a usable crop from an unusable one, and the choice is made before you press record.

Crop-then-scale is how the camera pipeline itself works, so the loss is not an editing artefact. Android's Camera2 documentation describes SCALER_CROP_REGION as "The desired region of the sensor to read out for this capture. This control can be used to implement digital zoom", and states that output streams "use this rectangle to produce their output, cropping to a smaller region if necessary to maintain the stream's aspect ratio, then scaling the sensor input to match the output's configured resolution" ([developer.android.com](https://developer.android.com/reference/android/hardware/camera2/CaptureRequest), checked 14 October 2026).

## Why does a centred crop cut the subject's eyes out of the frame?

Because a vertical frame puts the eyeline about a third of the way down, and a centred 16:9 window starts below the eyeline. In a 1920 pixel tall frame, upper-third framing puts the eyes near y = 640. A centred 607 pixel tall window runs from y = 656 to y = 1264, so the eyeline sits about 16 pixels above the top edge of that window and a centred crop of a correctly framed talking head starts at the mouth.

Drag the crop window up instead of leaving it centred. Moving the window up 219 pixels, 11.4% of the frame height, puts it between y = 437 and y = 1045 and lands the eyes a third of the way down inside the horizontal frame. Every vertical clip needs the same correction, which is why batch-cropping a folder of vertical files produces a folder of chin shots.

## Why does a cropped vertical never look like a real wide shot?

Because the crop keeps none of the width that makes a wide shot wide. Phone cameras read out a 4:3 sensor frame, which is 3024×4032 pixels on a 12 megapixel camera. A 9:16 recording cut from that sensor frame uses 2268 of the 3024 available pixels of width, 75% of the horizontal field of view, and a 16:9 crop taken from the vertical file inherits the narrowing.

Take the same 16:9 framing from the full 4:3 readout and the frame measures 3024×1701 pixels, against 2268×1275 cut from the vertical file. That is 78% more area and a third more horizontal field of view. No editor recovers the difference, because those pixels were never written to the file.

## What are the three ways to put a vertical clip into a 16:9 slot?

Crop it, pillarbox it, or record both shapes in the first place. The first two are documented video scaling behaviours rather than editing tricks, and each carries a fixed price. The step-by-step for each in Photos, iMovie and CapCut is in [how to convert vertical video to horizontal](https://contentcam.app/blog/convert-vertical-video-to-horizontal/).

- **Crop, which is aspect fill.** Apple's AVFoundation documentation describes AVVideoScalingModeResizeAspectFill: "This mode crops the video to fit the destination dimensions, preserving the aspect ratio of the source video" ([developer.apple.com](https://developer.apple.com/documentation/avfoundation/avvideoscalingmoderesizeaspectfill), checked 14 October 2026). Price: 68.4% of the picture, plus the eyeline correction above.
- **Pillarbox, which is aspect fit.** The same documentation describes AVVideoScalingModeResizeAspect: "This mode preserves the aspect ratio of the source and fills the remaining areas with black to fit the destination dimensions" ([developer.apple.com](https://developer.apple.com/documentation/avfoundation/avvideoscalingmoderesizeaspect), checked 14 October 2026). A 1080×1920 clip at full height inside a 1920×1080 frame is 607 pixels wide with 656 pixels of filler down each side, so 31.6% of the delivered width carries picture. Swapping a blurred copy of the clip in for the black changes the colour of the filler and nothing else.
- **Record both shapes.** Price: your time, which is usually cheaper than either option above.

## Does auto-reframe in an editor fix the problem?

Auto-reframe chooses a better crop; auto-reframe does not add picture. A subject tracker slides the same 31.6% window around to follow a face, which beats a static centred crop for one person standing still. The tracker fails in four predictable cases: two people at opposite edges of the frame, a hand or a product entering from the bottom edge, a subject who stands up, and any shot where the face and the action sit in different parts of the frame. In each case the tracker picks one and loses the other, often panning while deciding, which reads as a camera move nobody filmed.

Generative fill is not a rescue either, because anything that extends a frame sideways is inventing picture that was never in front of the lens. On a plain wall that passes. On a hand, a face or a sign a brand client sees it immediately.

## Is cropping horizontal to vertical any better?

The pixel loss is identical, but the loss lands somewhere more survivable. A 1920×1080 horizontal clip cropped to a full height 9:16 is 607×1080, the same 81/256. What differs is the part thrown away. Horizontal compositions put the subject near the middle and the context at the sides, so a centred crop usually keeps the subject and loses the room. Vertical compositions run information up and down the frame, so the same crop loses the eyeline, the product in the subject's hands, or both.

The 4K rule holds in this direction too. A 3840×2160 recording cropped to 9:16 at full height is 1215×2160, comfortably above 1080×1920, so a 4K horizontal take yields a true 1080p vertical cut.

## How should you frame a vertical shot so the horizontal crop survives?

Film at 4K, keep the eyeline and the action between 23% and 54% of the vertical frame height, and leave the top and bottom edges empty on purpose.

- **Film 4K when one take has to serve both shapes.** 2160×1215 is a deliverable crop. 1080×607 is not.
- **Compose to the horizontal window, not to the vertical frame.** After the eyeline correction, that window sits between 23% and 54% of the frame height. Lay a thumb across the top quarter of the phone screen while you set up and you are looking at roughly what the horizontal version will show.
- **Frame looser than feels right.** A loose vertical costs you some empty space. A tight vertical costs you the horizontal version entirely.
- **Keep the movement horizontal.** A pan, a walk and a hand crossing the frame all survive the crop. A tilt, a stand-up and anything entering from the bottom edge do not.
- **Record both shapes from the full sensor frame.** This is what I built [ContentCam](https://contentcam.app/) to do: cut the 9:16 and the 16:9 from the same 4:3 readout, so the horizontal file keeps the full sensor width instead of inheriting the vertical file's 75%.

## Should you shoot vertical or horizontal for each platform?

The rule underneath every row: a video looks best when its shape matches the screen it plays on. Where I could check the platform's own help page, the row says so; the rest describe how the app displays video, not an official spec.

| Platform | Shoot | Why |
| --- | --- | --- |
| TikTok | Vertical 9:16 | The feed is full screen on a phone held upright, so anything wider plays as a strip with empty space above and below. |
| Instagram Reels | Vertical 9:16 | Same full-screen, upright feed as TikTok. |
| YouTube Shorts | Vertical 9:16 | YouTube Help: a Short is "up to 3 minutes" with "a square or vertical aspect ratio". Vertical fills the screen; square does not. |
| YouTube main feed | Horizontal 16:9 | YouTube Help: "The standard aspect ratio for YouTube on a computer is 16:9." Vertical videos on computer browsers may get extra padding at the sides. |
| LinkedIn | Either | LinkedIn Help lists an accepted aspect ratio range of 1:2.4 to 2.4:1, so both upload fine. In the phone feed, a taller video takes up more of the screen. |
| X | Either | The feed shows both shapes inline. Taller takes more of a phone screen; wide suits screen recordings and anything watched on a laptop. |
| Facebook feed | Either; vertical for Facebook Reels | The main feed shows both. Facebook Reels is a full-screen upright feed like Instagram's. |
| Website embeds | Horizontal 16:9 | Most article layouts and embedded players are wide. A vertical video inside a wide player sits between empty side panels. |

YouTube and LinkedIn rows checked against [YouTube Help: Video resolution and aspect ratios](https://support.google.com/youtube/answer/6375112), [YouTube Help: Upload YouTube Shorts](https://support.google.com/youtube/answer/12779649) and [LinkedIn Help: video specs](https://www.linkedin.com/help/linkedin/answer/a548372), 3 November 2026.

The split comes down to this: the fast feeds people swipe through on a phone are vertical, and the places people sit back and watch, or search and find a video months later, are horizontal.

## Vertical or horizontal: the decision in one table

| Your situation | Shoot |
| --- | --- |
| Only TikTok, Reels or Shorts | Vertical 9:16 |
| Only the main YouTube feed, a website or a TV | Horizontal 16:9 |
| LinkedIn, X or the Facebook feed only | Either; vertical if your audience watches on phones |
| A vertical feed and a horizontal player | Both, from one take |
| Not sure yet | Both, so you never have to crop later |

## Common questions

**Can you convert a vertical video to horizontal without losing quality?** No. The conversion is a crop, and the crop keeps 31.6% of the picture. The only version that ends well is cropping a 4K vertical, where the surviving 2160×1215 is still larger than 1080p.

**What resolution should you film at if you need both shapes?** 4K. A 4K vertical take crops to a real 1080p horizontal file, while a 1080p vertical take crops to 1080×607, which is below 720p.

**Does AI upscaling rescue a 1080×607 crop?** An upscaler sharpens edges and invents texture, and at phone size the result can pass. An upscaler cannot restore the 68.4% of the frame that was cut away, and the missing picture, not the softness, is what looks wrong.

**Why do vertical clips look so small on YouTube?** A pillarboxed 9:16 clip inside a 16:9 player is 607 pixels wide out of 1920, so 31.6% of the width carries the picture and the remaining 1312 pixels carry black or blur.

**Try ContentCam free.** Records vertical and horizontal at the same time, on iPhone and Android.

★ Rated 4.8 by 580+ creators on the [App Store](https://apps.apple.com/app/id6765881795) and [Google Play](https://play.google.com/store/apps/details?id=app.contentcam.android). [](https://apps.apple.com/app/apple-store/id6765881795?pt=128838819&ct=b-why-cropping-vertical-looks-wrong&mt=8) [](https://play.google.com/store/apps/details?id=app.contentcam.android&referrer=utm_source%3Dblog%26utm_campaign%3Dwhy-cropping-vertical-to-horizontal-looks-wrong)

Related: [filming b-roll that works vertical and wide](https://contentcam.app/blog/film-b-roll-vertical-and-wide/) · [vertical vs horizontal video, and which to shoot](https://contentcam.app/blog/why-cropping-vertical-to-horizontal-looks-wrong/) · [how to record landscape video on iPhone](https://contentcam.app/blog/how-to-record-landscape-video-on-iphone/) · [filming UGC in vertical and horizontal from one take](https://contentcam.app/blog/film-ugc-vertical-and-horizontal/) · [how to convert vertical video to horizontal](https://contentcam.app/blog/convert-vertical-video-to-horizontal/)
