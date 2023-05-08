import tkinter as tk
from PIL import Image, ImageTk    


class ImageDisplayGUI:
    def __init__(self, image_path='resources/images/no_image_available.png'):
        self.root = tk.Tk()
        self.root.title("Jump Jump Auto Player")
        self.current_image = image_path