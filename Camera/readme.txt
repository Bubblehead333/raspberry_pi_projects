# Security Camera v 1.0
#
#

# Run on boot
Comment out the command in 

sudo nano .bashrc

This will boot Raspberry Pi as normal, but run the camera
when RPi has finished booting.

# Saved Video
The saved video will be stored under/home/pi/Videos/
To play video using command line:

omxplayer home/pi/Videos/testresvideo.h264

# Testing
- Whether it can read a reg plate
- How long it can record for
- How long the battery lasts for
- Whether solar power is an option

# To Implement
- Needs to delete oldest footage to make way for new footage
  4GB Buffer?
- Stop execution command