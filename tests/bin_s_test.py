from unittest import TestCase, main
from tested.binary_search_package import bin_search
from tested.binary_search_package.bin_search import list_gen
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(bin_search))
    return tests


class BinSearchTest(TestCase):
    def test_int_in_list_input(self):
        self.assertEqual(list_gen(n=100, value=21), ('ID =', 2))

    def test_int_not_in_list_input(self):
        self.assertEqual(list_gen(n=100, value=80), 'No value')

    def test_char_in_input_input(self):
        with self.assertRaises(TypeError) as e:
            list_gen(n='100', value='80')
        self.assertEqual('Введите числа', e.exception.args[0])


if __name__ == '__main__':
    main()
