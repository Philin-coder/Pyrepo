from unittest import TestCase, main
from tested.max_num_ammount_int_package import max_num_ammount
from tested.max_num_ammount_int_package.max_num_ammount import num_div
from tested.max_num_ammount_int_package.max_num_ammount import mx_finder
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(max_num_ammount))
    return tests


class MaxNumAmmTest(TestCase):
    def test_ints_in_input_num_div(self):
        self.assertEqual(num_div(n=12), 6)

    def test_ints_in_input_mx_finder(self):
        self.assertEqual(mx_finder(a=1, b=128), 120)

    def test_char_in_input_mx_finder(self):
        with self.assertRaises(TypeError) as e:
            mx_finder(a='1', b='128')
        self.assertEqual('Передан неправильный тип данных', e.exception.args[0])

    def test_char_in_input_num_div(self):
        with self.assertRaises(TypeError) as e:
            num_div(n='12')
        self.assertEqual('Передан неправильный тип данных', e.exception.args[0])


if __name__ == '__main__':
    main()
