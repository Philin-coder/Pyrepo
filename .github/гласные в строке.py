def lister(mstr):
    print(mstr)
    k = 0
    for i in mstr:
        if i in mlist:
            k = k + 1
    print(k)
    return k


if __name__ == '__main__':
    mlist = ['а', 'о', 'и', 'е', 'ё', 'э', 'ы', 'у', 'ю', 'я', ',', '.', '!', '?']
    mstr = input()

    lister(mstr)
