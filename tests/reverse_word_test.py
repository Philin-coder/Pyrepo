from unittest import TestCase, main
from tested.reverse_word_list_package import reverse_woe_list
from tested.reverse_word_list_package.reverse_woe_list import finder
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(reverse_woe_list))
    return tests


class ReverseWoeListTest(TestCase):
    def test_simple_reverse(self):
        self.assertEqual(finder(text_str='мама мыла раму', n=1), 'алым')

    def test_simple_english_reverse(self):
        self.assertEqual(finder(text_str='asta la vista , Baby ', n=2), 'atsiv')

    def test_simple_rus_reverse_zero(self):
        self.assertEqual(finder(text_str='от топота копыт пыль по полю летит ', n=0), 'то')

    def test_empty_str_and_zero_ind(self):
        with self.assertRaises(TypeError) as e:
            finder(text_str='', n=0)
        self.assertEqual('Введите строку, затем - целое число', e.exception.args[0])

    def test_empty_str_and_zero_ind(self):
        with self.assertRaises(TypeError) as e:
            finder(text_str='1', n=0)
        self.assertEqual('Введите строку, затем - целое число', e.exception.args[0])


if __name__ == '__main__':
    main()
