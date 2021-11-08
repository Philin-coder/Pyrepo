from unittest import TestCase, main
from tested.file_sym_count_package import fs_counter
from tested.file_sym_count_package.fs_counter import cont_gen
from tested.file_sym_count_package.fs_counter import write_to_file
from tested.file_sym_count_package.fs_counter import file_reader
from tested.file_sym_count_package.fs_counter import sym_counter
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(fs_counter))
    return tests


class FileSymCountTest(TestCase):
    def test_cont_gen_right_input(self):
        self.assertEqual(cont_gen(text_str='просто данные'), 'просто данные')

    def test_cont_gen_wrong_input(self):
        with self.assertRaises(TypeError) as e:
            cont_gen(text_str={'просто данные'})
        self.assertEqual('Пeредан неверный тип данных.', e.exception.args[0])

    def test_write_to_file_right(self):
        self.assertEqual(write_to_file(my_filename='c_test', f_ext='txt', fdata=cont_gen(text_str='просто данные ')),
                         'file_created')

    def test_write_to_file_wrong_data(self):
        with self.assertRaises(TypeError) as e:
            write_to_file(my_filename='c_test', f_ext=1, fdata=cont_gen(text_str='просто данные '))
        self.assertEqual('Файл имеет неверный тип ', e.exception.args[0])

    def test_file_reader_right(self):
        self.assertEqual(file_reader(my_filename='c_test', f_ext='txt'), ['просто данные \n'])

    def test_file_reader_wrong(self):
        with self.assertRaises(FileNotFoundError) as e:
            file_reader(my_filename='tst', f_ext='txt')
        self.assertEqual('это не файл', e.exception.args[0])

    def test_sym_counter_right(self):
        self.assertEqual(sym_counter(c_data=file_reader(my_filename='c_test', f_ext='txt'), ch='о'), 2)

    def test_sym_counter_wrong(self):
        with self.assertRaises(TypeError) as e:
            sym_counter(c_data=[], ch='о')
        self.assertEqual('Передан не список, либо список пуст ', e.exception.args[0])


if __name__ == '__main__':
    main()
