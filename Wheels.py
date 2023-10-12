from sshkeyboard import listen_keyboard
import RPi.GPIO as GPIO
import time

# Set the GPIO pin numbers
motorR_pin = 8
motorL_pin = 14
DirR_pin = 27
DirL_pin = 22

# Configure the GPIO mode
GPIO.setmode(GPIO.BCM)

# Set up the motor pins as an output
GPIO.setup(motorR_pin, GPIO.OUT)
GPIO.setup(motorL_pin, GPIO.OUT)
GPIO.setup(DirR_pin, GPIO.OUT)
GPIO.setup(DirL_pin, GPIO.OUT)

# Create PWM instances for the left and right motors
motorR_pwm = GPIO.PWM(motorR_pin, 100)
motorL_pwm = GPIO.PWM(motorL_pin, 100)

def TurnRight(speed=100):
    GPIO.output(DirL_pin, GPIO.HIGH)
    GPIO.output(DirR_pin, GPIO.LOW)
    motorR_pwm.ChangeDutyCycle(0)
    motorL_pwm.ChangeDutyCycle(speed)
    print("Turning Right")

def TurnLeft(speed=90):
    GPIO.output(DirR_pin, GPIO.HIGH)
    GPIO.output(DirL_pin, GPIO.LOW)
    motorR_pwm.ChangeDutyCycle(speed)
    motorL_pwm.ChangeDutyCycle(0)
    print("Turning Left")

def FullSpeed(speed=100):
    GPIO.output(DirL_pin, GPIO.LOW)
    GPIO.output(DirR_pin, GPIO.LOW)
    motorR_pwm.ChangeDutyCycle(speed)
    motorL_pwm.ChangeDutyCycle(speed)
    print("Going Full Speed")

def GoBackward(speed=100):
    GPIO.output(DirL_pin, GPIO.HIGH)
    GPIO.output(DirR_pin, GPIO.HIGH)
    motorR_pwm.ChangeDutyCycle(speed)
    motorL_pwm.ChangeDutyCycle(speed)
    print("Going Backward")

while True:
    listen_keyboard()
    if listen_keyboard('w'):
        FullSpeed()
    elif listen_keyboard('s'):
        GoBackward()
    elif listen_keyboard('a'):
        TurnLeft()
    elif listen_keyboard('d'):
        TurnRight()
    else:
        motorR_pwm.ChangeDutyCycle(0)
        motorL_pwm.ChangeDutyCycle(0)
