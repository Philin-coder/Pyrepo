def counter(n):
    s = 0
    end = False
    while not end:
        s += n % 10
        n = n // 10
        if n == 0:
            if s < 10:
                end = True
            else:
                n = s
                s = 0

    print(s)


if __name__ == '__main__':
    n = int(input())
    counter(n)
