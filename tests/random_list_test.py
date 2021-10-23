from unittest import TestCase, main
from tested.random_list_package import random_list
from tested.random_list_package.random_list import random_list_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(random_list))
    return tests


class RandTest(TestCase):
    def test_is_int(self):
        self.assertTrue((isinstance(random_list_func(start_p=-10, end_p=10), int)) is True, 'не число')

    def test_is_random_int(self):
        self.assertTrue((-10 <= random_list_func(start_p=-10, end_p=10) <= 10) is True, 'не рандом')

    def test_is_random_list(self):
        self.assertIsInstance([random_list_func(start_p=-10, end_p=10)], list)

    def test_wrong_input(self):
        with self.assertRaises(TypeError) as e:
            [random_list_func(start_p='-10', end_p='10') for _ in range(12)]
        self.assertEqual('передан неверный тип данных', e.exception.args[0])


if __name__ == '__main__':
    main()
