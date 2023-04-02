def get_push_duration_from_distance(pixel_distance) -> float:
    """Converts the pixel distance between two marks on the image into
    seconds for the servo to push.

    :param pixel_distance: number of pixels between the two image marks
    :return: push duration in seconds for the servo to push
    """
    push_duration = pixel_distance/100

    return push_duration