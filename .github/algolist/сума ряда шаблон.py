# S = a/1 + a/2 + a/3 + ... a/n
a = int(input('a = '))
n = int(input('n = '))

# цикл for
S = 0
for i in range(1, n + 1):
    S += a / i
print(S)

# цикл while
S = 0
i = 1
while i <= n:
    S += a / i
    i += 1
print(S)

# цикл repeat-until
S = 0
i = 1
while True:
    S += a / i
    i += 1
    if i > n:
        break
print(S)
