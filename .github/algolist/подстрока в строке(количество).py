def counter(mystring, mysubstr):
    res = mystring.count(mysubstr)
    print(res)
    return res


if __name__ == '__main__':
    mystring = input()
    mysubstr = input()
    counter(mystring, mysubstr)
