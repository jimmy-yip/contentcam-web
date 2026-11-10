# Why Does My iPhone Video Look Choppy in Low Light? (Auto FPS, 2026)

Source: https://contentcam.app/blog/iphone-video-choppy-low-light-auto-fps/

Auto FPS drops iPhone video from 30 to 24 fps when the light is low. Why that looks choppy, why 24 fps clips stutter in a 30 fps edit, how to check a clip, and where to turn it off.

By Jimmy, developer of ContentCam · 19 October 2026

Most likely because of Auto FPS. Apple's iPhone User Guide says that "iPhone can improve the video quality in low-light situations by automatically reducing the frame rate to 24 fps." Fewer frames a second lets each frame collect more light, so the picture gets brighter and cleaner, but movement is sampled less often and starts to judder. Drop that 24 fps clip into a 30 fps edit and it gets worse, because the editor has to repeat frames to fill the gaps. You can turn it off at Settings > Camera > Record Video > Auto FPS.

## What does Auto FPS do on iPhone?

Auto FPS lets the iPhone Camera app lower the frame rate from 30 fps to 24 fps when the light is poor. Apple's current guide, for iOS 27, gives three choices under Settings > Camera > Record Video > Auto FPS: apply it to 30 fps video only, apply it to both 30 and 60 fps video, or turn it off. The same page adds that "on iPhone 18 Pro models, Auto FPS also works when you record in 4K."

Older iPhones name the setting differently. Apple's iOS 16 guide says that on iPhone XS, iPhone XR, iPhone 11 models and iPhone SE (2nd generation), the switch is called Auto Low Light FPS, in the same Record Video menu.

The trade is simple arithmetic. A frame at 30 fps lasts 33.3 milliseconds, so the longest it can be exposed is 1/30 of a second. At 24 fps a frame lasts 41.7 milliseconds, so the limit rises to 1/24 of a second. That's 25% more light per frame, which is the whole reason Auto FPS exists.

## Why does 24 fps look choppy on a phone?

At 24 fps the camera captures movement in steps 41.7 milliseconds apart instead of 33.3. Film crews hide those steps with slow camera moves and deliberate motion blur. Handheld phone footage does the opposite: quick pans, walking shots and text sliding across the frame. In those shots the steps show as judder.

Low light adds a second problem. Once the iPhone is using the longest exposure it can, anything that moves smears across each frame. Judder plus smear is what people describe as laggy or choppy night footage.

Playback can make it uneven too. A typical 60 Hz screen refreshes 2.5 times per 24 fps frame, so frames are held alternately for 3 refreshes and 2 (50 and 33 milliseconds). Motion moves in a slightly irregular rhythm, which is most visible on slow pans.

## Why does a 24 fps clip stutter in a 30 fps edit?

Because 30 divided by 24 is 1.25. To turn 4 source frames into 5 timeline frames, an editor working at 30 fps repeats one frame in every five, 6 duplicate frames a second, or one hitch every 167 milliseconds. Some editors blend neighbouring frames instead, which trades the hitch for ghosting. Either way the low-light clips move differently from the daylight clips around them.

This is the trap with Auto FPS. It depends on the light when you film, so a night out filmed with Auto FPS on can leave you with a mix of 30 fps and 24 fps clips, and you only notice once they're cut together.

## How do you check what frame rate an iPhone clip was recorded at?

On a Mac, open the clip in QuickTime Player and choose Window > Show Movie Inspector, or press Command-I. Apple's QuickTime Player guide says the inspector shows the video's frame rate in fps, along with its HDR format, compression format and size.

For a batch of clips, ffprobe, the free command-line tool from the FFmpeg project, is quicker: ffprobe -v error -select_streams v:0 -show_entries stream=avg_frame_rate -of csv=p=0 clip.mov

