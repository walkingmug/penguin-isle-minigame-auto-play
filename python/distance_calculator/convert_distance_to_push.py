"""Functions for converting pixel distance to expected seconds.
"""


def get_push_duration_from_distance(percent_distance) -> float:
    """Converts the pixel distance (Euclidean) between two points into seconds.

    :param percent_distance: Euclidean percent distance between the two image marks
    :return: push duration in seconds for the servo to push
    """
    DURATION_FORMULA = 0.95 #1/(100/0.5)
    push_duration = round((percent_distance*DURATION_FORMULA), 2)

    return push_duration
