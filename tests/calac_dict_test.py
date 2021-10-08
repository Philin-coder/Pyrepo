from unittest import TestCase, main
from tested.anoter_calc_dict_package import calc_dict
from tested.anoter_calc_dict_package.calc_dict import dict_count_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(calc_dict))
    return tests


class CalcDictTest(TestCase):
    def test_add_ints_in_input(self):
        self.assertEqual(dict_count_func(x=2, y=5, key_to_find='add'), 7)

    def test_sub_ints_in_input(self):
        self.assertEqual(dict_count_func(x=2, y=5, key_to_find='sub'), -3)

    def test_mul_ints_in_input(self):
        self.assertEqual(dict_count_func(x=2, y=5, key_to_find='mul'), 10)

    def test_div_ints_in_input(self):
        self.assertEqual(dict_count_func(x=2, y=5, key_to_find='div'), 0.4)

    def test_divZero_ints_in_input(self):
        with self.assertRaises(ZeroDivisionError) as e:
            dict_count_func(x=2, y=0, key_to_find='div')
        self.assertEqual('на ноль делить -Зло ', e.exception.args[0])

    def test_wrong_operation_code(self):
        with self.assertRaises(ValueError) as e:
            dict_count_func(x=2, y=0, key_to_find='div_v')
        self.assertEqual('неверно введен код операции', e.exception.args[0])

    def test_chars_in_input(self):
        with self.assertRaises(TypeError) as e:
            dict_count_func(x='2', y=4, key_to_find='div')
        self.assertEqual(
            'введите 2 числа и код операции(add- сложение, sub- вычитание, mul-умножене, div- деленеи)',
            e.exception.args[0])


if __name__ == '__main__':
    main()
