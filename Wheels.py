import keyboard

def on_key_event(e):
    if e.name in ['w', 'a', 's', 'd']:
        print("test")

keyboard.on_press(on_key_event)

keyboard.wait()
