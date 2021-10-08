from unittest import TestCase, main
from tested.dig_root_package import dig_root
from tested.dig_root_package.dig_root import dig_root_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(dig_root))
    return tests


class DigRootTest(TestCase):
    def test_ints_even(self):
        self.assertEqual(dig_root_func(n=12), 3)

    def test_ints_zero(self):
        self.assertEqual(dig_root_func(n=0), 0)

    def test_ints_odd(self):
        self.assertEqual(dig_root_func(n=1123), 7)

    def test_ints_wrong(self):
        with self.assertRaises(TypeError) as e:
            dig_root_func(n='1123')
        self.assertEqual('Введите число', e.exception.args[0])

    def test_ints_neg(self):
        with self.assertRaises(TypeError) as e:
            dig_root_func(n=-10)
        self.assertEqual('Введите число', e.exception.args[0])


if __name__ == '__main__':
    main()
