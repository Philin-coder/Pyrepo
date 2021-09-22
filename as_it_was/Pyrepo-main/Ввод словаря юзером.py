def dictgen():
    mdict = dict([input('введите ключ и значение через пробел').split() for i in range(3)])
    print(mdict)
    mlist.append(mdict)
    print(mlist)


if __name__ == '__main__':
    mlist = []
    dictgen()
