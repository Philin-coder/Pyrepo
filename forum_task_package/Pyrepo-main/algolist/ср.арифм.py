import random


def filegen(fname):
    mlist = [random.randint(-10, 10) * 0.1 for i in range(10)]

    with open(fname + '.' + fext2, 'w', encoding='utf-8') as fp:
        print(mlist, file=fp, sep="\n")
    print(mlist)
    for i in mlist:
        if i > 0:
            mlist1.append(i)
    l = 1 / len(
        mlist1)  # сложный корень, это , как правидл число в степени, равной 1/n. где n - показатель корня, то есть - для куюа будет 3
    print(l)
    for i in mlist:
        i = i * i  # перемножаем числа списка
        i ** l
    sg = i ** l  # возводим

    print(sg)


if __name__ == '__main__':
    fext2 = 'txt'
    mlist1 = []
    filegen(fname='проба')
