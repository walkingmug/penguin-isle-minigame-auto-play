import cv2
import numpy as np


def get_working_area(img: np.array) -> np.array:
    """ Removes reduntant image parts (first and fourth y-axis quarter) since
    the icebergs in the game only appear on the middle two quarters of the image.

    :param img: Source image to be cropped
    :return: The image with the croppet first and fourth quarter of the y-axis
    """
    # keep first and last quarter of the image
    hh, _ = img.shape[:2]
    crop_of_relevant_area = img[int(hh/4):int(hh-(hh/4)),]

    # write result to disk
    # cv2.imwrite("temp/screenshots/crop_of_relevant_area.jpg", crop_of_relevant_area)

    return crop_of_relevant_area


def get_screenshare() -> np.array:
    """Crops the screenshare from the screenshot image.

    :return: An image of the cropped screenshare.
    """
    img = cv2.imread('temp/screenshots/screenshot.png')

    # get color bounds of green box
    lower = (0, 195, 70)  # lower bound for each channel
    upper = (0, 205, 80)  # upper bound for each channel

    # create the black and white mask
    bw_mask = cv2.inRange(img, lower, upper)

    # get the diagonal endpoints of the white mask
    white_loc_in_mask = np.where(bw_mask == 255)
    xmin, ymin, xmax, ymax = np.min(white_loc_in_mask[1]), np.min(
        white_loc_in_mask[0]), np.max(white_loc_in_mask[1]), np.max(white_loc_in_mask[0])

    # crop the image at the bounds
    crop_of_screenshare = img[ymin:ymax, xmin:xmax]

    # write result to disk
    # cv2.imwrite("temp/screenshots/green_box_mask.jpg", mask)
    # cv2.imwrite("temp/screenshots/green_box_cropped.jpg", crop)

    return crop_of_screenshare


def crop_image_to_working_area() -> np.array:
    """Extracts the working area from a screenshot.

    :return: A cropped image of the working area.
    """
    screenshare = get_screenshare()
    working_area = get_working_area(screenshare)

    return working_area
