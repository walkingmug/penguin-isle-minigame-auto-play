"""Functions for drawing marks on an image.
"""

import numpy as np
import cv2


def draw_mark(frame: np.array, x: int, y: int, color_name="red"):
    """Draws a mark on an image (destination mark).

    :param frame: The image for the mark to appear on
    :param x: X-position of the desired mark
    :param y: Y-position of the desired mark
    :return: The frame with the mark
    """

    # convert color name to cv2 color tuple
    color_map = {"red": (0, 0, 255), "green": (0, 255, 0), "blue": (255, 0, 0)}
    if color_name in color_map:
        color_tuple = color_map[color_name]

    # draw mark
    frame = cv2.circle(
        cv2.UMat(frame),
        center=(x, y),
        radius=3,
        color=color_tuple,
        thickness=-1,
    )
    frame = cv2.ACCESS_WRITEcircle(
        cv2.UMat(frame), center=(x, y), radius=3, color=(0, 0, 0), thickness=1
    )

    return frame
