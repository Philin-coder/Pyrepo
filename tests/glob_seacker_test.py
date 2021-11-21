from unittest import TestCase, main
from tested.global_seak_package import fsp
from tested.global_seak_package.fsp import mask_finder
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(fsp))
    return tests


class MTest(TestCase):
    def test_mask_is_list(self):
        self.assertIsInstance(mask_finder(text_str='./*.py'), list)

    def test_mask_is_list_of_str_end_py(self):
        self.assertTrue((all(isinstance(i, str) for i in mask_finder(text_str='./*.py')) and all(
            i.endswith('.py') for i in mask_finder(text_str='./*.py'))) is True, 'нет строк в списке')

    def test_mask_finder_wrong(self):
        with self.assertRaises(TypeError) as e:
            mask_finder(text_str='')
        self.assertEqual('Передан неверный тип данных, либо - пустая строка', e.exception.args[0])


if __name__ == '__main__':
    main()
