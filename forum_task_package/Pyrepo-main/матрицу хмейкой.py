n, m = map(int, input().split())
a = []
w = -1
a2 = []
for i in range(n):
    a1 = []
    for j in range(m):
        w = w + 1
        a1.append(w)

    if i % 2 == 1:
        a1.reverse()
        a.append(a1)
    else:
        a.append(a1)

for i in a:
    for j in range(m):
        print('{:<3d}'.format(i[j]), end='')
    print()