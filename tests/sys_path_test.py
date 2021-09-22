from unittest import TestCase, main, expectedFailure
from tested.sis_path_pacage import system_path
from tested.sis_path_pacage.system_path import find_path
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(system_path))
    return tests


class SysTest(TestCase):
    # @expectedFailure
    def testFilePath_works(self):
        self.assertEqual(find_path(), 'F:\\code\\Result\\Python\\template\\tested\\sis_path_pacage',
                         '//home//runner//work//Pyrepo/Pyrepo//tested//sis_path_pacage')


if __name__ == '__main__':
    main()
