Title: How to turn $$ into a circle in a video
Tags: tech, video, gps
Slug: video-tech
Authors: dane foster
Summary: I have no life.
Date: 2016-10-19 19:59

Thing's I use to make the videos with lap times and whatnot:

  * [TomTom Bandit Action Camera](https://www.tomtom.com/en_us/action-camera/action-camera/)

  * [Race Render 3](http://racerender.com/RR3/Features.html)

  * GoPro3 HD Black

  * Panasonic TG-Tracker

  * Macbook pro

  * Mac mini

  * lots of hard drive space (13GB per hour per camera of 1080P)

  * ffmpeg.. lots of ffmpeg.

Step 1, Recording
===
The TomTom has GPS builtin, and it's amazingly accurate. Enough that I don't need to fiddle with the data. The TG-Tracker has thus far been not great.. so still experimenting.

Place cameras somewhere stable on bike and point where you want to see.

Step 2, Begin the process
===

This starts with importing the video from the TomTom into Bandit Studio, the desktop app. The only reason we do this is Bandit Studio can extract the GPS data (as GPX) from the video. So, import, extract, delete from Bandit Studio and quit.

Step 3, Process more
===

This step kinda depends on what you want to produce, for a normal day I've got individual files per race. Easy. For the enduro I had 4 separate files I wanted to concatenate. ffmpeg to the rescue;

```
for i in `ls *.MP4`; do echo "file '$i'" >> list.txt
ffmpeg -f concat -i list.txt -c copy output.mp4
```

The GPX files are in the same boat, but just use vi and figure it out.

Step 4, Finally, into some useful software
===

Fire up RaceRender, start a new project, I use the Data Overlay - Simple.

![step 2393]({photo}video-gps/rr_step_1.png)

Select your combined video, and combined GPX file. Fuck around a lot with the Side by Side tool to get the GPS lock time sync'd with the video feed.


![step 2394]({photo}video-gps/rr_step_2.png)

I've only done single video feeds thus far, so don't need to get into the timeline. I've got a set of data object presets for the race already set out, the track map, speed, and lap board (10 laps, with fastest highlighted).

![step 2395]({photo}video-gps/rr_step_3.jpg)

Once the GPS + video is sync'd, and the object set applied, you're pretty much ready.

Next race we should have some multi-angle, so will be adding some cuts and/or picture-in-picture.

Step 5, Wait.
===

Render it all out, this may take some time. A 1h11m video took ~5hours on a quad-core i7.

Step X, Upload to Youtube
===

Youtube is dumb, and sometimes only takes 15min video, so if it's longer split the output like so:

```
ffmpeg -i Enduro.mp4 -acodec copy -vcodec copy -ss 0 -t 00:12:00 OUTFILE-1.mp4
ffmpeg -i Enduro.mp4 -acodec copy -vcodec copy -ss 00:12:00 -t 00:12:00
OUT-2.mp4
ffmpeg -i Enduro.mp4 -acodec copy -vcodec copy -ss 00:24:00 -t 00:12:00
OUT-3.mp4
ffmpeg -i Enduro.mp4 -acodec copy -vcodec copy -ss 00:36:00 -t 00:12:00
OUT-4.mp4
ffmpeg -i Enduro.mp4 -acodec copy -vcodec copy -ss 00:48:00 -t 00:13:42
OUT-5.mp4
```

Upload with your favourite tool and profit !
