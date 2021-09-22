def IsPrime(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    res = d * d > n
    print(res)
    return res


if __name__ == '__main__':
    n = int(input())
    IsPrime(n)
