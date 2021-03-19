def isprime(n):
    mlist = []
    for i in range(n + 1):
        mlist.append(i)
    mlist[1] = 0
    i = 2
    while i <= n:
        if mlist[i] != 0:
            j = i + i
            while j <= n:
                mlist[j] = 0
                j = j + i
        i += 1
    mlist = set(mlist)
    mlist.remove(0)
    print(*mlist)


if __name__ == '__main__':
    n = int(input())
    isprime(n)
