#TODO: and me
def foo(f, h, v):
    nn = range(len(f))
    if h - 2 in nn and v + 1 in nn:
        f[h - 2][v + 1] = 1
    if h - 2 in nn and v - 1 in nn:
        f[h - 2][v - 1] = 1
    if h - 1 in nn and v - 2 in nn:
        f[h - 1][v - 2] = 1
    if h + 1 in nn and v - 2 in nn:
        f[h + 1][v - 2] = 1
    if h + 2 in nn and v - 1 in nn:
        f[h + 2][v - 1] = 1
    if h + 2 in nn and v + 1 in nn:
        f[h + 2][v + 1] = 1
    if h - 1 in nn and v + 2 in nn:
        f[h - 1][v + 2] = 1
    if h + 1 in nn and v + 2 in nn:
        f[h + 1][v + 2] = 1


n = int(input('Field size: '))
m = int(input('Horses amount: '))
field = [[0] * n for i in range(n)]
for i in range(m):
    x = int(input(f'x{i}: '))
    y = int(input(f'y{i}: '))
    field[x][y] = 1
    foo(field, x, y)

print(n * n - sum([sum(row) for row in field]))
