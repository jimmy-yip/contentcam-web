# How Do You Film Workout Videos on Your Phone? (2026)

Source: https://contentcam.app/blog/film-workout-videos-phone/

Camera distance, tripod height, frame rate and shutter for filming workouts on a phone, how to beat gym light flicker at 50Hz and 60Hz, and how to get a TikTok cut and a YouTube cut from one session.

By Jimmy, developer of ContentCam · 26 October 2026

Phone workout footage usually fails for four mechanical reasons, none of them the phone. The camera is too close and on the ultra wide lens, so limbs bend. The phone is on automatic, so exposure jumps every time a chrome plate crosses the frame. The shutter does not match the gym's mains frequency, so the LED panels roll dark bars up the picture. And the session is filmed in one aspect ratio, so the YouTube version ends up a cropped strip of the TikTok version. Each has a fixed setting as a fix.

## Where should you put the phone to film a workout?

Put the phone 2.5 to 3 metres back on the main (1x) lens, with the lens at hip height, 1.0 to 1.2 metres off the floor. That distance fits a standing adult head to toe with some headroom, and that height puts the camera at the middle of the body instead of looking down at it. Three placements cover nearly every exercise:

- **Side on, hip height, 2.5 to 3 metres.** The form angle: squat depth, hip hinge, bar path and knee travel read only from the side. Film this one first.
- **Three-quarter front, 45 degrees off the shoulder line.** Looks like content rather than a coaching clip, because it shows the face and the movement.
- **Low for floor work.** Press-ups, planks and hip thrusts want the lens 0.3 to 0.5 metres off the floor, 2 metres back, level with the body.

Stay off the ultra wide (0.5x) lens closer than about 2 metres. It stretches whatever sits near the frame edge, so an arm at full extension reads longer and thicker than it is and a straight barbell reads as curved. Use it for one case: a rack jammed against a mirror where 3 metres of floor does not exist.

## What frame rate and shutter speed should you use for workout videos?

Shoot 30fps with a 1/60 shutter for anything you will talk over, and 60fps with a 1/120 shutter for anything you want to slow down. 60fps on a 30fps timeline runs at half speed with every frame real, which is what makes a clean rep look heavy. 120fps gives quarter speed: too slow for a full set, right for a 2 second detail such as a bar leaving the chest.

The numbers come from the 180 degree shutter rule: shutter at double the frame rate. 1/48 at 24fps, 1/50 at 25fps, 1/60 at 30fps, 1/100 at 50fps, 1/120 at 60fps. A faster shutter freezes each frame on its own and makes fast limb movement strobe, which is why a kettlebell swing filmed at 1/500 in bright gym light looks jerky rather than sharp. Pick the rate per exercise, not per session; both cut together on a 30fps timeline.

## Why does gym lighting make dark bars roll across phone video?

Gym LED and fluorescent panels pulse at twice the mains frequency, and a shutter speed that is not a whole multiple of that pulse records some frames brighter than others. Australia, the UK and Europe run 50Hz mains, so the light pulses 100 times a second and 1/50 and 1/100 are safe. North America and much of Japan run 60Hz, so the pulse is 120 times a second and 1/60 and 1/120 are safe.

Phone cameras carry a documented setting for this. Android's Camera2 API defines CONTROL_AE_ANTIBANDING_MODE_50HZ as "The camera device will adjust exposure duration to avoid banding problems with 50Hz illumination sources", with a matching 60HZ constant and an AUTO mode that "will automatically adapt its antibanding routine to the current illumination condition" ([developer.android.com](https://developer.android.com/reference/android/hardware/camera2/CaptureRequest), checked 26 October 2026).

The trap at 50Hz mains: 60fps wants 1/120 under the 180 degree rule, and 1/120 is not a multiple of a 100Hz pulse. In a 50Hz country, film slow motion at 1/100 and accept a little more motion blur, or shoot 50fps.

## What camera settings should you lock before a set?

Lock exposure, focus and white balance before the first rep. A gym is full of moving high contrast objects: chrome plates, a white singlet, a black rubber floor, a mirror. Automatic exposure re-meters on every one, so the lifter's face brightens and darkens through a set that was lit identically throughout.

Apple's AVFoundation documents AVCaptureDevice.ExposureMode.locked as "A mode that locks exposure for the device" and AVCaptureDevice.FocusMode.locked as "A mode that locks device focus" ([developer.apple.com](https://developer.apple.com/documentation/avfoundation/avcapturedevice/exposuremode-swift.enum/locked), checked 26 October 2026). Android's Camera2 API carries CONTROL_AE_LOCK and CONTROL_AWB_LOCK for the same job, and tap-and-hold on a stock camera app sets the first two.

