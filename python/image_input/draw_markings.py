import numpy as np
from cv2 import circle

def draw_src_mark(frame: np.array, x_src: int, y_src: int):
    """Draws a red mark on an image.

    :param frame: The image for the mark to appear on
    :param x_src: X-position of the desired mark
    :param y_src: Y-position of the desired mark
    :return: The frame with the mark
    """
    frame = circle(
        frame, center=(x_src, y_src), radius=3, color=(0, 0, 255), thickness=-1)
    frame = circle(
        frame, center=(x_src, y_src), radius=3, color=(0, 0, 0), thickness=1)
    
    return frame