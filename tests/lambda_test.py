from unittest import TestCase, main
from tested.lamda_package import lamtest
from tested.lamda_package.lamtest import func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(lamtest))
    return tests


class lamtests(TestCase):
    def test_lam_right(self):
        self.assertEqual(func(1, 4), 17)


if __name__ == '__main__':
    main()
