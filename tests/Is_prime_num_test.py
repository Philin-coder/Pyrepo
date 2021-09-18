from unittest import TestCase, main
from tested.Is_prime_num_package import is_prime
from tested.Is_prime_num_package.is_prime import is_prime_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(is_prime))
    return tests


class ISPrimeTest(TestCase):
    def test_IsPrime_True(self):
        self.assertEqual(is_prime_func(n=2), True)

    def test_IsPrime_False(self):
        self.assertEqual(is_prime_func(n=12), False)

    def test_IsPrime_Char(self):
        with self.assertRaises(TypeError) as e:
            is_prime_func(n='12')
        self.assertEqual('введите целое число', e.exception.args[0])


if __name__ == '__main__':
    main()
