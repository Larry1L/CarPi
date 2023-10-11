import RPi.GPIO as GPIO
import time

# Set the GPIO pin numbers (pin 8 & 14)
motorR_pin = 8
motorL_pin = 14
sensor_pin = 4  # Example GPIO pin, adjust to your setup

# Configure the GPIO mode
GPIO.setmode(GPIO.BCM)

# Set up the motor pins as an output
GPIO.setup(motorR_pin, GPIO.OUT)
GPIO.setup(motorL_pin, GPIO.OUT)
# Set up the sensor pin as an input
GPIO.setup(sensor_pin, GPIO.IN)


# Create PWM instances for the left and right motors
motorR_pwm = GPIO.PWM(motorR_pin, 100)  # PWM frequency (Hz)
motorL_pwm = GPIO.PWM(motorL_pin, 100)

# Start PWM with 0% duty cycle (stopped)
motorR_pwm.start(0)
motorL_pwm.start(0)

try:
    if GPIO.input(sensor_pin) == GPIO.HIGH:
        print("Sensor is detecting a line at startup")
    else:
        print("Sensor is not detecting a line at startup")

    while True:
        if GPIO.input(sensor_pin) == GPIO.HIGH:
            print("Line detected")
        else:
            print("No line detected")
        time.sleep(0.1)  # Adjust the sleep time as needed

def TurnRight():
    motorR_pwm.ChangeDutyCycle(25)  # Adjust duty cycle to control speed
    motorL_pwm.ChangeDutyCycle(100)  # Full speed
    time.sleep(0.1)

def TurnLeft():
    motorR_pwm.ChangeDutyCycle(100)  # Full speed
    motorL_pwm.ChangeDutyCycle(25)  # Adjust duty cycle to control speed
    time.sleep(0.1)

def FullSpeed():
    motorR_pwm.ChangeDutyCycle(100)  # Full speed for the right motor
    motorL_pwm.ChangeDutyCycle(100)  # Full speed for the left motor
    time.sleep(0.1)
def MidSpeed():
    motorR_pwm.ChangeDutyCycle(66)  # Full speed for the right motor
    motorL_pwm.ChangeDutyCycle(66)  # Full speed for the left motor
    time.sleep(0.1)
def LowSpeed():
    motorR_pwm.ChangeDutyCycle(33)  # Full speed for the right motor
    motorL_pwm.ChangeDutyCycle(33)  # Full speed for the left motor
    time.sleep(0.1)

def StopDriving():
    motorR_pwm.ChangeDutyCycle(0)  # Stop
    motorL_pwm.ChangeDutyCycle(0)
    time.sleep(1)

try:
    while True:
        time.sleep(3)
        FullSpeed()
        time.sleep(3)
        MidSpeed()
        time.sleep(3)
        LowSpeed()
        time.sleep(3)
        TurnLeft()
        time.sleep(3)
        TurnRight()
        time.sleep(3)
        StopDriving()

except KeyboardInterrupt:
    pass

finally:
    # Clean up GPIO settings
    motorR_pwm.stop()
    motorL_pwm.stop()
    GPIO.cleanup()
