import random


def masgen(n):
    for i in range(2, 10):
        mlist.append(i)
    print(mlist)
    for i in mlist:
        if (min(mlist) % 2 == 0):
            print(min(mlist))
        elif print("нету")


if __name__ == '__main__':
    n = int(input())
    mlist = []
    masgen(n)
