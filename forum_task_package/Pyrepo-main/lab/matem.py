import math


def schet(x, y, z, t):
    y = 5 * math.atan(x) - (1 / 4) * math.acos(x) * ((x + 3) - math.fabs(x - y) + (x * x)) / (
            math.fabs(x - y) * z + (x * x))  # продсчет
    print(y)  # печать
    return y  # возврат


if __name__ == '__main__':
    x = 0.1722  # параметы
    y = 6.33  # параметы
    z = 3.5 ** (10 ** (-4))  # параметы
    t = -172.025  # параметы
    schet(x, y, z, t)  # функция
