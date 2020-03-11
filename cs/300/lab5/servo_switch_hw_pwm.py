# Name:  Hamilton Mutschler
#        Daniel Ackuaku
# For:   Lab 5 in CS 300 at Calvin University
# Date:  March 13, 2020

import time
import pigpio
from random import randint

# Constants
MOTOR = 18      # Connect servomotor to BCM 18
SWITCH = 12     # Connect switch to BCM 12

pi = pigpio.pi()
# set switch pin to input
pi.set_mode(SWITCH, pigpio.INPUT)
# set internal pulldown on switch input
pi.set_pull_up_down(SWITCH, pigpio.PUD_UP)
# set debouncing value for switch
pi.set_glitch_filter(SWITCH, 200)

# set initial state to wait for button
STATE = "WAIT_FOR_BUTTON"

# callback function to handle behavior on a switch press
def switch_press(gpio, level, tick):
    global STATE
    print("switch pressed")
    STATE = "RANDOM_MOVE"
# set callback for switch input
pi.callback(SWITCH, pigpio.FALLING_EDGE, switch_press)

# main program
if not pi.connected:
    exit(0)
else:
    print("pigpio daemon connected")

# set the servo motor
pi.set_servo_pulsewidth(MOTOR, 0)
try:
    while True:
        # if state = 0, continue to wait for button press
        if STATE == "WAIT_FOR_BUTTON":
            continue
        # if state = 1, generate random movement of servo
        else:
            print("generating random movement")
            RANDOM_PWM = randint(0,2)
            if RANDOM_PWM == 0:
                print('setting angle = -90 degrees')
                pi.set_servo_pulsewidth(MOTOR, 1000)
            elif RANDOM_PWM == 1:
                print('setting angle = 0 degrees')
                pi.set_servo_pulsewidth(MOTOR, 1500)
            else:
                print('setting angle = 90 degrees')
                pi.set_servo_pulsewidth(MOTOR, 2000)
            STATE = "WAIT_FOR_BUTTON"
except KeyboardInterrupt:
    pi.stop()
    print("program terminated")