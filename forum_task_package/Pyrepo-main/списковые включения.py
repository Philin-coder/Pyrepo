import random


def lister(n):
    mlist = [random.randint(1, 100) for i in range(n)]
    print(mlist)
    mlist = [random.randint(1, 100) if i % 2 == 0 else i + 1 for i in range(n)]
    print(*mlist)


if __name__ == '__main__':
    lister(n=12)
