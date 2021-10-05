from unittest import TestCase, main
from tested.astrix_replacer_package import astrix_latin_replacer
from tested.astrix_replacer_package.astrix_latin_replacer import find_replacer_astrix_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(astrix_latin_replacer))
    return tests


class AstrixTest(TestCase):
    def test_simple_string(self):
        self.assertEqual(find_replacer_astrix_func(text_str='test'), 'test')

    def test_astrix_string(self):
        self.assertEqual(find_replacer_astrix_func(text_str='kas*tle'), '...')

    def test_rus_string(self):
        self.assertEqual(find_replacer_astrix_func(text_str='проб*а'), 'проб')

    def test_dig_string(self):
        with self.assertRaises(TypeError) as e:
            find_replacer_astrix_func(text_str=123)
        self.assertEqual('Введите  строку ', e.exception.args[0])

    def test_hidden_dig_string(self):
        with self.assertRaises(TypeError) as e:
            find_replacer_astrix_func(text_str='123')
        self.assertEqual('Введите  строку ', e.exception.args[0])


if __name__ == '__main__':
    main()
