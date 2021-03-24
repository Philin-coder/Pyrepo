from statistics import median
import random


def findmed(n):
    mlist = [random.randint(1, 10) for i in range(n)]
    print(*mlist)
    print(median(mlist))


if __name__ == '__main__':
    findmed(n=5)
