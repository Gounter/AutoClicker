from gambler import Gambler
import time
import pyautogui
from jumper import Jumper


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
    print("Starting D2 gamble routine in 3 seconds")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    merchant_position = get_position("Place your cursor over merchant.")
    gamble_position = get_position("Place your cursor over the gamble option.")
    item_position = get_position("Place your cursor over the item to buy.")
    print("Please close the gamble shop now.")
    time.sleep(3)

    gm = Gambler(merchant_position, gamble_position, item_position, 31)
    gm.gamble()


def jumper_routine():
    jp = Jumper()
    jp.keep_jumping()


def menu():
    print("Choose routine to run:")
    print("   1 - Lost Ark AFK killer")
    print("   2 - Diablo 2 gambler")
    print("   9 - Exit")
    option = input("Enter option number ")
    if option == "1":
        jumper_routine()
    elif option == "2":
        d2_gamble()
    elif option == "9":
        exit(0)
    else:
        menu()


if __name__ == '__main__':
    menu()
