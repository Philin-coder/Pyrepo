print("enter number of columns")
a = int(input())
print("enter number of rows")
b = int(input())
m = []
for i in range(a):
    if i == 0:
        m.append(1)
    else:
        m.append(0)
n = []
for i in range(b):
    n.append(m)
for i in range(b):
    print(*n[i])
    print()
