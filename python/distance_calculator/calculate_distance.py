def get_distance_in_pixels(x1, y1, x2, y2):
    """Calculates the pixel distance between two marks in an image.

    :param x1: X-value of mark 1.
    :param y1: Y-value of mark 1.
    :param x2: X-value of mark 2.
    :param y2: Y-value of mark 2.
    :return: The pixel distance between two marks.
    """
    # get coordinates of marks
    distance = ((int(x2) - int(x1))**2 + (int(y2) - int(y1))**2)**0.5
    return distance
