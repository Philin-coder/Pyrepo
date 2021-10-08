from unittest import TestCase, main
from tested.index_list_package import index_gen
from tested.index_list_package.index_gen import mas_index_gen_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(index_gen))
    return tests


class IndLIstTestCase(TestCase):
    def test_ind_even(self):
        self.assertEqual(mas_index_gen_func(n=4), {1: 0, 2: 1, 3: 2, 4: 3})

    def test_ind_odd(self):
        self.assertEqual(mas_index_gen_func(n=15), {1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 7, 9: 8, 10: 9, 11: 10,
                                                    12: 11, 13: 12, 14: 13, 15: 14})

    def test_ind_zero(self):
        self.assertEqual(mas_index_gen_func(n=0), {})

    def test_ind_minus(self):
        self.assertEqual(mas_index_gen_func(n=-10), {})

    def test_ind_emp(self):
        with self.assertRaises(TypeError) as e:
            mas_index_gen_func(n='')
        self.assertEqual('Введите целое число', e.exception.args[0])

    def test_ind_char(self):
        with self.assertRaises(TypeError) as e:
            mas_index_gen_func(n='f')
        self.assertEqual('Введите целое число', e.exception.args[0])


if __name__ == '__main__':
    main()
