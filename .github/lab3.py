# 3) Дано натуральное число n. Можно ли представить его в виде суммы трех квадратов натуральных чисел? Если можно, то
# a. указать тройку xyz таких натуральных чисел, что n= x2 + y2 + z2 ;
# b. указать все тройки xyz таких натуральных чисел, что n= x2 + y2 + z2 .
import math


def checker(n: float) -> list:
    print(n)
    sn = round(math.sqrt(n))
    for i in range(sn):
        for j in range(sn):
            for k in range(sn):
                s = i * i + j * j + k * k
                if s == n:
                    print(s)
                if n == i + j + k:
                    mlist.append(n)
                elif n == j + k:
                    mlist.append(mlist2)
    print(mlist1)
    print(mlist2)


if __name__ == '__main__':
    mlist = []
    mlist1 = []
    mlist2 = []
    n = float(input())
    checker(n)
