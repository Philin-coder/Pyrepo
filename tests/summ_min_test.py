from unittest import TestCase, main
from tested.summ_min_str_package import summ_min_str
from tested.summ_min_str_package.summ_min_str import find_sum_min_str_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(summ_min_str))
    return tests


class SummMinTest(TestCase):
    def test_min_works(self):
        self.assertEqual(find_sum_min_str_func(arr=[
            [1, 2, 3, 4, 5, 6, 7, 8, 10],
            [1, 2, 3, 4, 5, 6, 7, 8, 10],
            [1, 2, 3, 4, 5, 6, 7, 8, 10],
            [1, 2, 3, 4, 5, 6, 7, 8, 10],
            [1, 2, 3, 4, 5, 6, 7, 8, 10],
            [1, 2, 3, 4, 5, 6, 7, 8, 10],
            [1, 2, 3, 4, 5, 6, 7, 8, 10],
            [1, 2, 3, 4, 5, 6, 7, 8, 10],
            [1, 2, 3, 4, 5, 6, 7, 8, 10],
            [1, 2, 3, 4, 5, 6, 7, 8, 10]

        ]), 10)

    def test_min_not_list(self):
        with self.assertRaises(TypeError) as e:
            find_sum_min_str_func(arr=(
                [1, 2, 3, 4, 5, 6, 7, 8, 10],
                [1, 2, 3, 4, 5, 6, 7, 8, 10],
                [1, 2, 3, 4, 5, 6, 7, 8, 10],
                [1, 2, 3, 4, 5, 6, 7, 8, 10],
                [1, 2, 3, 4, 5, 6, 7, 8, 10],
                [1, 2, 3, 4, 5, 6, 7, 8, 10],
                [1, 2, 3, 4, 5, 6, 7, 8, 10],
                [1, 2, 3, 4, 5, 6, 7, 8, 10],
                [1, 2, 3, 4, 5, 6, 7, 8, 10],
                [1, 2, 3, 4, 5, 6, 7, 8, 10]

            ))
        self.assertEqual('Введен не спиисок а tuple', e.exception.args[0])


if __name__ == '__main__':
    main()
