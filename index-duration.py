import pyautogui
import time

text_to_type = "Your Text Here"

time.sleep(2)

start_time = time.time()
max_run_time = 60  # Atur waktu dalam detik

while True:
    current_time = time.time()
    elapsed_time = current_time - start_time

    if elapsed_time >= max_run_time:
        break

    pyautogui.typewrite(text_to_type)
    pyautogui.press("enter")
    time.sleep(2)

print("Program berhenti!")
