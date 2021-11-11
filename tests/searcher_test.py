from unittest import TestCase, main
from tested.search_in_file_package import searcher
from tested.search_in_file_package.searcher import cont_gen
from tested.search_in_file_package.searcher import write_to_file
from tested.search_in_file_package.searcher import file_reader
from tested.search_in_file_package.searcher import wordfinder
from tested.search_in_file_package.searcher import max_digit_finder
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(searcher))
    return tests


class Search(TestCase):
    def test_get_content_is_str(self):
        self.assertIsInstance(cont_gen(title_pages='Facebook'), str)

    def test_get_content_is_not_empty(self):
        self.assertIsNotNone(cont_gen(title_pages='Facebook'))

    def test_get_content_wrong(self):
        with self.assertRaises(TypeError) as e:
            cont_gen(title_pages='')
        self.assertEqual('передан неверный тип данных,либо -пустая строка', e.exception.args[0])

    def test_write_to_file_right(self):
        self.assertEqual(write_to_file(file_name='wiki_test', f_ext='txt', f_data=cont_gen(title_pages='Facebook')),
                         'file_created')

    def test_write_to_file_wrong(self):
        with self.assertRaises(ValueError) as e:
            write_to_file(file_name='wiki_test', f_ext='tt', f_data=cont_gen(title_pages='Facebook'))
        self.assertEqual('файл имеет неверный тип', e.exception.args[0])

    def test_file_reader_right(self):
        self.assertIsInstance(file_reader(file_name='wiki_test', f_ext='txt'), list)

    def test_file_reader_is_not_empty(self):
        self.assertIsNotNone(file_reader(file_name='wiki_test', f_ext='txt'))

    def test_file_reader_wrong(self):
        with self.assertRaises(FileNotFoundError) as e:
            file_reader(file_name='wiki_test', f_ext='123')
        self.assertEqual('нет такого файла', e.exception.args[0])

    def test_word_finders_is_list(self):
        self.assertIsInstance(wordfinder(conv_data=file_reader(file_name='wiki_test', f_ext='txt')), list)

    def test_word_finders_is_list_of_strings(self):
        self.assertTrue(
            (all([isinstance(i, str) for i in
                  wordfinder(conv_data=file_reader(file_name='wiki_test', f_ext='txt'))])) is True,
            'не буква')

    def test_word_finders_is_not_empty(self):
        self.assertIsNotNone(wordfinder(conv_data=file_reader(file_name='wiki_test', f_ext='txt')))

    def test_word_finders_wrong(self):
        with self.assertRaises(TypeError) as e:
            wordfinder(conv_data=123)
        self.assertEqual('Передан неверный тип данных, либо - пустой список', e.exception.args[0])

    def test_max_digit_finder(self):
        self.assertEqual(max_digit_finder(conv_data=file_reader(file_name='wiki_test', f_ext='txt')), 2004)

    # def test_digit_finders_is_int(self):
    #     self.assertIsInstance(max_digit_finder(conv_data=file_reader(file_name='wiki_test', f_ext='txt')), int)

    def test_max_digit_finder_wrong(self):
        with self.assertRaises(TypeError) as e:
            max_digit_finder(conv_data=[])
        self.assertEqual('Передан неверный тип данных, либо - пустой список', e.exception.args[0])


if __name__ == '__main__':
    main()
