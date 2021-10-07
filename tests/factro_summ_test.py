from unittest import TestCase, main
from tested.factor_sum_package import factor_sum
from tested.factor_sum_package.factor_sum import factor_sum_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(factor_sum))
    return tests


class FactorTest(TestCase):
    def test_summing(self):
        self.assertEqual(factor_sum_func(n=10), ('Sum: ', 1.7182818011463847))

    def test_wrong_input(self):
        with self.assertRaises(TypeError) as e:
            factor_sum_func(n='10')
        self.assertEqual('Введите целое число', e.exception.args[0])


if __name__ == '__main__':
    main()
