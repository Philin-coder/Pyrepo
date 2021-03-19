import re


def reg(mstr):
    res = re.sub(r'[^\w\s]', '', mstr)
    print(res)
    return res


if __name__ == '__main__':
    mstr = input()

    reg(mstr)
