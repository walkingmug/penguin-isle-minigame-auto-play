import numpy as np


def convert_pixel_dist_to_percent_dist(
    x1: int, y1: int, x2: int, y2: int, frame: np.array
) -> float:
    """Computes the percentage distance of two marks on the image.

    :param x1: Pixel number for mark 1 on x-axis
    :param y1: Pixel number for mark 1 on y-axis
    :param x2: Pixel number for mark 2 on x-axis
    :param y2: Pixel number for mark 2 on y-axis
    :param frame: An image where the marks are located
    :return: The percentage distance of two marks from the image
    """
    height, width, _ = frame.shape

    x1_percent = x1 / width
    y1_percent = y1 / height
    x2_percent = x2 / width
    y2_percent = y2 / height

    return x1_percent, y1_percent, x2_percent, y2_percent
