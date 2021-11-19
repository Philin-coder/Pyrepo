from unittest import TestCase, main
from tested.one_more_json_read_writer_package import jsoner
from tested.one_more_json_read_writer_package.jsoner import cont_gen
from tested.one_more_json_read_writer_package.jsoner import conv_data
from tested.one_more_json_read_writer_package.jsoner import write_file
from tested.one_more_json_read_writer_package.jsoner import read_file
from tested.one_more_json_read_writer_package.jsoner import as_it_was
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(jsoner))
    return tests


class MyTestCase(TestCase):
    def test_cont_gen_right(self):
        self.assertEqual(cont_gen(text_str='text string'), 'text string')

    def test_cont_gen_wrong(self):
        with self.assertRaises(TypeError) as e:
            cont_gen(text_str=123)
        self.assertEqual('передан неверный тип данных, либо - пустая строка', e.exception.args[0])

    def test_conv_data_right(self):
        self.assertEqual(conv_data(text=cont_gen(text_str='text string')), {'text': 'word', 'string': 'word'})

    def test_data_conv_data_wrong(self):
        with self.assertRaises(TypeError) as e:
            conv_data(text=cont_gen(text_str=''))
        self.assertEqual('передан неверный тип данных, либо - пустая строка', e.exception.args[0])

    def test_write_to_file_right(self):
        self.assertEqual(write_file(filename='data1.json', fdata=conv_data(text=cont_gen(text_str='text string'))),
                         'file_created')

    def test_write_to_file_wrong(self):
        with self.assertRaises(ValueError) as e:
            write_file(filename='data.jso', fdata=conv_data(text=cont_gen(text_str='text string')))
        self.assertEqual('Файл имеет неверный тип', e.exception.args[0])

    def test_read_file_right(self):
        self.assertEqual(read_file(filename='data1.json'), {'text': 'word', 'string': 'word'})

    def test_file_read_wrong(self):
        with self.assertRaises(FileNotFoundError) as e:
            read_file(filename='dat.json')
        self.assertEqual('нет такого файла', e.exception.args[0])

    def test_as_it_was_right(self):
        self.assertEqual(as_it_was(fdata=read_file(filename='data1.json')), 'text, string')

    def test_as_it_was_wrong(self):
        with self.assertRaises(TypeError) as e:
            as_it_was(fdata=str('t'))
        self.assertEqual('Передан неверный тип данных', e.exception.args[0])


if __name__ == '__main__':
    main()
