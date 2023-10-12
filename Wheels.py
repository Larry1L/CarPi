import RPi.GPIO as GPIO
import keyboard
import time

# Define GPIO pin numbers for your motors
motorL_pin1 = 17  # Replace with your actual GPIO pin
motorL_pin2 = 18  # Replace with your actual GPIO pin
motorR_pin1 = 19  # Replace with your actual GPIO pin
motorR_pin2 = 20  # Replace with your actual GPIO pin

# Configure GPIO pins for motor control
GPIO.setmode(GPIO.BCM)
GPIO.setup(motorL_pin1, GPIO.OUT)
GPIO.setup(motorL_pin2, GPIO.OUT)
GPIO.setup(motorR_pin1, GPIO.OUT)
GPIO.setup(motorR_pin2, GPIO.OUT)

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

# Listen for keyboard input
@listen_to('keydown', ['w', 'a', 's', 'd'])
def on_key(event):
    if event.key == 'w':
        FullSpeed()
    elif event.key == 'a':
        TurnLeft()
    elif event.key == 'd':
        TurnRight()
    elif event.key == 's':
        StopDriving()

try:
    while True:
        time.sleep(0.1)  # Keep the program running
except KeyboardInterrupt:
    pass
finally:
    StopDriving()  # Stop the motors
    GPIO.cleanup()  # Cleanup GPIO pins
