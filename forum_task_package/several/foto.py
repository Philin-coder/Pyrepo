from tkinter import *
import socket
import os
from PIL import Image, ImageTk
from time import sleep
import pygame


class App(Frame):
    root = Tk()
    root.geometry("640x480")

    img = Image.open("1.jpg")
    render = ImageTk.PhotoImage(img)
    root.title("test")
    initil = Label(root, image=render)
    initil.image = render
    initil.pack()
    root.mainloop()
    sleep(3)
    root.quit()
    run = App()
