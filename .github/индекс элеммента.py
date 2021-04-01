
def findind(n):
    mlist = list(map(int, input().split()))
    print(mlist)
    for i in mlist:
        if i == n:
            print(mlist.index(i))


if __name__ == '__main__':
    n = int(input())
    findind(n)
