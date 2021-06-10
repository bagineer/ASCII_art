from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import os


class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("ASCII art")
        self.geometry("{}x{}".format(640, 480))
        self.resizable(False, False)
        self.grid_columnconfigure(0, weight=1)
        # self.grid_rowconfigure(0, weight=1)
        # self.grid
        self.img_label = None
        self.img = None
        self.IMAGE_SIZE = 400
        self.initialize()

    def initialize(self):
        btn_frame = Frame(self, background="red")
        btn_frame.grid(row=0, column=0, sticky="NSEW")

        sel_btn = Button(btn_frame, text="Select", command=self.select_file)
        sel_btn.grid(row=0, column=0)

        res_btn = Button(btn_frame, text="Result")
        res_btn.grid(row=0, column=1)

        img_frame = Frame(self, background="yellow")
        img_frame.grid(row=1, column=0, sticky="NSEW")

        self.img_label = Label(img_frame, width=self.IMAGE_SIZE, height=self.IMAGE_SIZE)
        self.img_label.pack()

    def select_file(self):
        img_name = filedialog.askopenfilename(initialdir="./images",
                                              title="Select Image File",
                                              filetypes=(("image files", "*.jpg *.png"),
                                                         ("all files", "*.*")))
        if img_name:
            img = Image.open(img_name, mode="r")

            if img.size[0] > img.size[1]:
                width = self.IMAGE_SIZE
                height = int(img.size[1] * self.IMAGE_SIZE / img.size[0])
            else:
                width = int(img.size[0] * self.IMAGE_SIZE / img.size[1])
                height = self.IMAGE_SIZE

            img = img.resize((width, height), Image.ANTIALIAS)
            self.img = ImageTk.PhotoImage(img)
            self.img_label.config(image=self.img)


if __name__ == "__main__":
    app = App()
    app.mainloop()
