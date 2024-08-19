def f(n, x, y):
    if n > 0:

        if n == 1:
            print(n, x, y)
        else:
            f(n - 1, x, y)
            f(n - 2, y, 6 - x - y)
            print(0, x, y)
            f(n - 2, 6 - x - y, x)
            f(n - 1, x, y)


print(f(n=int(input()), x=1, y=3))
