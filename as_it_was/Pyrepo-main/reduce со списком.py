import random
from functools import reduce


def masgen(n):
    mlist = [random.randint(1, 10) for i in range(n)]
    print(*mlist)
    res1 = reduce(lambda res, i: [i] + res, [1, 2, 3, 4], [])
    print(res1)


if __name__ == '__main__':
    masgen(n=12)
