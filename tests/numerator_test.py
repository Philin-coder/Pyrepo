from unittest import TestCase, main
from tested.find_only_nums import numerator
from tested.find_only_nums.numerator import num_finder
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(numerator))
    return tests


class NumeratorTest(TestCase):
    def test_is_list(self):
        self.assertIsInstance(num_finder(text_str='abc83 cde7 1 b 24'), list)

    def test_is_int_in_list(self):
        self.assertTrue(
            (all(isinstance(i, int) for i in num_finder(text_str='abc83 cde7 1 b 24')) is True, 'в списке не цифры'))

    def test_digit_in_input(self):
        with self.assertRaises(TypeError) as e:
            num_finder(text_str=837124)
        self.assertEqual('Передан неверный тип данных, либо - пустая строка', e.exception.args[0])

    def test_str_only_in_input(self):
        with self.assertRaises(TypeError) as e:
            num_finder(text_str='abc cde')
        self.assertEqual('Передан неверный тип данных, либо - пустая строка', e.exception.args[0])

    def test_empty_str_in_input(self):
        with self.assertRaises(TypeError) as e:
            num_finder(text_str='')
        self.assertEqual('Передан неверный тип данных, либо - пустая строка', e.exception.args[0])


if __name__ == '__main__':
    main()
