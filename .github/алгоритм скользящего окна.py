a = [1, 2, 34, 3, 45, 67, 28, 2, 44, 9, 19, 123, 134, 6, 7, 23, 4, 43]
t = 80
s = k = kmax = 0
res = []
for i in range(len(a)):
    if s + a[i] < t:
        k += 1
    else:
        s -= a[i-k]
    s += a[i]
    if k >= kmax:
        if k > kmax:
            res = []
        kmax = k
        if s < t:
            res.append(i+1)
print(*[a[i-kmax:i] for i in res], sep='\n')
