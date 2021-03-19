# 2)Выяснить, имеется ли среди S1 … Sn пара соседствующих букв но или он.
def finder(mstr: str) -> bool:
    print(mstr)
    if ('НО' in mstr) or ('ОН' in mstr):
        res = True
        print(res)
    else:
        res = False
        print(res)
    return res


if __name__ == '__main__':
    mstr = input()
    finder(mstr)
