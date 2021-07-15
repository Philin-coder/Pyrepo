N = int(input("Введите N: "))
st = [' '] * N
for i in range(N):
    st[N-1-i] = i+1
    print(*st)
    
for i in range(N):
    st[i] = ' '
    print(*st)