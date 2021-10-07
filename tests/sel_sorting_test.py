from unittest import TestCase, main
from tested.select_sorting_package import sel_sorting
from tested.select_sorting_package.sel_sorting import sel_sorting_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(sel_sorting))
    return tests


class SelSortTest(TestCase):
    def test_int_list_input(self):
        self.assertEqual(sel_sorting_func(ints=[1, 2, 3, 1, 2, 3, 1, 2, -6, 4, 1]), [-6, 1, 1, 1, 1, 2, 2, 2, 3, 3, 4])

    def test_wrong_list_input(self):
        with self.assertRaises(TypeError) as e:
            sel_sorting_func(ints=[1, 2, 3, 1, 2, 3, 1, 2, -6, 4, 1, '2'])
        self.assertEqual('Переданы неверые  данные', e.exception.args[0])


if __name__ == '__main__':
    main()
