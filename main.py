from python.image_input.get_image_from_software import get_image_from_software
from python.image_input.get_markings import get_markings
from python.distance_calculator.calculate_distance import get_distance_in_pixels
from python.distance_calculator.convert_distance import get_push_duration_from_distance
from python.arduino_serial_operations.serial_operations import ArduinoSerial
from python.image_processing.object_detection.source_detection import get_center_of_source_iceberg
from python.image_processing.object_detection.destination_detection import get_center_of_destination_iceberg
from python.image_input.screenshot_frame import ScreenshotFrame
from python.gui.app import ImageDisplayGUI
import time

def main() -> None:
    screen_img = ScreenshotFrame()
    # gui = ImageDisplayGUI()

    # perform image processing and update frames
    while True:
        # save a screenshot image from a given software
        get_image_from_software("Zoom - Google Chrome")

        # automatically detect source and destination on image
        # if it cannot be detected, manually ask the user to input them
        screen_img.get_screen_img()
        screen_img.find_source()
        screen_img.find_destination()
        screen_img.update_frame_with_src_and_dest()
        screen_img.display_frame()

        # display image on GUI
        # current_frame = screen_img.get_frame()
        # gui.set_image(current_frame)
        # gui.root.update_idletasks()
        # gui.root.update()
        
        # calculate the distance between the two marks
        x1, y1 = screen_img.x_src, screen_img.y_src
        x2, y2 = screen_img.x_dest, screen_img.y_dest
        distance_between_marks = get_distance_in_pixels(x1, y1, x2, y2)

        # convert the distance to seconds
        push_duration = get_push_duration_from_distance(distance_between_marks)
        print(push_duration)

        # perform movement on the servo
        servo = ArduinoSerial()
        servo.move_servo(push_duration)
        time.sleep(3)


if __name__=="__main__":
    main()