class Employee(object):
    def __init__(self, name, surname, age):
        """
        Пример работы с property/
        :param name: Имя.
        :param surname: Фамилия.
        :param age: Возраст
        Образец вызова
        man = Employee("john", "smith", 20)
        man.__str__()
        'имя john\t,  фамилия smith\t Возраст 20\t'
        """
        self.__name = name
        self.__surname = surname
        self.__age = age

    @property
    def name(self):
        if isinstance(self.__name, str) and self.__name is not None:
            return self.__name
        else:
            raise TypeError('Передан неверный тип данных')

    @property
    def surname(self):
        if isinstance(self.__surname, str) and self.__surname is not None:
            return self.__surname
        else:
            raise TypeError('Передан неверный тип данных')

    @property
    def age(self):
        if isinstance(self.__age, float) and self.__age != 0 and self.__age > 0:
            return self.__age
        else:
            raise ValueError('Передан неверный возраст')

    @age.setter
    def age(self, age):
        if age in range(1, 100):
            self.__age = age
        else:
            print('не верно')

    def disp(self):
        return self.__str__()

    def __str__(self):
        return "имя {}\t,  фамилия {}\t Возраст {}\t".format(self.__name, self.__surname, self.__age)


if __name__ == '__main__':
    man = Employee("john", "smith", 20)
    print(man.disp())
