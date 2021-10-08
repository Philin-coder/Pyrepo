from unittest import TestCase, main
from tested.Type_demo_package import type_demo
from tested.Type_demo_package.type_demo import immut
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(type_demo))
    return tests


class TupleTest(TestCase):
    def test_type_demo_working(self):
        self.assertEqual(immut(), '<class \'tuple\'>')

    def test_error(self):
        self.assertTrue((type((1, 1)).__name__ == 'tuple') is True, "не картежем")


if __name__ == '__main__':
    main()
