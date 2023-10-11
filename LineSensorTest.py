import RPi.GPIO as GPIO
import time

# Configure GPIO pins
GPIO.setmode(GPIO.BCM)
sensorL_pin = 4  # Example GPIO pin, adjust to your setup
sensorR_pin = 17 # Example GPIO pin, adjust to your setup

# Set up the sensor pin as an input
GPIO.setup(sensor_pin, GPIO.IN)

try:
    if GPIO.input(sensorL_pin) == GPIO.LOW:
        print("Left Sensor is detecting a line at startup")

    if GPIO.input(sensorR_pin) == GPIO.LOW:
        print("Left Sensor is detecting a line at startup")

    while True:
        if GPIO.input(sensorL_pin) == GPIO.LOW:
            print("Left Sensor - Line detected")

        if GPIO.input(sensorR_pin) == GPIO.LOW:
            print("Left Sensor - Line detected")

        time.sleep(1)  # Adjust the sleep time as needed

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
