import tkinter as tk
import numpy as np
from PIL import Image, ImageTk
from cv2 import imread

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300
NO_IMAGE_FOUND_PATH = "python/gui/resources/images/no_image_available.png"


class ImageDisplayGUI:
    def __init__(self, image_path=NO_IMAGE_FOUND_PATH):
        self.root = tk.Tk()
        self.root.title("Jump Jump Auto Player")
        self.image_path = image_path
        self.radiobutton_choice = tk.IntVar()

        self._add_auto_radiobutton()
        self._add_manual_radiobutton()

        self.current_image = Image.open(self.image_path)
        self.photo = ImageTk.PhotoImage(self.current_image)

        self.canvas = tk.Canvas(
            self.root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
        self.canvas.pack()
        self.set_image(self.photo)
        self.root.mainloop()

    def set_image(self, img: np.array):
        self.canvas.create_image(0, 0, anchor=tk.NW, image=img)

    def get_image(self, img_path: str):
        return imread(img_path)

    def _add_auto_radiobutton(self):
        auto_radiobutton = tk.Radiobutton(
            self.root, text="Auto", variable=self.radiobutton_choice, value=1)
        auto_radiobutton.pack(side="right", anchor=tk.N)

    def _add_manual_radiobutton(self):
        manual_radiobutton = tk.Radiobutton(
            self.root, text="Manual", variable=self.radiobutton_choice, value=2)
        manual_radiobutton.pack(side="right", anchor=tk.N)

    def get_radiobutton_choice(self):
        return self.radiobutton_choice


a = ImageDisplayGUI()
