from unittest import TestCase, main
from tested.most_common_in_file_package import most_com
from tested.most_common_in_file_package.most_com import cont_gen
from tested.most_common_in_file_package.most_com import data_conv_str
from tested.most_common_in_file_package.most_com import write_file
from tested.most_common_in_file_package.most_com import most_common_sym
import doctest
from collections import Counter


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(most_com))
    return tests


class CommInFileTest(TestCase):
    def test_cont_gen_right(self):
        self.assertEqual(cont_gen(start_p=97, end_p=123, num=10),
                         ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                          't', 'u', 'v', 'w', 'x', 'y', 'z', 'kk'])

    def test_cont_gen_wrong(self):
        with self.assertRaises(TypeError) as e:
            cont_gen(start_p=97, end_p='123', num='10')
        self.assertEqual('Передан неверный тип данных', e.exception.args[0])

    def test_data_conv_str_right(self):
        self.assertEqual(data_conv_str(letters=cont_gen(start_p=97, end_p=123, num=10)), 'abcdefghijklmnopqrstuvwxyzkk')

    def test_data_conv_str_wrong(self):
        with self.assertRaises(TypeError) as e:
            data_conv_str(letters=[])
        self.assertEqual('Передан не список, либо,-список пуст', e.exception.args[0])

    def test_write_to_file_right(self):
        self.assertEqual(write_file(filename='com_test', f_ext='txt',
                                    fdata=data_conv_str(letters=cont_gen(start_p=97, end_p=123, num=10))),
                         'file_created')

    def test_write_to_file_wrong(self):
        with self.assertRaises(ValueError) as e:
            write_file(filename='com_test', f_ext='tt',
                       fdata=data_conv_str(letters=cont_gen(start_p=97, end_p=123, num=10)))
        self.assertEqual('Файл имеет неверный тип', e.exception.args[0])

    def test_most_common_sym_right(self):
        self.assertEqual(most_common_sym(filename='com_test', f_ext='txt'), Counter(
            {'k': 3, 'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1, 'h': 1, 'i': 1, 'j': 1, 'l': 1, 'm': 1,
             'n': 1, 'o': 1, 'p': 1, 'q': 1, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 1, 'w': 1, 'x': 1, 'y': 1, 'z': 1}))

    def test_most_common_sym_wrong(self):
        with self.assertRaises(FileNotFoundError) as e:
            most_common_sym(filename='com_test', f_ext='tt')
        self.assertEqual('Такого файла нет ', e.exception.args[0])


if __name__ == '__main__':
    main()
