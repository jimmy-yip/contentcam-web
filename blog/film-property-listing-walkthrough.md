# How Do You Film a Property Listing Walkthrough on a Phone? (2026)

Source: https://contentcam.app/blog/film-property-listing-walkthrough/

Walk at half pace with the phone at 1.4 metres, lock exposure, white balance and focus before you start, and shoot the room when its own windows are in shade. The full method for a one-take listing walkthrough.

By Jimmy, developer of ContentCam · 7 October 2026

A phone walkthrough of a house usually fails for three mechanical reasons. The phone is on automatic, so it rebrightens in every doorway and changes colour between a daylit kitchen and a lamp-lit hall. The agent walks at normal speed, so no room is on screen long enough to read. The phone is held high and tilted down, so every vertical line in the house leans. Fix those three and a phone walkthrough looks like a camera walkthrough.

## What order should you walk a property in?

Walk the property the way a buyer physically would: street approach, front door, entry, main living space, kitchen, bedrooms from largest to smallest, bathrooms, laundry, then outside. A buyer watching a tour is building a floor plan in their head, and a cut from the main bedroom back to the front step destroys it.

Walk the property once with nothing recording first. That pass is where you find the bin in shot, the door that swings into frame, the mirror that will show you holding the phone, and the rooms whose windows are facing the sun right now.

Put the best room second, not first. Opening on the entry and then revealing the living space gives the video somewhere to go. Opening on the best room means every shot after it is a step down.

## How fast should you walk when filming a property walkthrough?

Walk at roughly half your normal pace, about 0.7 metres per second against a normal walking speed of around 1.4, and hold the phone at about 1.4 metres off the floor. That height is chest height for most adults, and it is deliberately lower than eye level: a slightly low camera makes ceilings look taller.

Keep the phone level. The instinct in a small room is to tilt up to get the ceiling in, and tilting is what makes door frames and wall corners splay outwards at the edges of the frame. A level phone keeps vertical lines vertical, which is most of what separates a property video from a holiday video.

Technique for the walk itself: both hands on the phone, elbows pressed into your ribs, knees soft, heel to toe. Walk through doorways square on, and keep going straight for two seconds after the door frame leaves the shot rather than turning in the doorway. Turning while walking is the move that makes viewers feel seasick.

Use the main camera, not the ultra wide, for the walk. An ultra wide sits around a 13mm full frame equivalent against roughly 24mm for a main camera, and at 13mm straight lines bend near the frame edge and rooms read as longer than they are. Save the ultra wide for one static corner shot of a bathroom too small to shoot any other way.

## What camera settings should you lock before a property walkthrough?

Lock exposure, white balance and focus before the walk starts, and set the shutter to double the frame rate. Automatic versions of all three change their mind mid-shot, and a listing walkthrough crosses more lighting conditions in 90 seconds than almost any other kind of video.

