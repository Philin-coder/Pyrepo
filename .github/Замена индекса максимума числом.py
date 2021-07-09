n = 5
mylist = list(map(int, input().split()[:n]))
print(*mylist)
mylist[mylist.index(max(mylist))] = 1000
print(mylist)
