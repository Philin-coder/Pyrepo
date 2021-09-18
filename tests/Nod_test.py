from unittest import TestCase, main
from tested.Nod_package import gcd_finder
from tested.Nod_package.gcd_finder import nod
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(gcd_finder))
    return tests


class NodeTest(TestCase):
    def test_int_in_input(self):
        self.assertEqual(nod(a=12, b=128), 4)

    def test_char_in_input(self):
        with self.assertRaises(TypeError) as e:
            nod(a=12, b='128')
        self.assertEqual('Введите целое число', e.exception.args[0])

    def test_float_in_input(self):
        with self.assertRaises(TypeError) as e:
            nod(a=12, b=1.28)
        self.assertEqual('Введите целое число', e.exception.args[0])


if __name__ == '__main__':
    main()
