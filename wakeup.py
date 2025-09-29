import time
from wakepy import keep

#pip install wakepy
# The "keep.running()" mode prevents your system from sleeping or suspending,
# but it allows your screen to turn off or lock, which is more power-efficient.
# For keeping the screen on, you can use "keep.presenting()" instead.
print("Script is running and preventing the system from sleeping. Press Ctrl+C to stop.")

try:
    with keep.running():
        # This is where your Teams activity script logic goes
        # For example, simulate a key press every few minutes
        while True:
            # The pyautogui command from the previous example can go here
            # Since wakepy keeps the system awake, this just needs to keep Teams active
            # For example, toggle a non-disruptive key like 'numlock'
            # Note: For this to work, you still need pyautogui installed (pip install pyautogui)
            import pyautogui
            import datetime

            pyautogui.press('numlock')
            print(f"Numlock key pressed at {datetime.datetime.now().strftime('%H:%M:%S')} to maintain active status in Teams.")
            time.sleep(60) # Sleep for 1 minutes
except KeyboardInterrupt:
    print("\nScript stopped by user. The system will now resume normal power management.")
