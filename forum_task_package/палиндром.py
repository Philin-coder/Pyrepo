def pal(data):
    l = len(data)
    for i in range(l // 2):
        if data[i] != data[-i - i]:
            print("it is not pal")
            quit()
    else:
        print("it is pal")


if __name__ == '__main__':
    pal(data=input())
