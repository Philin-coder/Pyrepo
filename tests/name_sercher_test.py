from unittest import TestCase, main
from tested.file_searcher_package import searcher
from tested.file_searcher_package.searcher import file_write
from tested.file_searcher_package.searcher import file_read
from tested.file_searcher_package.searcher import name_searcher
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(searcher))
    return tests


class SearchInFileTest(TestCase):
    def test_write_to_file_right(self):
        self.assertEqual(file_write(file_name='phone_test', fext='txt',
                                    full_names=['John Doe 995678378274 8953894859 783748583', 'Adilet 995782738783',
                                                'Ivan Pupkin 738428374827 78382738482']), 'file_created')

    def test_write_to_file_wrong(self):
        with self.assertRaises(TypeError) as e:
            file_write(file_name='phone_test', fext='txt', full_names=None)
        self.assertEqual('Передан неверный тип данных, ли -пустой список', e.exception.args[0])

    def test_file_read_right(self):
        self.assertEqual(file_read(file_name='phone_test', f_ext='txt'), [
            "['John Doe 995678378274 8953894859 783748583', " \
            "'Adilet 995782738783', 'Ivan Pupkin 738428374827 78382738482']\n"])

    def test_file_reader_wrong(self):
        with self.assertRaises(ValueError) as e:
            file_read(file_name='phone_test', f_ext='123')
        self.assertEqual('Файл имеет неверный тип', e.exception.args[0])

    def test_name_searcher_right(self):
        self.assertEqual(name_searcher(file_name='phone_test', fext='txt'),
                         ' John Doe 995678378274 8953894859 783748583   Adilet 995782738783   Ivan Pupkin 738428374827 78382738482 ')

    def test_name_searcher_wrong(self):
        with self.assertRaises(FileNotFoundError) as e:
            name_searcher(file_name='phone_test', fext='t')
        self.assertEqual('нет такого файла', e.exception.args[0])


if __name__ == '__main__':
    main()
