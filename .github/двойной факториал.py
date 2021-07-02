def double_fact(n):
    p=1
    while(n>=1):
        p=p*n
        n-=2
    return p
    
print(double_fact(7))