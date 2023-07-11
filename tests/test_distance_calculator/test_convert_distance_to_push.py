from python.distance_calculator import convert_distance_to_push


def test_can_convert_percent_distance_to_push_duration():
    PERCENT_DIST = 0.5
    expected_result = 0.47
    result = convert_distance_to_push.get_push_duration_from_distance(PERCENT_DIST)
    assert (
        result == expected_result
    ), "Wrong convertion of distance (%) to push duration (s)"
