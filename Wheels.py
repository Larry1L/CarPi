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
GPIO.cleanup()

# Set up the motor pins as an output
GPIO.setup(motorR_pin, GPIO.OUT)
GPIO.setup(motorL_pin, GPIO.OUT)
GPIO.setup(DirR_pin, GPIO.OUT)
GPIO.setup(DirL_pin, GPIO.OUT)

# Create PWM instances for the left and right motors
motorR_pwm = GPIO.PWM(motorR_pin, 1000)
motorL_pwm = GPIO.PWM(motorL_pin, 1000)

# Start PWM with 0% duty cycle (stopped)
motorR_pwm.start(0)
motorL_pwm.start(0)


# Define motor control functions
def TurnLeft(speed=1000):
    GPIO.output(DirL_pin, GPIO.LOW)
    GPIO.output(DirR_pin, GPIO.LOW)
    motorR_pwm.ChangeDutyCycle(speed * 0.25)
    motorL_pwm.ChangeDutyCycle(speed)
    print("Turning Right")

def TurnRight(speed=1000):
    GPIO.output(DirR_pin, GPIO.LOW)
    GPIO.output(DirL_pin, GPIO.LOW)
    motorR_pwm.ChangeDutyCycle(speed)
    motorL_pwm.ChangeDutyCycle(speed * 0.25)
    print("Turning Left")

def FullSpeed(speed=1000):
    GPIO.output(DirL_pin, GPIO.LOW)
    GPIO.output(DirR_pin, GPIO.LOW)
    motorR_pwm.ChangeDutyCycle(speed)
    motorL_pwm.ChangeDutyCycle(speed)
    print("Going Full Speed")

def GoBackward(speed=1000):
    GPIO.output(DirL_pin, GPIO.HIGH)
    GPIO.output(DirR_pin, GPIO.HIGH)
    motorR_pwm.ChangeDutyCycle(speed)
    motorL_pwm.ChangeDutyCycle(speed)
    print("Going Backward")

# Define a simple function to handle key presses
def press(key):
    if key == 'w':
        FullSpeed()
    elif key == 's':
        GoBackward()
    elif key == 'a':
        TurnLeft()
    elif key == 'd':
        TurnRight()

while True:
    listen_keyboard(on_press = press)
    FullSpeed()

# You can add cleanup and exit code here if needed
