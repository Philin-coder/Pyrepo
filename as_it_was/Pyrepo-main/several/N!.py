n = 10
s = 0
j = 1
for i in range(1, n + 1):
    j *= i
    print(j)  # просто так)))
    s += 1 / j
print('Sum: ', s)
