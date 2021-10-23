from unittest import TestCase, main
from tested.random_uniform_list_package import random_uniform_list
from tested.random_uniform_list_package.random_uniform_list import num_gen
import doctest
import random


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(random_uniform_list))
    return tests


class MyFloatTest(TestCase):
    def setUp(self):
        self.ng = num_gen(start_p=1, end_p=10)
        self.ng(n=8)

    def test_is_floating_point(self):
        self.assertTrue((isinstance(num_gen(start_p=1, end_p=10), float) is True, 'не вещественное число'))

    def test_is_random_float(self):
        self.assertTrue((1.0 <= random.uniform(1.0, 10.0) <= 10.0) is True, 'не рандом')

    def test_wrong_input(self):
        with self.assertRaises(TypeError) as e:
            self.ng = num_gen(start_p='1', end_p='10')
        self.assertEqual('Передан неверный тип данных', e.exception.args[0])

    def test_wrong_n(self):
        with self.assertRaises(TypeError) as e:
            self.ng(n='8')
        self.assertEqual('Передан неверный тип данных', e.exception.args[0])


if __name__ == '__main__':
    main()
