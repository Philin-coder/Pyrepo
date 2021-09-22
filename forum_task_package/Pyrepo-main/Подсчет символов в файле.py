def zapis(my_filename, fext2):
    with open(my_filename + '.' + fext2, 'w', encoding='utf-8') as fp:
        print('проба', file=fp, sep="\n")


def reader(my_filename, fext2, ch):
    k = 0
    with open(my_filename + '.' + fext2, 'r', encoding='utf-8') as fp:
        data = fp.readlines()
    print(data)
    for i in ''.join(data):
        if i.lower() == ch:
            k += 1
    print(k)


if __name__ == '__main__':
    my_filename = None
    fex2 = None
    ch = None
    zapis(my_filename='проба', fext2='txt')
    reader(my_filename='проба', fext2='txt', ch='а')
