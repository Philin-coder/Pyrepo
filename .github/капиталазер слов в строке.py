def capitalizer():
    mlist = list(map(str, input().split()))
    for i in mlist:
        i = str(i)
        i = i.capitalize()
        print(i)


if __name__ == '__main__':

    capitalizer()
