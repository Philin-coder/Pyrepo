from unittest import TestCase, main
from tested.is_prime_range_package import is_primer
from tested.is_prime_range_package.is_primer import is_prime_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(is_primer))
    return tests


class ISPrimeTest(TestCase):
    def test_int_input(self):
        self.assertEqual(is_prime_func(n=12), [1, 2, 3, 5, 7, 11])

    def test_int_one_input(self):
        self.assertEqual(is_prime_func(n=2), [1, 2])

    def test_char_in_input(self):
        with self.assertRaises(TypeError) as e:
            is_prime_func(n='a')
        self.assertEqual('Введите целое полложительное число не равное 0', e.exception.args[0])

    def test_zero_in_input(self):
        with self.assertRaises(TypeError) as e:
            is_prime_func(n=0)
        self.assertEqual('Введите целое полложительное число не равное 0', e.exception.args[0])

    def test_negs_in_input(self):
        with self.assertRaises(TypeError) as e:
            is_prime_func(n=-10)
        self.assertEqual('Введите целое полложительное число не равное 0', e.exception.args[0])


if __name__ == '__main__':
    main()
