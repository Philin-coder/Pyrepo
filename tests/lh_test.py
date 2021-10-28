from unittest import TestCase, main
from tested.lh_package import lh
from tested.lh_package.lh import list_gen
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(lh))
    return tests


class LHTest(TestCase):
    def test_works_even(self):
        self.assertEqual(list_gen(n=12),
                         [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, -10, -9, -8, -7, -6, -5])

    def test_works_odd(self):
        self.assertEqual(list_gen(n=11), 'местами не меняем')

    def test_wrong_input_zero(self):
        with self.assertRaises(TypeError) as e:
            list_gen(n=0)
        self.assertEqual('введите целое положительное число, не равное 0', e.exception.args[0])

    def test_wrong_input_neg(self):
        with self.assertRaises(TypeError) as e:
            list_gen(n=-10)
        self.assertEqual('введите целое положительное число, не равное 0', e.exception.args[0])

    def test_wrong_input_char(self):
        with self.assertRaises(TypeError) as e:
            list_gen(n='10')
        self.assertEqual('введите целое положительное число, не равное 0', e.exception.args[0])


if __name__ == '__main__':
    main()
