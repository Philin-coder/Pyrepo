def collect(vvod):
    print(vvod)
    sp = vvod.split()
    for i in sp:
        if i not in mlist:
            mlist.append(i)
    print((mlist))
    return mlist


if __name__ == '__main__':
    mlist = []
    vvod = str(input())
    collect(vvod)
