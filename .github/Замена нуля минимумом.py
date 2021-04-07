
import random


def exchengge(n):
    mlist = [random.randint(-10, 0) for i in range(n)]
    print(*mlist)
    for i in mlist:
        if i == 0:
            mlist[mlist.index(i)] = min(mlist)
    print(*mlist)


if __name__ == '__main__':
    exchengge(n=5)
