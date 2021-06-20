nm = input().split()  
n = int(nm[0])
m = int(nm[1])
max_i = 0
max_j = 0
a = [[int(j) for j in input().split()] for i in range(n)]
for i in range(0, n): # n=3 ----- 0,1,2
    for j in range(0, m): # m=4 ----0,1,2,3
        if a[i][j] > a[max_i][max_j]:
            max_i = i
            max_j = j
print(max_i, max_j)