import pyautogui
import time

text_to_type = "Your Text Here"

time.sleep(2)

while True:
    pyautogui.typewrite(text_to_type)
    pyautogui.press("enter")
    time.sleep(2)
