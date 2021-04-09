import random 
def middle(n):
    cnt=0
    mlist=[random.randint(-50,50 ) for i in range(n)]
    print(*mlist)
    min_ind=mlist.index(min(mlist))
    max_ind=mlist.index(max(mlist))
    
    if max_ind<min_ind:
        min_ind,max_ind=max_ind,min_ind
    for i  in range(min_ind+1, max_ind):
        if mlist[i]>0:
            cnt+=1
    print(cnt)


if __name__ == '__main__':
    middle(n=5)
    