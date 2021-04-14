
def pr(a, b, c,p, q, r):
    if (a/b==p/q):
        print("Прямые параллельны\n")
    if (a/b!=p/q): 
        print("Прямые пересекаются\n")
    if (a/p==b/q==c/r):
        print("Прямые совпадают\n")
    
    

if __name__ == '__main__':
    a, b, c,p, q, r=float(input())
    pr(a, b, c,p, q, r)

     
    