from unittest import TestCase, main
from tested.row_and_col_sum_package import summer
from tested.row_and_col_sum_package.summer import row_plus_col
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(summer))
    return tests


class LSummTest(TestCase):
    def test_works(self):
        self.assertEqual(row_plus_col(n=3, m=5), [4, 6])

    def test_wrong_input(self):
        with self.assertRaises(TypeError) as e:
            row_plus_col(n='3', m='5')
        self.assertEqual('\'str\' object cannot be interpreted as an integer', e.exception.args[0])


if __name__ == '__main__':
    main()
