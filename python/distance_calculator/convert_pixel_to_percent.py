"""Converts the position of a pixel in an image from pixel-position to
percentage-position. Used to be compatible with different screen resolutions.
"""


def convert_pixel_to_percent_position(
    x1: int, y1: int, x2: int, y2: int, height: int, width: int
) -> float:
    """Divides the pixel by the total amount of pixels to get precentage part.

    :param x1: Pixel number for mark 1 on x-axis
    :param y1: Pixel number for mark 1 on y-axis
    :param x2: Pixel number for mark 2 on x-axis
    :param y2: Pixel number for mark 2 on y-axis
    :param height: The image height in pixels
    :param width: The image width in pixels
    :return: The percentage distance of two marks from the image
    """

    x1_percent = x1 / width
    y1_percent = y1 / height
    x2_percent = x2 / width
    y2_percent = y2 / height

    return x1_percent, y1_percent, x2_percent, y2_percent
