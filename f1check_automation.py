import pyautogui
import time
import keyboard  # For keybinding

def automate_mawb_search():
    pyautogui.hotkey('ctrl', 'c')  # Copy MAWB number
    time.sleep(0.3)

    pyautogui.hotkey('alt', 'tab')  # Switch to Chrome
    time.sleep(0.6)

    pyautogui.click(x=321, y=110)  # Click search box (Adjust coordinates as needed)
    time.sleep(0.5)

    pyautogui.hotkey('ctrl', 'v')  # Paste MAWB number
    time.sleep(0.3)

    pyautogui.press('enter')  # Press Enter
    time.sleep(0.5)

    pyautogui.hotkey('alt','tab')#switch back to excel

# Bind script to F8 key (change to any key you prefer)
keyboard.add_hotkey("F9", automate_mawb_search)

print("Automation ready! Press F9 to run the script.")
keyboard.wait("esc")  # Keeps the script running until you press 'esc' to stop
