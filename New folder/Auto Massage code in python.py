import pyautogui
import time
import random


time.sleep(4)
massage = 15
while massage > 0 :
    pyautogui.typewrite(f'Hay! Whats Up{random.randint(1,100)}')
    pyautogui.press('enter')
    massage -= 1





