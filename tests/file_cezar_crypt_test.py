from unittest import TestCase, main
from tested.file_cezar_crypt_package import cezar_crypter
from tested.file_cezar_crypt_package.cezar_crypter import to_cript_word
from tested.file_cezar_crypt_package.cezar_crypter import write_file
from tested.file_cezar_crypt_package.cezar_crypter import file_read
from tested.file_cezar_crypt_package.cezar_crypter import cesar_encode
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(cezar_crypter))
    return tests


class FileCezarCryptTest(TestCase):
    def test_to_cript_word_right(self):
        self.assertEqual(to_cript_word(text_str='ave cezar'), 'ave cezar')

    def test_to_cript_word_wrong(self):
        with self.assertRaises(TypeError) as e:
            to_cript_word(text_str='')
        self.assertEqual('Передан неверный тип данных', e.exception.args[0])

    def test_write_to_file_right(self):
        self.assertEqual(
            write_file(file_name='to_cript_text', f_ext='txt', f_fdata=to_cript_word(text_str='ave cezar')),
            'file_created')

    def test_write_to_file_wrong(self):
        with self.assertRaises(ValueError) as e:
            write_file(file_name='to_cript_text', f_ext='tt', f_fdata=to_cript_word(text_str='ave cezar'))
        self.assertEqual('Файл имеет неверный тип', e.exception.args[0])

    def test_file_reader_right(self):
        self.assertEqual(file_read(file_name='to_cript_text', f_ext='txt'), 'ave cezar ')

    def test_file_reader_wrong(self):
        with self.assertRaises(FileNotFoundError) as e:
            file_read(file_name='to_cript_tex', f_ext='txt')
        self.assertEqual('нет такого файла', e.exception.args[0])

    def test_cesar_encode_right(self):
        self.assertEqual(cesar_encode(line=file_read(file_name='to_cript_text', f_ext='txt'), shift=1), 'bwf df{bs ')

    def test_cesar_encode_wrong(self):
        with self.assertRaises(TypeError) as e:
            cesar_encode(line='', shift=1)
        self.assertEqual('Передан неверный тип данных, или неверный диапазон шага', e.exception.args[0])


if __name__ == '__main__':
    main()
