import random


def medfinder(n):
    mlist = [random.randint(-10, 10) for i in range(n)]
    print(mlist)
    strlst = sorted(mlist)
    # print(strlst)
    lstlen = len(mlist)
    index = (lstlen - 1) // 2
    if lstlen % 2 == 0:
        res = strlst[index]
        print(res)
        return res
    else:
        res = (strlst[index] + strlst[index + 1]) / 2.0
        print(res)
        return res


if __name__ == '__main__':
    n = int(input())
    medfinder(n)
