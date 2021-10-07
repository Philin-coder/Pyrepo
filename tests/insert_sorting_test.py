from unittest import TestCase, main
from tested.insert_sort_package import insert_sort
from tested.insert_sort_package.insert_sort import insertion_sort
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(insert_sort))
    return tests


class InsertSortTest(TestCase):
    def test_list_of_ints(self):
        self.assertEqual(insertion_sort(ints=[1, 2, 3, 1, 2, 3, 1, 2, -6, 4, 1]), [-6, 1, 1, 1, 1, 2, 2, 2, 3, 3, 4])

    def test_wrong_list_of_ints(self):
        with self.assertRaises(TypeError) as e:
            insertion_sort(ints=[1, 2, 3, 1, 2, 3, 1, 2, -6, 4, 1, '1'])
        self.assertEqual('Переданы неверные данне', e.exception.args[0])


if __name__ == '__main__':
    main()
