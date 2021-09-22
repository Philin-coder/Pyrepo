import math


def tabul():
    dx = 0.1
    x = -dx
    while x <= 2:
        x = x + dx
        y = x ** 4
        print(y)


if __name__ == '__main__':
    tabul()
