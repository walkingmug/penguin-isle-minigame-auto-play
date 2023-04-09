from edge_detection import get_edges_from_image
from crop_to_working_area import crop_image_to_working_area
import cv2
import numpy as np


def get_center_of_destination_iceberg():
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

    # set the circularity filter (circular edges)
    params.filterByCircularity = False
    params.minCircularity = 0.01
    params.maxCircularity = 1

    # set the convexity filter (interruption of the shape)
    params.filterByConvexity = True
    params.minConvexity = 0.9
    params.maxConvexity = 1

    # set the inertia filter (ellipticity)
    params.filterByInertia = False
    params.minInertiaRatio = 0.2
    params.maxInertiaRatio = 1

    # Create a detector with the parameters
    detector = cv2.SimpleBlobDetector_create(params)

    # Detect blobs
    keypoints = detector.detect(img)

    # Draw detected blobs as red circles
    img_with_keypoints = cv2.drawKeypoints(img, keypoints, np.array([]), (0, 0, 255),
                                           cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    # Draw the center of the circle
    center
    for keypoint in keypoints:
        x, y = int(keypoint.pt[0]), int(keypoint.pt[1])
        cv2.circle(img_with_keypoints, (x, y), 2, (0, 255, 0), -1)
        center = [x, y]
    
    # Show the image with detected blobs
    # cv2.imshow("Blobs", img_with_keypoints)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    return center
