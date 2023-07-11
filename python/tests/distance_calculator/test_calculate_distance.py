from python.distance_calculator import calculate_distance


def test_euclidean_distance():
    x_src, y_src, x_dest, y_dest = 10, 15, 30, 35
    expected_result = 28.284271247461902
    result = calculate_distance.get_euclidean_distance(x_src, y_src, x_dest, y_dest)
    assert result == expected_result, "Miscalculation in Euclidean distance."
