"""Functions for manually inputting marks on an image.
"""

import cv2
from python.image_processing.image_transformation.crop_to_working_area import crop_image_to_working_area


click_type = ''
img_title = ''
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
    global click_type
    global x1, y1, x2, y2
    global img
    global img_title

    # Get click coordinates and stop after two clicks
    if event == cv2.EVENT_LBUTTONDOWN:
        if click_type == 'src':
            x1 = x
            y1 = y
        elif click_type == 'dest':
            x2 = x
            y2 = y
        else:
            raise ValueError(f"Variable 'click_type' must be either 'src' \
                             or 'dest', but '{click_type}' was given.")
        click_type = ''
        # cv2.destroyAllWindows()

        # draw a mark on the click
        cv2.circle(img, center=(x, y), radius=3,
                   color=(0, 0, 255), thickness=-1)
        cv2.imshow(img_title, img)


def get_markings(cropped_img, mark_src=False, mark_dest=False) -> int:
    """Lets the user input two marks on the image.
    """
    global img
    global click_type
    global img_title

    img = cropped_img

    # get source mark from user
    if mark_src == True:
        click_type = 'src'
        img_title = 'Mark source'
        cv2.imshow(img_title, img)
        cv2.setMouseCallback(img_title, click_event)

    # get destination mark from user
    if mark_dest == True:
        click_type = 'dest'
        img_title = 'Mark destination'
        cv2.imshow(img_title, img)
        cv2.setMouseCallback(img_title, click_event)

    # auto get source and destination marks
    if mark_src == False and mark_dest == False:
        return -1

    # wait for a key to be pressed to exit
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return x1, y1, x2, y2
