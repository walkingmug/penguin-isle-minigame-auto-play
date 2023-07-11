"""Functions for calculating the distance between two pixels.
"""


def get_euclidean_distance(x_src, y_src, x_dest, y_dest) -> float:
    """Calculates the pixel distance (Euclidean) between two marks in an image.

    :param x_src: X-value of source mark
    :param y_src: Y-value of source mark
    :param x_dest: X-value of destination mark
    :param y_dest: Y-value of destination mark
    :return: The pixel distance between two marks
    """
    pixel_distance = ((x_dest - x_src) ** 2 + (y_dest - y_src) ** 2) ** 0.5
    return pixel_distance
