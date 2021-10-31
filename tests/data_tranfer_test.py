from unittest import TestCase, main
from tested.data_transfer_package import transferer
from tested.data_transfer_package.transferer import create_matrix
from tested.data_transfer_package.transferer import show_matrix
import doctest
import random


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(transferer))
    return tests


class TransferTest(TestCase):
    def test_is_random_int(self):
        self.assertTrue((0 <= random.randint(0, 9) <= 9) is True, 'не рандом')

    def setUp(self):
        self.mt = create_matrix(n=4)

    def test_int_in_input(self):
        self.assertIsInstance([[random.randint(0, 9) for _ in range(5)] for _ in range(5)], list)

    def test_show_matrix(self):
        self.assertIsNotNone(self.mt, 'Передан None')

    def test_create_matrix_wrong_input(self):
        with self.assertRaises(TypeError) as e:
            my_matrix = create_matrix(n='4')
        self.assertEqual('Введите число', e.exception.args[0])

    def test_show_matrix_wrong_input(self):
        with self.assertRaises(TypeError) as e:
            show_matrix(None)
        self.assertEqual('Для вывода передан не список', e.exception.args[0])


if __name__ == '__main__':
    main()
