def move(n, a, b):
    if n == 1:
        print(n, a, b)
    else:
        move(n - 1, a, b)
        print(n, a, 6 - a - b)
        move(n - 1, b, a)
        print(n, 6 - a - b, b)
        move(n - 1, a, b)


if __name__ == '__main__':
    move(n=int(input()), a=1, b=3)
