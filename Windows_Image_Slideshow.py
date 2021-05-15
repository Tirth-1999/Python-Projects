import time
from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()


class Slider:
    def __init__(self, root):
        self.root = root
        self.root.title("SLIDER")
        self.root.iconbitmap(
            r"C:\Users\Chandrika Jaikishan\Desktop\TIRTH\DATA SCIENCE\python samples\calculator-icon_34473.ico")
        self.root.geometry("300x300+-7+0")

        self.img1 = ImageTk.PhotoImage(
            Image.open(r"C:\Users\Chandrika Jaikishan\Desktop\TIRTH\DATA SCIENCE\python samples\photos\img.jpg"))
        self.img2 = ImageTk.PhotoImage(
            Image.open(r"C:\Users\Chandrika Jaikishan\Desktop\TIRTH\DATA SCIENCE\python samples\photos\img1.jpg"))
        self.img3 = ImageTk.PhotoImage(Image.open(r"./photos/img2.jpg"))
        self.img4 = ImageTk.PhotoImage(Image.open(r"./photos/img3.jpg"))
        self.img_list = [self.img1, self.img2, self.img3, self.img4]
        self.frame = LabelFrame(self.root)
        self.frame.place(x=25, y=25, width=250, height=250)
        self.Lbl = Label(self.frame, image=self.img_list[0], bd=0)
        self.Lbl.place(x=-2, y=-2)
        self.Lbl2 = Label(self.frame, image=self.img_list[1], bd=0)
        self.Lbl2.place(x=250, y=-2)
        self.x = 250
        self.slid()

    def slid(self):
        count = 0
        if self.x != 0:
            self.x -= 1
        count += 1
        if self.x == 0:
            time.sleep(1)
            self.x = 250
            self.Lbl.config(image=self.img_list[count])
            self.Lbl2.config(image=self.img_list[count + 1])
            self.Lbl2.place(x=self.x - 2, y=-2)
            self.Lbl2.after(10, self.slid)

        obj = Slider(root)
        root.mainloop()
