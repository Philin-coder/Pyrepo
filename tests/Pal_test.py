from unittest import TestCase, main
from tested.dig_pal_package import dig_pal
from tested.dig_pal_package.dig_pal import dig_pal_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(dig_pal))
    return tests


class MyTestCase(TestCase):
    def test_not_pal_int(self):
        self.assertEqual(dig_pal_func(data=1213), 'Число  не являетмся палиндроом')

    def test_pal_int(self):
        self.assertEqual(dig_pal_func(data=123), 'Число являетмся палиндроом')

    def test_char_in_input(self):
        with self.assertRaises(TypeError) as e:
            dig_pal_func(data='123')
        self.assertEqual('Введите число', e.exception.args[0])


if __name__ == '__main__':
    main()
