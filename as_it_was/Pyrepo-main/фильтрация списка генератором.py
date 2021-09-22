import random


def filt(n):
    mlist = [random.randint(1, 10) for i in range(n)]
    print(*mlist)
    print([i for i in mlist if i > 5])
    return mlist


if __name__ == '__main__':
    assert filt(n=12)
