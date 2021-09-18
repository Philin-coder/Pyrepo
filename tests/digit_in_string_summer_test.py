from unittest import TestCase, main
from tested.digit_in_string_summer_package import digit_in_string_summer
from tested.digit_in_string_summer_package.digit_in_string_summer import digit_summer_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(digit_in_string_summer))
    return tests


class DigitInStringSummerTest(TestCase):
    def test_simple_summ(self):
        self.assertEqual(digit_summer_func(text_str='лес 123 поле 356'), 20)

    def test_no_digit(self):
        self.assertEqual(digit_summer_func(text_str='лес, дол,   поле '),0)

    def test_no_letters(self):
        self.assertEqual(digit_summer_func(text_str='123'), 6)

    def test_epty_string(self):
        with self.assertRaises(TypeError) as e:
            digit_summer_func(text_str='')
        self.assertEqual('Введите непустую строку, содержащую цифры',e.exception.args[0])

    def test_digits_only(self):
        with self.assertRaises(TypeError) as e:
            digit_summer_func(text_str=123)
        self.assertEqual('Введите непустую строку, содержащую цифры', e.exception.args[0])

if __name__ == '__main__':
    main()
