def summ_of_devizions(x):
    mlist = [i for i in range(1, x + 1) if x % 2 == 0]
    print(mlist)
    print(sum(mlist))


if __name__ == '__main__':
    x = int(input())
    summ_of_devizions(x)
