from unittest import TestCase
from tested.replacer_package import replacer
from tested.replacer_package.replacer import str_conv_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(replacer))
    return tests


class ReplaxerTest(TestCase):
    def test_repl_english(self):
        self.assertEqual(str_conv_func(input_string='google', repl_string='@'), '@2g 2o 1l 1e ')

    def test_english_another_repl(self):
        self.assertEqual(str_conv_func(input_string='Peple', repl_string='#'), '#2e 1P 1p 1l ')

    def test_wrong_input(self):
        with self.assertRaises(TypeError) as e:
            str_conv_func(input_string=1, repl_string='#')
        self.assertEqual('Введите непустую строку', e.exception.args[0])


if __name__ == '__main__':
    unittest.main()
