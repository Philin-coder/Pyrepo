from unittest import TestCase, main
from tested.another_calc_package import calc
from tested.another_calc_package.calc import calculate
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(calc))
    return tests


class CalcTest(TestCase):
    def test_calc_plus(self):
        self.assertEqual(calculate(operation='+', a=2, b=3), 5)

    def test_calc_minus(self):
        self.assertEqual(calculate(operation='-', a=6, b=2), 4)

    def test_calc_dev(self):
        self.assertEqual(calculate(operation='/', a=18, b=2), 9)

    def test_calc_mul(self):
        self.assertEqual(calculate(operation='*', a=18, b=2), 36)

    def test_calc_div_zero(self):
        with self.assertRaises(ZeroDivisionError) as e:
            calculate(operation='/', a=18, b=0)
        self.assertEqual('на ноль не делим ', e.exception.args[0])

    def test_calc_char_in_input(self):
        with self.assertRaises(TypeError) as e:
            calculate(operation='/', a=18, b='200')
        self.assertEqual('введите  код операции, затем 2 числа', e.exception.args[0])

    def test_calc_wrong_sign(self):
        with self.assertRaises(ValueError) as e:
            calculate(operation='&', a=18, b=200)
        self.assertEqual('Нужных знаков нет ', e.exception.args[0])


if __name__ == '__main__':
    main()
