from unittest import TestCase, main
from tested.mask_finder_package import mask_finder
from tested.mask_finder_package.mask_finder import get_files
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(mask_finder))
    return tests


class MaskTest(TestCase):
    def test_get_files_list(self):
        self.assertIsInstance(get_files(msk='*.py'), list)

    def test_str_in_list(self):
        self.assertTrue((all(isinstance(i, str) for i in get_files(msk='*.py'))) is True, 'в списке не строки')

    def test_end_mask(self):
        self.assertTrue(
            ('*.py'.endswith('py') and (
                all(i.endswith('.py') for i in get_files(msk='*.py')))) is True,
            'не совпадают с маской')

    def test_get_files_wrong(self):
        with self.assertRaises(TypeError) as e:
            get_files(msk='')
        self.assertEqual('Передан неверный тип данных', e.exception.args[0])


if __name__ == '__main__':
    main()
