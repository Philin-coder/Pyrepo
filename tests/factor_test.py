from unittest import TestCase, main
from tested.factor_package import factor
from tested.factor_package.factor import factorial_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(factor))
    return tests


class FactorTest(TestCase):
    def test_factor_int(self):
        self.assertEqual(factorial_func(n=3), 6)

    def test_factor_char(self):
        with self.assertRaises(TypeError) as e:
            factorial_func(n='3')
        self.assertEqual('Введите целое число', e.exception.args[0])


if __name__ == '__main__':
    main()
