def num_div(n):
    r = 2
    i = 2
    while (i * i <= n):
        if n % i == 0:
            r += 1
        if n // i != i:
            r += 1
        i += 1
    return r


def task(a, b):
    xmax = 0
    dmax = 0
    x = b
    while (x >= a):
        nd = num_div(x)
        if nd > dmax:
            dmax = nd
            xmax = x
        x -= 1
    return xmax


[a, b] = map(int, input().split(' '))
print(task(a, b))
