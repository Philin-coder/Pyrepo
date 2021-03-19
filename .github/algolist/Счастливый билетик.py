def happy(s):
    if sum([int(char) for char in s[:3]]) == sum([int(char) for char in s[-3:]]):
        print("Счастливый")
    else:
        print("Обычный")


if __name__ == '__main__':
    s = input()
    happy(s)
