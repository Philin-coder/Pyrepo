import random


def masgen(n):
    mlist = [random.randint(1, 10) for i in range(n)]
    print(mlist)
    for i in mlist:
        print(mlist.index(i))


if __name__ == '__main__':
    n = int(input())
    masgen(n)
