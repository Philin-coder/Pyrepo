want = input("Какую операцию необходимо провести (+,-,/,*) :")
a = float(input('Введите первое число :'))
b = float(input("Введите второе число :"))
if want == '+':
    c = a + b
    print(c)
elif want == '-':
    c = a - b
    print(c)
elif want == '/':
    c = a / b
    print(c)
elif want == '*':
    c = a * b
    print(c)
print('Подсчет выполнен!')
