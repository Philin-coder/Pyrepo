from unittest import TestCase, main
from tested.chord_meth_package import chord_meth
from tested.chord_meth_package.chord_meth import f
from tested.chord_meth_package.chord_meth import f1
from tested.chord_meth_package.chord_meth import chord_method
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(chord_meth))
    return tests


class ChordTest(TestCase):
    def test_first_func_float_input(self):
        self.assertEqual(f(x=12.0), -15.418879797456006)

    def test_first_func_int_input(self):
        self.assertEqual(f(x=12), -15.418879797456006)

    def test_first_func_char_input(self):
        with self.assertRaises(TypeError) as e:
            f(x='12')
        self.assertEqual('Введено не число', e.exception.args[0])

    def test_second_func_float_input(self):
        self.assertEqual(f1(x=11.0), -1.1978952727983705)

    def test_second_func_int_input(self):
        self.assertEqual(f1(x=11), -1.1978952727983705)

    def test_second_func_char_input(self):
        with self.assertRaises(TypeError) as e:
            f1(x='11')
        self.assertEqual('Введено не число', e.exception.args[0])

    def test_main_func_float_input(self):
        self.assertEqual(chord_method(a=100.0, b=100.0), 35.77152063957297)

    def test_main_func_int_input(self):
        self.assertEqual(chord_method(a=100, b=100), 35.77152063957297)

    def test_main_func_char_input(self):
        with self.assertRaises(TypeError) as e:
            chord_method(a='100', b='100')
        self.assertEqual('Введено не число', e.exception.args[0])

    def test_main_func_wrong_data_input(self):
        with self.assertRaises(ValueError) as e:
            chord_method(a=10.0, b=20.0)
        self.assertEqual('Value not invalidate', e.exception.args[0])


if __name__ == '__main__':
    main()
