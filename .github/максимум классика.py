import random
n = 25
mlist = [random.randint(-19, 10) for i in range(n)]
print(mlist)
m = mlist[0]
for i in mlist:
    if i > 0 and i % 5 == 0:
        if i > m:
            m = i
print(m)
