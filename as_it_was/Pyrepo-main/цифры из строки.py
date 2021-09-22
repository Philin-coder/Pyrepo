def deldigit(mstr, mstr1):
    for i in mstr:
        if i not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
            mstr1 = mstr1 + i
    print(mstr1)


if __name__ == '__main__':
    mstr = input()
    mstr1 = ''
    deldigit(mstr, mstr1)
