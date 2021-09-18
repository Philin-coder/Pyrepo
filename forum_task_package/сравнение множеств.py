def setgen(mstr, mstr1):
    mset = set(mstr)
    mset1 = set(mstr1)
    print(mset)
    print(mset1)
    print(mset.issubset(mset1))
    print(mset == mset1)


if __name__ == '__main__':
    print(setgen(mstr=input(), mstr1=input()))
