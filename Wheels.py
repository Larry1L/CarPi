import RPi.GPIO as GPIO
import time

# Your setup code here

input("Press Enter to start...")

# Define GPIO pin numbers for your sensors
sensorL_pin = 17
sensorR_pin = 18

# Configure GPIO pins for input
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensorL_pin, GPIO.IN)
GPIO.setup(sensorR_pin, GPIO.IN)

try:
    FullSpeed(0)
    while True:
        if GPIO.input(sensorL_pin) == GPIO.LOW and GPIO.input(sensorR_pin) == GPIO.LOW:
            print("Both Sensors - Line detected")
            FullSpeed()
        elif GPIO.input(sensorL_pin) == GPIO.LOW:
            print("Left Sensor - Line detected")
            TurnRight()
        elif GPIO.input(sensorR_pin) == GPIO.LOW:
            print("Right Sensor - Line detected")
            TurnLeft()
except KeyboardInterrupt:
    pass
finally:
    motorR_pwm.stop()
    motorL_pwm.stop()
    GPIO.cleanup()
