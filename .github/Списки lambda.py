import random
 
 
def list_with_random_numbers(n: int) -> list:
    mlist = list(random.randint(1, 10) for i in range(n))
    return mlist
 
 
def generate_list_with_squared_numbers(mlist: list) -> list:
    return (list(map(lambda x: x**2, [int(input()) for _ in range(int(input()))])))
 
 
if __name__ == '__main__':
    print(list_with_random_numbers(n := int(input())))
    print(generate_list_with_squared_numbers(list_with_random_numbers(n=5)))