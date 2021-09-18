from unittest import TestCase, main
from tested.withlistworkpackage import init_list
from tested.withlistworkpackage.init_list import int_list_gen
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(init_list))
    return tests


class WithListWorkTest(TestCase):

    def test_what_in_input(self):
        self.assertIsInstance([i for i in range(36) if i > 3.5], list)

    def test_what_in_outoutput(self):
        self.assertIsInstance(len([i for i in range(36) if i > 3.5]) / sum([i for i in range(36) if i > 3.5]), float)

    def test_what_in_equivalence(self):
        self.assertEqual(int_list_gen(), 19.5)


if __name__ == '__main__':
    main()
