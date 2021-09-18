from unittest import TestCase, main
from tested.repeat_until_package import row_sum
from tested.repeat_until_package.row_sum import row_sum_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(row_sum))
    return tests


class RowSumRepeatUntilTest(TestCase):
    def test_row_sum_repeat_until_int_in_input(self):
        self.assertEqual(row_sum_func(a=12, n=2), 18.0)

    def test_row_sum_repeat_until_zero_in_input(self):
        self.assertEqual(row_sum_func(a=0, n=0), 0)

    def test_row_sum_repeat_until_char_in_input(self):
        with self.assertRaises(TypeError) as e:
            row_sum_func(a=10, n='2')
        self.assertEqual('Введите целые числа(диапазон и шаг)', e.exception.args[0])


if __name__ == '__main__':
    main()
