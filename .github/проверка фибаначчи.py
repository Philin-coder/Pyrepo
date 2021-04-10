def fibtest(n):
    if n == 1:
        print('true')
    else:
        a = 1
        b = 1
        c = 0
        while c < n:
            c = a+b
            a = b
            b = c
        if c == n:
            print('true')
        else:
            print('false')


if __name__ == '__main__':
    fibtest(n=5)
