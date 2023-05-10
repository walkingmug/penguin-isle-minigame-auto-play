"""Classes for capturing screenshots and performing image processing. 
"""

from python.image_processing.image_transformation.crop_to_working_area import crop_image_to_working_area
from python.image_processing.object_detection.source_detection import get_center_of_source_iceberg
from python.image_processing.object_detection.destination_detection import get_center_of_destination_iceberg
import cv2
import numpy as np


class ScreenshotFrame:
    """Captures screenshots, performs source and destination detection,
    shows final image.
    """
    def __init__(self):
        pass
    
    def get_screen_img(self, screenshot: np.array):
        self.current_frame = crop_image_to_working_area(screenshot)
        # self.current_frame = cv2.imread(
            # "temp/screenshots/crop_of_relevant_area.jpg")

    def find_source(self):
        self.x_src, self.y_src = get_center_of_source_iceberg(
            self.current_frame)

    def find_destination(self):
        self.x_dest, self.y_dest = get_center_of_destination_iceberg(
            self.current_frame)

    def draw_source_on_frame(self):
        self.current_frame = cv2.circle(
            self.current_frame, center=(self.x_src, self.y_src), radius=3, color=(0, 0, 255), thickness=-1)
        self.current_frame = cv2.circle(
            self.current_frame, center=(self.x_src, self.y_src), radius=3, color=(0, 0, 0), thickness=1)

    def draw_destination_on_frame(self):
        self.current_frame = cv2.circle(
            self.current_frame, center=(self.x_dest, self.y_dest), radius=3, color=(0, 255, 0), thickness=-1)
        self.current_frame = cv2.circle(
            self.current_frame, center=(self.x_dest, self.y_dest), radius=3, color=(0, 0, 0), thickness=1)

    def update_frame_with_src_and_dest(self):
        self.draw_destination_on_frame()
        self.draw_source_on_frame()

    def get_frame(self):
        return self.current_frame

    def display_frame(self):
        cv2.destroyAllWindows()
        cv2.imshow("Screenshot", self.current_frame)
        cv2.waitKey(1)

