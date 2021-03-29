from random import randint
from functools import reduce
 
def transp(arr):
    return list(map(lambda *x : x,*arr))
 
def task(arr):
    tarr=transp(arr)
    return reduce(lambda acc,x: x*acc,list(map(min,tarr)))
    
arr=[[randint(2,22) for _ in range(10)] for _ in range(10)]
 
print(task(arr))