def masgen(a, b, step):
    mlist = [i for i in range(a, b, step)]
    print(*mlist)


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    step = int(input())
    masgen(a, b, step)
