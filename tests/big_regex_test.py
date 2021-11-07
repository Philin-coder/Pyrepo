from unittest import TestCase, main
from big_regex_package import regexer
from big_regex_package.regexer import cont_gen
from big_regex_package.regexer import write_to_file
from big_regex_package.regexer import one_sym
from big_regex_package.regexer import one_letter
from big_regex_package.regexer import letters_with_spaces
from big_regex_package.regexer import letters_only
from big_regex_package.regexer import first_word_only

import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(regexer))
    return tests


class BigRegexTest(TestCase):
    def test_cont_gen_right_input(self):
        self.assertEqual(cont_gen(file_cont='AV is largest Analytics community of India'),
                         'AV is largest Analytics community of India')

    def test_cont_gen_wrong_input(self):
        with self.assertRaises(TypeError) as e:
            cont_gen(file_cont={'AV is largest Analytics community of India'})
        self.assertEqual('Передан неверный тип данных', e.exception.args[0])

    def test_write_to_file_right(self):
        self.assertEqual(write_to_file(file_name='r_test', f_ext='txt',
                                       fdata=cont_gen(file_cont='AV is largest Analytics community of India')),
                         'file_created')

    def test_write_to_file_wrong(self):
        with self.assertRaises(ValueError) as e:
            write_to_file(file_name='r_test', f_ext='tt',
                          fdata=cont_gen(file_cont='AV is largest Analytics community of India'))
        self.assertEqual('Файл имеет неправильный тип ', e.exception.args[0])

    def test_one_sym_right(self):
        self.assertEqual(one_sym(my_filename='r_test', f_ext='txt'),
                         ['[', "'", 'A', 'V', ' ', 'i', 's', ' ', 'l', 'a', 'r', 'g', 'e', 's', 't', ' ', 'A', 'n', 'a',
                          'l', 'y', 't', 'i', 'c', 's', ' ', 'c', 'o', 'm', 'm', 'u', 'n', 'i', 't', 'y', ' ', 'o', 'f',
                          ' ', 'I', 'n', 'd', 'i', 'a', '\\', 'n', "'", ']'])

    def test_one_sym_wrong(self):
        with self.assertRaises(FileNotFoundError) as e:
            one_sym(my_filename='r_test', f_ext='tt')
        self.assertEqual('Файл имеет неверный тип ', e.exception.args[0])

    def test_one_letter_right(self):
        self.assertEqual(one_letter(my_filename='r_test', f_ext='txt'),
                         ['A', 'V', 'i', 's', 'l', 'a', 'r', 'g', 'e', 's', 't', 'A', 'n', 'a', 'l', 'y', 't', 'i', 'c',
                          's', 'c', 'o', 'm', 'm', 'u', 'n', 'i', 't', 'y', 'o', 'f', 'I', 'n', 'd', 'i', 'a', 'n'])

    def test_one_letter_wrong(self):
        with self.assertRaises(FileNotFoundError) as e:
            one_letter(my_filename='r_test', f_ext='tt')
        self.assertEqual('Файл имеет неверный тип ', e.exception.args[0])

    def test_letters_with_spaces_right(self):
        self.assertEqual(letters_with_spaces(my_filename='r_test', f_ext='txt'),
                         ['', '', 'AV', '', 'is', '', 'largest', '', 'Analytics', '', 'community', '', 'of', '',
                          'India', '', 'n', '', '', ''])

    def test_letters_with_spaces_wrong(self):
        with self.assertRaises(FileNotFoundError) as e:
            letters_with_spaces(my_filename='r_test', f_ext='tt')
        self.assertEqual('Файл имеет неверный тип ', e.exception.args[0])

    def test_letters_only_right(self):
        self.assertEqual(letters_only(my_filename='r_test', f_ext='txt'),
                         ['AV', 'is', 'largest', 'Analytics', 'community', 'of', 'India', 'n'])

    def test_letters_only_wrong(self):
        with self.assertRaises(FileNotFoundError) as e:
            letters_only(my_filename='r_test', f_ext='tt')
        self.assertEqual('Файл имеет неверный тип ', e.exception.args[0])


if __name__ == '__main__':
    main()
