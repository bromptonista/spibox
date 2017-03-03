import time
import datetime
import subprocess
import os
import RPi.GPIO as GPIO

def get_file_name():
    return datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S")

PIR = 4
def photo():
    for i in range(1,2):
        capturename = get_file_name()
        print('Motion detected! Taking snapshot')
        # Changed settings to 5MP - original was 640x480 pictures, see
        # https://www.raspberrypi.org/documentation/usage/camera/raspicam/raspistill.md
        # for documentation of raspberry pi camera use for stills
        cmd="raspistill -w 2592 -h 1944 -n -t 10 -q 10 -e jpg -th none -o /home/pi/spibox/capture/" + capturename+"_%d.jpg" % (i)
        camerapid = subprocess.call(cmd,shell=True)
        # taking video clip at 1080p30, 15Mbit/s, 25sec
        cmd="raspivid -w 1920 -h 1080 -fps 30 -b 15000000 -n -t 25000 -o /home/pi/spibox/capture/" + capturename+"_%d.mp4" % (i)
        camerapid = subprocess.call(cmd,shell=True)


GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR, GPIO.IN, GPIO.PUD_DOWN)

try:
    print "Turning on motion sensor..."

    # Loop until PIR indicates nothing is happening
    while GPIO.input(PIR)==1:
        Current_State  = 0

    print "  Sensor ready"

    while True:
        print('Waiting for movement')
        GPIO.wait_for_edge(PIR,GPIO.RISING)
        photo()

except KeyboardInterrupt:
  print "  Bye for now"
  # Reset GPIO
  GPIO.cleanup()
