import cv2
import numpy as np
from crop_to_working_area import crop_image_to_working_area


def edge_detection() -> np.array:
    """Performs Canny edge detection on an image.

    :return: A b&w image with the edges in white and background in black.
    """
    # get image
    img = crop_image_to_working_area()

    # convert image to grayscale
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # set lower and upper threshold (found by trial and error)
    t_lower = 50
    t_upper = 150

    # find edges with Canny
    edges = cv2.Canny(img, t_lower, t_upper)
    
    # show result
    # cv2.imshow("edges", edges)
    # cv2.waitKey(0)

    return edges

