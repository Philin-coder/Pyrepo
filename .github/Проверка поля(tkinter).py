import tkinter
from tkinter import *
from tkinter import messagebox


def test():
    if fameo_entry.get().endswith('й'):
        messagebox.showinfo("заканчивается")

    else:
        messagebox.showinfo('не заканчивается')


root = Tk()
root.title('Test')
root.geometry('300x256')
fameo = StringVar()
nameo = StringVar()
famr = StringVar()
namer = StringVar()
otchr = StringVar()
fameo_label = Label(text="введите фамилию  отца")
nameo_label = Label(text="введите имя   отца")
famr_label = Label(text="введите фамилию  ребенка")
namer_label = Label(text="введите имя  ребенка")
otchr_label = Label(text="введите отчество  ребенка")

fameo_label.grid(row=0, column=0)
nameo_label.grid(row=1, column=0)
famr_label.grid(row=2, column=0)
namer_label.grid(row=3, column=0)
otchr_label.grid(row=4, column=0)

fameo_entry = Entry(textvariable=fameo)
nameo_entry = Entry(textvariable=nameo)
famr_entry = Entry(textvariable=famr)
namer_entry = Entry(textvariable=namer)
otchr_entry = Entry(textvariable=otchr)

fameo_entry.grid(row=0, column=1, padx=5, pady=5)
nameo_entry.grid(row=1, column=1, padx=5, pady=5)
famr_entry.grid(row=2, column=1, padx=5, pady=5)
namer_entry.grid(row=3, column=1, padx=5, pady=5)
otchr_entry.grid(row=4, column=1, padx=5, pady=5)
test_button = Button(text="click me", command=test)
test_button.grid(row=5, column=1)

root.mainloop()
