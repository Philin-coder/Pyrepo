k = a.count(0)
for i in range(k - 1):
    a[a.index(0)] = ''

print(sum(a[a.index(0):]))
