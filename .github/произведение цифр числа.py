def findnum(x):
    p = 1
    while(x != 0):
        p = p*(x % 10)
        x = x//10
    print(p)
    if x > p:
        print('больше')
    if x < p:
        print('меньше')


if __name__ == '__main__':
    x = int(input())
    findnum(x)
