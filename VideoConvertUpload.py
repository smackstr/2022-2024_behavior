#cycle through folder of videos to convert .h264 to .mp4 and upload to google drive

import os
from picamera import PiCamera, Color
from time import sleep
import datetime as dt
import os
import socket

directory = "/home/pi/mnt/usb/"
conversion = 30 #set this to account for speed of camera, which ensures that the .mp4 length is the same as the recorded length

# convert video to MP4 on Raspberry Pi
# should remove files from Raspberry Pi after checking they've copied correctly, since the script will otherwise duplicate .h264 -> .mp4 for files
for filename in os.listdir(directory): 
    if filename.endswith(".h264"):
        os.system("MP4Box -quiet -add {videoname}.h264 -fps {conversion} {newvideoname}.mp4".format(conversion = conversion, videoname = os.path.join(os.path.splitext(os.path.join(directory + '/' + filename))[0]), newvideoname = os.path.join(os.path.splitext(os.path.join(directory + '/' + filename))[0])))
        continue #forces to execute to next iteration of loop
    else:
        continue #forces to execute to next iteration of loop

#copy any new videos to google drive
os.system("rclone copy --update --verbose --include *.h264 {directory} gdrive:Research/USU/RaspberryPi/RawVideos".format(directory=directory))
os.system("rclone copy --update --verbose --include *.mp4 {directory} gdrive:Research/USU/RaspberryPi/MP4Videos".format(directory=directory))
