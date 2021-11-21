from unittest import TestCase, main
from tested.mx_mult_package import mx_mult
from tested.mx_mult_package.mx_mult import mx_mult_func
import doctest
import random


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(mx_mult))
    return tests


class MxMultTest(TestCase):
    def test_is_random_int(self):
        self.assertTrue(0 <= random.randint(1, 10) <= 10)

    def test_mx_mult_returns_tuple(self):
        self.assertIsInstance(mx_mult_func(n=5, m=5), tuple)

    def ints_in(self):
        self.assertTrue(
            any(i.isdigit() for i in
                mx_mult_func(n=5, m=5) and any(isinstance(i, str) for i in mx_mult_func(n=5, m=5)))
            is True, 'есть  цифры и буквы')

    def test_mx_mult_char_in(self):
        with self.assertRaises(TypeError) as e:
            mx_mult_func(n='5', m='5')
        self.assertEqual('передан неверный тип данных', e.exception.args[0])


if __name__ == '__main__':
    main()
