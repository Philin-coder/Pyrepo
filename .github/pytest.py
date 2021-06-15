

def masgen() -> list:
    mlist = list(range(0, 49))
    print(mlist)
    for j, i in enumerate(mlist):
        if i < 15:
            mlist[j] = -1
    print(mlist)


if __name__ == '__main__':
    print(masgen())
