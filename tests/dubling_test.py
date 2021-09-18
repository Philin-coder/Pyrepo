from unittest import TestCase, main
from tested.dubling_package import dubling
from tested.dubling_package.dubling import repeat_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(dubling))
    return tests


class DublingTest(TestCase):
    def test_dash_in_string(self):
        self.assertEqual(repeat_func(n=3, text_str='s-s'), 's, s, s, s')

    def test_dash_only_in_string(self):
        self.assertEqual(repeat_func(n=3, text_str='---'), '')

    def test_string_without_dash(self):
        self.assertEqual(repeat_func(n=3, text_str='мир'), 'мир')

    def test_length_of_iput(self):
        with self.assertRaises(ValueError) as e:
            repeat_func(n=4, text_str='мир')
        self.assertEqual('строка должна быть нужной длинны', e.exception.args[0])

    def test_chars_in_input(self):
        with self.assertRaises(TypeError) as e:
            repeat_func(n='4', text_str='мир')
        self.assertEqual('Введите  длинну строки, затем -саму строку', e.exception.args[0])


if __name__ == '__main__':
    main()
