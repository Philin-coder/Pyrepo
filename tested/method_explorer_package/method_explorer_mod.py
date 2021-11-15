class First(object):
    @staticmethod
    def my_exm_method(test_str: str) -> str:
        """
        Тестовый метод (искомый).
        :param test_str: текстовая строка, выводимая методом.
        :return: то, что выводит метод.
        >>> Fr = First()
        >>> Fr.my_exm_method(test_str='hello')
        'hello'
        >>> Fr.class_method_viewer(cl_name=First)
        ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'class_method_finder', 'class_method_viewer', 'my_exm_method']
        >>> Fr.class_method_finder(dir_list=Fr.class_method_viewer(cl_name=First), meth_name='my_exm_method')
        'Метод my_exm_method найден'
        >>> Fr.class_method_finder(dir_list=Fr.class_method_viewer(cl_name=First), meth_name='y_exm_method')
        'Метод y_exm_method  не найден'

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
        if cl_name is not None and __class__ == First:
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
