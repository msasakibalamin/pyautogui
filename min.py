import pyautogui #pip install pyautogui
import time
messsage = 5
while messsage > 0:
    time.sleep(4)
    pyautogui.typewrite('I love you.')
    time.sleep(2)
    pyautogui.press('enter')
    messsage = messsage - 1

