from unittest import TestCase, main
from tested.second_input_package import second_input
from tested.second_input_package.second_input import second_input_finder_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(second_input))
    return tests


class SInputTest(TestCase):
    def test_it_works_english(self):
        self.assertEqual(second_input_finder_func(text_str='sims', t_ch='s'), 3)

    def test_it_works_russian(self):
        self.assertEqual(second_input_finder_func(text_str='окко', t_ch='о'), 3)

    def test_no_second_input(self):
        with self.assertRaises(IndexError) as e:
            second_input_finder_func(text_str='сало', t_ch='а')
        self.assertEqual('проверьте ввод, возможно, слово содержит символ всего 1 раз', e.exception.args[0])

    def test_no_char(self):
        with self.assertRaises(TypeError) as e:
            second_input_finder_func(text_str='окко', t_ch='')
        self.assertEqual('Введите  непустую символьную строку и искомый символ, не равный пробелу (не цифру)',
                         e.exception.args[0])

    def test_no_word(self):
        with self.assertRaises(TypeError) as e:
            second_input_finder_func(text_str='', t_ch='о')
        self.assertEqual('Введите  непустую символьную строку и искомый символ, не равный пробелу (не цифру)',
                         e.exception.args[0])

    def test_no_word(self):
        with self.assertRaises(TypeError) as e:
            second_input_finder_func(text_str='1окко1', t_ch='1')
        self.assertEqual('Введите  непустую символьную строку и искомый символ, не равный пробелу (не цифру)',
                         e.exception.args[0])


if __name__ == '__main__':
    main()
