from unittest import TestCase, main
from tested.uniq_in_list_pacage import uniq_in_list
from tested.uniq_in_list_pacage.uniq_in_list import set_gen
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(uniq_in_list))
    return tests


class UniqInListTest(TestCase):
    def test_is_list(self):
        self.assertTrue(isinstance(list(set((1, 2, 2, 3, 4, 5))), list) is True, "не  список")

    def test_is_uniq(self):
        self.assertFalse(list((1, 2, 2, 3, 4, 5)) == list(set((1, 2, 3, 4, 5))), "списки равы")

    def test_is_right(self):
        self.assertEqual(set_gen(), [1, 2, 3, 4, 5])

    if __name__ == '__main__':
        main()