A result of 30/1 or very close to 30 means the clip ran at 30 fps. Anything near 24 means Auto FPS reduced it. When I ran this check across 27 of my own iPhone 13 and iPhone 16 clips, 32 minutes and 57,972 frames in total, every frame lasted 33 milliseconds and none lasted 41 or 42. All 27 were filmed in daylight, which is exactly when Auto FPS shouldn't trigger. The clips to check are the dark ones.

## Should you turn Auto FPS off?

Turn Auto FPS off if any of these apply:

- You'll cut the footage together with clips filmed at 30 fps.
- The scene has fast movement: kids, pets, sport, dancing, or a walking shot.
- You're filming a screen, scrolling text or anything with hard edges moving across the frame.

Leave it on if the low-light scene is mostly still, or if you edit the whole project at 24 fps anyway. There a brighter, cleaner image is worth more than smooth motion.

Turning Auto FPS off doesn't add light. At 30 fps the iPhone has 25% less exposure time per frame to work with, so dark scenes get noisier. Fix that with light rather than frame rate. [How to film low light video on a phone](https://contentcam.app/blog/film-low-light-video-phone/) and [how to light a video with no windows](https://contentcam.app/blog/light-video-no-windows/) cover the cheap ways to do that.

## Does Auto FPS affect other camera apps?

Auto FPS is a setting for Apple's Camera app, in its own Record Video menu. Apps with manual controls, such as Blackmagic Camera, set the frame rate themselves, so check the frame rate setting inside whichever app you film with. For more on choosing a frame rate in the first place, see [24 vs 30 vs 60 fps for social media](https://contentcam.app/blog/24fps-vs-30fps-vs-60fps-social-media/).

## FAQ

### Why is my iPhone video 24 fps when I set it to 30?

Auto FPS lowered it. In low light the iPhone can reduce 30 fps video to 24 fps to let each frame collect more light. Turn it off in Settings > Camera > Record Video > Auto FPS.

### What is Auto Low Light FPS?

It's the older name for the same feature, used on iPhone XS, iPhone XR, iPhone 11 models and iPhone SE (2nd generation).

### Does Auto FPS work in 4K?

Apple's iOS 27 guide says Auto FPS also works in 4K on iPhone 18 Pro models.

### Does turning off Auto FPS make low light video worse?

It makes it smoother but noisier. At 30 fps each frame gets 25% less exposure time than at 24 fps, so add light to the scene rather than relying on the lower frame rate.

**Try ContentCam free.** Records vertical and horizontal at the same time, on iPhone and Android.

★ Rated 4.8 by 580+ creators on the [App Store](https://apps.apple.com/app/id6765881795) and [Google Play](https://play.google.com/store/apps/details?id=app.contentcam.android). [](https://apps.apple.com/app/apple-store/id6765881795?pt=128838819&ct=b-iphone-video-choppy-auto-fps&mt=8) [](https://play.google.com/store/apps/details?id=app.contentcam.android&referrer=utm_source%3Dblog%26utm_campaign%3Diphone-video-choppy-low-light-auto-fps)

Related: [24 vs 30 vs 60 fps for social media](https://contentcam.app/blog/24fps-vs-30fps-vs-60fps-social-media/) · [how to film low light video on a phone](https://contentcam.app/blog/film-low-light-video-phone/) · [why the iPhone switches lenses while recording](https://contentcam.app/blog/iphone-camera-switching-lenses-while-recording/) · [recording long videos on iPhone without overheating](https://contentcam.app/blog/record-long-video-iphone-without-overheating/) · [why an iPhone video stops recording by itself](https://contentcam.app/blog/iphone-video-stopped-recording-by-itself/)

Sources: Apple, iPhone User Guide, "Change video recording settings on iPhone" (iOS 27, support.apple.com, checked 22 October 2026); Apple, iPhone User Guide, "Change video recording settings on iPhone" (iOS 16, checked 22 October 2026); Apple, QuickTime Player User Guide, "View information about media files" (checked 22 October 2026). Frame measurements: ffprobe on 27 of my own iPhone 13 and iPhone 16 clips, October 2026.
