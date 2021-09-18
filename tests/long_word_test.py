from unittest import TestCase, main
from tested.longest_word_package import longest_word
from tested.longest_word_package.longest_word import long_word
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(longest_word))
    return tests


class longWordTestCase(TestCase):
    def test_long_word(self):
        self.assertEqual(long_word(text_str='Проба третья'), (6, 'третья'))

    def test_long_word_wrong(self):
        with self.assertRaises(ValueError) as e:
            long_word(text_str='')
        self.assertEqual('Введите строку', e.exception.args[0])


if __name__ == '__main__':
    main()
