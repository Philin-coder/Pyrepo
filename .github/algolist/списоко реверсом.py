def masgen(n) -> list:
    mlist = [i for i in range(n + 1)]
    print(mlist)
    res = mlist[::-1]
    print(res)
    return res


if __name__ == '__main__':
    n = int(input())
    masgen(n)
