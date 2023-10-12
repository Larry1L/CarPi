import RPi.GPIO as GPIO
import time

# Set the GPIO pin numbers (pin 8 & 14)
motorR_pin = 8
motorL_pin = 14
DirR_pin = 27 
DirL_pin = 22
sensorL_pin = 4  # Example GPIO pin, adjust to your setup
sensorR_pin = 17  # Example GPIO pin, adjust to your setup

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
motorR_pwm = GPIO.PWM(motorR_pin, 100)  # PWM frequency (Hz)
motorL_pwm = GPIO.PWM(motorL_pin, 100)

# Start PWM with 0% duty cycle (stopped)
motorR_pwm.start(0)
motorL_pwm.start(0)

def TurnRight():
    GPIO.output(DirL_pin, GPIO.HIGH)
    GPIO.output(DirR_pin, GPIO.LOW)
    motorR_pwm.ChangeDutyCycle(25)  # Adjust duty cycle to control speed
    motorL_pwm.ChangeDutyCycle(25)  # Full speed

def TurnLeft():
    GPIO.output(DirR_pin, GPIO.HIGH)
    GPIO.output(DirL_pin, GPIO.LOW)
    motorR_pwm.ChangeDutyCycle(25)  # Full speed
    motorL_pwm.ChangeDutyCycle(25)  # Adjust duty cycle to control speed

def FullSpeed():
    GPIO.output(DirL_pin, GPIO.LOW)
    GPIO.output(DirR_pin, GPIO.LOW)
    motorR_pwm.ChangeDutyCycle(25)  # Full speed for the right motor
    motorL_pwm.ChangeDutyCycle(25)  # Full speed for the left motor
def FullSpeed2():
    GPIO.output(DirL_pin, GPIO.LOW)
    GPIO.output(DirR_pin, GPIO.LOW)
    motorR_pwm.ChangeDutyCycle(50)  # Full speed for the right motor
    motorL_pwm.ChangeDutyCycle(50)  # Full speed for the left motor

def StopDriving():
    motorR_pwm.ChangeDutyCycle(0)  # Stop
    motorL_pwm.ChangeDutyCycle(0)

# Wait for the user to press Enter to start
input("Press Enter to start...")

FullSpeed2()

try:
    while True:
        if GPIO.input(sensorL_pin) == GPIO.LOW:
            print("Left Sensor - Line detected")
            TurnRight()
        elif GPIO.input(sensorR_pin) == GPIO.LOW:
            print("Right Sensor - Line detected")
            TurnLeft()
        else:
            FullSpeed()

except KeyboardInterrupt:
    pass

finally:
    # Clean up GPIO settings
    motorR_pwm.stop()
    motorL_pwm.stop()
    GPIO.cleanup()
