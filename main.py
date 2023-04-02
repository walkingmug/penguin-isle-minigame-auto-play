from python.image_input.get_image_from_software import get_image_from_software
from python.image_input.get_markings import get_markings
from python.distance_calculator.calculate_distance import get_distance_in_pixels
from python.distance_calculator.convert_distance import get_push_duration_from_distance
from python.arduino_serial_operations.serial_operations import Serial
from python.arduino_serial_operations.serial_operations import ArduinoSerial


def main() -> None:
    # save a screenshot image from a given software
    # get_image_from_software("Zoom - Google Chrome")

    # set the marks by clicking on the image
    x1, y1, x2, y2 = get_markings()

    # calculate the distance between the two marks
    distance_between_marks = get_distance_in_pixels(x1, y1, x2, y2)

    # convert the distance to seconds
    push_duration = get_push_duration_from_distance(distance_between_marks)

    # perform movement on the servo
    servo = ArduinoSerial()
    servo.move_servo(push_duration)

if __name__=="__main__":
    main()