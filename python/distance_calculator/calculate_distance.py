def get_distance_in_pixels(x_src, y_src, x_dest, y_dest) -> float:
    """Calculates the pixel distance (Euclidean) between two marks in an image.

    :param x_src: X-value of source mark
    :param y_src: Y-value of source mark
    :param x_dest: X-value of destination mark
    :param y_dest: Y-value of destination mark
    :return: The pixel distance between two marks
    """
    pixel_distance = ((int(x_dest) - int(x_src))**2 +
                      (int(y_dest) - int(y_src))**2)**0.5
    return pixel_distance
