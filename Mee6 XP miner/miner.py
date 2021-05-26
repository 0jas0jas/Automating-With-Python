import random
import pyautogui
import time
import sys



while True:
    secs = random.randint(20, 60)
    for remaining in range(secs, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write("{:2d} seconds remaining.".format(remaining))
        sys.stdout.flush()
        time.sleep(1)

    pyautogui.write('Hello')
    pyautogui.press('enter')