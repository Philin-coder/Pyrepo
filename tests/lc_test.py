from unittest import TestCase, main
from tested.listcom_pacage import l_comp
from tested.listcom_pacage.l_comp import list_sel_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(l_comp))
    return tests


class LcTest(TestCase):
    def test_is_list_return(self):
        self.assertTrue(isinstance(list((i * 3 if i % 2 else i * 2 for i in [i for i in range(1, 11)])), list) is True)

    def test_is_list_in(self):
        self.assertTrue(isinstance([i for i in range(1, 11)], list) is True)

    def test_is_list_lc_works(self):
        self.assertEqual(list_sel_func(), [3, 4, 9, 8, 15, 12, 21, 16, 27, 20])


if __name__ == '__main__':
    main()
