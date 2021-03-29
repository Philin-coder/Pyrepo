
def biner(m, n):
    for i in range(m, n+1):
        print(i, ' ', f'{i:b}')


if __name__ == '__main__':
    m = int(input())
    n = int(input())
    biner(m, n)
