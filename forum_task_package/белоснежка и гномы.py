n = int(input())
k, c = 0, 0
# Создание списка из списков [i, a, b, x]]
res = [[i, x, y, x + y] for i, x, y in
       zip(range(1, n + 1), list(map(int, input().split())), list(map(int, input().split())))]
# Сортировка пo "х" = a[i] + b[i] - по [3]-м
res.sort(key=lambda x: x[3], reverse=True)
for i in range(n - 1, -1, -1):
    # Проверка b[i] > sum(a[i+1:n]) - [2]-е > sum[[1]-e]
    d = res[i][2] - c
    c += res[i][1]
    if d <= 0:
        res = [[-1, 0]]
        break
# Печать индексов гномов - [0]-е элементы списков
print(' '.join([str(x[0]) for x in res]))
