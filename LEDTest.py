import RPi.GPIO as GPIO
import time
# Set the GPIO pin number (pin 8)
power_pin = 8

# Configure the GPIO mode
GPIO.setmode(GPIO.BCM)

# Set up the power pin as an output
GPIO.setup(power_pin, GPIO.OUT)

# Turn on power to the pin
GPIO.output(power_pin, GPIO.HIGH)

# Wait for some time (you can adjust the time as needed)
time.sleep(5)  # Power on for 5 seconds

# Turn off power to the pin
GPIO.output(power_pin, GPIO.LOW)

# Clean up GPIO settings
GPIO.cleanup()
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
        time.sleep(5)  # Power on for 5 seconds

        GPIO.output(power_pin, GPIO.LOW)  # Turn off power
        print("Null")
        time.sleep(5)  # Wait for 5 seconds

except KeyboardInterrupt:
    pass

finally:
    # Clean up GPIO settings
    GPIO.cleanup()
