from unittest import TestCase, main
from tested.string_com_package import string_comp
from tested.string_com_package.string_comp import str_comparer
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(string_comp))
    return tests


class StringCompTest(TestCase):
    def test_works_two_strings_pos(self):
        self.assertEqual(str_comparer(text_str='Проба первая', fnd_str='Проба'), 'вторая строка есть в первой')

    def test_works_two_strings_neg(self):
        self.assertEqual(str_comparer(text_str='Проба первая', fnd_str='тут'), 'Нет второй строки в первой')

    def test_wrong_input_first_empty_str(self):
        with self.assertRaises(TypeError) as e:
            str_comparer(text_str='', fnd_str='Проба')
        self.assertEqual('Введите 2 непустых  строки, не содержащих чисел', e.exception.args[0])

    def test_wrong_input_second_empty_str(self):
        with self.assertRaises(TypeError) as e:
            str_comparer(text_str='Проба первая', fnd_str='')
        self.assertEqual('Введите 2 непустых  строки, не содержащих чисел', e.exception.args[0])

    def test_wrong_input_first_digs_str(self):
        with self.assertRaises(TypeError) as e:
            str_comparer(text_str='1Проба первая', fnd_str='')
        self.assertEqual('Введите 2 непустых  строки, не содержащих чисел', e.exception.args[0])


if __name__ == '__main__':
    main()
