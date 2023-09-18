# Test shell code for release an image.

/opt/local/bin/ffmpeg -f avfoundation -video_size 1280x720 -framerate 30 -i "0" -vframes 1 cam_img.png

