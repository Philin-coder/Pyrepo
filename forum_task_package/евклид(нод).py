def gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    print(a)


if __name__ == '__main__':
    gcd(a=int(input()), b=int(input()))
