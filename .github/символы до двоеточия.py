def stringer(mstr: str) -> str:
    print(mstr)
    ind = mstr.find(':')
    res = mstr[:ind]
    print(res)
    return res


if __name__ == '__main__':
    mstr = input()
    stringer(mstr)
