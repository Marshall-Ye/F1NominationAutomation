import pyautogui
import time

print("Move your mouse to the search box. You have 5 seconds...")
time.sleep(5)  # Gives you time to move the mouse

x, y = pyautogui.position()  # Get the current mouse position
print(f"Mouse Position: x={x}, y={y}")
