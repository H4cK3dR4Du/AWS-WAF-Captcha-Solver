import os
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import shutil

class Yes:
    def __init__(self, root):
        self.root = root
        self.root.title("Image organizer by h4ck3dr4du")
        self.root.geometry("700x400")

        self.image_dir = 'images/'
        self.output_dir = 'dataset/'
        self.classes = ["Bed", "Bucket", "Chair", "Clock", "Hat", "Bag", "Curtain"]

        self.current_image_index = 0
        self.images = self.load_images()

        self.image_label = ttk.Label(root)
        self.image_label.pack(pady=10)

        self.class_buttons = []
        for idx, class_name in enumerate(self.classes):
            button = ttk.Button(root, text=class_name, command=lambda class_name=class_name: self.save_image(class_name))
            button.pack(side=tk.LEFT, padx=10, pady=10)
            self.class_buttons.append(button)

        self.show_image()

    def load_images(self):
        image_files = os.listdir(self.image_dir)
        return [os.path.join(self.image_dir, img) for img in image_files]

    def show_image(self):
        if self.current_image_index < len(self.images):
            img_path = self.images[self.current_image_index]
            img = Image.open(img_path)
            img = img.resize((400, 300))
            img = ImageTk.PhotoImage(img)
            self.image_label.configure(image=img)
            self.image_label.image = img
        else:
            messagebox.showinfo("Info", "No more images...")
            self.root.destroy()

    def save_image(self, class_name):
        img_path = self.images[self.current_image_index]
        filename = os.path.basename(img_path)
        output_class_dir = os.path.join(self.output_dir, class_name)

        os.makedirs(output_class_dir, exist_ok=True)
        shutil.copy(img_path, os.path.join(output_class_dir, filename))

        os.remove(img_path)

        self.current_image_index += 1
        self.show_image()

if __name__ == "__main__":
    root = tk.Tk()
    app = Yes(root)
    root.mainloop()
