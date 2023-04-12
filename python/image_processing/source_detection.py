from python.image_processing.edge_detection import get_edges_from_image
import cv2


def get_center_of_source_iceberg():
    """Finds the iceberg in the game where the character currently is.

    :return: The keypoint of the character, and the center position of it.
    """
    img = get_edges_from_image()

    # set up the SimpleBlobDetector with default parameters
    params = cv2.SimpleBlobDetector_Params()

    # set the threshold
    params.minThreshold = 244
    params.maxThreshold = 255

    # set the convexity filter (interruption of the shape)
    # take a lower convexity to account for the shape interruption by the character
    params.filterByConvexity = True
    params.minConvexity = 0.7
    params.maxConvexity = 0.8

    # create a detector with the parameters
    detector = cv2.SimpleBlobDetector_create(params)

    # detect blobs
    keypoints = detector.detect(img)

    # stop the execution if no destination was detected
    tot_destinations = len(keypoints)
    assert tot_destinations != 0, f"Expected 1 or more sources, but {tot_destinations} were given."

    # assume the bigger blob is the surface of the iceberg
    if len(keypoints) > 1:
        max_area = 0
        max_keypoint = None
        for kp in keypoints:
            area = kp.size ** 2 * 3.14159265
            if area > max_area:
                max_area = area
                max_keypoint = kp
    else:
        max_keypoint = keypoints

    # get the center of the circle (x, y)
    center = [int(max_keypoint.pt[0]), int(max_keypoint.pt[1])]

    return max_keypoint, center
