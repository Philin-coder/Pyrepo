def finder(mstr, n):
    print(mstr)
    res = mstr.split()
    indlist = [res.index(i) for i in res]
    print(indlist)
    for i in indlist:
        if i == n:
            res[i] = str(res[i])
            print(res[i])
            print(res[i][::-1])


if __name__ == '__main__':
    mstr = input()
    n = int(input())
    finder(mstr, n)
