"""Crops an image to avoid redundant image information.
"""

import cv2
import numpy as np


def crop_out_first_and_last_quarter(img: np.array) -> np.array:
    """Removes first and fourth quarter on y-axis.

    :param img: Source image to be cropped
    :return: The image with the cropped first and fourth quarter of the y-axis
    """
    img_height, _ = img.shape[:2]
    TOP_QUARTER = int(img_height/4)
    BOTTOM_QUARTER = int(img_height-(img_height/4))
    crop_of_relevant_area = img[TOP_QUARTER:BOTTOM_QUARTER,]

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
    working_area = crop_out_first_and_last_quarter(screenshare)

    return working_area
