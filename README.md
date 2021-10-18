# Extract-KeyFrame-Drone
Extract-KeyFrame-Drone : just test repository for KFS Project

## What is KeyFrame?

Keyframes are the important frames which contain information of a start/end point of an action. 

so this code purpose extraction important frame of video ( format : mp4, mov )

and then you should be know this code not working your video data so i recommend modify this code if try execution

## Setting Environment

```python
conda create -n ExtractKeyFrame python=3.8
conda activate ExtractKeyFrame
conda install -c conda-forge opencv -y
conda install matplotlib numpy -y
```

## How to use it


```python
# python KeyFrameExtract.py filename

## sample
python KeyFrameExtract.py sample.mp4
```

## ffmpeg command

```bash
ffmpeg -i filename -q:v 2 -vf select="eq(pict_type\,PICT_TYPE_I)" -vsync 0 frame1%03d.jpg
```

## Reference

- (Key Frame Extraction From Video),https://medium.com/@myworldsharma.jay/key-frame-extraction-from-video-9445564eb8ed
- use with ffmpeg (https://superuser.com/questions/669716/how-to-extract-all-key-frames-from-a-video-clip)
