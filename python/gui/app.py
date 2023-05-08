import tkinter as tk
from PIL import Image, ImageTk


class ImageDisplayGUI:
    def __init__(self, image_path='python/gui/resources/images/no_image_available.png'):
        self.root = tk.Tk()
        self.root.title("Jump Jump Auto Player")
        self.image_path = image_path

        self.current_image = Image.open(self.image_path)
        self.photo = ImageTk.PhotoImage(self.current_image)

        self.canvas = tk.Canvas(
            self.root, width=self.current_image.width, height=self.current_image.height)
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

        self.root.mainloop()
a = ImageDisplayGUI()