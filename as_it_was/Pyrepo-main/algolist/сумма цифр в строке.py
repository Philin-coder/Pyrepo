def digitfinder(mstr):
    for i in mstr:
        if i.isdigit():
            mlist.append(i)
    for i in mlist:
        i = int(i)
        mlist1.append(i)
    print(mlist1)
    print(sum(mlist1))
    return sum(mlist1)


if __name__ == '__main__':
    mlist = []
    mlist1 = []
    mstr = input()
    digitfinder(mstr)
