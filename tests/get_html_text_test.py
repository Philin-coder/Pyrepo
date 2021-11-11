from unittest import TestCase, main
from tested.html_text_package import html_text
from tested.html_text_package.html_text import get_content
from tested.html_text_package.html_text import write_to_file
from tested.html_text_package.html_text import read_from_file
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(html_text))
    return tests


class MyTestCase(TestCase):
    def test_get_content_is_str(self):
        self.assertIsInstance(get_content(m_html='https://ya.ru/'), str)

    def test_get_content_is_not_empty(self):
        self.assertIsNotNone(get_content(m_html='https://ya.ru/'))

    def test_get_content_wrong(self):
        with self.assertRaises(TypeError) as e:
            get_content(m_html='https://y.ru/')
        self.assertEqual('exceptions must derive from BaseException', e.exception.args[0])

    def test_write_to_file_right(self):
        self.assertEqual(write_to_file(file_name='html_text', f_ext='txt',
                                       f_data=get_content(m_html='https://ya.ru/')), 'file_created')

    def test_write_to_file_wrong(self):
        with self.assertRaises(ValueError) as e:
            write_to_file(file_name='html_text', f_ext=123,
                          f_data=get_content(m_html='https://ya.ru/'))
        self.assertEqual('файл имеет неверный тип', e.exception.args[0])

    def test_read_from_file_is_str(self):
        self.assertIsInstance(read_from_file(file_name='html_text', f_ext='txt'), str)

    def test_write_to_file_is_not_empty(self):
        self.assertIsNotNone(read_from_file(file_name='html_text', f_ext='txt'))

    def test_write_to_file_wrong(self):
        with self.assertRaises(FileNotFoundError) as e:
            read_from_file(file_name='html_text', f_ext='123')
        self.assertEqual('Такого файла нет', e.exception.args[0])


if __name__ == '__main__':
    main()
