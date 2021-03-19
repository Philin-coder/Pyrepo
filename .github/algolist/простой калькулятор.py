def counter(a, b, c, res):
    print("что делаем?")
    if c == '+':
        res = a + b

        print(res)
        return res
    elif c == '-':
        res = a - b
        print(res)
        return res
    elif c == '*':
        res = a * b
        print(res)
        return res
    elif c == '/':
        res = a / b
        print(res)
        return res


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = input()
    res = 0
    counter(a, b, c, res)
