import tkinter as tk
import numpy as np
from PIL import Image, ImageTk


CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300
NO_IMAGE_FOUND_PATH = 'python/gui/resources/images/no_image_available.png'


class ImageDisplayGUI:
    def __init__(self, image_path=NO_IMAGE_FOUND_PATH):
        self.root = tk.Tk()
        self.root.title("Jump Jump Auto Player")
        self.image_path = image_path

        self.current_image = Image.open(self.image_path)
        self.photo = ImageTk.PhotoImage(self.current_image)

        self.canvas = tk.Canvas(
            self.root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

        self.root.mainloop()

    def set_image(self, image: np.array):



a = ImageDisplayGUI()
