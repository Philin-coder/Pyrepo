f = int(input('введите номер квартиры '))  # кол-во квартир
v = int(input('введите кол-во подъездов '))  # кол-во подъездов
b = int(input('введите кол-во этажей '))  # кол-во этажей
n = int(input('введите кол-во квартир на этаже '))  # кол-во квартир на этаже
c = b * n  # кол-во квартир в подъезде
x = f // c
y = (x + 1)  # узнаём в каком подъезде квартира
z = f % c
d = z // n
s = (d + 1)  # узнаём на каком этаже
print(str(y) + ' подъезд')
print(str(s) + ' этаж')
