from unittest import TestCase, main
from tested.before_max_sorting_paxkage import before_max_sorting
from tested.before_max_sorting_paxkage.before_max_sorting import max_sort_gen_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(before_max_sorting))
    return tests


class BefireMaxSORTestCase(TestCase):
    def test_is_int_sort(self):
        self.assertEqual(max_sort_gen_func(ints=[2, 3, 4, 1, 10, 12]), [1, 2, 3, 4, 10, 12])

    def test_wrong_input(self):
        with self.assertRaises(TypeError) as e:
            max_sort_gen_func(ints=['a', 3, 4, 1, 10, 12])
        self.assertEqual('Введите список  чисел',e.exception.args[0])


if __name__ == '__main__':
    main()
