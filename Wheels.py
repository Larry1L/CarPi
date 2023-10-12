#Run this command to install library
#python3 -m pip install sshkeyboard 

from sshkeyboard import listen_keyboard
import RPi.GPIO as GPIO # Raspberry GPIO library
import time # Time library allowing for delays in the code

# Set the GPIO pin numbers (pin 8 & 14)
motorR_pin = 8 # Left motors pin
motorL_pin = 14 # Right motors pin
DirR_pin = 27 # Right motors direction pin
DirL_pin = 22 # Left motors direction pin
sensorL_pin = 4  # GPIO pin for the left sensor
sensorR_pin = 17  # GPIO pin for the right sensor

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
motorR_pwm = GPIO.PWM(motorR_pin, 100)  # PWM Speed (%)
motorL_pwm = GPIO.PWM(motorL_pin, 100)

# Start PWM with 0% duty cycle (stopped)
motorR_pwm.start(0)
motorL_pwm.start(0)

def TurnRight(speed=100): # Function for the car to turn right by making the left wheel drive backwards faster than the right wheel drives forward
    GPIO.output(DirL_pin, GPIO.HIGH)
    GPIO.output(DirR_pin, GPIO.LOW)
    motorR_pwm.ChangeDutyCycle(0)  # Adjust duty cycle to control speed
    motorL_pwm.ChangeDutyCycle(speed)  # Full speed
    print("Turning Right")

def TurnLeft(speed=90): # Function for the car to turn left by making the right wheel drive backwards faster than the left wheel drives forward
    GPIO.output(DirR_pin, GPIO.HIGH)
    GPIO.output(DirL_pin, GPIO.LOW)
    motorR_pwm.ChangeDutyCycle(speed)  # Full speed
    motorL_pwm.ChangeDutyCycle(0)  # Adjust duty cycle to control speed
    print("Turning Left")

def FullSpeed(speed=100): # Function for driving forward and making sure none of the wheels are backwards
    GPIO.output(DirL_pin, GPIO.LOW)
    GPIO.output(DirR_pin, GPIO.LOW)
    motorR_pwm.ChangeDutyCycle(speed)  # Full speed for the right motor
    motorL_pwm.ChangeDutyCycle(speed)  # Full speed for the left motor
def SlowSpeed(speed=20): # Function for driving forward and making sure none of the wheels are backwards
    GPIO.output(DirL_pin, GPIO.LOW)
    GPIO.output(DirR_pin, GPIO.LOW)
    motorR_pwm.ChangeDutyCycle(speed)  # Full speed for the right motor
    motorL_pwm.ChangeDutyCycle(speed)  # Full speed for the left motor
def StopDriving(): # Function to stop driving
    motorR_pwm.ChangeDutyCycle(0)
    motorL_pwm.ChangeDutyCycle(0)
    print("Stopping Motors")
def DriveBackwards(): # Function to stop driving
    GPIO.output(DirL_pin, GPIO.LOW)
    GPIO.output(DirR_pin, GPIO.LOW)
    motorR_pwm.ChangeDutyCycle(speed)  # Full speed for the right motor
    motorL_pwm.ChangeDutyCycle(speed)  # Full speed for the left motor

# Wait for the user to press Enter to start
input("Press Enter to start...")

try:
    
    while True:
        listen_keyboard(on_press = press)
        if keyboard.is_pressed('w'):
            FullSpeed()
        elif keyboard.is_pressed('a'):
            TurnLeft()
        elif keyboard.is_pressed('s'):
            DriveBackwards()
        elif keyboard.is_pressed('d'):
            TurnRight()
        else:
            SlowSpeed()

except KeyboardInterrupt: # Emergency terminal stop button ( CTRL + C )
    pass

finally:
    # Clean up GPIO settings
    motorR_pwm.stop()
    motorL_pwm.stop()
    GPIO.cleanup()
