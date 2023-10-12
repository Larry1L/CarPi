import RPi.GPIO as GPIO
import time
from pynput import keyboard

# Your setup code here

input("Press Enter to start...")

def on_key_release(key):
    if key == keyboard.Key.esc:
        return False
    elif key.char == 'w':
        FullSpeed()
    elif key.char == 'a':
        TurnLeft()
    elif key.char == 'd':
        TurnRight()
    elif key.char == 's':
        StopDriving()

# Listen for key releases
with keyboard.Listener(on_release=on_key_release) as listener:
    try:
        FullSpeed(0)
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
    except KeyboardInterrupt:
        pass
    finally:
        listener.stop()
        motorR_pwm.stop()
        motorL_pwm.stop()
        GPIO.cleanup()
