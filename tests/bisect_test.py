from unittest import TestCase, main
from tested.bisect_package import bis
from tested.bisect_package.bis import binary_search
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(bis))
    return tests


class MyTestCase(TestCase):
    def test_x_more(self):
        self.assertEqual(binary_search(a=[1, 2, 3, 4, 5], x=5, lo=2), 4)

    def test_lo_more(self):
        self.assertEqual(binary_search(a=[1, 2, 3, 4, 5], x=2, lo=5), -1)

    def test_lo_equal(self):
        self.assertEqual(binary_search(a=[1, 2, 3, 4, 5], x=2, lo=2), -1)

    def test_hi_None(self):
        self.assertEqual(binary_search(a=[1, 2, 3, 4, 5], x=4, lo=2, hi=None), 3)

    def test_hi_not_None(self):
        self.assertEqual(binary_search(a=[1, 2, 3, 4, 5], x=4, lo=2, hi=4), 3)

    def test_hi_wrong(self):
        with self.assertRaises(TypeError) as e:
            binary_search(a=[1, 2, 3, 4, 5], x='4', lo='2', hi=4)
        self.assertEqual('передан невереый тип данных', e.exception.args[0])


if __name__ == '__main__':
    main()
