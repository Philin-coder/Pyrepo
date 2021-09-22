import random


def listgen(n):
    mlist = [random.randint(-10, 10) for i in range(n)]
    print(mlist)
    print(mlist[n // 2:])
    print(mlist[:n // 2])


if __name__ == '__main__':
    n = int(input())
    listgen(n)
