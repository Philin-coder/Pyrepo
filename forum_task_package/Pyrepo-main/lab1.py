# 1) Даны целые числа pq a1 … a67 ( p>q≥0 ) . В последовательности a1 … a67 заменить нулями члены, модуль которых при делении на p дает в остатке q
# проверка -12, 2,0

import random


def randomer(n: int, p: int, q: int) -> list:
    mlist = [random.randint(1, 67) for i in range(n)]
    print(mlist)
    for i in range(len(mlist)):
        if mlist[i] % p == q:
            mlist1.append(i)
    print(mlist1)


if __name__ == '__main__':
    mlist1 = []
    n = int(input())
    p = int(input())
    q = int(input())
    randomer(n, p, q)
