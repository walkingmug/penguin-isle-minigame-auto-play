import cv2
import numpy as np


def get_screenshare_position() -> np.array:
    img = cv2.imread('temp/screenshots/screenshot.png')

    # get color bounds of green box
    lower = (0, 195, 70)  # lower bound for each channel
    upper = (0, 205, 80)  # upper bound for each channel

    # create the black and white mask
    bw_mask = cv2.inRange(img, lower, upper)

    # get bounds of green pixels
    white_loc_in_mask = np.where(bw_mask == 255)
    xmin, ymin, xmax, ymax = np.min(white_loc_in_mask[1]), np.min(
        white_loc_in_mask[0]), np.max(white_loc_in_mask[1]), np.max(white_loc_in_mask[0])

    # crop the image at the bounds
    crop = img[ymin:ymax, xmin:xmax]

    # write result to disk
    # cv2.imwrite("temp/screenshots/green_box_mask.jpg", mask)
    # cv2.imwrite("temp/screenshots/green_box_cropped.jpg", crop)

    return crop
