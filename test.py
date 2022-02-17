import random

import pyautogui

while True:
    X,Y = pyautogui.size()
    X1=random.randint(0,X)
    Y1=random.randint(0,Y)
    pyautogui.moveTo(X1, Y1)