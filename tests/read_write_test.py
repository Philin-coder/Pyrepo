from unittest import TestCase, main
from tested.read_write_package import read_writer
from tested.read_write_package.read_writer import gen_cont_file
from tested.read_write_package.read_writer import write_to_file
from tested.read_write_package.read_writer import file_reader
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(read_writer))
    return tests


class MyReadWriteTest(TestCase):
    def test_str_in_input(self):
        self.assertEqual(gen_cont_file(data_str='проба'), 'проба')

    def test_wrong_input(self):
        with self.assertRaises(TypeError) as e:
            gen_cont_file(data_str='')
        self.assertEqual('Передан неверный  тип данных', e.exception.args[0])

    def test_right_in_file(self):
        self.assertEqual(write_to_file(file_name='test', f_ext='txt', fdata=gen_cont_file(data_str='проба')),
                         'file_created')

    def test_wrong_in_file(self):
        with self.assertRaises(ValueError) as e:
            write_to_file(file_name='test', f_ext='tt', fdata=gen_cont_file(data_str='проба'))
        self.assertEqual('Файл имеет неверное расширение', e.exception.args[0])

    def test_right_reader(self):
        self.assertEqual(file_reader(file_name='test', f_ext='txt'), ['проба\n'])

    def test_wrong_reader(self):
        with self.assertRaises(FileNotFoundError) as e:
            file_reader(file_name='tes', f_ext='tx')
        self.assertEqual('это  не файл', e.exception.args[0])


if __name__ == '__main__':
    main()
