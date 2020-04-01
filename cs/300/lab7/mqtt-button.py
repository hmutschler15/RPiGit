# CS300 MQTT Lab
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import time
# Constants
BROKER = 'mqtt.eclipse.org' # Set the MQTT broker (change if needed)
PORT = 1883
QOS = 0
BUTTON1 = 12
BUTTON2 = 16
MESSAGE1 = '1'
MESSAGE2 = '2'

# Setup GPIO mode
GPIO.setmode(GPIO.BCM)

# Use GPIO 12 & 16 as button inputs
GPIO.setup(BUTTON1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Setup MQTT client and callbacks
client = mqtt.Client()
client.connect(BROKER, PORT, 60)

# Callback function when buttons are pressed
def button_callback(channel):
    global client
    if channel == 12:
        (result, num) = client.publish('hlm25/button', MESSAGE1, qos=QOS)
        if result != 0:
            print('PUBLISH returned error:', result)
    else:
        (result, num) = client.publish('hlm25/button', MESSAGE2, qos=QOS)
        if result != 0:
            print('PUBLISH returned error:', result)

# Detect a falling edge on input pin
GPIO.add_event_detect(BUTTON1, GPIO.FALLING, callback=button_callback, bouncetime=500)
GPIO.add_event_detect(BUTTON2, GPIO.FALLING, callback=button_callback, bouncetime=500)

client.loop_start()
while True:
    time.sleep(10)

print("Done")
client.disconnect()
GPIO.cleanup() # clean up GPIO