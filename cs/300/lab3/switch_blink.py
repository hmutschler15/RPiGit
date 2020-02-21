# Name: Hamilton Mutschler
# For:  Lab 3 in CS 300 at Calvin University
# Date: February 21, 2020
import RPi.GPIO as GPIO

# set up GPIO pins to BCM
GPIO.setmode(GPIO.BCM)
# set BCM pin 12 to an input
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# set BCM pin 16 to an output
GPIO.setup(16, GPIO.OUT)
# initialize LED to off
GPIO.output(16, 0)
LEDstate = 0
SWstate = 1

# function to control the status of the LED
def LED_control():
    global LEDstate
    # change the state of the LED
    LEDstate = not LEDstate
    GPIO.output(16, LEDstate)

# main program loop
while(True):
    # switch not pressed and was pressed before
    if GPIO.input(12)==False and SWstate==1:
        # toggle LED
        LED_control()
        # change state of switch
        SWstate = 0
    # switch pressed and was not pressed before
    if GPIO.input(12)==True and SWstate==0:
        # change state of switch
        SWstate = 1