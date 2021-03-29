n = int(input("n="))
res = []
for i in range(2**n):
    s = ""
    for j in range(n):
        s = str(i % 2)+s
        i = i//2
    res.append(s)
print(res)
