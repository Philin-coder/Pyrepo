def euler(n):
    res = n
    for i in range(2, n):
        i * i
        if n % i == 0:
            while (n % i == 0):
                n /= i
                res -= res / i
            print(res)
    if (n > 1):
        res -= res / n
    print(res)
    return res


if __name__ == '__main__':
    n = int(input())
    euler(n)
