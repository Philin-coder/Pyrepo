import random


def randomizer(n):
    mlist = [random.randint(-10, 10) for i in range(n)]
    print(mlist)


if __name__ == '__main__':
    n = int(input())
    randomizer(n)
