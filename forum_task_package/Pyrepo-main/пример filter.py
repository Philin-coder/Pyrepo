import random


def filt(n):
    mlist = [random.randint(1, 10) for i in range(n)]
    print(*mlist)
    print(list(filter(lambda i: i > 5, mlist)))


if __name__ == '__main__':
    filt(n=12)
