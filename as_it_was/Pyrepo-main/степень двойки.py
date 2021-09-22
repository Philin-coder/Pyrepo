def check2rec(num):
    if num == 1:
        res = True
        print(res)
        return res
    if num & 1:
        res = False
        print(res)
        return res
    return check2rec(num >> 1)


if __name__ == '__main__':
    num = int(input())
    check2rec(num)
