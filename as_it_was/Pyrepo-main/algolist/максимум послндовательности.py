a = [4, 8, 2]
mx = a[0]
for i in range(len(a)):
    if mx < a[i]:
        mx = a[i]
id = a.index(mx)
b = [mx]
del a[id]
c = b + a
print(c)
