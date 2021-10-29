from unittest import TestCase, main
from tested.even_mixed_list import lister
from tested.even_mixed_list.lister import even_finder
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(lister))
    return tests


class LstMixTest(TestCase):
    def test_works(self):
        self.assertEqual(even_finder(mixed_vals=[1, 2, 3, 4, 6, 7, 9, 'a']), [2, 4, 6])

    def test_wrong_input(self):
        with self.assertRaises(TypeError) as e:
            even_finder(mixed_vals={1, 2, 3, 4, 6, 7, 9, 'a'})
        self.assertEqual('передан не список, или-список пуст ', e.exception.args[0])

    def test_empty_lst(self):
        with self.assertRaises(TypeError) as e:
            even_finder(mixed_vals=[])
        self.assertEqual('передан не список, или-список пуст ', e.exception.args[0])


if __name__ == '__main__':
    main()
