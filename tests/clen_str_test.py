from unittest import TestCase, main
from tested.clean_str_package import cleaner_str
from tested.clean_str_package.cleaner_str import cleaner
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(cleaner_str))
    return tests


class ClenStrTest(TestCase):
    def test_str_in_input_true(self):
        self.assertEqual(cleaner(text_str='проооба'), 'проба')

    def test_str_in_input_false(self):
        self.assertEqual(cleaner(text_str='оса'), 'оса')

    def test_ints_in_input(self):
        with self.assertRaises(TypeError) as e:
            cleaner(text_str=1),
        self.assertEqual('Введите строку', e.exception.args[0])


if __name__ == '__main__':
    main()
