# Дано K наборов ненулевых целых чисел. Признаком завершения каждого набора является число 0. Вычислить среднее арифметическое всех элементов во всех наборах.
def nabor(k):
    print(k)
    for i in range(k):
        print("nabor", i)
        s = 0
        n = 0
        a = int(input())
        while a != 0:
            s += a
            n = n + 1
            a = int(input())

    if (n != 0):
        print(s / n)
    else:
        print("нельзя делитьь на 0")


if __name__ == '__main__':
    k = int(input())
    nabor(k)
