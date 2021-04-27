
a = int(input("первая точка "))
b = int(input("вторая точка "))
while True:
    x = int(input("ввод x "))
    y = int(input("ввод y "))
    if y == a*x+b:
        print('точка лежит на прямой')
    else:
        print('Нэт')
