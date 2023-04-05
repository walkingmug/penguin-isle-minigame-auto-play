from PIL import Image


def open_image(img='temp\screenshots\screenshot.png'):
    return Image.open(img)

def crop_image(img):
    