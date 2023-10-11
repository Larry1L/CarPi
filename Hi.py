import RPi.GPIO as GPIO
import time

# Set the GPIO pin numbers (pin 8 & 14)
motorR_pin = 8
motorL_pin = 14

# Configure the GPIO mode
GPIO.setmode(GPIO.BCM)

# Set up the motor pins as an output
GPIO.setup(motorR_pin, GPIO.OUT)
GPIO.setup(motorL_pin, GPIO.OUT)

# Create PWM instances for the left and right motors
motorR_pwm = GPIO.PWM(motorR_pin, 100)  # PWM frequency (Hz)
motorL_pwm = GPIO.PWM(motorL_pin, 100)

# Start PWM with 0% duty cycle (stopped)
motorR_pwm.start(0)
motorL_pwm.start(0)

def TurnRight():
    motorR_pwm.ChangeDutyCycle(50)  # Adjust duty cycle to control speed
    motorL_pwm.ChangeDutyCycle(100)  # Full speed
    time.sleep(1)
    motorR_pwm.ChangeDutyCycle(0)  # Stop
    motorL_pwm.ChangeDutyCycle(0)
    time.sleep(1)

def TurnLeft():
    motorR_pwm.ChangeDutyCycle(100)  # Full speed
    motorL_pwm.ChangeDutyCycle(50)  # Adjust duty cycle to control speed
    time.sleep(1)
    motorR_pwm.ChangeDutyCycle(0)  # Stop
    motorL_pwm.ChangeDutyCycle(0)
    time.sleep(1)

def DriveForward():
    motorR_pwm.ChangeDutyCycle(100)  # Full speed for the right motor
    motorL_pwm.ChangeDutyCycle(100)  # Full speed for the left motor
    time.sleep(1)

def StopDriving():
    motorR_pwm.ChangeDutyCycle(0)  # Stop
    motorL_pwm.ChangeDutyCycle(0)
    time.sleep(1)

try:
    while True:
        TurnLeft()

except KeyboardInterrupt:
    pass

finally:
    # Clean up GPIO settings
    motorR_pwm.stop()
    motorL_pwm.stop()
    GPIO.cleanup()
