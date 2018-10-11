#from pynput.keyboard import Key, Listener
import pyautogui
from pynput import keyboard


def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

#def on_press(key):
#    key_press = key
#    print("PRESSED", key_press)
#   if key_press == "'a'":
#        print("A HEARD!")

#with Listener(on_press=on_press) as listener:
#    listener.join()'a'

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()