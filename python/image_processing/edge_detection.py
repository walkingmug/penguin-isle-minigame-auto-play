import cv2
import numpy as np


def edge_detection(img: np.array):
    img = get_screenshare()
    
    # convert to grayscale
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # find edges with Canny
    edges = cv2.Canny(img, 10, 20, apertureSize=3)
    # show and save the result
    cv2.imshow("edges", edges)
    cv2.waitKey(0)