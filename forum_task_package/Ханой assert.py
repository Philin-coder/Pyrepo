def move(n, start, finish):
    if n == 1:
        print("Перенести диск 1 со стержня", start, "на стержень", finish)
    else:
        temp = (6 - start) - finish
        move(n - 1, start, temp)
        print("Перенести диск", n, "со стержня", start, "на стержень", finish)
        res = (n - 1, temp, finish)

        return res


if __name__ == '__main__':
    assert move(10, 1, 3)
    print(move(10, 1, 3))
