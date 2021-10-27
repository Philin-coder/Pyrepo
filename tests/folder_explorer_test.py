from unittest import TestCase, main
from tested.folder_exolorer_package import folder_exp
from tested.folder_exolorer_package.folder_exp import folder_explorer
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(folder_exp))
    return tests


class MyTestCase(TestCase):
    def test_works(self):
        self.assertIsInstance(folder_explorer(), str)


if __name__ == '__main__':
    main()
