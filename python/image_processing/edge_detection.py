import cv2
import numpy as np
from crop_to_working_area import crop_image_to_working_area


def perform_morphological_operations(edges: np.array):
    # perform dilation to complete circles
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (4,4))
    edges = cv2.dilate(edges, kernel, iterations=1)

    return edges


def get_edges_from_image() -> np.array:
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

    # perform dilation to complete circles
    edges = perform_morphological_operations(edges)
    
    # save result
    # cv2.imwrite("temp/screenshots/edge.jpg", edges)

    return edges
