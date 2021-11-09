from unittest import TestCase, main, skipUnless
from tested.disk_letter_package import disk_letterer
from tested.disk_letter_package.disk_letterer import disk_letter_func
import doctest
import sys


@skipUnless(sys.platform.startswith("win"), "requires Windows")
def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(disk_letterer))
    return tests


class DiskLetterTest(TestCase):
    def test_is_list(self):
        self.assertIsInstance(disk_letter_func(letters=(
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z')), list)

    @skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_get_disc(self):
        self.assertEqual(disk_letter_func(letters=(
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V',
            'W', 'X', 'Y', 'Z')), ['C:', 'D:', 'E:', 'F:', 'G:'])

    def test_get_wrong(self):
        with self.assertRaises(TypeError) as e:
            disk_letter_func(letters=None)
        self.assertEqual('Передан неверный тип данных', e.exception.args[0])


if __name__ == '__main__':
    main()
