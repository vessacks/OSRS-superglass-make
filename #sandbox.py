#sandbox
import cv2 as cv
from cv2 import threshold
from cv2 import _InputArray_STD_BOOL_VECTOR
import numpy as np
import os
from windmouse import wind_mouse
from windowcapture import WindowCapture
from vision import Vision
import pyautogui
from pyHM import Mouse
import time
from action import Action

wincap = WindowCapture('RuneLite - Vessacks')
sand_vision = Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\superglass make\\image library\\sand.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_GRAYSCALE)
sand_action = Action('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\superglass make\\image library\\sand.png')
withdraw_18_action = Action('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\superglass make\\image library\\withdraw_18.png')

WITHDRAW_18_OFFSET = [-117,64]

'''
time.sleep(10)
print(str(pyautogui.position()))
time.sleep(10)
print(str(pyautogui.position()))
'''



while True:
    sand_clickpoint= sand_action.rightClick([180,117])
    withdraw_18_screenPoint = [sand_clickpoint[0]+WITHDRAW_18_OFFSET[0], sand_clickpoint[1] +WITHDRAW_18_OFFSET[1]]
    withdraw_18_clickPoint = withdraw_18_action.click(withdraw_18_screenPoint)

print('foo')