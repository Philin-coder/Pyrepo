import fnmatch


def matcher(f):
    for i in range(5):
        if fnmatch.fnmatch(f):
            mlist.append('YES')
        else:
            mlist.append('NO')
        return '\n'.join(mlist)


if __name__ == '__main__':
    mlist = []
    f = input()
    n = input()
    print(matcher(f='*.py'))
