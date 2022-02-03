import gambler
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

def d2_gamble():
    merchant_position = get_position("Place your cursor over merchant.")
    gamble_position = get_position("Place your cursor over the gamble option.")
    item_position = get_position("Place your cursor over the item to buy.")
    print("Please close the gamble shop now.")
    time.sleep(3)

    gm = gambler.Gambler(merchant_position, gamble_position, item_position, 31)
    gm.gamble()

if __name__ == '__main__':

