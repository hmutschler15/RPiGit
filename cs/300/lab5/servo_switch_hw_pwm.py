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
pi.set_glitch_filter(SWITCH, 300)

# set initial PWM and ANGLE values
MIN_PWM = 1000
ZERO_PWM = 1500
MAX_PWM = 2000
MIN_ANGLE = -90
MAX_ANGLE = 90

# set initial state to wait for button
STATE = "WAIT_FOR_BUTTON"

# move the servo motor to the passed angle
def move_to_angle(degrees):
    PWM = degrees * (MAX_PWM - MIN_PWM) / (MAX_ANGLE - MIN_ANGLE) + ZERO_PWM
    # set servo to random pwm value
    pi.set_servo_pulsewidth(MOTOR, PWM)

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
            RANDOM_ANGLE = randint(MIN_ANGLE, MAX_ANGLE)
            # move the servo motor to generated angle
            move_to_angle(RANDOM_ANGLE)
            print("moved to angle "+str(RANDOM_ANGLE))
            # reset state to waiting for button
            STATE = "WAIT_FOR_BUTTON"
except KeyboardInterrupt:
    pi.stop()
    print("program terminated")