from unittest import TestCase, main
from tested.mul_table_package import mul_table
from tested.mul_table_package.mul_table import mul_table_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(mul_table))
    return tests


class MulTest(TestCase):
    def test_works(self):
        self.assertIsInstance(mul_table_func(), str)


if __name__ == '__main__':
    main()
