from gpiozero import Servo
import time

# Use the pigpio pin factory for servo control
from gpiozero.pins.pigpio import PiGPIOFactory
factory = PiGPIOFactory()

# Create a Servo object and specify the GPIO pin where your servo is connected
servo = Servo(3, pin_factory=factory)  # Adjust the GPIO pin (17) to match your setup

# Define the angle for forward and backward positions
forward_angle = 90
backward_angle = -90

try:
    while True:
        # Move the servo forward for 2 seconds
        servo.value = forward_angle / 180.0
        time.sleep(2)

        print("true")

        # Move the servo backward for 3 seconds
        servo.value = backward_angle / 180.0
        time.sleep(3)

except KeyboardInterrupt:
    pass

finally:
    # Reset the servo to the neutral position (optional)
    servo.value = None
    servo.close()
