import random


def massgen(n):
    mlist = [random.randint(0, 100) for i in range(n)]
    print(mlist)
    print(max(mlist))
    print(mlist.index(max(mlist)))


if __name__ == '__main__':
    n = int(input())
    massgen(n)
