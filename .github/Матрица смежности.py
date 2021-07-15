from functools import reduce
 
def graph(elist):
    n=reduce(lambda acc,edge : max(acc,max(edge[0],edge[1])),elist,0)
    matr=[[0 for _ in range(1,n+1)] for _ in range(1,n+1)]
    for (v1,v2) in elist:
        matr[v1-1][v2-1]=1
        matr[v2-1][v1-1]=1
    return matr    
        
def task(matr):
    
    n=len(matr)
    
    # Печать матрицы смежности
    
    print("матрица смежности:")
    for row in matr:
        print(*row)
 
    # Есть ли вершины, не смежные с другими
    
    i_list=[]
    for i,row in enumerate(matr):
        if sum(row)-row[i]==0:
            i_list.append(i+1)
    if len(i_list)==0:
        print("изолированных вершин нет")
    else:
        print("номера изолированных вершин:")
        for i in i_list:
            print(i,end=' ')
        print()    
 
    # Номера смежных вершин
    
    for i in range(n):
        i_list=[]
        for j in range(n):
            if matr[i][j]!=0:
                i_list.append(j+1)
        print("Вершина",(i+1),"смежные:",*i_list)        
 
task(graph([(1,2),(1,3),(2,4),(2,7),(2,2),(3,6),(5,5)])    )