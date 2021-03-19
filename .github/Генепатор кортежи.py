import random


def t_check(n):
    mt = tuple(random.randint(-10, 10) for i in range(n))
    print(mt)
    mt1 = (mt[0], mt[1], mt[-3])
    print(mt1)
    return mt1


if __name__ == '__main__':
    n = int(input())
    t_check(n)