Locking is a documented camera state on both platforms. Apple's AVFoundation documentation describes AVCaptureDevice.ExposureMode.locked as "A mode that locks exposure for the device" and WhiteBalanceMode.locked as "A mode that locks the white balance state" ([developer.apple.com](https://developer.apple.com/documentation/avfoundation/avcapturedevice/whitebalancemode-swift.enum), checked 7 October 2026). Android's Camera2 API carries the same pair as capture request keys CONTROL_AE_LOCK and CONTROL_AWB_LOCK, "Whether auto-exposure (AE) is currently locked to its latest calculated values" ([developer.android.com](https://developer.android.com/reference/android/hardware/camera2/CaptureRequest), checked 7 October 2026). Any camera app with manual controls is setting these.

- **Frame rate and shutter.** 30fps with a 1/60 shutter. At 25fps use 1/50, at 24fps use 1/48. A faster shutter sharpens each frame and makes a walking shot stutter, which is the single most common reason a walkthrough looks wrong without anyone being able to say why.
- **White balance.** One fixed Kelvin value for the whole property. Around 5600K when daylight through windows is the main source, 2700K to 3000K under warm domestic bulbs, and the daylight value wins in any room where both are present. Automatic white balance will drift in a hallway with a warm bulb and then drift back in the kitchen, so the house looks like three different houses in one video.
- **Exposure.** Set it in the brightest room you will walk into, then lock it. Set in a dark hall, every lit room clips to white the moment you step in.
- **Focus.** Lock it about two metres out. Phone wide lenses hold a deep enough depth of field that the rest of a normal room stays sharp, and locking stops the autofocus pulsing every time a door frame crosses the centre of the frame.

## How do you film a room with a bright window in it?

Expose for the room and let the window go white, or put the window behind the camera. A phone cannot hold both ends of that frame. Direct sun outdoors sits around EV 15 on the standard exposure scale and a normally lit interior around EV 7 or 8, so the two are seven to eight stops apart, well past what a small sensor renders in one exposure.

Four things that shrink the gap:

- **Time each room to its own windows.** Film east-facing rooms in the afternoon and west-facing rooms in the morning. With the sun off the glass, the frame holds both the interior and a readable view outside.
- **Prefer an overcast day for interiors.** Cloud is a softbox over the whole property. Save the clear morning for exteriors and the pool.
- **Close sheer curtains, not heavy ones.** Sheers pull the window brightness down towards the room without blacking out the view, which is often what the room is being sold on.
- **Decide on the lamps room by room.** In a daylit room, switch warm lamps off so the colour stays consistent. In a windowless bathroom or a laundry, switch everything on.

## How do you frame a room so it reads at its real size?

Stand in a corner with your back near the wall, phone level at 1.4 metres, and get both some floor and some ceiling into the frame. Floor and ceiling together give a viewer scale. A frame of wall and benchtop with neither gives them nothing to measure against, which is why so many kitchen clips look like they could be any size at all.

Shoot along the long diagonal of a room rather than straight down the short wall, and leave a doorway, a chair or a bed in frame as a size reference. Hold each static room shot 5 to 8 seconds. Under 3 seconds, a viewer registers that a room exists and nothing more.

Resist the urge to put the ultra wide on a small room to make it look bigger. Buyers who walk in after watching the video notice, and the walkthrough is the part of the listing that is supposed to be the honest one.

## What audio does a listing walkthrough need?

Record a voiceover afterwards in a furnished room, or clip a microphone to your shirt. An empty house is the worst acoustic environment most people will ever record in: hard floors, bare walls, no soft furnishing anywhere, and a long reverb tail that no software removes cleanly.

If you talk to camera during the walk, clip a microphone to the centre of your chest about 20cm below your chin, cable out of shot. If you record the voiceover later, do it in a carpeted room with curtains and a sofa. Either way, switch off the air conditioning, the pool pump and the range hood, and close any window facing a road before the first take.

## How do you get a vertical Reel and a wide YouTube tour from one walkthrough?

Frame the walk so the point of every shot sits inside the centre third, then cut the vertical and the wide version from the same files. The arithmetic is unforgiving: crop a 16:9 recording to a full-height 9:16 vertical and 81/256 of the original width survives, which is 31.6%. Anything you put near the left or right edge of the wide frame is simply not in the Reel.

The two cuts want different material, so shoot both in each room: one static hold and one walking pass. The wide YouTube tour is built from the static holds and runs longer. The vertical cut is built from the movement, the reveals through doorways and the one feature the property is actually sold on.

The other option is capturing both aspect ratios in the same take so the vertical is cut from the full sensor frame rather than from the finished wide file, which is the problem [ContentCam](https://contentcam.app/) was built for. Either way, the framing discipline is the same: centre third, nothing important at the edges.

## What else do you need to film besides the walkthrough?

Seven shots, filmed after the walk while you are still on site:

- The street approach, 6 to 8 seconds, walking towards the front door.
- The street number or the front door hardware, held static.
- The one feature the property is sold on, held longer than anything else in the video.
- A kitchen wide and a kitchen detail, such as the tapware or the benchtop edge.
- The outdoor space, filmed low enough to show the ground surface.
- The reverse angle: standing inside the best room, looking out of its window.
- A slow pan across the main living space with nothing happening in it, for the end of the edit.

Check storage before you leave the office. 4K at 30fps on a 50 Mbps setting writes 6.25 MB a second, 375 MB a minute, so 20 minutes of walkthrough plus retakes is about 7.5 GB. Clear 15 GB and you will not be deleting holiday photos in someone else's driveway.

## Common questions

**Should a property walkthrough be filmed vertical or horizontal?** Both, from the same visit. YouTube, the agency website and the portal listing want 16:9, while Instagram Reels, TikTok and YouTube Shorts want 9:16. Cropping one from the other keeps 31.6% of the width, so frame for both from the start.

**How long should a listing video be?** Keep the wide tour under about two minutes and the vertical cut between 20 and 40 seconds. A long walkthrough is not more informative, it is the same information at a slower rate.

**Do you need a gimbal to film a property walkthrough?** Not for flat floors. Both hands, elbows in and a slow heel-to-toe walk handle a single level. Stairs are the exception, because there is no body technique that removes the vertical bounce of climbing, so a gimbal earns its place in a two-storey property.

**Should anything be removed before filming?** Clear people and pets out of the house, and put away family photographs, mail, prescriptions, calendars and anything with a name or a street number on it. Those details are legible on a 4K frame, and a listing video is a public document.

**Try ContentCam free.** Records vertical and horizontal at the same time, on iPhone and Android.

★ Rated 4.8 by 580+ creators on the [App Store](https://apps.apple.com/us/app/contentcam-dual-camera-video/id6765881795) and [Google Play](https://play.google.com/store/apps/details?id=app.contentcam.android). [](https://apps.apple.com/us/app/contentcam-dual-camera-video/id6765881795?pt=128838819&ct=b-film-property-listing-walkthrough&mt=8) [](https://play.google.com/store/apps/details?id=app.contentcam.android&referrer=utm_source%3Dblog%26utm_campaign%3Dfilm-property-listing-walkthrough)

Related: [how to hold your phone steady while filming](https://contentcam.app/blog/hold-phone-steady-while-filming/) · [filming b-roll that works vertical and wide](https://contentcam.app/blog/film-b-roll-vertical-and-wide/) · [filming outdoors in wind, backlight and bright sun](https://contentcam.app/blog/film-outdoors-wind-backlight-sun/)
