import random
from functools import reduce


def multer(n):
    mlist = [random.randint(1, 10) for i in range(n)]
    print(*mlist)
    res1 = reduce(lambda res, i: res * i, mlist, 1)
    print(res1)


if __name__ == '__main__':
    multer(n=int(input()))
