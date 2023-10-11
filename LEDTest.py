import RPi.GPIO as GPIO
import time

# Set the GPIO pin number (pin 8)
power_pin = 8

# Configure the GPIO mode
GPIO.setmode(GPIO.BCM)

# Set up the power pin as an output
GPIO.setup(power_pin, GPIO.OUT)

try:
    while True:  # Loop indefinitely
        GPIO.output(power_pin, GPIO.HIGH)  # Turn on power
        print("Power")
        time.sleep(1)  # Power on for 1 second

        GPIO.output(power_pin, GPIO.LOW)  # Turn off power
        print("Null")
        time.sleep(1)  # Wait for 1 second

except KeyboardInterrupt:
    pass

finally:
    # Clean up GPIO settings
    GPIO.cleanup()
