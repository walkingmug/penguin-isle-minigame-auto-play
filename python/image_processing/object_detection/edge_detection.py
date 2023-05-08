import cv2
import numpy as np
from python.image_processing.image_transformation.crop_to_working_area import crop_image_to_working_area


def dilate_edges(edges_img: np.array) -> np.array:
    """Performs dilation to complete the circles.

    :param edges_img: Image with detected edges
    :return: Image with dilated edges
    """
    # perform dilation to complete circles
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (4,4))
    edges_img = cv2.dilate(edges_img, kernel, iterations=1)

    return edges_img


def detect_edges_on_image(cropped_img) -> np.array:
    """Performs Canny edge detection on an image.

    :return: A b&w image with the edges in white and background in black.
    """
    # convert image to grayscale
    cropped_img = cv2.cvtColor(cropped_img, cv2.COLOR_BGR2GRAY)

    # set lower and upper threshold (found by trial and error)
    LOWER_THRESH = 50
    UPPER_THRESH = 150

    # find edges with Canny
    edges = cv2.Canny(cropped_img, LOWER_THRESH, UPPER_THRESH)

    # perform dilation to complete circles
    edges = dilate_edges(edges)

    # save result
    # cv2.imwrite("temp/screenshots/edge.jpg", edges)

    return edges
