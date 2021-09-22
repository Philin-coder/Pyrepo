import random


def avg(n):
    mlist = [random.randint(-10, 10) for i in range(n)]
    print(mlist)
    print(sum(mlist) / len(mlist))


if __name__ == '__main__':
    n = int(input())
    avg(n)
