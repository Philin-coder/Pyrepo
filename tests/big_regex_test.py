from unittest import TestCase, main
from tested.big_regex_package import regexer
from tested.big_regex_package.regexer import cont_gen
from tested.big_regex_package.regexer import write_to_file
from tested.big_regex_package.regexer import one_sym
from tested.big_regex_package.regexer import one_letter
from tested.big_regex_package.regexer import letters_with_spaces
from tested.big_regex_package.regexer import letters_only
from tested.big_regex_package.regexer import first_word_only
from tested.big_regex_package.regexer import last_word_only
from tested.big_regex_package.regexer import two_letters_from_begin_no_spaces
from tested.big_regex_package.regexer import two_letters_from_begin_no_spaces_as_word
from tested.big_regex_package.regexer import dom_finder
from tested.big_regex_package.regexer import date_finder
from tested.big_regex_package.regexer import year_finder
from tested.big_regex_package.regexer import vols_in_begin
from tested.big_regex_package.regexer import invert_search
from tested.big_regex_package.regexer import invert_search_with_space
from tested.big_regex_package.regexer import num_checker
from tested.big_regex_package.regexer import str_cleaner
from tested.big_regex_package.regexer import str_cleaner_spaces
from tested.big_regex_package.regexer import html_cleaner
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

    def test_first_word_only_right(self):
        self.assertEqual(first_word_only(text_str='AV is largest Analytics community of India'), ['AV'])

    def test_first_word_only_wrong(self):
        with self.assertRaises(TypeError) as e:
            first_word_only(text_str=123)
        self.assertEqual('Передана не строка, или-строка пуста', e.exception.args[0])

    def test_last_word_only_right(self):
        self.assertEqual(last_word_only(text_str='AV is largest Analytics community of India'), ['India'])

    def test_last_word_only_wrong(self):
        with self.assertRaises(TypeError) as e:
            last_word_only(text_str=123)
        self.assertEqual('Передана не строка, или-строка пуста', e.exception.args[0])

    def test_two_letters_from_begin_no_spaces(self):
        self.assertEqual(two_letters_from_begin_no_spaces(my_filename='r_test', f_ext='txt'),
                         ['AV', 'is', 'la', 'rg', 'es', 'An', 'al', 'yt', 'ic', 'co', 'mm', 'un', 'it', 'of', 'In',
                          'di'])

    def test_two_letters_from_begin_no_spaces_as_word_right(self):
        self.assertEqual(two_letters_from_begin_no_spaces_as_word(my_filename='r_test', f_ext='txt'),
                         ['AV', 'is', 'la', 'An', 'co', 'of', 'In', "n'"])

    def test_dom_finder_right(self):
        self.assertEqual(
            dom_finder(text_str='abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz'),
            ['com', 'in', 'com', 'biz'])

    def test_dom_finder_wrong(self):
        with self.assertRaises(TypeError) as e:
            dom_finder(text_str=123)
        self.assertEqual('Передана не строка, или-строка пуста', e.exception.args[0])

    def test_date_finder_right(self):
        self.assertEqual(
            date_finder(text_str='Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009'),
            ['12-05-2007', '11-11-2011', '12-01-2009'])

    def test_date_finder_wrong(self):
        with self.assertRaises(TypeError) as e:
            date_finder(text_str='')
        self.assertEqual('Передана не строка, или-строка пуста', e.exception.args[0])

    def test_year_finder_right(self):
        self.assertEqual(
            year_finder(text_str='Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009'),
            ['2007', '2011', '2009'])

    def test_year_finder_wrong(self):
        with self.assertRaises(TypeError) as e:
            year_finder(text_str='')
        self.assertEqual('Передана не строка, или-строка пуста', e.exception.args[0])

    def test_vols_in_begin_right(self):
        self.assertEqual(vols_in_begin(text_str='Task, is , very very, difficult to Me'), ['is'])

    def test_vols_in_begin_wrong(self):
        with self.assertRaises(TypeError) as e:
            vols_in_begin(text_str='')
        self.assertEqual('Передана не строка, или-строка пуста', e.exception.args[0])

    def test_invert_search_right(self):
        self.assertEqual(invert_search(text_str='Task, is , very very, difficult to Me'),
                         ['Task', 'very', ' very', 'difficult', ' to', ' Me'])

    def test_invert_search_wrong(self):
        with self.assertRaises(TypeError) as e:
            invert_search(text_str='')
        self.assertEqual('Передана не строка, или-строка пуста', e.exception.args[0])

    def test_invert_search_with_spaces_right(self):
        self.assertEqual(invert_search_with_space(text_str='AV is largest Analytics community of India'),
                         ['largest', 'community'])

    def test_invert_search_with_spaces_wrong(self):
        with self.assertRaises(TypeError) as e:
            invert_search_with_space(text_str='')
        self.assertEqual('Передана не строка, или-строка пуста', e.exception.args[0])

    def test_num_checker_right(self):
        self.assertEqual(num_checker(nums=['9999999999', '999999-999', '99999x9999']), 'yes')

    def test_num_checker_wrong(self):
        with self.assertRaises(TypeError) as e:
            num_checker(nums=[])
        self.assertEqual('Передан не список , или-список пуст', e.exception.args[0])

    def test_str_cleaner_right(self):
        self.assertEqual(str_cleaner(text_str='no more;fake,snd,lie,for me'),
                         ['no', 'more', 'fake', 'snd', 'lie', 'for', 'me'])

    def test_str_cleaner_wrong(self):
        with self.assertRaises(TypeError) as e:
            str_cleaner(text_str='')
        self.assertEqual('Передан неверный тип данных', e.exception.args[0])

    def test_str_cleaner_spaces_right(self):
        self.assertEqual(str_cleaner_spaces(text_str='no more;fake,snd,lie,for me'), 'no more fake snd lie for me')

    def test_str_cleaner_spaces_wrong(self):
        with self.assertRaises(TypeError) as e:
            str_cleaner_spaces(text_str='')
        self.assertEqual('Передан неверный тип данных', e.exception.args[0])

    def test_html_cleaner_right(self):
        self.assertEqual(
            html_cleaner(text_str='1NoahEmma2LiamOlivia3MasonSophia4JacobIsabella5WilliamAva6EthanMia7MichaelEmily'),
            [('Noah', 'Emma'), ('Liam', 'Olivia'), ('Mason', 'Sophia'), ('Jacob', 'Isabella'), ('William', 'Ava'),
             ('Ethan', 'Mia'), ('Michael', 'Emily')])

    def test_html_cleaner_wrong(self):
        with self.assertRaises(TypeError) as e:
            html_cleaner(text_str='')
        self.assertEqual('Передан неверный тип данных', e.exception.args[0])


if __name__ == '__main__':
    main()
