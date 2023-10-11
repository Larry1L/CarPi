import RPi.GPIO as GPIO
import time

# Set the GPIO pin number (pin 3)
motor_pin = 3

# Configure the GPIO mode
GPIO.setmode(GPIO.BCM)

# Set up the motor pin as an output
GPIO.setup(motor_pin, GPIO.OUT)

# Function to start the motor
def start_motor():
    GPIO.output(motor_pin, GPIO.HIGH)

# Function to stop the motor
def stop_motor():
    GPIO.output(motor_pin, GPIO.LOW)

try:
    while True:  # Loop indefinitely
        start_motor()
        time.sleep(2)  # Run the motor for 2 seconds
        print("Motor is running...")
        stop_motor()
        print("Motor stopped...")
        time.sleep(1)  # Wait for 1 second

except KeyboardInterrupt:
    pass

finally:
    # Clean up GPIO settings
    GPIO.cleanup()
