def dlin(mstr):
    dx = [(len(x), x) for x in mstr.split()]
    dx = dict(dx)
    print(dx)
    print(max(dx), dx[max(dx)])


if __name__ == '__main__':
    mstr = input()
    dlin(mstr)
