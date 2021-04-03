import random


def masgen(n):
    mlist = [random.randint(1, 10)  for i in range(n)]
    
    print(sum([i for i in mlist if i%3==0]))


if __name__ == '__main__':

    masgen(n=14)
