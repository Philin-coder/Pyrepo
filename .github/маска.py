import fnmatch


def matcher(f, n):
    for i in range(5):
        if fnmatch.fnmatch(f, n):
            mlist.append('YES')
        else:
            mlist.append('NO')
        print('\n'.join(mlist))


if __name__ == '__main__':
    mlist = []
    f = input()
    m = input()
