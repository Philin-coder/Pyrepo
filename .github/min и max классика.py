import random
n = 5
mlist = [random.randint(-19, 10) for i in range(n)]
print(mlist)
m = mlist[0]
mn = mlist[0]
for i in mlist:
    if i > m:
        m = i
    if i < mn:
        mn = i
print(m)
print(mn)
