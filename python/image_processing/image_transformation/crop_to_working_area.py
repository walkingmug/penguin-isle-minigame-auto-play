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
    TOP_PART = int(img_height / 4)
    BOTTOM_PART = int(img_height - (img_height / 3))
    crop_of_relevant_area = img[TOP_PART:BOTTOM_PART, :]

    return crop_of_relevant_area


def get_screenshare_from_screenshot(screenshot: np.array) -> np.array:
    """Crops the screenshare from the screenshot image.

    :param screenshot: Full-screen screenshot to look for screenshare section
    :return: An image of the cropped screenshare
    """
    # create black and white mask based on green color channel bounds
    LOWER_BOUND = (0, 195, 70)
    UPPER_BOUND = (0, 205, 80)
    bw_mask = cv2.inRange(screenshot, LOWER_BOUND, UPPER_BOUND)

    # get the diagonal endpoints of the white mask
    white_loc_in_mask = np.where(bw_mask == 255)
    xmin, ymin, xmax, ymax = (
        np.min(white_loc_in_mask[1]),
        np.min(white_loc_in_mask[0]),
        np.max(white_loc_in_mask[1]),
        np.max(white_loc_in_mask[0]),
    )

    # crop the image at the bounds
    crop_of_screenshare = screenshot[ymin:ymax, xmin:xmax]

    return crop_of_screenshare


def crop_image_to_working_area(screenshot: np.array) -> np.array:
    """Extracts the working area from a screenshot.

    :param screenshot: Screenshot from screenshare to crop out irrelevant parts
    :return: A cropped image of the working area.
    """
    screenshare = get_screenshare_from_screenshot(screenshot)
    working_area = crop_out_first_and_last_quarter(screenshare)

    return working_area
