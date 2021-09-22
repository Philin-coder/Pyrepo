import numpy
import random


def teat(n):
    res = numpy.array([random.random() for i in range(n)])
    print(res)


if __name__ == '__main__':
    n = int(input())
    teat(n)
