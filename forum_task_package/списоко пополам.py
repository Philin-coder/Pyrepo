import random


def listgen(n):
    mlist = [random.randint(-10, 10) for i in range(n)]

    if n % 2 != 0:
        print('местами не меняем')
    else:
        # print(mlist)
        return mlist[n // 2:] + mlist[0:n // 2]


if __name__ == '__main__':
    print(listgen(n=int(input())))
