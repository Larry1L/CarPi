import RPi.GPIO as GPIO
import time
import keyboard

# Set the GPIO pin numbers (pin 8 & 14)
motorR_pin = 8
motorL_pin = 14
sensorL_pin = 4  # Example GPIO pin, adjust to your setup
sensorR_pin = 17  # Example GPIO pin, adjust to your setup

# Configure the GPIO mode
GPIO.setmode(GPIO.BCM)

# Set up the motor pins as an output
GPIO.setup(motorR_pin, GPIO.OUT)
GPIO.setup(motorL_pin, GPIO.OUT)
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
    motorR_pwm.ChangeDutyCycle(0)  # Adjust duty cycle to control speed
    motorL_pwm.ChangeDutyCycle(100)  # Full speed

def TurnLeft():
    motorR_pwm.ChangeDutyCycle(100)  # Full speed
    motorL_pwm.ChangeDutyCycle(0)  # Adjust duty cycle to control speed

def FullSpeed():
    motorR_pwm.ChangeDutyCycle(66)  # Full speed for the right motor
    motorL_pwm.ChangeDutyCycle(66)  # Full speed for the left motor

def StopDriving():
    motorR_pwm.ChangeDutyCycle(0)  # Stop
    motorL_pwm.ChangeDutyCycle(0)

# Wait for the user to press Enter to start
input("Press Enter to start...")

FullSpeed()

try:
    while True:
        if GPIO.input(sensorL_pin) == GPIO.LOW:
            print("Left Sensor - Line detected")
            TurnRight()
        if GPIO.input(sensorR_pin) == GPIO.LOW:
            print("Right Sensor - Line detected")
            TurnLeft()
        
        # Check for arrow key presses
        if keyboard.is_pressed('left'):
            TurnLeft()
        elif keyboard.is_pressed('right'):
            TurnRight()
        elif keyboard.is_pressed('down'):
            StopDriving()
        else:
            FullSpeed()
        
        time.sleep(0.1)  # Adjust the sleep time as needed

except KeyboardInterrupt:
    pass

finally:
    # Clean up GPIO settings
    motorR_pwm.stop()
    motorL_pwm.stop()
    GPIO.cleanup()
