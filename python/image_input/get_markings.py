import cv2
from python.image_processing.crop_to_working_area import crop_image_to_working_area


click_counter = 0
x1 = None
y1 = None
x2 = None
y2 = None


def click_event(event, x, y, flags, params) -> None:
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


def get_markings() -> int:
    """Lets the user input two marks on the image.
    """
    # Read and display the image
    img = crop_image_to_working_area()
    cv2.imshow('image', img)

    # Read the markings
    cv2.setMouseCallback('image', click_event)

    cv2.circle(img, center=(x1,y1), radius=50, color=(0, 255, 0), thickness=-1)

    # wait for a key to be pressed to exit
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return x1, y1, x2, y2

get_markings()