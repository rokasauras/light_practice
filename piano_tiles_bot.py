# Import necessary libraries
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

# Function to perform a mouse click at a specific position (x, y)
def click(x, y):
    win32api.SetCursorPos((x, y))  # Move the mouse cursor to the specified position (x, y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)  # Simulate a left mouse button down event
    time.sleep(1)  # Pause execution for 1 second (simulating a click action)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)  # Simulate a left mouse button up event

# Continuous loop until the 'q' key is pressed
while keyboard.is_pressed('q') == False:

    # Check if the pixel at (601, 560) is black (color [0, 0, 0] in RGB)
    if pyautogui.pixel(601, 560)[0] == 0:
        click(601, 560)  # Perform a click at position (601, 560)

    # Check if the pixel at (694, 560) is black (color [0, 0, 0] in RGB)
    if pyautogui.pixel(694, 560)[0] == 0:
        click(694, 560)  # Perform a click at position (694, 560)

    # Check if the pixel at (767, 560) is black (color [0, 0, 0] in RGB)
    if pyautogui.pixel(767, 560)[0] == 0:
        click(767, 560)  # Perform a click at position (767, 560)

    # Check if the pixel at (850, 560) is black (color [0, 0, 0] in RGB)
    if pyautogui.pixel(850, 560)[0] == 0:
        click(850, 560)  # Perform a click at position (850, 560)
