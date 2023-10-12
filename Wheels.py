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

# Define motor control functions (you can modify these as needed)
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
