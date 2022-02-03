from random import randint

import pyautogui
import time
import os


def jump():
    pyautogui.keyDown('space')
    time.sleep(randint(1, 15))
    pyautogui.keyUp('space')


def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)



class Jumper:
    def __init__(self):
        self.iterations = 0

    def keep_jumping(self):
        while 1 == 1:
            clear_console()
            print("Close the tab to stop.")
            print(f"Amount of jumps currently at: {self.iterations}")
            jump()
            self.iterations += 1
