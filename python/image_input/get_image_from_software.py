"""Functions for capturing image screenshot from a software.
"""

import win32gui
import win32con
import time
import PIL.Image


def get_image_from_software(window_name="Zoom - Google Chrome") -> PIL.Image:
    """Takes a screenshot from a software window.

    :param window_name: the name of the window that holds the screenshare
    :raises ValueError: If the window is not found, return an error
    :return: A screenshot from a given software
    """

    # Find the handle of the window
    zoom_hwnd = win32gui.FindWindow(None, window_name)
    if zoom_hwnd == 0:
        raise ValueError(f'Window "{window_name}" does not exist.')

    # Display the window
    win32gui.ShowWindow(zoom_hwnd, win32con.SW_MAXIMIZE)
    time.sleep(5)

    # Get the coordinates of the window and take a screenshot
    (left, top, right, bottom) = win32gui.GetWindowRect(zoom_hwnd)
    PADDING = 500
    screenshot = ImageGrab.grab(
        bbox=(left, top, right + PADDING, bottom + PADDING)
    )
    screenshot.thumbnail((1000, 1000))

    return screenshot
