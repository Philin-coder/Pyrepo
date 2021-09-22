# сумма чисел кратных 5 и не делящихся на 9
def func(n):
    for i in range(n):
        if n > 99:
            if i % 3 == 0 and i % 10 != 0:
                mlist.append(i)
            res = sum(mlist)
    print(res)
    return res


if __name__ == '__main__':
    n = int(input())
    mlist = []
    func(n)
