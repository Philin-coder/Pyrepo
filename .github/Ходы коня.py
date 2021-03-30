a, n, m = [], int(input()) - 1, int(input()) - 1
for i in range(8):
    a.append(['.'] * 8)
a[n][m] = 'K'
for i in range(1, 9):
    if i == 1 and m + 2 <= 7 and n - 1 >= 0:
        a[n - 1][m + 2] = '*'
    elif i == 2 and m + 2 <= 7 and n + 1 <= 7:
        a[n + 1][m + 2] = '*'
    elif i == 3 and n + 2 <= 7 and m + 1 <= 7:
        a[n + 2][m + 1] = '*'
    elif i == 4 and n + 2 <= 7 and m - 1 >= 0:
        a[n + 2][m - 1] = '*'
    elif i == 5 and m - 2 >= 0 and n + 1 < 7:
        a[n + 1][m - 2] = '*'
    elif i == 6 and m - 2 >= 0 and n - 1 >= 0:
        a[n - 1][m - 2] = '*'
    elif i == 7 and m - 1 >= 0 and n - 2 >= 0:
        a[n - 2][m - 1] = '*'
    elif i == 8 and n - 2 >= 0 and m + 1 <= 7:
        a[n - 2][m + 1] = '*'
for i in range(8):
    print(' '.join(a[i]))
