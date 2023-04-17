import cv2
from python.image_processing.crop_to_working_area import crop_image_to_working_area


click_counter = 0
x1 = None
y1 = None
x2 = None
y2 = None
img_title = ''


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
    global img 
    global img_title

    # Get click coordinates and stop after two clicks
    if event == cv2.EVENT_LBUTTONDOWN:   
        print(click_counter)   
        if click_counter == 2:
            x1 = x
            y1 = y
        elif click_counter == 1:
            x2 = x
            y2 = y
            cv2.destroyAllWindows()
        click_counter -= 1

        # draw a mark on left click
        cv2.circle(img, center=(x,y), radius=3, color=(0, 0, 255), thickness=-1)
        cv2.imshow(img_title, img)


def get_markings(mark_src=False, mark_dest=False) -> int:
    """Lets the user input two marks on the image.
    """
    global img
    global click_counter
    global img_title

    # read and display the image
    img = crop_image_to_working_area()

    # get N number of marks from user
    if mark_src==True and mark_dest==True:
        # set number of clicks and image title
        click_counter = 2
        img_title = 'Mark source and destination'

        # read the markings
        cv2.imshow(img_title, img)
        cv2.setMouseCallback(img_title, click_event)
    elif mark_src==True and mark_dest==False:
        # set number of clicks and image title
        click_counter = 1
        img_title = 'Mark source'

        # read the markings
        cv2.imshow(img_title, img)
        cv2.setMouseCallback(img_title, click_event)
    elif mark_src==False and mark_dest==True:
        # set number of clicks and image title
        click_counter = 1
        img_title = 'Mark destination'

        # read the markings
        cv2.imshow(img_title, img)
        cv2.setMouseCallback(img_title, click_event)
    else:
        return -1
    
    # wait for a key to be pressed to exit
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return x1, y1, x2, y2
