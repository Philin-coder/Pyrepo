import numpy
import random


def masscreate(n, m):
    x = numpy.random.randint(100, size=(n, m))
    print(x * 0.1)


if __name__ == '__main__':
    masscreate(n=int(input()), m=int(input()))
