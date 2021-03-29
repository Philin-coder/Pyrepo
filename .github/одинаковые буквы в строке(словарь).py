
def findletter(mstr):
    mdict = dict.fromkeys(mstr, 0)
    for i in mstr:
        mdict[i] += 1
    print(mdict)


if __name__ == '__main__':
    findletter(mstr='мир')
