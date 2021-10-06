from unittest import TestCase, main
from tested.ins_package import ins
from tested.ins_package.ins import inspect_func
from tested.ins_package.ins import view_f
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(ins))
    return tests


class InspectTest(TestCase):
    def test_inspect_func_int(self):
        self.assertEqual(inspect_func(2, 3), 5)

    def test_inspect_func_char(self):
        with self.assertRaises(TypeError) as e:
            inspect_func('2', '3')
        self.assertEqual('Введите числа, в качестве аргументов', e.exception.args[0])

    def test_view_works(self):
        self.assertEqual(view_f(inspect_func),
                         ['def', 'inspect_func', 'arg1', 'arg2', 'Демонстрация', 'функционала', 'inspect', 'param',
                          'arg1', 'первый', 'аргумент', 'анализируемой', 'функии', 'param', 'arg2', 'второй',
                          'аргумент', 'анализируемой', 'функии', 'return', 'результат', 'работы', 'анализируемой',
                          'функии', 'inspect_func', '2', '3', '5', 'if', 'isinstance', 'arg1', 'int', 'and',
                          'isinstance', 'arg2', 'int', 'return', 'arg1', 'arg2', 'else', 'raise', 'TypeError',
                          'Введите', 'числа', 'в', 'качестве', 'аргументов'])


if __name__ == '__main__':
    main()
