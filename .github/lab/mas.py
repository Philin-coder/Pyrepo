def masgen():
    p = 0  # пзначение для среднего
    mlist = [i for i in range(36)]  # получаем генератором 35 чисел
    print(mlist)  # выводим список
    for j in mlist:  # пока чсло в списке
        if j > 3.5:  # проверяем условие
            p = sum(mlist) / len(mlist)  # если подходит, считаем средне
    print(p)  # выводим


if __name__ == '__main__':
    masgen()
