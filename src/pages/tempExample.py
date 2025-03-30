import RPi.GPIO as GPIO
import time

# Pin configuration
LIGHT_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(LIGHT_PIN, GPIO.OUT)

# Turn on the light
GPIO.output(LIGHT_PIN, GPIO.HIGH)
time.sleep(5)

# Turn off the light
GPIO.output(LIGHT_PIN, GPIO.LOW)
GPIO.cleanup()