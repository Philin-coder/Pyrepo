import math


def difur(a, e):
    v = 0
    v = ((1 + e * math.cos(v)) ** 2) / ((1 - (e ** 2)) ** (3 / 2)) * (math.sqrt(f * m) / a ** 3)
    print(v)


if __name__ == '__main__':
    f = 6.672 * 10 ** -12
    m = 5.9737 * 10 ** 24
    a = float(input())
    e = float(input())
    difur(a, e)
