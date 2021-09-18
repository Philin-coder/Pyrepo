from unittest import TestCase, main
from tested.rusletterfinder_package import rusfinder
from tested.rusletterfinder_package.rusfinder import finder
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(rusfinder))
    return tests


class RegexTest(TestCase):
    def test_str_in_input(self):
        self.assertEqual(finder(str_input='123wwwабв'), 3)

    def test_digit_in_input(self):
        with self.assertRaises(TypeError) as e:
            finder(str_input=123)
        self.assertEqual('Введите строку', e.exception.args[0])


if __name__ == '__main__':
    main
