from python.image_processing.edge_detection import get_edges_from_image
from python.image_input.get_markings import get_markings
import cv2
 

def get_center_of_destination_iceberg():
    """Finds the iceberg in the game where the character needs to travel.

    :return: The keypoint of the character, and the center position of it.
    """
    img = get_edges_from_image()

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

    # create a detector with the parameters
    detector = cv2.SimpleBlobDetector_create(params)

    # detect blobs
    keypoints = detector.detect(img)

    # manually mark destination center if it couldn't be found
    if len(keypoints) != 1:
        x1, y1, _, _ = get_markings(mark_dest=True)
        center = [x1, y1]
    else:
        center = [int(keypoints[0].pt[0]), int(keypoints[0].pt[1])]

    return keypoints, center
