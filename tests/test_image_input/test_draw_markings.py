from python.image_input import draw_markings
import numpy
import pytest


@pytest.mark.parametrize("color", ["red", "green", "blue"])
def test_can_change_value_on_numpy_array(color):
    img = numpy.random.rand(50, 50, 3)
    x, y = 30, 40
    color_map = {"red": [0, 0, 255], "green": [0, 255, 0], "blue": [255, 0, 0]}

    img_expected = img
    img_expected[x, y] = color_map[color]
    img_result = draw_markings.draw_mark(img, x, y, color)

    assert img_result.all() == img_expected.all()
