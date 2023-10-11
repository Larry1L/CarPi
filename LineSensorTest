import RPi.GPIO as GPIO
import time

# Configure GPIO pins
GPIO.setmode(GPIO.BCM)
sensor_pin = 2  # Example GPIO pin, adjust to your setup

# Set up the sensor pin as an input
GPIO.setup(sensor_pin, GPIO.IN)

try:
    while True:
        if GPIO.input(sensor_pin) == GPIO.LOW:
            print("Line detected")
        else:
            print("No line detected")
        time.sleep(0.1)  # Adjust the sleep time as needed

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
