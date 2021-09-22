n = 52
for i in range(n):
    x = int(i ** .5 + .5)
    k = x + 1 - abs(i - 1 - x ** 2)
    print('* ' * k)
