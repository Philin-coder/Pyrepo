def fibonacci(max):  # генератор (а не функция, т.к. оператор return заменён на yield)
    a, b = 0, 1
    while a < max:
        yield a  # return a, + запоминаем место рестарта для следующего вызова
        a, b = b, a + b  # параллельное присваивание, которое выполняется одновременно и параллельно


mlist = []
mlist1 = []
for n in fibonacci(4000000):  # используем генератор fibonacci() как итератор
    # print(n)  # печатаем все числа Фибоначчи меньшие 100 через пробел

    mlist.append(n)
print(mlist)
for i in mlist:
    if i % 2 == 0 and i < 4000000:
        mlist1.append(i)

print(sum(mlist1))
