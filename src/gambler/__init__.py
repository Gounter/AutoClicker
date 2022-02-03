import pyautogui
import time


class Gambler:
    def __init__(self, merchant_position, gamble_position, item_position, iterations):
        self.iterations = iterations
        self.item_position = item_position
        self.gamble_position = gamble_position
        self.merchant_position = merchant_position

    def gamble(self):
        for x in range(self.iterations):
            self.shift_left_click(self.merchant_position)
            time.sleep(0.25)
            self.left_click(self.merchant_position)
            time.sleep(0.25)
            self.left_click(self.gamble_position)
            time.sleep(0.25)
            self.right_click(self.item_position)
            time.sleep(0.15)
            self.escape()

    @staticmethod
    def shift_left_click(position):
        pyautogui.keyDown('shift')
        pyautogui.click(x=position[0], y=position[1])
        pyautogui.keyUp('shift')

    @staticmethod
    def left_click(position):
        pyautogui.click(x=position[0], y=position[1])

    @staticmethod
    def right_click(position):
        pyautogui.moveTo(x=position[0], y=position[1])
        pyautogui.click(x=position[0], y=position[1], button=pyautogui.RIGHT, clicks=2)

    @staticmethod
    def escape():
        pyautogui.press("esc")

