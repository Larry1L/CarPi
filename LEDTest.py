import RPi.GPIO as GPIO
import time

# Set the GPIO pin numbers
motorR_pin = 8
motorL_pin = 14
DirR_pin = 27
DirL_pin = 22
sensorL_pin = 4
sensorR_pin = 17

# Configure the GPIO mode
GPIO.setmode(GPIO.BCM)

# Set up the motor pins as an output
GPIO.setup(motorR_pin, GPIO.OUT)
GPIO.setup(motorL_pin, GPIO.OUT)
GPIO.setup(DirR_pin, GPIO.OUT)
GPIO.setup(DirL_pin, GPIO.OUT)

# Set up the sensor pins as inputs
GPIO.setup(sensorL_pin, GPIO.IN)
GPIO.setup(sensorR_pin, GPIO.IN)

# Create PWM instances for the left and right motors
motorR_pwm = GPIO.PWM(motorR_pin, 100)
motorL_pwm = GPIO.PWM(motorL_pin, 100)

# Start PWM with 0% duty cycle (stopped)
motorR_pwm.start(0)
motorL_pwm.start(0)

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

def FullSpeed(speed):
    GPIO.output(DirL_pin, GPIO.LOW)
    GPIO.output(DirR_pin, GPIO.LOW)
    motorR_pwm.ChangeDutyCycle(speed)
    motorL_pwm.ChangeDutyCycle(speed)
    print(f"Going Full Speed with speed {speed}")

def FullSpeed2():
    FullSpeed(100)
    print("Starting Motors")

def StopDriving():
    motorR_pwm.ChangeDutyCycle(0)
    motorL_pwm.ChangeDutyCycle(0)
    print("Stopping Motors")

# Wait for the user to press Enter to start
input("Press Enter to start...")

try:
    speed = int(input("Enter the speed for FullSpeed: "))
    FullSpeed(speed)
    
    while True:
        if GPIO.input(sensorL_pin) == GPIO.LOW and GPIO.input(sensorR_pin) == GPIO.LOW:
            print("Both sensors - Line detected")
            FullSpeed(speed)
        elif GPIO.input(sensorL_pin) == GPIO.LOW:
            print("Left Sensor - Line detected")
            TurnRight()
        elif GPIO.input(sensorR_pin) == GPIO.LOW:
            print("Right Sensor - Line detected")
            TurnLeft()
        else:
            FullSpeed(speed)

except KeyboardInterrupt:
    pass

finally:
    motorR_pwm.stop()
    motorL_pwm.stop()
    GPIO.cleanup()
