from unittest import TestCase, main
from tested.regex_punctuation_del_package import regex_p_del
from tested.regex_punctuation_del_package.regex_p_del import reg_del_pun
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(regex_p_del))
    return tests


class DelPunctTest(TestCase):
    def test_right_string(self):
        self.assertEqual(reg_del_pun(text_str='мир, труд, май'), 'мир труд май')

    def test_right_string_capital(self):
        self.assertEqual(reg_del_pun(text_str='МИР, ТРУД, МАЙ'), 'МИР ТРУД МАЙ')

    def test_right_string_englis(self):
        self.assertEqual(reg_del_pun(text_str='pice, Craft, May'), 'pice Craft May')

    def test_right_string_no_punctiation(self):
        self.assertEqual(reg_del_pun(text_str='Миру мир'), 'Миру мир')

    def test_ints_in_input(self):
        with self.assertRaises(TypeError) as e:
            reg_del_pun(text_str=1)
        self.assertEqual('Введите непустую строку, а не int', e.exception.args[0])

    def test_float_in_input(self):
        with self.assertRaises(TypeError) as e:
            reg_del_pun(text_str=1.0)
        self.assertEqual('Введите непустую строку, а не float', e.exception.args[0])

    def test_empty_str_in_input(self):
        with self.assertRaises(ValueError) as e:
            reg_del_pun(text_str='')
        self.assertEqual('Введите непустую строку', e.exception.args[0])


if __name__ == '__main__':
    main()
