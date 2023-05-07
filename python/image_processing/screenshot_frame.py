from python.image_processing.crop_to_working_area import crop_image_to_working_area


class ScreenshotFrame:
    def __init__(self):
        self.current_frame = crop_image_to_working_area()