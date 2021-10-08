from unittest import TestCase, main
from functools import reduce
from tested. reduce_example_package import reducwe
from tested.reduce_example_package.reducwe import red_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(reducwe))
    return tests


class ReducerTest(TestCase):
    def test_reducer_works(self):
        self.assertEqual(red_func(), [4, 3, 2, 1])

    def test_reducer_list_in(self):
        self.assertTrue(isinstance([i for i in range(1, 11)], list) is True, "не  список ")

    def test_reducer_list_out(self):
        self.assertTrue(isinstance(reduce(lambda res, i: [i] + res, [1, 2, 3, 4], []), list) is True, "не  список")


if __name__ == '__main__':
    main()
