def task(a, b, c):
    k = 4 - len(set([a, b, c]))
    if k == 1:
        k = 0
    return k


if __name__ == '__main__':
    print(task(a=int(input()), b=int(input()), c=int(input())))
