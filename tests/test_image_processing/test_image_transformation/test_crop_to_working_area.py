from python.image_processing.image_transformation import crop_to_working_area
import numpy


def test_can_crop_out_irrelevant_areas():
    img = numpy.random.rand(50, 50, 3)
    img_height, _ = img.shape[:2]
    TOP_PART = int(img_height / 4)
    BOTTOM_PART = int(img_height - (img_height / 3))
    expected_result = img[TOP_PART:BOTTOM_PART,]
    result = crop_to_working_area.crop_out_first_and_last_quarter(img)
    assert (
        result.all() == expected_result.all()
    ), "Could not properly crop out irrelevant image parts."
