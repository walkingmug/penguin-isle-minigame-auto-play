import cv2


def draw_source_and_destination(src: list, dest: list) -> None:

    # draw detected blobs as red circles
    img_with_keypoints = cv2.drawKeypoints(img, keypoints, np.array([]), (0, 0, 255),
                                           cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

        # draw the center of the circle as a green dot
    center = []
    for keypoint in keypoints:
        x, y = int(keypoint.pt[0]), int(keypoint.pt[1])
        cv2.circle(img_with_keypoints, (x, y), 2, (0, 255, 0), -1)
        center = [x, y]

    # show the image with detected blobs
    # cv2.imshow("Blobs", img_with_keypoints)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()