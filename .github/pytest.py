import random


def zapis(my_filename, fext2):
    n = 8
    mlist = list(random.randint(1, 100) for i in range(n))

    with open(my_filename + '.' + fext2, 'w', encoding='utf-8') as fp:
        print(mlist, file=fp, sep="\n")
        return mlist


def reader(my_filename, fext2):
    with open(my_filename + '.' + fext2, 'r', encoding='utf-8') as fp:
        data = fp.readlines()
    print(data)
    s = 0
    for i in data:
        i=int(i)
        s+=i
    print(s)


if __name__ == '__main__':
    my_filename = None
    fex2 = None
    zapis(my_filename='test', fext2='txt')
    reader(my_filename='test', fext2='txt')
