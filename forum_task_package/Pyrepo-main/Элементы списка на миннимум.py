import random


def massgen(n):
    mlist = [random.randint(1, 10) for i in range(n)]
    print(*mlist)
    minim = min(mlist)
    print(minim)
    for i in range(1, len(mlist)):
        mlist[i] = minim, mlist[i]
    print(*mlist)


if __name__ == '__main__':
    n = int(input())
    massgen(n)
