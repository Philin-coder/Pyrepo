def chet(a):
    for i in range(a):
        if i % 2 != 0:
            mlist.append(i)
    print(mlist)
    with open(my_filename + '.' + fext2, 'w', encoding='utf-8') as fp:
        print(mlist, file=fp, sep="\n")
        fp.close()
    return mlist


if __name__ == '__main__':
    my_filename = input('файл')
    fext2 = '.txt'
    mlist = []
    a = int(input())
    chet(a)
