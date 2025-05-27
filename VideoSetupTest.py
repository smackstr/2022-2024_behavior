from picamera import PiCamera
from time import sleep
camera = PiCamera()
camera.start_preview()
sleep(60) #adjust the number to match the number of seconds you want the preview to show for
camera.stop_preview()
