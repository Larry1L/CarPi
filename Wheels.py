import RPi.GPIO as GPIO
import time

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

# Define GPIO pin numbers for your sensors
sensorL_pin = 17
sensorR_pin = 18

# Configure GPIO pins for input
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensorL_pin, GPIO.IN)
GPIO.setup(sensorR_pin, GPIO.IN)

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
