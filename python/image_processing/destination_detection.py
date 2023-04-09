from edge_detection import get_edges_from_image
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

    # set the convexity filter (interruption of the shape)
    params.filterByConvexity = True
    params.minConvexity = 0.9
    params.maxConvexity = 1

    # create a detector with the parameters
    detector = cv2.SimpleBlobDetector_create(params)

    # detect blobs
    keypoints = detector.detect(img)

    # stop the execution if more than one destination was detected
    tot_destinations = len(keypoints)
    assert tot_destinations == 1, f"There should be exactly one destination, {tot_destinations} were given."

    # get the center of the circle (x, y)
    center = [int(keypoints[0].pt[0]), int(keypoints[0].pt[1])]

    return center


get_center_of_destination_iceberg()
