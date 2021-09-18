from unittest import TestCase, main
from tested.one_more_sort_package import sorter
from tested.one_more_sort_package.sorter import sorting_mas_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(sorter))
    return tests


class SimpleSortTest(TestCase):
    def test_it_works_even(self):
        self.assertEqual(sorting_mas_func(mixed_list=[4, 8, 2]), [8, 4, 2])

    def test_it_works_odd(self):
        self.assertEqual(sorting_mas_func(mixed_list=[1, 2, 3]), [3, 1, 2])

    def test_it_works_mixed(self):
        self.assertEqual(sorting_mas_func(mixed_list=[3, 1, 6]), [6, 3, 1])

    def test_it_works_alpha(self):
        with self.assertRaises(TypeError) as e:
            sorting_mas_func(mixed_list=['a', 'b', 'c'])
        self.assertEqual('Получен не список цифр', e.exception.args[0])


if __name__ == '__main__':
    main()
