def finder(mstr: str) -> str:
    print(mstr)
    for i in range(len(mstr)):
        if not '*' in mstr:
            res = mstr
            print(res)
            return res
    else:
        ind = mstr.find('*')
        ind = int(ind) + 1
        print(ind)
        res = (mstr[:ind - 1])
        print(res)
        for i in res:
            if (ord(i) >= 97) and (ord(i) <= 122) or ((ord(i) >= 41) and (ord(i) <= 90)):
                res = res.replace(i, '.')
        print(res)
        return res


if __name__ == '__main__':
    mstr = input()
    finder(mstr)
