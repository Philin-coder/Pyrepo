from unittest import TestCase, main
from tested.list_double_killer_package import list_redubler
from  tested.list_double_killer_package.list_redubler import deleter
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(list_redubler))
    return tests


class RedublerTest(TestCase):
    def test_redubler_works(self):
        self.assertEqual(deleter(), [50, '0032', 765])

    def test_redubler_is_list_in(self):
        self.assertTrue(isinstance([50, '0032', 17, 25, 765, 217, 25, 217, 17], list) == True, "не список")

    def test_redubler_is_list_out(self):
        self.assertTrue(isinstance([i for i in [50, '0032', 17, 25, 765, 217, 25, 217, 17] if
                                    [50, '0032', 17, 25, 765, 217, 25, 217, 17].count(i) == 1], list) == True,
                        "не список")


if __name__ == '__main__':
    main()
