#!/bin/bash
# extract frames from multiple videos
# google search key word : How to extract frames from all videos in a folder using ffmpeg
# code reference : https://stackoverflow.com/questions/13408493/an-and-operator-for-an-if-statement-in-bash

# this code must be modify if added usable extension
if [ "$1" == '' ] || [ "$1" == 'MOV' ] || [ "$1" == 'MP4' ]; then
    echo "Usage: $0 <FILE-EXTENSIONS, MP4|MOV|ETC>";
    exit;
fi

fileext=$1;
resultfolder="frames";
[ ! -d "$resultfolder" ] && mkdir "$resultfolder";

# loop for frame extraction from videos
for file in ./*."$fileext"; do
    result = "$resultfolder/${file}"
    mkdir -p "$result"
    ffmpeg -i "$file" -q:v 2 -vf select="eq(pict_type\,PICT_TYPE_I)" -vsync 0 "$result/frame%03d.jpg";
done