- **Exposure.** Meter on the lifter's face, then lock. Gym ceilings are bright and gym floors are dark, so an unlocked camera splits the difference and leaves the person too dark.
- **White balance.** One fixed Kelvin value per location. Gym LED panels generally sit between 4000K and 5000K, daylight through glass is nearer 5600K, and older fluorescent tubes are greener than either.
- **Focus.** Lock it with the lifter standing on the spot, so the lens stops hunting when someone walks between the camera and the rack.

## How do you film a workout for TikTok and YouTube at the same time?

Keep the whole body inside the centre third of the wide frame, or record both aspect ratios in the same take. The arithmetic is brutal: crop a 16:9 recording to full height 9:16 and 81/256 of the original width survives, which is 31.6%. A barbell that fills a wide frame is 68% gone in the vertical cut, and the usual casualty is the end of the bar with the plates on it. Going the other way is worse: crop a 1080 x 1920 vertical to 16:9 and you are left with 1080 x 608, below 720p and unusable as a YouTube main video.

So either film every set twice, once framed wide and once vertical, or record 9:16 and 16:9 together in one take, which is the problem [ContentCam](https://contentcam.app/) was built for: one set, two correctly framed files, the same rep in both. Either way the discipline is the same: nothing that matters goes near the left or right edge of the wide frame.

## What audio can you actually get in a gym?

Assume gym audio is unusable and plan a voiceover. A commercial gym gives you ceiling music you cannot license, plate noise, air conditioning and other members talking, and no phone microphone separates a voice from that at 3 metres. For sync sound, clip a lavalier microphone to the centre of the chest 20cm below the chin and talk between sets, not during them. Grab 10 seconds of the empty gym too: that room tone under a voiceover makes a kitchen-table recording sound like it happened in the gym.

## Common questions

**What is the best camera angle for filming squats and deadlifts?** Side on, lens at hip height, 2.5 to 3 metres away, whole bar in frame. It is the only angle showing squat depth and bar path together. A three-quarter front angle is the better looking shot and the worse coaching shot.

**Should fitness videos be filmed vertical or horizontal?** Both, from one session. TikTok, Instagram Reels and YouTube Shorts want 9:16; a YouTube main video or a coaching library wants 16:9. Cropping one from the other keeps 31.6% of the width or drops the height to 608 pixels, so frame for both while filming.

**Do you need a gimbal to film workout content?** Not for the main angles, because the camera stays static on a tripod while the body moves. A gimbal earns its place only if you walk the camera around the lifter.

**What white balance should you use in a gym?** Set a fixed value between 4000K and 5000K for LED panels, closer to 5600K if a wall of glass is lighting the room, and leave it there for the session. Automatic white balance drifts the moment the lifter moves from under a panel into daylight.

**How do you film yourself alone in a busy gym?** Film in the quiet hour, wedge a mini tripod on a bench or a rack rather than standing a full tripod in a walkway, and hold it to three sets per exercise. Ask the staff first, and never keep a frame with another member identifiable in it.

**How long should a workout clip be?** Cut the vertical version to 15 to 30 seconds, which is two or three reps and one cue, and let the wide version run as long as the explanation needs.

**Try ContentCam free.** Records vertical and horizontal at the same time, with manual exposure, white balance, ISO and shutter. On iPhone and Android.

 Rated 4.8 by 580+ creators on the [App Store](https://apps.apple.com/us/app/contentcam-dual-camera-video/id6765881795) and [Google Play](https://play.google.com/store/apps/details?id=app.contentcam.android). [](https://apps.apple.com/us/app/contentcam-dual-camera-video/id6765881795?pt=128838819&ct=b-film-workout-videos-phone&mt=8) [](https://play.google.com/store/apps/details?id=app.contentcam.android&referrer=utm_source%3Dblog%26utm_campaign%3Dfilm-workout-videos-phone)

Related: [24fps vs 30fps vs 60fps for social media](https://contentcam.app/blog/24fps-vs-30fps-vs-60fps-social-media/) · [how to hold your phone steady while filming](https://contentcam.app/blog/hold-phone-steady-while-filming/) · [filming for TikTok and YouTube at the same time](https://contentcam.app/blog/film-for-tiktok-and-youtube-at-the-same-time/)
