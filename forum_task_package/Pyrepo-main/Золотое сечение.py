def golden_ratio(i):
    a, b = 0, 1
    n = 1
    while n <= i:
        a, b = b, a + b
        n += 1
        if n == i - 1:
            b1 = b
    return (b1 / b)


print(golden_ratio(int(input())))
