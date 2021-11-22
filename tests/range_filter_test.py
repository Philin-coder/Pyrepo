from unittest import TestCase, main
from tested.filt_range_package import filt_range
from tested.filt_range_package.filt_range import another_mas_gen
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(filt_range))
    return tests


class MyLGenTestCase(TestCase):
    def test_int_in_input(self):
        self.assertEqual(another_mas_gen(n=80),
                         [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43,
                          44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66,
                          67, 68, 69, 70])

    def test_is_list(self):
        self.assertIsInstance(another_mas_gen(80), list)

    def test_char_in_input(self):
        with self.assertRaises(TypeError) as e:
            another_mas_gen(n='80')
        self.assertEqual('передан неверный тип данных', e.exception.args[0])


if __name__ == '__main__':
    main()
