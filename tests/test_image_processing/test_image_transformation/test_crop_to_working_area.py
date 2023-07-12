from python.image_processing.image_transformation import crop_to_working_area
import numpy


def test_can_crop_out_irrelevant_areas():
    img = numpy.random.rand(50, 50, 3)
    img_height, _ = img.shape[:2]
    TOP_PART = int(img_height / 4)
    BOTTOM_PART = int(img_height - (img_height / 3))
    expected_result = img[TOP_PART:BOTTOM_PART, :]
    result = crop_to_working_area.crop_out_first_and_last_quarter(img)
    assert (
        result.all() == expected_result.all()
    ), "Could not properly crop out irrelevant image parts."


def test_can_extract_screenshare_from_full_screenshot():
    img = numpy.random.rand(50, 50, 3)

    # create green square outline
    img[10:12, 20:30] = [0, 200, 75]  # top horizontal green line
    img[30:32, 20:30] = [0, 200, 75]  # bottom horizontal green line
    img[10:32, 20:22] = [0, 200, 75]  # left vertical green line
    img[10:32, 30:32] = [0, 200, 75]  # right vertical green line

    expected_result = img[
        10:32,
        30:32,
    ]
    result = crop_to_working_area.get_screenshare_from_screenshot(img)
    assert (
        result.all() == expected_result.all()
    ), "Incorrect cropping out screenshare from full screenshot."
