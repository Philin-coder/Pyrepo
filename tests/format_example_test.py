from unittest import TestCase, main
from tested.format_example_again_package import format_example
from tested.format_example_again_package.format_example import format_example_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(format_example))
    return tests


class FormatExampleTest(TestCase):
    def test_format_example_int_in_input(self):
        self.assertEqual(format_example_func(start_int=4),
                         'prev number for this  number  3 and next number for the number 5')

    def test_format_example_char_in_input(self):
        with self.assertRaises(TypeError) as e:
            format_example_func(start_int='4')
        self.assertEqual('Введите  целое число а не str', e.exception.args[0])

    def test_format_example_float_in_input(self):
        with self.assertRaises(TypeError) as e:
            format_example_func(start_int=4.1)
        self.assertEqual('Введите  целое число а не float', e.exception.args[0])


if __name__ == '__main__':
    main()
