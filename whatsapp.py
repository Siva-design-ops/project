import pyautogui
import time
time.sleep(10)
msg="Vastalya is a mad girl."
for i in range(0,15):
    pyautogui.write(msg)
    pyautogui.press('enter')
