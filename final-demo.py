import time
import pyautogui

# Enable PyAutoGUI failsafe (move mouse to any corner to abort instantly)
pyautogui.FAILSAFE = True

print("🚨 Starting Terminal-based automation in 3 seconds. Do NOT touch your mouse or keyboard!")
time.sleep(3)

# -------------------------------------------------------------
# STEP 1: Open Terminal and type the command to launch Chrome
# -------------------------------------------------------------
print("Step 1: Opening Terminal and launching Chrome...")
pyautogui.hotkey('command', 'space')  # Open Spotlight
time.sleep(0.8)

# Type command in Terminal to open a new Google Chrome instance
pyautogui.typewrite('"Google Chrome"', interval=0.05)
pyautogui.press('enter')
time.sleep(3.0)  # Wait for Chrome to launch

# -------------------------------------------------------------
# STEP 2: Typewrite the weather URL in the new browser tab
# -------------------------------------------------------------
print("Step 2: Navigating to the weather site...")
pyautogui.hotkey('command', 't')  # Ensure a clean new tab
time.sleep(0.8)
pyautogui.typewrite('https://wttr.in/Chennai?format=3', interval=0.05)
pyautogui.press('enter')
time.sleep(4.0)  # Wait for weather data to load fully

# -------------------------------------------------------------
# STEP 3: Copy the page data and close the tab
# -------------------------------------------------------------
print("Step 3: Copying data and closing the tab...")
pyautogui.hotkey('command', 'a')  # Select all text
time.sleep(0.5)
pyautogui.hotkey('command', 'c')  # Copy to clipboard
time.sleep(0.5)
pyautogui.hotkey('command', 'w')  # Close the active weather tab
time.sleep(1.0)

# -------------------------------------------------------------
# STEP 4: Open TextEdit and create a new file
# -------------------------------------------------------------
print("Step 4: Opening TextEdit for a new file...")
pyautogui.hotkey('command', 'space')  # Open Spotlight
time.sleep(0.8)
pyautogui.typewrite('TextEdit', interval=0.08)
pyautogui.press('enter')
time.sleep(2.0)  # Wait for TextEdit to launch
pyautogui.hotkey('command', 'n')  # Force a brand new document
time.sleep(0.8)

# -------------------------------------------------------------
# STEP 5: Paste the data and save the file
# -------------------------------------------------------------
print("Step 5: Pasting content and saving file...")
pyautogui.hotkey('command', 'v')  # Paste copied weather data
time.sleep(1.0)
pyautogui.hotkey('command', 's')  # Open Save dialog
time.sleep(1.2)

# Type filename and confirm
pyautogui.typewrite('weather_report.txt', interval=0.08)
time.sleep(0.5)
pyautogui.press('enter')          # Confirm save
time.sleep(1.0)

print("✅ Automation completed successfully via Terminal and PyAutoGUI!")