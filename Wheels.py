import RPi.GPIO as GPIO
import time

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
    motorR_pwm.ChangeDutyCycle(33)  # Right motor goes forward
    motorL_pwm.ChangeDutyCycle(speed)

def TurnLeft(speed=90):
    GPIO.output(DirR_pin, GPIO.HIGH)
    GPIO.output(DirL_pin, GPIO.LOW)
    motorR_pwm.ChangeDutyCycle(speed)
    motorL_pwm.ChangeDutyCycle(33)  # Left motor goes forward

def FullSpeed(speed=33):
    GPIO.output(DirL_pin, GPIO.LOW)
    GPIO.output(DirR_pin, GPIO.LOW)
    motorR_pwm.ChangeDutyCycle(speed)
    motorL_pwm.ChangeDutyCycle(speed)

def FullSpeed2():
    FullSpeed(50)  # Full speed for both motors

def StopDriving():
    motorR_pwm.ChangeDutyCycle(0)
    motorL_pwm.ChangeDutyCycle(0)

input("Press Enter to start...")

try:
    FullSpeed2()
    
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
        else:
            FullSpeed2()

except KeyboardInterrupt:
    pass

finally:
    motorR_pwm.stop()
    motorL_pwm.stop()
    GPIO.cleanup()
