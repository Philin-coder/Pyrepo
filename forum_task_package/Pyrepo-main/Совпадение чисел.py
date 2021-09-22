def task(a, b, c):
    k = 4 - len(set([a, b, c]))
    if k == 1:
        k = 0
    print(k)
    return k


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())
    task(a, b, c)
