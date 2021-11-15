class First(object):
    @staticmethod
    def my_func(test_str) -> str:
        """
        Тестовый метод (искомый).
        :param test_str: текстовая строка, выводимая методом.
        :return: то, что выводит метод.
        """
        if isinstance(test_str, str):
            return test_str
        else:
            raise TypeError('Передан неверный тип данных ')

    @staticmethod
    def class_method_viewer(cl_name: object) -> list:
        """
        Просмотр методов заданного класса.
        :param cl_name: имя класса.
        :return: список методов заданного класса.
        """
        if isinstance(cl_name, object) and cl_name.__name__ == 'First':
            return dir(cl_name)
        else:
            raise TypeError('передан неверный тип данных')

    @staticmethod
    def class_method_finder(dir_list: list, meth_name: str) -> str:
        """
        Поиск метода заданного класса.
        :param dir_list:  список методов заданного класса.
        :param meth_name: искомый метод.
        :return: Найден, или нет искомый метод.
        """
        if isinstance(dir_list, list) and isinstance(meth_name, str):
            if meth_name in dir_list:
                return f'Метод {meth_name} найден'
            else:
                return f'Метод {meth_name}  не найден'
        else:
            raise TypeError('передан неверный тип данных')


if __name__ == '__main__':
    Fr = First()
    print(Fr.my_func(test_str='hello'))
    print(Fr.class_method_viewer(cl_name=First))
    print(Fr.class_method_finder(dir_list=Fr.class_method_viewer(cl_name=First), meth_name='my_func'))
    print(Fr.class_method_finder(dir_list=Fr.class_method_viewer(cl_name=First), meth_name='y_func'))
