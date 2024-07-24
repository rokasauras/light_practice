from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:

    if pyautogui.pixel(601, 560)[0] == 0:
        click(601, 560)

    if pyautogui.pixel(694, 560)[0] == 0:
        click(694, 560)

    if pyautogui.pixel(767, 560)[0] == 0:
        click(767, 560)

    if pyautogui.pixel(850, 560)[0] == 0:
        click(850, 560)       

