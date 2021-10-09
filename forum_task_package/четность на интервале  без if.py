def chet(a, b):
    for i in range(a, b + 1):
        print(i, ' ', i & 1 != 1)


if __name__ == '__main__':
    print(chet(a=int(input()), b=int(input())))
