"""Functions for converting pixel distance to expected seconds.
"""


def get_push_duration_from_distance(pixel_distance) -> float:
    """Converts the pixel distance (Euclidean) between two points into seconds.

    :param pixel_distance: Euclidean pixel distance between the two image marks
    :return: push duration in seconds for the servo to push
    """
    DURATION_FORMULA = 1/(100/1.8)
    push_duration = round((pixel_distance*DURATION_FORMULA), 2)

    return push_duration
