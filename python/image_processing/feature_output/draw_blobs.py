import cv2
import numpy as np


def draw_source_and_destination(
    src_img: np.array, src_kpts, src_center: list, dest_kpts, dest_center: list
) -> None:
    # draw the source blob as red
    img_with_keypoints = cv2.drawKeypoints(
        src_img,
        (src_kpts,),
        np.array([]),
        (0, 0, 255),
        cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS,
    )
    # img_with_keypoints = cv2.circle(
    #     img_with_keypoints,
    #     center=src_center,
    #     radius=2,
    #     color=(0, 0, 255),
    #     thickness=-1,
    # )

    # draw the destination blob as green
    img_with_keypoints = cv2.drawKeypoints(
        img_with_keypoints,
        dest_kpts,
        np.array([]),
        (0, 255, 0),
        cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS,
    )
    # img_with_keypoints = cv2.circle(
    #     img_with_keypoints,
    #     center=dest_center,
    #     radius=2,
    #     color=(0, 255, 0),
    #     thickness=-1,
    # )

    # show the image with the source and destination blobs
    cv2.imshow("Blobs", img_with_keypoints)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
