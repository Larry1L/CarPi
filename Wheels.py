try:
    while True:
        if keyboard.is_pressed('w'):
            print('W pressed')
            FullSpeed()
        elif keyboard.is_pressed('a'):
            print('A pressed')
            TurnLeft()
        elif keyboard.is_pressed('d'):
            print('D pressed')
            TurnRight()
        else:
            print('No key pressed')
            StopDriving()
        time.sleep(0.1)
except KeyboardInterrupt:
    pass
finally:
    StopDriving()
    GPIO.cleanup()
