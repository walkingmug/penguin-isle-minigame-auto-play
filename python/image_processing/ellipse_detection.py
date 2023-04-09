from edge_detection import get_edges_from_image
from crop_to_working_area import crop_image_to_working_area
import cv2
import numpy as np


def get_blobs_from_image():
    img = get_edges_from_image()
    # img = crop_image_to_working_area()
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

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
    params.filterByConvexity = False
    params.minConvexity = 0.9
    params.maxConvexity = 1

    # set the inertia filter (ellipticity)
    params.filterByInertia = False
    params.minInertiaRatio = 0.8
    params.maxInertiaRatio = 1

    # Create a detector with the parameters
    detector = cv2.SimpleBlobDetector_create(params)

    # Detect blobs
    keypoints = detector.detect(img)

    # Draw detected blobs as red circles
    img_with_keypoints = cv2.drawKeypoints(img, keypoints, np.array([]), (0, 0, 255),
                                           cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    # Show the image with detected blobs
    cv2.imshow("Blobs", img_with_keypoints)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


get_blobs_from_image()