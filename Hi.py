from gpiozero import Motor
from time import sleep

motor = Motor(forward=4, backward=14)

while True:
    motor.forward()
    sleep(5)
    motor.backward()
    sleep(5)


import time

while True:
    print("test")
    time.sleep(3)  # Sleep for 3 seconds
