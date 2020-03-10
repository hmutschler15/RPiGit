# Name:  Hamilton Mutschler
#        Daniel Ackuaku
# For:   Lab 5 in CS 300 at Calvin University
# Date:  March 13, 2020

import time
import pigpio
from random import randint

# Constants
MOTOR = 18  # Connect servomotor to BCM 18
STATE = 0
pi = pigpio.pi()

if not pi.connected:
    exit(0)

pi.set_servo_pulsewidth(MOTOR, 0)
try:
    while True:
        # if state = 0, continue to wait for button press
        if STATE == 0:
            continue
        # if state = 1, generate random movement of servo
        else:
            RANDOM_PWM = random(0,2)
            if RANDOM_PWM == 0:
                print('setting angle = -90 degrees')
                pi.set_servo_pulsewidth(MOTOR, 1000)
            elif RANDOM_PWM == 1:
                print('setting angle = 0 degrees')
                pi.set_servo_pulsewidth(MOTOR, 1500)
            else:
                print('setting angle = 90 degrees')
                pi.set_servo_pulsewidth(MOTOR, 2000)
except KeyboardInterrupt:
    pi.stop()