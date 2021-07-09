from tkinter import *
from tkinter import messagebox
import os
import matplotlib.pyplot as plt
from PIL import Image
from PIL import ImageTk
from PIL import ImageGrab
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfile

class Paint(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        print(parent)
        self.parent = parent
        self.color = "black"
        self.brush_size = 2

        self.setUI()

    def set_color(self, new_color):
        self.color = new_color

    def set_brush_size(self, new_size):
        self.brush_size = new_size

    def draw(self, event):
        self.canv.create_oval(event.x - self.brush_size,
                                event.y - self.brush_size,
                                event.x + self.brush_size,
                                event.y + self.brush_size,
                                fill=self.color, outline=self.color)

    def setUI(self):
        self.pack(fill=BOTH, expand=1)
        # Размещаем активные элементы на родительском окне

        self.columnconfigure(6, weight=1)
        # Даем седьмому столбцу возможность растягиваться, благодаря
        # чему кнопки не будут разъезжаться при ресайзе

        self.rowconfigure(2, weight=1)
        # То же самое для третьего ряда

        self.canv = Canvas(self, bg='white')
        # Создаем поле для рисования, устанавливаем белый фон

        self.canv.grid(row=2, column=0, columnspan=7, padx=5, pady=5, sticky=E + W + S + N)
        # Прикрепляем канвас методом grid. Он будет находится в 3м ряду, первой колонке,
        # и будет занимать 7 колонок, задаем отступы по X и Y в 5 пикселей, и заставляем
        # растягиваться при растягивании всего окна

        self.canv.bind("<B1-Motion>", self.draw)
        # Привязываем обработчик к канвасу. <B1-Motion> означает "при движении
        # зажатой левой кнопки мыши" вызывать функцию draw

        color_lab = Label(self, text="Цвет кисти: ")
        # Создаем метку для кнопок изменения цвета кисти

        color_lab.grid(row=0, column=0, padx=6)
        # Устанавливаем созданную метку в первый ряд и
        # первую колонку, задаем горизонтальный отступ в 6 пикселей

        red_btn = Button(self, text="Красный", width=8,command=lambda: self.set_color("red"))
        # Создание кнопки:  Установка текста кнопки, задание ширины
        # кнопки (10 символов), функция вызываемая при нажатии кнопки.

        red_btn.grid(row=0, column=1)
        # Устанавливаем кнопку

        # Создание остальных кнопок повторяет ту же логику, что и создание
        # кнопки установки красного цвета, отличаются лишь аргументы.

        green_btn = Button(self, text="Зеленый", width=8, command=lambda: self.set_color("green"))
        green_btn.grid(row=0, column=2)

        blue_btn = Button(self, text="Синий", width=8, command=lambda: self.set_color("blue"))
        blue_btn.grid(row=0, column=3)

        black_btn = Button(self, text="Чёрный", width=8, command=lambda: self.set_color("black"))
        black_btn.grid(row=0, column=4)

        white_btn = Button(self, text="Белый", width=8, command=lambda: self.set_color("white"))
        white_btn.grid(row=0, column=5)

        clear_btn = Button(self, text="Очистить", width=8, command=lambda: self.canv.delete("all"))
        clear_btn.grid(row=0, column=6, sticky=W)

        size_lab = Label(self, text="Размер кисти: ")
        size_lab.grid(row=1, column=0, padx=5)

        one_btn = Button(self, text="2", width=8, command=lambda: self.set_brush_size(2))
        one_btn.grid(row=1, column=1)

        two_btn = Button(self, text="5", width=8, command=lambda: self.set_brush_size(5))
        two_btn.grid(row=1, column=2)

        five_btn = Button(self, text="7", width=8, command=lambda: self.set_brush_size(7))
        five_btn.grid(row=1, column=3)

        seven_btn = Button(self, text="10", width=8, command=lambda: self.set_brush_size(10))
        seven_btn.grid(row=1, column=4)

        ten_btn = Button(self, text="20", width=8, command=lambda: self.set_brush_size(20))
        ten_btn.grid(row=1, column=5)

        twenty_btn = Button(self, text="50", width=8, command=lambda: self.set_brush_size(50))
        twenty_btn.grid(row=1, column=6, sticky=W)

def importImage():
    global paint

    fname = askopenfilename(filetypes=[("Изображения", "*.jpeg;*.jpg;*.png;*.gif")])

    if fname is not None:
        try:
           img = ImageTk.PhotoImage(Image.open(fname))
           paint.canv.background = img
           paint.canv.create_image(0, 0, anchor=NW, image=img)
        except Exception as err:
            messagebox.showerror("Ошибка загрузки файла", err)


def saveImg():
    global paint

    fname = asksaveasfile(mode='w', defaultextension=".jpg", filetypes=[("JPEG", ".jpg")])
    if fname is None:
        return

    x = paint.canv.winfo_rootx() + 2
    y = paint.canv.winfo_rooty() + 2
    xx = x + paint.canv.winfo_width() - 4
    yy = y + paint.canv.winfo_height() - 4
    ImageGrab.grab(bbox=(x, y, xx, yy)).save(fname)


def main():
    global paint

    root = Tk()
    root.title('Programm')
    root.geometry("850x650+250+50")
    # Создание окна, смена его названия, размера и положения

    mainmenu = Menu(root)
    root.config(menu=mainmenu)

    filemenu = Menu(mainmenu, tearoff=0)
    filemenu.add_command(label="Очистить холст", command=lambda: paint.canv.delete("all"))
    filemenu.add_command(label="Импорт", command=importImage)
    filemenu.add_command(label="Сохранить нарисованное", command=saveImg)
    filemenu.add_command(label="Выход", command=root.quit)

    helpmenu = Menu(mainmenu, tearoff=0)
    helpmenu.add_command(label="Помощь")
    helpmenu.add_command(label="О программе")

    mainmenu.add_cascade(label="Файл", menu=filemenu)
    mainmenu.add_cascade(label="Справка", menu=helpmenu)
    # Добавление меню и его дальнейшее наполнение с подменю

    paint = Paint(root)
    # Функция, открывающая возможность рисовать

    root.mainloop()


if __name__ == '__main__':
    main()