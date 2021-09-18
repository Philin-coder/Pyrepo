# 3. Объектно-ориентированное программирование на Python. Стандартные классы. Пользовательские классы. Имитация функции.
# Цель лабораторной работы — описать выбранную ранее предметную область при помощи иерархии классов.
# Обеспечить вывод иерархии при помощи метода test(), вызывающего ее строковое представление.


class emloye(object):
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age in range(1, 100):
            self.__age = age
        else:
            print('не верно')

    def disp(self):
        print(self.__str__())

    def __str__(self):
        return "имя {}\t,  фамилия {}\t Возраст {}\t".format(self.__name, self.__surname, self.__age)


if __name__ == '__main__':
    man = emloye("john", "smith", 20)
    print(man)
