from unittest import TestCase, main
from tested.euler_package import euler_func
from tested.euler_package.euler_func import phi
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(euler_func))
    return tests


class EulerFuncTest(TestCase):
    def test_ints_in_input(self):
        self.assertEqual(phi(n=12), 2.0)

    def test_char_in_input(self):
        with self.assertRaises(TypeError) as e:
            phi(n='100')
        self.assertEqual('Введите целое число', e.exception.args[0])


if __name__ == '__main__':
    main()
