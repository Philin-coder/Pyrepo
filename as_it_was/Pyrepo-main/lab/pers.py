class Person:  # создаем класс
    def __init__(self, name, job=None, pay=0):  # инициализируем поля
        self.name = name  # получение полей
        self.job = job  # получение полей
        self.pay = pay  # получение полей

    def lastName(self):  # выворд имени
        return self.name.split()[-1]  # получаем строку имя+ фамили, делим по пробелу, берем 1(по периодц)

    def giveresize(self, persent):
        self.pay = int(self.pay * (1 + persent))  # начмиисление зарполаты

    def mystr(self):
        return '[Person: %s, %s]' % (self.name, self.pay)  # встроенны принт и вывод


class Manager(Person):  # класс менеджер
    def __init__(self, name, pay):  # получаеые поля
        def giveresize(self, persent, bonus=100):  # передаваемые в них значения
            Person.giveresize(self, persent + bonus)  # изменнения зарплаты


if __name__ == '__main__':  # точка входа
    Ivan = Person('Иван Петров')  # объекты классов, с заполняемыми значениями
    john = Person('John Sidorov', job='dev', pay=100000)  # передача значений
    print(Ivan)  # вывод, но, поскольку ф-ция встроенная, печататься будет объект
    print(john)  # вывод, но, поскольку ф-ция встроенная, печататься будет объект
