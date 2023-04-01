import cv2


click_counter = 0
x1 = None
y1 = None
x2 = None
y2 = None


def click_event(event, x, y, flags, params):
    """Checks for left mouse clicks and stops after two clicks

    :param event: _description_
    :param x: _description_
    :param y: _description_
    :param flags: _description_
    :param params: _description_
    """
    global click_counter
    global x1, y1, x2, y2

    # Get click coordinates and stop after two clicks
    if event == cv2.EVENT_LBUTTONDOWN:      
        click_counter += 1
        if click_counter == 1:
            x1 = x
            y1 = y
        else:
            x2 = x
            y2 = y
            cv2.destroyAllWindows()


def get_markings():
    """Lets the user input two marks on the image.
    """
    # Read and display the image
    img = cv2.imread("temp\screenshots\screenshot.png")
    cv2.imshow('image', img)

    # Read the markings
    cv2.setMouseCallback('image', click_event)

    # wait for a key to be pressed to exit
    cv2.waitKey(0)
  
    # close the window
    cv2.destroyAllWindows()

    return x1, y1, x2, y2
