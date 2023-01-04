import time
import pyautogui
from PIL import ImageGrab
import numpy as np

screenWidth, screenHeight = pyautogui.size()

# TODO: Try pyautogui.getpixel instead of numpy

def grab_image():
    img = ImageGrab.grab(bbox=(1661, 400, 1730, 439))
    img_arr = np.array(img)
    colour, counts = np.unique(img_arr.reshape(-1, 3), axis=0, return_counts=True)
    return counts[0]


pyautogui.moveTo(1700, 450)
pyautogui.leftClick()

playing = True
while playing:
    time.sleep(0.01)
    pixels = grab_image()
    if grab_image() > 10:
        pyautogui.press("space")

