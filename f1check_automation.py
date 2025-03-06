import pyautogui
import time
import keyboard
import tkinter as tk
from tkinter import messagebox
import psutil
import sys
import os
import json

# File to store user settings
CONFIG_FILE = "config.json"

def save_position(x, y):
    """Save mouse position to a config file."""
    config = {"search_box_x": x, "search_box_y": y}
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f)
    messagebox.showinfo("Position Saved", f"Search box position set to: ({x}, {y})")

def set_mouse_position():
    """Guide the user to set the mouse position."""
    messagebox.showinfo("Set Position", "Move your mouse over the search box and press ENTER.")
    while True:
        if keyboard.is_pressed("enter"):
            x, y = pyautogui.position()
            save_position(x, y)
            break
        time.sleep(0.1)

def load_position():
    """Load mouse position from the config file."""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return {"search_box_x": 500, "search_box_y": 100}  # Default position

# Prevent multiple instances
def check_existing_instance():
    current_pid = os.getpid()
    current_name = os.path.basename(__file__)

    for process in psutil.process_iter(['pid', 'name']):
        try:
            if process.info['name'] == "python.exe" or process.info['name'] == "pythonw.exe":
                if process.info['pid'] != current_pid:
                    print("Another instance is already running. Exiting...")
                    sys.exit(0)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

# Call the function to prevent multiple instances
check_existing_instance()

def automate_f1check():

    """Performs the automation process using the stored search box position."""
    pos = load_position()
    search_box_x, search_box_y = pos["search_box_x"], pos["search_box_y"]

    pyautogui.hotkey('ctrl', 'c')  # Copy MAWB number
    time.sleep(0.3)

    pyautogui.hotkey('alt', 'tab')  # Switch to Chrome
    time.sleep(0.3)

    pyautogui.click(x=search_box_x, y=search_box_y)  # Click search box (Adjust coordinates as needed)
    time.sleep(0.3)

    pyautogui.hotkey('ctrl', 'v')  # Paste MAWB number
    time.sleep(0.3)

    pyautogui.press('enter')  # Press Enter
    time.sleep(0.3)

    pyautogui.hotkey('alt','tab')#switch back to excel
    time.sleep(0.3)

    pyautogui.press('down')



# UI Setup
def create_ui():
    root = tk.Tk()
    root.title("F1 Check Automation")
    root.geometry("300x200")

    label = tk.Label(root, text="Press F9 to Run", font=("Arial", 12))
    label.pack(pady=20)

    set_position_button = tk.Button(root, text="Set Search Box Position", command=set_mouse_position, font=("Arial", 12))
    set_position_button.pack(pady=5)

    exit_button = tk.Button(root, text="Exit", command=root.quit, font=("Arial", 12))
    exit_button.pack(pady=10)

    # Bind F9 key to trigger automation
    keyboard.add_hotkey("f9", automate_f1check)

    root.mainloop()

# Run UI
create_ui()