import math
import pylab
import matplotlib.pyplot as plt


# подгрузили библиотечки

def U(x, y):  # моя функция
    return x ** 3 * y ** 3


def F(x, y):  # её вторая производная
    return 6 * x * y ** 3 + 6 * y * x ** 3


# сетка 1х1, по х= 0..1, по y= 0..1
x = 0.0
y = 0.0
N = 30
h = 1 / (N + 1)  # шаг
i = 0  # счётчик просто
F = -400.0  # посчитала это число как в документе, непонятно, почему оно такое, но так работает
xlist = []  # списки проинициализировала
ylist = []
u_i_j = (1 / h ** 2 * (U(x + h, y) + U(x - h, y)) + 1 / h ** 2 * (U(x, y - h) + U(x, y + h)) - F) / (
        4 / h ** 2)  # стартовое значение проинициализировала, формула #из документа
y_list = []

while i < N:
    xlist.append(x)  # записываем значения
    ylist.append(u_i_j)
    y_list.append(U(x, y))
    i += 1
    x = i * h
    y = x  # п.ч. у меня i=j (см. документ)
    u_i_j = (1 / h ** 2 * (U(x + h, y) + U(x - h, y)) + 1 / h ** 2 * (U(x, y - h) + U(x, y + h)) - F) / (
            4 / h ** 2)  # тупо обновляем значение каждый шаг
print('it is okey')  # просто проверка выхода из цикла

# типа построили
pylab.plot(xlist, ylist)
pylab.plot(xlist, y_list)
pylab.show()
