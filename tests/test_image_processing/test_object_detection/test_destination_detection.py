from python.image_processing.object_detection import destination_detection
import cv2
import numpy


def test_can_detect_simple_blob(monkeypatch):
    # black filled circle on white background
    circle_img = numpy.full(
        shape=(30, 30, 3), fill_value=255, dtype=numpy.uint8
    )
    circle_center = [15, 15]
    circle_img = cv2.circle(
        img=circle_img,
        center=circle_center,
        radius=5,
        color=[0, 0, 0],
        thickness=-1,
    )

    # exit cv2.imshow() popup if displayed
    monkeypatch.setattr(cv2, "waitKey", lambda _: 27)  # press Esc
    (
        result_x,
        result_y,
        _,
    ) = destination_detection.get_center_of_destination_iceberg(
        circle_img, manual=False
    )
    expected_result = circle_center

    assert [
        result_x,
        result_y,
    ] == expected_result, "Failed to auto detect simple circle."
