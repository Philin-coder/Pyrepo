import math


def tabul():
    dx = 2.0
    x = -dx
    while x <= 30 and x > 0:
        x = x + dx
        y = x ** 2 + 3
        print(y)


if __name__ == '__main__':
    tabul()
