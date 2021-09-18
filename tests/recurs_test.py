from unittest import TestCase, main
from tested.Recursion_package import recusion_example
from  tested.Recursion_package.recusion_example import factorial_iterative_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(recusion_example))
    return tests


class RecursionTest(TestCase):
    def test_pos_int(self):
        self.assertEqual(factorial_iterative_func(num=3), 'Факториал 3 это 6')

    def test_neg_int(self):
        self.assertEqual(factorial_iterative_func(num=-3), 'Факториал не вычисляется для отрицательных чисел')

    def test_char(self):
        with self.assertRaises(TypeError) as e:
            factorial_iterative_func(num='')
        self.assertEqual('Введите число',e.exception.args[0])


if __name__ == '__main__':
    main()
