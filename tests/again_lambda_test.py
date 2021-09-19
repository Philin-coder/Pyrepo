from unittest import TestCase, main
from tested.the_second_lambda_package import lamtets2
from tested.the_second_lambda_package.lamtets2 import func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(lamtets2))
    return tests


class LambTest(TestCase):

    def test_lam_works(self):
        self.assertEqual(func(1, 4), 17)


if __name__ == '__main__':
    main()
