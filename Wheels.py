import RPi.GPIO as GPIO
import time
import keyboard

motorR_pin = 8
motorL_pin = 14
DirR_pin = 27
DirL_pin = 22
sensorL_pin = 4
sensorR_pin = 17

GPIO.setmode(GPIO.BCM)

GPIO.setup(motorR_pin, GPIO.OUT)
GPIO.setup(motorL_pin, GPIO.OUT)
GPIO.setup(DirR_pin, GPIO.OUT)
GPIO.setup(DirL_pin, GPIO.OUT)
GPIO.setup(sensorL_pin, GPIO.IN)
GPIO.setup(sensorR_pin, GPIO.IN)

motorR_pwm = GPIO.PWM(motorR_pin, 100)
motorL_pwm = GPIO.PWM(motorL_pin, 100)

motorR_pwm.start(0)
motorL_pwm.start(0)

def TurnRight(speed=90):
    GPIO.output(DirL_pin, GPIO.HIGH)
    GPIO.output(DirR_pin, GPIO.LOW)
    motorR_pwm.ChangeDutyCycle(33)
    motorL_pwm.ChangeDutyCycle(speed)

def TurnLeft(speed=90):
    GPIO.output(DirR_pin, GPIO.HIGH)
    GPIO.output(DirL_pin, GPIO.LOW)
    motorR_pwm.ChangeDutyCycle(speed)
    motorL_pwm.ChangeDutyCycle(33)

def FullSpeed(speed=100):
    GPIO.output(DirL_pin, GPIO.LOW)
    GPIO.output(DirR_pin, GPIO.LOW)
    motorR_pwm.ChangeDutyCycle(speed)
    motorL_pwm.ChangeDutyCycle(speed)

def StopDriving():
    motorR_pwm.ChangeDutyCycle(0)
    motorL_pwm.ChangeDutyCycle(0)

input("Press Enter to start...")

try:
    FullSpeed(90)

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

        # Check for key presses
        if keyboard.is_pressed('w'):
            FullSpeed()
        elif keyboard.is_pressed('a'):
            TurnLeft()
        elif keyboard.is_pressed('d'):
            TurnRight()
        elif keyboard.is_pressed('s'):
            StopDriving()

except KeyboardInterrupt:
    pass

finally:
    motorR_pwm.stop()
    motorL_pwm.stop()
    GPIO.cleanup()
