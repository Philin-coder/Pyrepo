from unittest import TestCase, main
from tested.lambda_tre_package import lamtest
from tested.lambda_tre_package.lamtest import func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(lamtest))
    return tests


class OneSTRTest(TestCase):
    def test_one_str_TRue(self):
        self.assertEqual(func(5), True)

    def test_one_str_false(self):
        self.assertEqual(func(2), False)


if __name__ == '__main__':
    main()
