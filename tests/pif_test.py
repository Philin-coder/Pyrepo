from unittest import TestCase, main
from tested.pifagor_package import pif_table
from tested.pifagor_package.pif_table import pif_table_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(pif_table))
    return tests


class PifTest(TestCase):

    def test_is_a_string(self):
        self.assertIsInstance(pif_table_func(), str)


if __name__ == '__main__':
    main()
