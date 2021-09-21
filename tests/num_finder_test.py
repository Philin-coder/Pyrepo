from unittest import TestCase, main
from tested.big_nums_seaker_package import num_seacker
from tested.big_nums_seaker_package.num_seacker import string_big_digit_finder
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(num_seacker))
    return tests


class NumFinderTestCase(TestCase):
    def test_works(self):
        self.assertEqual(string_big_digit_finder(
            text_str='1.152000000000D+05-1.303851604462D-07-5.331575505977D-01-3.986060619354D+07'),
            ['1.152000000000', '+05', '-1.303851604462', '-07', '-5.331575505977', '-01',
             '-3.986060619354', '+07'])

    def test_works_mixed_str(self):
        self.assertEqual(string_big_digit_finder(text_str='Мир 1'), ['1'])

    def test_wrong_input_str(self):
        with self.assertRaises(TypeError) as e:
            string_big_digit_finder(text_str='Мир')
        self.assertEqual('Передана строка, не содержащая цифр в нужном формате, либо - пустая', e.exception.args[0])

    def test_wrong_input_empty_str(self):
        with self.assertRaises(TypeError) as e:
            string_big_digit_finder(text_str='')
        self.assertEqual('Передана строка, не содержащая цифр в нужном формате, либо - пустая', e.exception.args[0])


if __name__ == '__main__':
    main()
