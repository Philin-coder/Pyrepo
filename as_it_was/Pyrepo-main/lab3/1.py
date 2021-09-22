# Вывести
# на
# экран
# таблицу
# кубических
# корней
# первых
# десяти
# целых
# положительных
# чисел.

import random


def sq(n):
    mlist = [random.randint(1, 40) for i in range(n)]
    print(mlist)
    mlist1 = [mlist[i] ** (1 / 3) for i in range(n)]
    print(mlist1)


if __name__ == '__main__':
    n = int(input())
    sq(n)
