def massgen():
    mlist = list(map(int, input().split()))
    print(*mlist)
    k = 1
    for i in range(0, len(mlist)-1):
        if mlist[i] != mlist[i+1]:
            k += 1
    print(k)


if __name__ == '__main__':
    massgen()
