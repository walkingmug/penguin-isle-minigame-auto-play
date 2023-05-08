from python.image_processing.edge_detection import get_edges_from_image
from python.image_input.get_markings import get_markings
import cv2


def get_center_of_source_iceberg(cropped_img):
    """Finds the iceberg in the game where the character currently is.

    :return: The keypoint of the character, and the center position of it.
    """
    img = get_edges_from_image(cropped_img)

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

    # assume the bigger blob is the surface of the iceberg
    if len(keypoints) > 1:
        max_area = 0
        max_keypoint = None
        for kp in keypoints:
            area = kp.size ** 2 * 3.14159265
            if area > max_area:
                max_area = area
                max_keypoint = kp
        x1 = int(max_keypoint.pt[0])
        y1 = int(max_keypoint.pt[1])
    elif len(keypoints) == 1:
        max_keypoint = keypoints
        print(type(max_keypoint))
        print(cv2.KeyPoint_convert(max_keypoint)[0][0])
        x1 = int(cv2.KeyPoint_convert(max_keypoint)[0][0])
        y1 = int(cv2.KeyPoint_convert(max_keypoint)[0][1])

    # manually mark source center if it couldn't be found
    elif len(keypoints) < 1:
        x1, y1, _, _ = get_markings(mark_src=True)

    return x1, y1
