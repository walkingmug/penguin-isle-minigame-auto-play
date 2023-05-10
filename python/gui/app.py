import tkinter as tk
import numpy as np
from PIL import Image, ImageTk
from cv2 import imread, imshow
from threading import Thread

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300
DEFAULT_IMG_PATH = "python/gui/resources/images/no_image_available.png"


class ImageDisplayGUI:
    def __init__(self, image_path=DEFAULT_IMG_PATH):
        self.root = tk.Tk()
        self.root.title("Jump Jump Auto Player")
        self.image_path = image_path
        self.radiobutton_choice = tk.IntVar()

        self._add_auto_radiobutton()
        self._add_manual_radiobutton()

        self.canvas = tk.Canvas(
            self.root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
        self.canvas.pack()

        self.current_image = Image.open(self.image_path)
        self.photo = ImageTk.PhotoImage(self.current_image)
        self.image_on_canvas = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

        # self.root.update_idletasks()
        # self.root.update()
        self.root.mainloop()
    
    def run(self, img: np.array):
        thread_1 = Thread(target=self.set_image(img))
        thread_1.start()

    def set_corr_image(self, pth = "C:/Vullnet/Side Projects/python/PenguinIsle minigame auto-play/penguin-isle-minigame-auto-play/temp/screenshots/crop_of_relevant_area.jpg"):
        img = Image.open(pth)
        img = ImageTk.PhotoImage(img)
        self.canvas.itemconfig(self.image_on_canvas, image=img)

    def set_image(self, img: np.array):
        #Rearrang the color channel
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(img)
        self.canvas.itemconfig(self.image_on_canvas, image=img)

        self.root.after(10000, self.set_image)

    def read_image(self, img_path: str):
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


# import time
# import cv2
# a = ImageDisplayGUI()
# time.sleep(3)
# pth = "C:/Vullnet/Side Projects/python/PenguinIsle minigame auto-play/penguin-isle-minigame-auto-play/temp/screenshots/crop_of_relevant_area.jpg"
# img = a.read_image(pth)
# a.set_corr_image(pth)
# time.sleep(3)

# a = imread("C:/Vullnet/Side Projects/python/PenguinIsle minigame auto-play/penguin-isle-minigame-auto-play/temp/screenshots/crop_of_relevant_area.jpg")
# imshow("a",a)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
