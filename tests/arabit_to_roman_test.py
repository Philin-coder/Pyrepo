from unittest import TestCase, main
from tested.arabic_to_roman_package import arabic_to_roman
from tested.arabic_to_roman_package.arabic_to_roman import arabic_to_roman_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(arabic_to_roman))
    return tests


class ArabitToRomanTest(TestCase):
    def test_arabic_to_roman_even_ints_two_signs(self):
        self.assertEqual(arabic_to_roman_func(n=12), 'XII')

    def test_arabic_to_roman_even_ints_one_sign(self):
        self.assertEqual(arabic_to_roman_func(n=8), 'VIII')

    def test_arabic_to_roman_odd_ints_one_sign(self):
        self.assertEqual(arabic_to_roman_func(n=5), 'V')

    def test_arabic_to_roman_big_int(self):
        self.assertEqual(arabic_to_roman_func(n=128), 'CXXVIII')

    def test_arabic_to_roman_negative_int(self):
        with self.assertRaises(TypeError) as e:
            arabic_to_roman_func(n=-8)
        self.assertEqual('Должно быть введено целое  положительное число, не равное 0', e.exception.args[0])

    def test_arabic_to_roman_zero_in_input(self):
        with self.assertRaises(TypeError) as e:
            arabic_to_roman_func(n=0)
        self.assertEqual('Должно быть введено целое  положительное число, не равное 0', e.exception.args[0])

    def test_arabic_to_roman_char_in_input(self):
        with self.assertRaises(TypeError) as e:
            arabic_to_roman_func(n='8')
        self.assertEqual('Должно быть введено целое  положительное число, не равное 0', e.exception.args[0])


if __name__ == '__main__':
    main()
