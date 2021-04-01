#является ли сумма 2 значной
def findnum(x):
    s = 0
    while(x != 0):
        s = s+(x % 10)
        x = x//10
    print(s)
    if s in range(10, 100):
        print('является')
    else:
        print('нет')


if __name__ == '__main__':
    x = int(input())
    findnum(x)
