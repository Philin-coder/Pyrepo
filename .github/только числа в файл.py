def stringer(mstr: str) -> str:
    print(mstr)
    res = ''.join(i for i in mstr if not i.isdigit())
    print(res)
    with open('проба' + '.' + 'txt', 'w', encoding='utf-8') as fp:
        print(res, file=fp, sep="\n")
    return res


if __name__ == '__main__':
    mstr = input()
    stringer(mstr)
