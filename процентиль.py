import random


def porc(mlist, P):
    mlist = sorted(mlist)
    n = int(round(P * len(mlist) + 0.5))
    return mlist[n - 1]


if __name__ == '__main__':
    mlist = [random.randint(1, 10) for i in range(10)]
    P = random.uniform(0, 1)
    porc(mlist, P)
    print(porc(mlist, P))
