import RPi.GPIO as GPIO
import time
import os
import sys
import argparse
import rpi_backlight as bl

GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
timeout = 0
counter = 0
"""
brightness value of screen can be between 11 and 255
"""

def motionSensor(channel):
    if GPIO.input(21):
        global counter
        counter += 1
        global timeout
        timeout = 0
        print ("motion detected {}".format(counter))
        try:
            bl.set_brightness(255)    
        except (OSError, IOError) as err:
            if err.errno == 13:
                print ("permission denied {}".format(err.errno))
             
GPIO.add_event_detect(21,GPIO.BOTH, callback=motionSensor, bouncetime=300)

try:
    while True:
        timeout += 1
        print ("timeout {}".format(timeout))
        time.sleep(1)
        try:
            if timeout > 60:
                print ("Motion not detected. Wave your hand in front of sensor")
                """bl.set_brightness(11)"""
        except (OSError, IOError) as err:
            if err.errno == 13:
                print ("permission denied")   

finally:
    GPIO.cleanup()
    print ("Clean up")
