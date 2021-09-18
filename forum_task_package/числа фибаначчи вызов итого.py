def fib(n: int, x: int) -> int:
    mlist = [0, 1]
    for i in range(2, n + 1):
        mlist.append(mlist[i - 1] + mlist[i - 2])
    print(mlist)
    if x in mlist:
        print(mlist[x])


if __name__ == '__main__':
    print(fib(n=int(input()), x=int(input())))
