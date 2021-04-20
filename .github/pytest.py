def test(mstr):
    for i in mstr:
        if i.isdigit():
            mlist.append(i)
    print(*mlist)


if __name__ == '__main__':
    mlist = []
    test(mstr='Андрей Петров 14.06.1996 Москва')
