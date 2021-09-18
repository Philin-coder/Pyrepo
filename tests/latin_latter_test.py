from unittest import TestCase, main
from tested.latin_latter_package import latin_later
from tested.latin_latter_package.latin_later import stringer
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(latin_later))
    return tests


class LatTestCase(TestCase):
    def test_tat_works(self):
        self.assertEqual(stringer(), 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')


if __name__ == '__main__':
    main()
