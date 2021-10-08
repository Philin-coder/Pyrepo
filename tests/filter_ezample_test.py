from unittest import TestCase, main
from tested.filter_ezample_package import filter_ex
from tested.filter_ezample_package.filter_ex import filter_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(filter_ex))
    return tests


class FilterExampleTest(TestCase):
    def test_works(self):
        self.assertEqual(filter_func(n=12), [6, 7, 8, 9, 10, 11, 12])

    def test_works_zero_in_input(self):
        self.assertEqual(filter_func(n=0), [])

    def test_works_negative_in_input(self):
        self.assertEqual(filter_func(n=0), [])

    def test_ints_in_input(self):
        with self.assertRaises(TypeError) as e:
            filter_func(n='1')
        self.assertEqual('Введите количество элесентов последовательности(целое  число)', e.exception.args[0])


if __name__ == '__main__':
    main()
