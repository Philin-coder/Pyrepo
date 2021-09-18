from unittest import TestCase, main
from tested.row_sum_for_package import row_sum
from tested.row_sum_for_package.row_sum import row_sum_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(row_sum))
    return tests


class RowDumForTest(TestCase):
    def test_row_sum_for_int_in_input(self):
        self.assertEqual(row_sum_func(a=12, n=2), 18.0)

    def test_row_sum_for_zero_in_input(self):
        self.assertEqual(row_sum_func(a=0, n=0), 0)

    def test_row_sum_for_char_in_input(self):
        with self.assertRaises(TypeError) as e:
            row_sum_func(a=10, n='2')
        self.assertEqual('Введите целые числа(диапазон и шаг)', e.exception.args[0])


if __name__ == '__main__':
    main()
