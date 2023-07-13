"""Functions for capturing image screenshot from a software.
"""

import win32gui
import win32con
import time
import PIL.Image
from PIL import ImageGrab


def get_image_from_software(window_name="Zoom - Google Chrome") -> PIL.Image:
    """Takes a screenshot from a software window.

    :raises ValueError: If the window is not found
    """
    # Find the handle of the window
    zoom_hwnd = win32gui.FindWindow(None, window_name)
    if zoom_hwnd == 0:
        raise ValueError(f'Window "{window_name}" does not exist.')

    # Display the window
    win32gui.ShowWindow(zoom_hwnd, win32con.SW_SHOWNORMAL)
    time.sleep(20)

    # Get the coordinates of the window and take a screenshot
    (left, top, right, bottom) = win32gui.GetWindowRect(zoom_hwnd)
    screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))

    return screenshot
