
import pyautogui as chi
import time
import numpy as np
import random

width = np.random.randint(0, 1921)
print(width)
hight = np.random.randint(0, 1080)
print(hight)
count = 0
automation = True
while count <=6 :
    x = random.randint(0, 850)
    y = random.randint(300, 1000)
    chi.moveTo(x, y, 0.5)
    time.sleep(2)
    count += 1

if count >= 6:
    automation = False
