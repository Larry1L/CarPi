import RPi.GPIO as GPIO
import time

# Set the GPIO pin numbers (pin 8 & 14)
motorR_pin = 8
motorL_pin = 14

# Configure the GPIO mode
GPIO.setmode(GPIO.BCM)

# Set up the motor pins as an output
GPIO.setup(motorR_pin, GPIO.OUT)
GPIO.setup(motorL_pin, GPIO.OUT)

def TurnRight():
    while True:  # Loop indefinitely
        GPIO.output(motorR_pin, GPIO.HIGH)  # Start the motor
        time.sleep(0.1)  # Run the motor for 0.1 seconds
        print("Turning Right")
        GPIO.output(motorR_pin, GPIO.LOW)  # Stop the motor
        time.sleep(0.1)  # Wait for 0.1 seconds

def TurnLeft():
    while True:  # Loop indefinitely
        GPIO.output(motorL_pin, GPIO.HIGH)  # Start the motor
        time.sleep(0.1)  # Run the motor for 0.1 seconds
        print("Turning Left")
        GPIO.output(motorR_pin, GPIO.100)  # Start the motor
        time.sleep(0.1)  # Run the motor for 0.1 seconds
        print("Turning Left")


def DriveForward():
    while True:  # Loop indefinitely
        GPIO.output(motorL_pin, GPIO.HIGH)  # Start the left motor
        GPIO.output(motorR_pin, GPIO.HIGH)  # Start the right motor
        time.sleep(0.1)  # Run both motors for 0.1 seconds
        print("Driving Forward")

try:
    TurnLeft()

except KeyboardInterrupt:
    pass

finally:
    # Clean up GPIO settings
    GPIO.cleanup()
