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
    try:
    while True:  # Loop indefinitely
        GPIO.output(motorR_pin, GPIO.HIGH)  # Start the motor
        time.sleep(0.1)  # Run the motor for 1 second
        print("Turning Right")

def TurnLeft():
    try:
    while True:  # Loop indefinitely
        GPIO.output(motorL_pin, GPIO.HIGH)  # Start the motor
        time.sleep(0.1)  # Run the motor for 1 second
        print("Turning Left")
def BrakeRight():
    try:
    while True:  # Loop indefinitely
        GPIO.output(motorR_pin, GPIO.LOW)  # Start the motor
        time.sleep(0.1)  # Run the motor for 1 second
        print("Turning Right")

def BrakeLeft():
    try:
    while True:  # Loop indefinitely
        GPIO.output(motorL_pin, GPIO.LOW)  # Start the motor
        time.sleep(0.1)  # Run the motor for 1 second
        print("Turning Left")
def DriveForward():
   try:
       while True: # Loop indefinitely
           GPIO.output(motorL_pin, GPIO.HIGH) # Starting both motors 
           GPIO.output(motorR_pin, GPIO.HIGH)
           print("Driving Forward")
try:
    while True:
    DriveForward():

except KeyboardInterrupt:
    pass

finally:
    # Clean up GPIO settings
    GPIO.cleanup()
