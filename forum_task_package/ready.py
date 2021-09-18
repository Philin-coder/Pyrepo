def comparer(mstr, mstr1):
    step = len(mstr1)
    for i in range(len(mstr) - step + 1):
        if mstr1 == mstr[i:i + step]:
            print('ёсть')


if __name__ == '__main__':
    comparer(mstr=input(), mstr1=input())
