from unittest import TestCase, main
from tested.without_nums_in_file_package import without_nums_filer
from tested.without_nums_in_file_package.without_nums_filer import str_without_nums
from tested.without_nums_in_file_package.without_nums_filer import write_to_file
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(without_nums_filer))
    return tests


class WithoutNumsInFileTest(TestCase):
    def test_mix_in_input(self):
        self.assertEqual(str_without_nums(mixed_str='1s2t3o4p'), 'stop')

    def test_not_str_in_input(self):
        with self.assertRaises(TypeError) as e:
            str_without_nums(mixed_str={'1s2t3o4p'})
        self.assertEqual('Передан неверный тип данных', e.exception.args[0])

    def test_write_to_file(self):
        self.assertEqual(write_to_file(file_name='test', f_ext='txt', f_data=str_without_nums(mixed_str='1s2t3o4p')),
                         'file_created')

    def test_write_to_file_wrong_data(self):
        with self.assertRaises(ValueError) as e:
            write_to_file(file_name='test', f_ext='tt', f_data=str_without_nums(mixed_str='1s2t3o4p'))
        self.assertEqual('Файл имеет неверный тип', e.exception.args[0])


if __name__ == '__main__':
    main()
