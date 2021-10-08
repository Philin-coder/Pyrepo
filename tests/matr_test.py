from unittest import TestCase, main
from tested.matr_package import matr
from tested.matr_package.matr import matrix_gen
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(matr))
    return tests


class MatrixTest(TestCase):
    def test_more_zero(self):
        self.assertEqual(matrix_gen(a=2, b=2), [0, 1])

    def test_symbols(self):
        with self.assertRaises(TypeError) as e:
            matrix_gen(a='2', b=2)
        self.assertEqual('Введены не числа', e.exception.args[0])


if __name__ == '__main__':
    main()
