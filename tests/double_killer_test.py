from unittest import TestCase, main
from tested.double_killer_package import double_killer
from tested.double_killer_package.double_killer import double_finder
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(double_killer))
    return tests


class double_killerTest(TestCase):
    def test_doublekiller_works(self):
        self.assertEqual(double_finder(repeated_sym=[1, 1, 2, 3, 3, 3, 4, 6]), [1, 3])

    def test_doublekiller_works_sym(self):
        self.assertEqual(double_finder(repeated_sym=['1', '1', '2']), ['1'])

    def test_doublekiller_works_empty(self):
        self.assertEqual(double_finder(repeated_sym=[]), [])

    def test_not_list(self):
        with self.assertRaises(TypeError) as e:
            double_finder(repeated_sym=1)
        self.assertEqual('ВВеден не список', e.exception.args[0])


if __name__ == '__main__':
    main()
