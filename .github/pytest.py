def masgen(n):

    mlist=list(map(int, input().split()[:n]))
    print(max(enumerate(mlist), key=lambda x: abs(x[1]))[0])

if __name__ == '__main__':
    masgen(n=5)
    
    