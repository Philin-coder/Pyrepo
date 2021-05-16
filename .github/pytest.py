import itertools
import random
from functools import reduce


def magen(n):
    mlist = list(random.randint(1, 10) for i in range(n))
    print(*mlist)
    print([i for i in mlist if i % 2 != 0])
    print(reduce((lambda x, y: x*y), [i for i in mlist if i % 2 != 0]))


if __name__ == '__main__':
    magen(n=4)
