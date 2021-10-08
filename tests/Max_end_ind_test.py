from unittest import TestCase, main
from tested.max_end_ind_package import max_end_ind
from tested.max_end_ind_package.max_end_ind import max_and_ind_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(max_end_ind))
    return tests


class MaxEndIdnTest(TestCase):
    def test_ints_in_input(self):
        self.assertEqual(max_and_ind_func(n=12, cycle_step=2), ' макссимум =11, его номер =5')

    def test_ints_in_input_step_odd(self):
        self.assertEqual(max_and_ind_func(n=12, cycle_step=1), ' макссимум =12, его номер =11')

    def test_char_in_input(self):
        with self.assertRaises(ValueError) as e:
            max_and_ind_func(n=12, cycle_step='1')
        self.assertEqual('Введите 2 целых числа граница диапазона и шаг', e.exception.args[0])


if __name__ == '__main__':
    main()
