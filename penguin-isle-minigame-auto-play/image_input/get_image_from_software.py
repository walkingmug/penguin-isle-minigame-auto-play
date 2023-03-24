import win32gui
from PIL import ImageGrab

# Find the handle of the Zoom window
zoom_hwnd = win32gui.FindWindow(None, "Zoom Meeting")

# Get the coordinates of the Zoom window
(left, top, right, bottom) = win32gui.GetWindowRect(zoom_hwnd)

# Take a screenshot of the Zoom window
screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))

# Save the screenshot to a file
screenshot.save('temp\screenshots\zoom_screenshot.png')
