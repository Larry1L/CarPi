import RPi.GPIO as GPIO
import time
import keyboard  # Import the keyboard library

# ... (your previous code for setup and functions)

# Function to check for arrow key presses
def check_keypress():
    if keyboard.is_pressed('w'):
        FullSpeed()
    elif keyboard.is_pressed('a'):
        TurnLeft()
    elif keyboard.is_pressed('d'):
        TurnRight()
    elif keyboard.is_pressed('s'):
        StopDriving()

# Wait for the user to press Enter to start
input("Press Enter to start...")

try:
    FullSpeed2()
    
    while True:
        check_keypress()  # Check for key presses

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
            FullSpeed()

except KeyboardInterrupt:
    pass

finally:
    motorR_pwm.stop()
    motorL_pwm.stop()
    GPIO.cleanup()
