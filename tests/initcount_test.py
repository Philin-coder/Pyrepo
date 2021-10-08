from unittest import TestCase, main
from tested.simple_count_package import initcount
from tested.simple_count_package.initcount import simple_expr
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(initcount))
    return tests


class InitCountTest(TestCase):
    def test_int_in_input(self):
        self.assertIsInstance(0.1722, float) or self.assertIsInstance(6.33, float) or self.assertIsInstance(
            172.025, float)

    def test_what_in_equivalence(self):
        self.assertEqual(simple_expr(x=0.1722, y=6.33, z=172.025), 0.8536129750647968)


if __name__ == '__main__':
    main()
