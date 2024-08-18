def matrixer(n: int) -> list:
    mlist = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i < j:
                mlist[i][j] = 0
            elif i > j:
                mlist[i][j] = 2
            else:
                mlist[i][j] = 1
    for row in mlist:
        print(' '.join([str(elem) for elem in row]))


if __name__ == '__main__':
    matrixer(n=int(input()))
