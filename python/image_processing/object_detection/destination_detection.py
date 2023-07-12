"""Functions for detecting blobs of regular shape.
"""

from python.image_processing.object_detection.edge_detection import (
    detect_edges_on_image,
)
from python.image_input.get_markings import get_markings
import cv2


def get_destination_blob_params():
    """Initialize and set the parameters for detecting the destination blob.

    :return: The blob detector with modified parameters
    """
    # set up the SimpleBlobDetector with default parameters
    params = cv2.SimpleBlobDetector_Params()

    # set the threshold
    params.minThreshold = 244
    params.maxThreshold = 255

    # set the area filter
    params.filterByArea = True
    params.minArea = 100
    params.maxArea = 100000

    # set the convexity filter (interruption of the shape)
    params.filterByConvexity = True
    params.minConvexity = 0.9
    params.maxConvexity = 1

    return params


def get_center_of_destination_iceberg(cropped_img, manual=False) -> int:
    """Finds the iceberg in the game where the character needs to travel.

    :param cropped_img: Image reduced to relevant parts only.
    :param manual: Bypass automatic detection of blobs.
    :return: The keypoint of the character, and the center position of it.
    """
    # let user manually select  destination
    if manual:
        _, _, x2, y2 = get_markings(cropped_img, mark_dest=True)
        return x2, y2

    # detect blobs with custom parameters
    img = detect_edges_on_image(cropped_img)
    params = get_destination_blob_params()
    detector = cv2.SimpleBlobDetector_create(params)
    keypoints = detector.detect(img)

    # manually mark destination center if it is not found
    if len(keypoints) != 1:
        _, _, x2, y2 = get_markings(cropped_img, mark_dest=True)
    else:
        x2 = int(keypoints[0].pt[0])
        y2 = int(keypoints[0].pt[1])

    return x2, y2
