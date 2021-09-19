from unittest import TestCase, main
from tested.roman_arabic_package import rom_arabic
from tested.roman_arabic_package.rom_arabic import roman_nums
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(rom_arabic))
    return tests


class RomanArabicTest(TestCase):
    def test_input_one(self):
        self.assertEqual(roman_nums(text_str='I'), 1)

    def test_input_two(self):
        self.assertEqual(roman_nums(text_str='II'), 2)

    def test_input_four(self):
        self.assertEqual(roman_nums(text_str='IV'), 4)

    def test_input_nums(self):
        with self.assertRaises(TypeError) as e:
            roman_nums(text_str='2')
        self.assertEqual('Введите римскую цифру большими латинскими буквами', e.exception.args[0])

    def test_input_low_case(self):
        with self.assertRaises(TypeError) as e:
            roman_nums(text_str='v')
        self.assertEqual('Введите римскую цифру большими латинскими буквами', e.exception.args[0])


if __name__ == '__main__':
    main()
