from unittest import TestCase, main
from tested.tupple_package import tuple_checker
from tested.tupple_package.tuple_checker import t_ind_check
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(tuple_checker))
    return tests


class TupleIndTest(TestCase):
    def test_odd_n(self):
        self.assertEqual(t_ind_check(n=5), (1, 2, 3))

    def test_even_n(self):
        self.assertEqual(t_ind_check(n=14), ((1, 2, 12)))

    def test_char_n(self):
        with self.assertRaises(TypeError) as e:
            t_ind_check(n='f')
        self.assertEqual('n вне допустимой области значенй', e.exception.args[0])

    def test_neg_n(self):
        with self.assertRaises(TypeError) as e:
            t_ind_check(n=-3)
        self.assertEqual('n вне допустимой области значенй', e.exception.args[0])

    def test_zero_n(self):
        with self.assertRaises(TypeError) as e:
            t_ind_check(n=0)
        self.assertEqual('n вне допустимой области значенй', e.exception.args[0])

    def test_less4_n(self):
        with self.assertRaises(TypeError) as e:
            t_ind_check(n=3)
        self.assertEqual('n вне допустимой области значенй', e.exception.args[0])


if __name__ == '__main__':
    main()
