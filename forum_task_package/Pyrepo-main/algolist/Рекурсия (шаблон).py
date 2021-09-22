def proc():
    x = int(input())
    if x != 0:
        proc()
        print(x)


proc()
