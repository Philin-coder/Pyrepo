from unittest import TestCase, main
from tested.another_calculator_with_dict_package import dict_arifm
from tested.another_calculator_with_dict_package.dict_arifm import counter_again
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(dict_arifm))
    return tests


class AnotherCalculatorWithDictTest(TestCase):
    def test_plus(self):
        self.assertEqual(counter_again(a=1, b=2, operation='+'), 3)

    def test_minus(self):
        self.assertEqual(counter_again(a=7, b=1, operation='-'), 6)

    def test_mul(self):
        self.assertEqual(counter_again(a=8, b=2, operation='*'), 16)

    def test_div(self):
        self.assertEqual(counter_again(a=8, b=2, operation='/'), 4.0)

    def test_wrong_sign(self):
        with self.assertRaises(ValueError) as e:
            counter_again(a=8, b=2, operation='&')
        self.assertEqual('Нужных знаков нет', e.exception.args[0])

    def test_chars_in_input(self):
        with self.assertRaises(TypeError) as e:
            counter_again(a=8, b='2', operation='/')
        self.assertEqual('Неверно введен тип операнда', e.exception.args[0])

    def test_div_zero(self):
        with self.assertRaises(ZeroDivisionError) as e:
            counter_again(a=8, b=0, operation='/')
        self.assertEqual('На ноль делить грешно', e.exception.args[0])


if __name__ == '__main__':
    main()
