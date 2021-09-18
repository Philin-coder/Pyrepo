import random


def masgen(n):
    mlist = [random.randint(1, 10) for i in range(n)]
    print(*mlist)
    mlist1 = [random.randint(1, 10) for i in range(n)]
    print(mlist1)
    mtotal = [i + j for i, j in zip(mlist, mlist1)] + (mlist if len(mlist) >= len(mlist1) else b)[
                                                      min(len(mlist), len(mlist1)):]
    return mtotal


if __name__ == '__main__':
    print(masgen(n=int(input())))
