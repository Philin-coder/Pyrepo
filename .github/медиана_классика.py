b=int(input())            
a=list(map(int,input().split()))
for elem in a:
    count=0
    for x in a:
        if x<elem:
            count+=1
    if count==len(a)//2:
        print(elem)
        break