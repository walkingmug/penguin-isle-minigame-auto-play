from python.image_input.get_image_from_software import get_image_from_software
from python.distance_calculator.calculate_distance import (
    get_euclidean_distance,
)
from python.distance_calculator.convert_distance_to_push import (
    get_push_duration_from_distance,
)
from python.arduino_serial_operations.serial_operations import ArduinoSerial

from python.image_input.screenshot_frame import ScreenshotFrame
from python.distance_calculator.convert_pixel_to_percent import (
    convert_pixel_to_percent_position,
)
import time


def main() -> None:
    screen_img = ScreenshotFrame()
    servo = ArduinoSerial()

    # perform image processing and update frames
    while True:
        # save a screenshot image from a given software
        screenshot = get_image_from_software("Zoom - Google Chrome")

        # automatically detect source and destination on image
        # if it cannot be detected, manually ask the user to input them
        screen_img.get_screen_img(screenshot)
        frame = screen_img.get_frame()
        screen_img.find_source(manual=False)
        screen_img.find_destination(manual=False)
        screen_img.get_keypoints_on_edges_img()
        screen_img.update_frame_with_src_and_dest()
        screen_img.display_frame()

        # convert pixel distance to percentage
        frame_height, frame_width, _ = frame.shape
        x1, y1, x2, y2 = convert_pixel_to_percent_position(
            screen_img.x_src,
            screen_img.y_src,
            screen_img.x_dest,
            screen_img.y_dest,
            frame_height,
            frame_width,
        )

        # calculate the distance between the two marks
        distance_between_marks = get_euclidean_distance(x1, y1, x2, y2)
        print(f"Distance: {distance_between_marks}")

        # convert the distance to seconds
        push_duration = get_push_duration_from_distance(distance_between_marks)
        print(f"Servo Push: {push_duration} seconds.")

        # perform movement on the servo
        servo.move_servo(push_duration)
        time.sleep(3)


if __name__ == "__main__":
    main()
