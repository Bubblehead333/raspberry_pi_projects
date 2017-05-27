
from picamera import PiCamera
import time
import datetime as dt
from time import sleep

# Security Camera v1.0
#
# If calculations are correct this program can collect 24 hours worth 
# of footage with a file size of 2GB.
# Has not tested if can read number plates and at what distance.

camera = PiCamera()

camera.resolution = (600, 480)
camera.brightness = 50
camera.framerate = 5

camera.start_preview()
camera.annotate_text = dt.datetime.now().strftime("%d/%m/%Y - %H:%M.%S")
camera.start_recording('/home/pi/Videos/testresvideo.h264')

start = dt.datetime.now()
while (dt.datetime.now() - start):
	camera.annotate_text = dt.datetime.now().strftime("%d/%m/%Y - %H:%M.%S")
	camera.wait_recording(0.2)
camera.stop_recording() 
camera.stop_preview()

# Camera works, but restarts every 10 seconds to update time field
#while(True):
#	camera.start_preview()
#	current_time = time.strftime("%H:%M:%S")
#	current_date = time.strftime("%d/%m/%y")
#	camera_time_text = ("Date: " + current_date + " Time " + current_time)
#	camera.annotate_text = camera_time_text
#	sleep(10)


#camera.start_preview()
#camera.start_recording('/home/pi/Videos/testresvideo.h264')
#sleep(5)
#camera.stop_recording()
#camera.stop_preview()
