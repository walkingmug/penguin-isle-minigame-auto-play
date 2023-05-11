import numpy as np
from cv2 import circle


def draw_src_mark(frame: np.array, x_dest: int, y_src: int):
    """Draws a red mark on an image (destination mark).

    :param frame: The image for the mark to appear on
    :param x_dest: X-position of the desired mark
    :param y_src: Y-position of the desired mark
    :return: The frame with the mark
    """
    frame = circle(
        frame, center=(x_dest, y_src), radius=3, color=(0, 0, 255), thickness=-1)
    frame = circle(
        frame, center=(x_dest, y_src), radius=3, color=(0, 0, 0), thickness=1)
    
    return frame

def draw_dest_mark(frame: np.array, x_dest: int, y_dest: int):
    """Draws a green mark on an image (destination mark).

    :param frame: The image for the mark to appear on
    :param x_dest: X-position of the desired mark
    :param y_dest: Y-position of the desired mark
    :return: The frame with the mark
    """
    frame = circle(
        frame, center=(x_dest, y_dest), radius=3, color=(0, 255, 0), thickness=-1)
    frame = circle(
        frame, center=(x_dest, y_dest), radius=3, color=(0, 0, 0), thickness=1)
    
    return frame