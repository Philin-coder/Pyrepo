def Combin1 (N, K):
    num = 0
    if K == 0 or K == N:
        C = 1
        print(C)
    else:
        C = Combin1(N-1, K)+Combin1(N-1, K-1)
        num += 1

 
if __name__ == '__main__':
    N = int(input("N= "))
    K = int(input("K= "))
    Combin1 (N, K)