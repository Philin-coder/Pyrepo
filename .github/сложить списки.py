import random


def summmer(n):
    mlist = list(random.randint(1, 10) for i in range(n))
    mlist1 = list(random.randint(1, 10) for i in range(n))
    return list(i+j for i, j in zip(mlist, mlist1))


if __name__ == '__main__':
    print(summmer(n=5))
