def isPrime(n):
    if n==1:
        return False
    k=2
    while(n>=k*k):
        if n%k==0:
            return False
        k+=1    
    return True
    
def sort_prime(arr):
    p=[]
    s=[]
    for a in arr:
        if isPrime(a):
            p.append(a)
        else:
            s.append(a)
    return p+s
    
print(sort_prime([3,4,7,8,9,1,2,12,11]))