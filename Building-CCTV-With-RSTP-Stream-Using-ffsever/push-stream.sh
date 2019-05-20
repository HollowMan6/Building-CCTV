#!/bin/bash 
echo "正在推流..."
echo "pushing the stream..."
ffmpeg -f v4l2 -i /dev/video0 -s 640x480 -r 24 -vcodec libx264 -an http://localhost:8866/feed1.ffm