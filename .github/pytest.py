import random


def massgen(n):
    mlist = [random.randint(1, 10) for i in range(n)]
    print(*mlist)

if __name__ == '__main__':
    massgen(n=7)
