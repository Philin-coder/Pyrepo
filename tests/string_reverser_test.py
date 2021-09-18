from unittest import TestCase, main
from tested.string_reverser_package import string_reverser
from tested.string_reverser_package.string_reverser import string_reverser_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(string_reverser))
    return tests


class StringREverserTest(TestCase):
    def test_string_revevrse(self):
        self.assertEqual(string_reverser_func(text_str='проба первая'), 'первая проба')

    def test_string_revevrser_ints_in(self):
        with self.assertRaises(TypeError) as e:
            string_reverser_func(text_str=1)
        self.assertEqual('Введите непустую строку', e.exception.args[0])

    def test_string_revevrser_empty_in(self):
        with self.assertRaises(TypeError) as e:
            string_reverser_func(text_str='')
        self.assertEqual('Введите непустую строку', e.exception.args[0])


if __name__ == '__main__':
    main()
