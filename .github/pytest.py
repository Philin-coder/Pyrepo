import re


def finddash(mstr):
    print(mstr)
    res = re.findall(r'-(\w+)-', mstr)
    print(res)
    return res


if __name__ == '__main__':
    mstr = input()
    finddash(mstr)
