"""Takes a screenshot of a specified screensharing software.
"""
import win32gui
import win32con
import time
from PIL import ImageGrab


def get_image_from_software(window_name="Zoom - Google Chrome") -> None:
    """Takes a screenshot from a software window and saves it.

    :raises ValueError: if the window is not found
    """
    # Find the handle of the window
    zoom_hwnd = win32gui.FindWindow(None, window_name)
    if zoom_hwnd == 0:
        raise ValueError(f"Window \"{window_name}\" does not exist.")

    # Display the window so that it can take a screenshot
    win32gui.ShowWindow(zoom_hwnd, win32con.SW_SHOWNORMAL)

    # Give some time for the window to show
    time.sleep(1)

    # Get the coordinates of the window
    (left, top, right, bottom) = win32gui.GetWindowRect(zoom_hwnd)

    # Take a screenshot of the window
    screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))

    # Minimize the window
    win32gui.ShowWindow(zoom_hwnd, win32con.SW_MINIMIZE)

    # Save the screenshot to a file
    screenshot.save('temp\screenshots\screenshot.png')
