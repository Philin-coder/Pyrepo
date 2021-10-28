from unittest import TestCase, main
from tested.numpy_matr_package import matrixer
from tested.numpy_matr_package.matrixer import np_mass_create
import doctest
import numpy


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(matrixer))
    return tests


class MyNumMatrixTest(TestCase):
    def test_is_nd_array_list(self):
        self.assertIsInstance(np_mass_create(n=2, m=2), numpy.ndarray)

    def test_wrong_input(self):
        with self.assertRaises(TypeError) as e:
            np_mass_create(n='2', m='2')
        self.assertEqual('Введите целые числа', e.exception.args[0])


if __name__ == '__main__':
    main()
