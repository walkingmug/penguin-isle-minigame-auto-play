from python.distance_calculator import convert_pixel_to_percent


def test_can_find_percent_from_pixel_position():
    x1, y1, x2, y2 = 10, 15, 30, 35
    height, width = 1080, 1920
    x1_exp, y1_exp, x2_exp, y2_exp = (
        0.005208333333333333,
        0.013888888888888888,
        0.015625,
        0.032407407407407406,
    )  # expected results
    (
        x1_res,
        y1_res,
        x2_res,
        y2_res,
    ) = convert_pixel_to_percent.convert_pixel_to_percent_position(
        x1, y1, x2, y2, height, width
    )
    print(
        x1_res,
        y1_res,
        x2_res,
        y2_res,
    )
    assert x1_res == x1_exp, "Cannot convert position of x1 to percent."
    assert y1_res == y1_exp, "Cannot convert position of y1 to percent."
    assert x2_res == x2_exp, "Cannot convert position of x2 to percent."
    assert y2_res == y2_exp, "Cannot convert position of y2 to percent."
