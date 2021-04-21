n=int(input())
k=0
for i in range(2,n):
    if n%i==0:
        k+=1
print(k)