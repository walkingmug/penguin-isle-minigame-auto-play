from python.image_input.get_image_from_software import get_image_from_software
from python.image_input.get_markings import get_markings
from python.distance_calculator.calculate_distance import get_distance_in_pixels
from python.distance_calculator.convert_distance import get_push_duration_from_distance
from python.arduino_serial_operations.serial_operations import ArduinoSerial
from python.image_processing.source_detection import get_center_of_source_iceberg
from python.image_processing.destination_detection import get_center_of_destination_iceberg


def main() -> None:
    while True:
        choice = input('Press Q to Quit:')
        if choice == "Q" or choice == "q":
            break
        # save a screenshot image from a given software
        # get_image_from_software("Zoom - Google Chrome")

        # automatically detect source and destination on image
        # if it cannot be detected, manually ask the user to input them
        x1, y1 = get_center_of_source_iceberg()
        x2, y2 = get_center_of_destination_iceberg()

        # calculate the distance between the two marks
        distance_between_marks = get_distance_in_pixels(x1, y1, x2, y2)

        # convert the distance to seconds
        push_duration = get_push_duration_from_distance(distance_between_marks)
        print(push_duration)

        # perform movement on the servo
        # servo = ArduinoSerial()
        # servo.move_servo(push_duration)


if __name__=="__main__":
    main()