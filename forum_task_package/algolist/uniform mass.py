import random


def masgen(n):
    mlist = [random.uniform(1, 10) for _ in range(n)]
    for i in mlist:
        mlist1.append(i - (sum(mlist) / len(mlist)))
    print(mlist1)


if __name__ == '__main__':
    mlist1 = []
    n = int(input())
    masgen(n)
