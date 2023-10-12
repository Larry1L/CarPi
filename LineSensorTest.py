import RPi.GPIO as GPIO
import keyboard
import time

# Define GPIO pin numbers for your motors
motorL_pin1 = 17  # Replace with your actual GPIO pin
motorL_pin2 = 18  # Replace with your actual GPIO pin
motorR_pin1 = 19  # Replace with your actual GPIO pin
motorR_pin2 = 20  # Replace with your actual GPIO pin

# Get the speed from the user at the start
speed = float(input("Enter the speed (0.0 to 1.0): "))

# Verify that the speed is within a valid range (0.0 to 1.0)
if not (0.0 <= speed <= 1.0):
    print("Invalid speed value. Please enter a value between 0.0 and 1.0.")
    exit(1)

# Configure GPIO pins for motor control
GPIO.setmode(GPIO.BCM)
GPIO.setup(motorL_pin1, GPIO.OUT)
GPIO.setup(motorL_pin2, GPIO.OUT)
GPIO.setup(motorR_pin1, GPIO.OUT)
GPIO.setup(motorR_pin2, GPIO.OUT)

# Calculate the speed values for FullSpeed based on user input
motor_speed = int(speed * 100)  # Convert the speed to a percentage

# Define motor control functions
def FullSpeed():
    GPIO.output(motorL_pin1, GPIO.HIGH)
    GPIO.output(motorL_pin2, GPIO.LOW)
    GPIO.output(motorR_pin1, GPIO.HIGH)
    GPIO.output(motorR_pin2, GPIO.LOW)

def TurnLeft():
    GPIO.output(motorL_pin1, GPIO.LOW)
    GPIO.output(motorL_pin2, GPIO.HIGH)
    GPIO.output(motorR_pin1, GPIO.HIGH)
    GPIO.output(motorR_pin2, GPIO.LOW)

def TurnRight():
    GPIO.output(motorL_pin1, GPIO.HIGH)
    GPIO.output(motorL_pin2, GPIO.LOW)
    GPIO.output(motorR_pin1, GPIO.LOW)
    GPIO.output(motorR_pin2, GPIO.HIGH)

def StopDriving():
    GPIO.output(motorL_pin1, GPIO.LOW)
    GPIO.output(motorL_pin2, GPIO.LOW)
    GPIO.output(motorR_pin1, GPIO.LOW)
    GPIO.output(motorR_pin2, GPIO.LOW)

try:
    while True:
        if keyboard.is_pressed('w'):
            FullSpeed()
        elif keyboard.is_pressed('a'):
            TurnLeft()
        elif keyboard.is_pressed('d'):
            TurnRight()
        else:
            StopDriving()
        time.sleep(0.1)
except KeyboardInterrupt:
    pass
finally:
    StopDriving()
    GPIO.cleanup()
