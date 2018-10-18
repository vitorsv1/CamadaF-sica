from pynput import keyboard

def on_press(key):
    if key == keyboard.Key.shift: # handles if key press is shift
        print('foo', end='')

def on_release(key):
    if key == keyboard.Key.shift:
        print()
    elif key == keyboard.Key.delete:
        print('bar')
    elif key == keyboard.Key.esc:
        return False

def get_current_key_input():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

get_current_key_input()