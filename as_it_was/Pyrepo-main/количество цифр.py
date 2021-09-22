def coonter(n):
    n = abs(n)

    count = 1
    n //= 10

    while n > 0:
        n //= 10
        count += 1
    print(count)


if __name__ == '__main__':
    n = int(input())
    coonter(n)
