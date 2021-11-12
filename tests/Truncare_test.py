from unittest import TestCase, main
from tested.truncate_pacage import truncater
from tested.truncate_pacage.truncater import cont_gen
from tested.truncate_pacage.truncater import write_to_file
from tested.truncate_pacage.truncater import reader
from tested.truncate_pacage.truncater import trunc
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(truncater))
    return tests


class TruncateTest(TestCase):
    def test_cont_gen_right(self):
        self.assertEqual(cont_gen(c_str='to_be_truncated_string'), 'to_be_truncated_string')

    def test_cont_gen_wrong(self):
        with self.assertRaises(TypeError) as e:
            cont_gen(c_str='')
        self.assertEqual('Передан неправильный тип данных, либо - пустая строка', e.exception.args[0])

    def test_write_to_file_right(self):
        self.assertEqual(
            write_to_file(my_filename='tr_test', f_ext='txt', fdata=cont_gen(c_str='to_be_truncated_string')),
            'file_created')

    def test_write_to_file_wrong(self):
        with self.assertRaises(ValueError) as e:
            write_to_file(my_filename='tr_test', f_ext='tt', fdata=cont_gen(c_str='to_be_truncated_string'))
        self.assertEqual('Файл имеет неверный тип', e.exception.args[0])

    def test_file_reader_right(self):
        self.assertEqual(reader(my_filename='tr_test', f_ext='txt'), ['to_be_truncated_string\n'])

    def test_file_reader_wrong(self):
        with self.assertRaises(FileNotFoundError) as e:
            reader(my_filename='tr_tet', f_ext='txt')
        self.assertEqual('Такого файла нет', e.exception.args[0])

    def test_trunc_right(self):
        self.assertEqual(trunc(my_filename='tr_test', f_ext='txt'), 'file_truncated')

    def test_trunc_wrong(self):
        with self.assertRaises(FileNotFoundError) as e:
            trunc(my_filename='tr_test', f_ext='tt')
        self.assertEqual('нет такого файла', e.exception.args[0])


if __name__ == '__main__':
    main()
