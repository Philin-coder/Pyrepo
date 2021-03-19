import re


def finder():
    k = 0
    r = re.compile("[а-яА-Я]+")  # получаем наши буквы
    russian = [j for j in filter(r.match, i)]  # получаем наши буквы формируем из них спиок
    print(russian)  # выводим
    for t in russian:  # пока буквы не кончились наращивать количество
        k += 1  # количество само по себе
    print(k)  # вывод


if __name__ == '__main__':
    i = input()  # слово
    finder()  # ф-ция обработки
