# mqtt-intersection-control.py
# Program to control operation operation of a traffic light
#         in an autonomous intersection via a button and MQTT
# Hamilton Mutschler & Drew Smits
# Final Project for CS 300 at Calvin University
# April 28, 2020

import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import time

# Constants
BROKER = 'iot.cs.calvin.edu'
USERNAME = "cs300" # Put broker username here
PASSWORD = "safeIoT" # Put broker password here
PORT = 8883
QOS = 0
TOPIC = 'hlm25/finalproject'
CERTS = '/etc/ssl/certs/ca-certificates.crt'
BUTTON = 16
MESSAGE = '1'

# Setup GPIO mode
GPIO.setmode(GPIO.BCM)
# Use GPIO 16 as button input
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# callback function when button is pressed
def button_callback(channel):
    global client
    if channel == 16:
        (result, num) = client.publish(TOPIC, MESSAGE, qos=QOS)
        if result != 0:
            print('PUBLISH returned error:', result)
        else:
            print("published intersection change msg")
    else:
        print("WARNING: unknown GPIO input detected")

# callback function when connecting to the MQTT broker
def on_connect(client, userdata, flags, rc):
    if rc==0:
        print('connected to',BROKER)
    else:
        print('connection to',BROKER,'failed\r\n return code=',rc)
        os._exit(1)

# Detect a falling edge on input pin
GPIO.add_event_detect(BUTTON, GPIO.FALLING, callback=button_callback, bouncetime=500)

# setup MQTT client and callback
client = mqtt.Client()
client.on_connect = on_connect
# sonnect to MQTT broker
client.username_pw_set(USERNAME, password=PASSWORD)
client.tls_set(CERTS)
client.connect(BROKER, PORT, 60)
client.loop_start()

# continuously wait for GPIO input
try:
    while True:
        continue
except KeyboardInterrupt:
    print("program terminated")
    client.disconnect()
    GPIO.cleanup() # clean up GPIO