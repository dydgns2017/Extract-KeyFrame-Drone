# Extract-KeyFrame-Drone
Extract-KeyFrame-Drone : just test repository for KFS Project

## What is KeyFrame?

Keyframes are the important frames which contain information of a start/end point of an action. 

so this code purpose extraction important frame of video ( format : mp4, mov )

and then you should be know this code not working your video data so i recommend modify this code if try execution

## ffmpeg command

```bash
ffmpeg -i filename -vf select="eq(pict_type\,PICT_TYPE_I)" -vsync vfr frame1%03d.png
```

## Reference

- [Key Frame Extraction From Video](https://medium.com/@myworldsharma.jay/key-frame-extraction-from-video-9445564eb8ed)
- [use with ffmpeg(1)](https://superuser.com/questions/669716/how-to-extract-all-key-frames-from-a-video-clip)
- [delete jiggling](https://mpetroff.net/2016/11/stabilizing-360-video-with-hugin/)
- [use with ffmpeg(2)](https://developpaper.com/arbitrary-extraction-of-video-frames-by-ffmpeg-python/)
- [camera stablisation with ffmpeg](http://blog.gregzaal.com/2014/05/30/camera-stabilisation-with-ffmpeg/)
- [reference code](https://blog.programster.org/ffmpeg-extract-images`)
- https://filme.imyfone.com/video-editing-tips/splitting-video-with-ffmpeg/
