import roman


def numer(mstr):
    res = roman.fromRoman(mstr)
    print(res)
    return res


if __name__ == '__main__':
    mstr = input()
    numer(mstr)
