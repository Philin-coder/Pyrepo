import random  # импорт нужной библиотеки


def masgen(n):
    mlist = [random.randint(-10, 10) for i in range(n)]  # генератором, получаем список
    print(mlist)  # выводим
    res = min(mlist)  # находим, так как есть встроенные a-ции
    print(res)  # печатаем
    return res  # возвращаем


if __name__ == '__main__':  # точка входа
    n = int(input())  # число элементов списка
    masgen(n)  # ф-ци обработки
