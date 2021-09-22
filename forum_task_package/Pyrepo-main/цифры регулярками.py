import re


def stringer(mstr):
    print(mstr)
    mlist = [re.findall(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?', mstr)]
    print(*mlist)


if __name__ == '__main__':
    # mstr=input()
    stringer(mstr='1.152000000000D+05-1.303851604462D-07-5.331575505977D-01-3.986060619354D+07')
