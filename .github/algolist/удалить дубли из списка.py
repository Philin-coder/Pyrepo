def deleter():
    mlist = [50, '0032', 17, 25, 765, 217, 25, 217, 17]
    mlist = [i for i in mlist if mlist.count(i) == 1]
    print(mlist)


if __name__ == '__main__':
    deleter()
