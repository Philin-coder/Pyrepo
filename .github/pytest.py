def goldbach(n):
    d = 2
    while d*d <= n and n % d != 0:
        d += 1
    return d*d > n


n = int(input())
if n == 4:
    print(2, 2)
else:
    d = 3
while not(goldbach(d) or not goldbach(n-d)):
    d += 1
print(n-d)
