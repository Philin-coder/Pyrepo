from unittest import TestCase, main
from tested.j_son_read_write_package import jsoner
from tested.j_son_read_write_package.jsoner import cont_gen
from tested.j_son_read_write_package.jsoner import data_convert
from tested.j_son_read_write_package.jsoner import write_file
from tested.j_son_read_write_package.jsoner import file_read
from tested.j_son_read_write_package.jsoner import as_str
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(jsoner))
    return tests


class MyTest(TestCase):
    def test_cont_gen_right(self):
        self.assertEqual(cont_gen(text_str='to be writen in Json'), 'to be writen in Json')

    def test_cont_gen_wrong(self):
        with self.assertRaises(TypeError) as e:
            cont_gen(text_str='')
        self.assertEqual('Передан неверный тип данных, либо  - пустая строка', e.exception.args[0])

    def test_data_convert_right(self):
        self.assertEqual(data_convert(conv_data=cont_gen(text_str='to be writen in Json')),
                         {'to': 'word', 'be': 'word', 'writen': 'word', 'in': 'word', 'Json': 'word'})

    def test_data_convert_wrong(self):
        with self.assertRaises(TypeError) as e:
            data_convert(conv_data=cont_gen(text_str={'to be writen in Json'}))
        self.assertEqual('Передан неверный тип данных, либо  - пустая строка', e.exception.args[0])

    def test_write_to_file_right(self):
        self.assertEqual(write_file(file_name='', f_ext='json',
                                    f_data=data_convert(conv_data=cont_gen(text_str='to be writen in Json'))),
                         'file_created')

    def test_file_read(self):
        self.assertEqual(file_read(file_name='data', f_ext='json'),
                         {'to': 'word', 'be': 'word', 'writen': 'word', 'in': 'word', 'Json': 'word'})

    def test_file_read_wrong(self):
        with self.assertRaises(FileNotFoundError) as e:
            file_read(file_name='data', f_ext='234son')
        self.assertEqual('нет такого файла', e.exception.args[0])

    def test_as_str_right(self):
        self.assertEqual(as_str(f_data=file_read(file_name='data', f_ext='json')), 'to  be  writen  in  Json')

    def test_data_conv_str_wrong(self):
        with self.assertRaises(TypeError) as e:
            as_str(f_data=tuple(file_read(file_name='data', f_ext='json')))
        self.assertEqual('Передан неверный тип данных', e.exception.args[0])


if __name__ == '__main__':
    main()
