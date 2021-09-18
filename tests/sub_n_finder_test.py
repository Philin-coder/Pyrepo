from unittest import TestCase, main
from tested.sub_n_finder_package import s_finder
from tested.sub_n_finder_package.s_finder import finder
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(s_finder))
    return tests


class SubnTest(TestCase):
    def test_chars_in_input(self):
        self.assertEqual(finder(sym='о', str_text='дорога'), ('дорога', 2))

    def test_ints_in_input(self):
        with self.assertRaises(TypeError) as e:
            finder(sym=1, str_text=11),
        self.assertEqual('Введите символ(не число) и строку для поиска', e.exception.args[0])


if __name__ == '__main__':
    main()
