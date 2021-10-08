from unittest import TestCase, main
from tested.digits_in_number_package import digit_counter
from tested.digits_in_number_package.digit_counter import digits_in_number
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(digit_counter))
    return tests


class DigitsInNumberTest(TestCase):
    def test_digit_in_input(self):
        self.assertEqual(digits_in_number(n=12), 2)

    def test_str_in_input(self):
        with self.assertRaises(TypeError) as e:
            self.assertEqual(digits_in_number(n='12'))
        self.assertEqual('Должно быть введено целое число', e.exception.args[0])

    def test_nothing_in_input(self):
        with self.assertRaises(TypeError) as e:
            self.assertEqual(digits_in_number(n=' '))
        self.assertEqual('Должно быть введено целое число', e.exception.args[0])


if __name__ == '__main__':
    main()
