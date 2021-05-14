N, b = map(int, input().split())
a = []
for i in range(N):
    a.append(int(input())
 
for i in range(N-1):
    for j in range(N-1):
        if a[j] > a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
    
 
print(a[b])