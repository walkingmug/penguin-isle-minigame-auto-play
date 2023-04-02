from penguin_isle_minigame_auto_play.image_input.get_image_from_software import get_image_from_software
from penguin_isle_minigame_auto_play.image_input.get_markings import get_markings
from penguin_isle_minigame_auto_play.distance_calculator.calculate_distance import get_distance_in_pixels


def main() -> None:
    # save a screenshot image from a given software
    get_image_from_software("Zoom - Google Chrome")

    # set the marks by clicking on the saved image
    x1, y1, x2, y2 = get_markings()

    # calculate the distance between the two marks
    distance = get_distance_in_pixels(x1, y1, x2, y2)


if __name__=="__main__":
    main()