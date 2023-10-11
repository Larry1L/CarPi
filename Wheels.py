import RPi.GPIO as GPIO
import time

# Set the GPIO pin number (pin 8)
motor_pin = 8

# Configure the GPIO mode
GPIO.setmode(GPIO.BCM)

# Set up the motor pin as an output
GPIO.setup(motor_pin, GPIO.OUT)

try:
    while True:  # Loop indefinitely
        GPIO.output(motor_pin, GPIO.HIGH)  # Start the motor
        time.sleep(1)  # Run the motor for 1 second
        print("test")
        GPIO.output(motor_pin, GPIO.LOW)  # Stop the motor
        time.sleep(1)  # Wait for 1 second

except KeyboardInterrupt:
    pass

finally:
    # Clean up GPIO settings
    GPIO.cleanup()
