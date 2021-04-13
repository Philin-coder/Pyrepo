import random
def masgen(n):
    mlist=list(random.randint(1, 50) for i in range(n))
    print(*mlist)
    p=1
    for i in mlist[mlist.index(max(mlist,key=abs))+1:]:
        p*=i
    print(p)
 
 
if __name__ == '__main__':
    
    masgen(n=5
