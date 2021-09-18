from unittest import TestCase, main
from tested.some_function_package import some_func
from tested.some_function_package.some_func import urg_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(some_func))
    return tests


class SomeFuncTest(TestCase):
    def test_float_in_input_with_yes(self):
        self.assertEqual(urg_func(x=1.0, y=2.0, xc=3.0, yc=4.0, r=5.0), 'YES')

    def test_float_in_input_with_NO(self):
        self.assertEqual(urg_func(x=-10.0, y=-10.0, xc=100.0, yc=-1.0, r=1.0), 'NO')

    def test_spaces_in_input_in_inputO(self):
        with self.assertRaises(TypeError) as e:
            urg_func(x='', y='-10.0', xc='100.0', yc='-1.0', r='1.0')
        self.assertEqual('Введите веществвенное число', e.exception.args[0])


if __name__ == '__main__':
    main()
