from tkinter import *
from PIL import Image, ImageTk
from time import sleep


class MyApp(Frame):
    root = Tk()
    root.geometry("640x480")

    img = Image.open("1.jpg")
    render = ImageTk.PhotoImage(img)
    root.title("test")
    init_l = Label(root, image=render)
    init_l.image = render
    init_l.pack()
    root.mainloop()
    sleep(3)
    root.quit()
    run = MyApp()
