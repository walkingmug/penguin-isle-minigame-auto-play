import cv2
import numpy as np


def draw_keypoint_circles(src_img: np.array, src_kpts, dest_kpts) -> None:
    # draw the source blob as red
    img_with_keypoints = cv2.drawKeypoints(
        src_img,
        (src_kpts,),
        np.array([]),
        (0, 0, 255),
        cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS,
    )

    # draw the destination blob as green
    img_with_keypoints = cv2.drawKeypoints(
        img_with_keypoints,
        dest_kpts,
        np.array([]),
        (0, 255, 0),
        cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS,
    )
