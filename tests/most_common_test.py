from unittest import TestCase, main
from tested.fraquency_analyse_package import find_common
from tested.fraquency_analyse_package.find_common import find_common_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(find_common))
    return tests


class MostComTest(TestCase):
    def test_int_in_input(self):
        self.assertEqual(find_common_func(mixed_values=[1, 2, 4, 5, 6, 7, 7, 7, 7, 7, 8]), 7)

    def test_char_in_input(self):
        self.assertEqual(find_common_func(mixed_values=['a', 'b', 'c', 'd', 'd', 'd']), 'd')

    def test_wrong_input_input(self):
        self.assertTrue(isinstance({'a', 'b', 'c', 'd', 'd', 'd'}, list) is False, 'передан несписок ')


if __name__ == '__main__':
    main()
