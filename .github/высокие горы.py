n = int(input())
sp = list(map(int, input().split()))
 
q = int(input())
for i in range(q):
    k, x = map(int, input().split())
    for j in range(k):
        sp[n - j - 1] += x
print(*sp)