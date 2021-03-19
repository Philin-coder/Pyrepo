import re


def finder(sym, mstr):
    print(re.subn(sym, sym, mstr))


if __name__ == '__main__':
    finder(sym=input(), mstr=input())
