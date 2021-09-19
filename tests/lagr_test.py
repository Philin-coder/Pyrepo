from unittest import TestCase, main
from tested.lagrange_package import lagr
from tested.lagrange_package.lagr import lagrange
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(lagr))
    return tests


class LagrTest(TestCase):
    def test_normal_input(self):
        self.assertEqual(lagrange(28, 2, 4), '5 1 1 1')

    def test_char_input(self):
        with self.assertRaises(TypeError) as e:
            lagrange('28', 2, 4)
        self.assertEqual('Введите  целые числа ', e.exception.args[0])

    def test_zero_input(self):
        with self.assertRaises(ZeroDivisionError) as e:
            lagrange(0, 0, 0)
        self.assertEqual('Нельзя делить на 0', e.exception.args[0])


if __name__ == '__main__':
    main()
