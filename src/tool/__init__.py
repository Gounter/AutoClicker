import time
import pyautogui


def get_position(message):
    print(message)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    return pyautogui.position()
