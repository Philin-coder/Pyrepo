from unittest import TestCase, main
from tested.cleaner_package import cleaner
from tested.cleaner_package.cleaner import cont_gen
from tested.cleaner_package.cleaner import write_to_file
from tested.cleaner_package.cleaner import read_file
from tested.cleaner_package.cleaner import searcher
from tested.cleaner_package.cleaner import res_writer
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(cleaner))
    return tests


class RegReadWriteTest(TestCase):
    def test_cont_gen_is_str(self):
        self.assertIsInstance(cont_gen(title_str='python'), str)

    def test_get_content_is_not_empty(self):
        self.assertIsNotNone(cont_gen(title_str='python'))

    def test_alpha_and_nums(self):
        self.assertTrue((any([i.isdigit() for i in cont_gen(title_str='python')]) and (any(
            [i.isalpha() for i in cont_gen(title_str='python')]))), 'не содержит цифр и букв')

    def test_get_content_wrong(self):
        with self.assertRaises(TypeError) as e:
            cont_gen(title_str='')
        self.assertEqual('Передан неверный тип данных, или -пустая строка', e.exception.args[0])

    def test_write_to_file_right(self):
        self.assertEqual(write_to_file(file_name='wiki2', f_ext='txt', f_data=cont_gen(title_str='python')),
                         'file_created')

    def test_write_to_file_wrong(self):
        with self.assertRaises(ValueError) as e:
            write_to_file(file_name='wiki2', f_ext='tt', f_data=cont_gen(title_str='PYTHON'))
        self.assertEqual('Файл имеет неверный тип', e.exception.args[0])

    def test_file_reader_is_str(self):
        self.assertIsInstance(read_file(file_name='wiki2', f_ext='txt'), str)

    def test_file_reader_is_not_empty(self):
        self.assertIsNotNone(read_file(file_name='wiki2', f_ext='txt'))

    def test_file_reader_wrong(self):
        with self.assertRaises(FileNotFoundError) as e:
            read_file(file_name='wik', f_ext='txt')
        self.assertEqual('нет такого файла', e.exception.args[0])

    def test_searcher_is_str(self):
        self.assertIsInstance(searcher(work_str=read_file(file_name='wiki2', f_ext='txt')), str)

    def test_searcher_is_not_empty(self):
        self.assertIsNotNone(searcher(work_str=read_file(file_name='wiki2', f_ext='txt')))

    def test_res_writer_right(self):
        self.assertEqual(res_writer(file_name='res', f_ext='txt',
                                    f_data=searcher(work_str=read_file(file_name='wiki2', f_ext='txt'))),
                         'file_created')

    def test_res_writer_wrong(self):
        with self.assertRaises(ValueError) as e:
            res_writer(file_name='res', f_ext='123',
                       f_data=searcher(work_str=read_file(file_name='wiki2', f_ext='txt')))
        self.assertEqual('Файл имеет неверный тип', e.exception.args[0])


if __name__ == '__main__':
    main()
