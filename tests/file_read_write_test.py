from unittest import TestCase, main
from tested.one_another_text_file_creator_package import file_creator
from tested.one_another_text_file_creator_package.file_creator import gen_cont
from tested.one_another_text_file_creator_package.file_creator import file_write
from tested.one_another_text_file_creator_package.file_creator import file_reader
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(file_creator))
    return tests


class FileReadWriteTest(TestCase):
    def test_cont_gen_right(self):
        self.assertEqual(gen_cont('yes'), 'yes')

    def test_cont_gen_wrong(self):
        with self.assertRaises(TypeError) as e:
            gen_cont('')
        self.assertEqual('Передан неверный тип данных, либо-пустая строка', e.exception.args[0])

    def test_file_create_right(self):
        self.assertEqual(file_write('n_test', f_ext='txt', fdata=gen_cont('yes')), 'file_created')

    def test_file_create_wrong(self):
        with self.assertRaises(ValueError) as e:
            file_write('n_test', f_ext=123, fdata=gen_cont('yes'))
        self.assertEqual('файл имеет неверный тип', e.exception.args[0])

    def test_file_reader_right(self):
        self.assertEqual(file_reader(file_name='n_test', f_ext='txt'), 'yes ')

    def test_file_reader_wrong(self):
        with self.assertRaises(FileNotFoundError) as e:
            file_reader(file_name='n_tt', f_ext='txt')
        self.assertEqual('это не файл', e.exception.args[0])


if __name__ == '__main__':
    main()
