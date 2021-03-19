import random


def masgen(n):
    mlist = [random.randint(-10, 10) for i in range(n)]
    ind = mlist.index(max(mlist))
    mlist = sorted(mlist[:ind]) + mlist[ind:]
    print(mlist)
    return mlist


if __name__ == '__main__':
    n = int(input())
    masgen(n)
