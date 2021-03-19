import re


def cleaner(mstr):
    res = re.sub(r'([а-яa-z])\1(?=\1)', '', mstr)
    print(res)
    return res


if __name__ == '__main__':
    mstr = input()
    cleaner(mstr)
