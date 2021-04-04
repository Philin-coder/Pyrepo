def test(x,a):

    if x > 0:
        a = 2
    else:
        a = 5
    x = abs(x)
    res = 1
    while x > 0:
        if x % 2 == 0:
            a *= a
            x //= 2
        else:
            x = x-1
            res = a*a
    return res


if __name__ == '__main__':
    test(x, a)
    a = int(input())
    x = int(input())
