from unittest import TestCase, main
from tested.merge_sorting_package import merge_sort
from  tested.merge_sorting_package.merge_sort import merge_sort_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(merge_sort))
    return tests


class MergeSortTest(TestCase):
    def test_merge_sort_works(self):
        self.assertEqual(merge_sort_func(mixed_ints=[54, 26, 93, 17, 77, 31, 44, 55, 20]),
                         ('Merging ', [17, 20, 26, 31, 44, 54, 55, 77, 93]))

    def test_merge_sort_set_in(self):
        with self.assertRaises(TypeError) as e:
            merge_sort_func(mixed_ints={54, 26, 93, 17, 77, 31, 44, 55, 20})
        self.assertEqual('введите список, а не set', e.exception.args[0])

    def test_merge_sort_tuple_in(self):
        with self.assertRaises(TypeError) as e:
            merge_sort_func(mixed_ints=(54, 26, 93, 17, 77, 31, 44, 55, 20))
        self.assertEqual('введите список, а не tuple', e.exception.args[0])


if __name__ == '__main__':
    main()
