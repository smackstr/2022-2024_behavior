#import necessary packages
from picamera import PiCamera, Color
from time import sleep
import datetime as dt
import os
import socket

#specify manually-assigned parts of naming convention for output video files
genusspecies = "RS" #replace with genus species code
clutch = "_A" #replace letter with appropriate letter for clutch
tank = "_L014" #replace with appropriate three-digit number for tank
test = "_Star" #replace word with Star for bucket startle, Swim for swimming performance, Jump for jumping performance
individual = "_01" #replace with two-digit number of individual from the same tank

# specify automatically-generated parts of naming convention and filepath
timestamp = dt.datetime.now().strftime('_%Y-%m-%d_%H.%M.%S_')
piname = str(socket.gethostname()) #adds name of specific raspberry pi since we are filming multiple arenas simultaneously
filename = "/home/pi/mnt/usb/{}".format(genusspecies + clutch + tank + timestamp + piname + test + individual) #sets filepath to usb drive

#initialize camera & determine settings
camera = PiCamera()
#camera.rotation = 90 #can rotate by 0, 90, 180, or 270
camera.resolution = (1920, 1080) #options are (1920,1080), (1280, 720), (640,480)
camera.framerate = 30
video_duration = 3600 #sets recording duration to X seconds

#preview the camera view and allow camera to warm up for number of seconds in sleep()
#alpha() makes preview slightly see through and can be set between 0 and 255
camera.start_preview(alpha=255)
sleep(2) #allows camera to warm up

#start recording and add timestamp
camera.annotate_background = Color('black')
start = dt.datetime.now()
camera.start_recording(filename+'.h264') #begins recording, saves to specified path with timestamp as the filename format
while (dt.datetime.now() - start).seconds < video_duration: #records video for amount set in video_duration
    camera.annotate_text = dt.datetime.now().strftime('%m-%d-%Y %H:%M:%S')
    camera.annotate_frame_num = True
    #camera.wait_recording(0.2)

#stop recording
camera.stop_recording()
camera.stop_preview()
camera.close() #releases camera resources