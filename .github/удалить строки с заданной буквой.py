def foo(lst: list, mchar:chr) -> list:
    return list(filter(lambda x: mchar not in x, lst))
if __name__ == '__main__':
    print(foo(lst=list(), mchar=chr(input())))
    
    