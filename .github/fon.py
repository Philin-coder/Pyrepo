import tkinter as tk
from PIL import ImageTk, Image


def show_image(path):
    root = tk.Tk()
    img = Image.open(path)
    width = 500
    ratio = (width / float(img.size[0]))
    height = int((float(img.size[1]) * float(ratio)))
    imag = img.resize((width, height), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(imag)
    panel = tk.Label(root, image=image)
    panel.pack(side="top", fill="both", expand="no")

    tk.Button(root, text='Quit', command=root.quit).place(x=250, y=250)

    root.mainloop()


show_image('D:/_Qt/img/cat.jpg')
