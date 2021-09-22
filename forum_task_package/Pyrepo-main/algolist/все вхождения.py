def changer(mstring, msubstr, msubstr2):
    print(mstring)
    print(msubstr)
    print(msubstr2)
    mstring = mstring.replace(msubstr, msubstr2)
    print(mstring)


if __name__ == '__main__':
    mstring = input("строку ")
    msubstr = input("что менять")
    msubstr2 = input("на что")
    changer(mstring, msubstr, msubstr2)
