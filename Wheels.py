import RPi.GPIO as GPIO
import time

# Set the GPIO pin number (pin 8)
motor_pin = 8

# Configure the GPIO mode
GPIO.setmode(GPIO.BCM)

# Set up the motor pin as an output
GPIO.setup(motor_pin, GPIO.OUT)

try:
    GPIO.output(motor_pin, GPIO.HIGH)
    time.sleep(1)
    print("test")
    GPIO.output(motor_pin, GPIO.LOW)

except KeyboardInterrupt:
    pass

finally:
    # Clean up GPIO settings
    GPIO.cleanup()
