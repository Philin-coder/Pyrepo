import random
 
 
def test(n: int) -> list:
 
    mlist = list(random.randint(1, 10) for i in range(n))
 
    return mlist
 
 
if __name__ == '__main__':
    print(test(n=int(input())))
