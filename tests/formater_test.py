from unittest import TestCase, main
from tested.fpack import fmod
from tested.fpack.fmod import format_func_again
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(fmod))
    return tests


class FormTest(TestCase):
    def test_works_float(self):
        self.assertEqual(format_func_again(d=20.4), ('площадь окружности равна и длина', ' ', '326.8513', ' ', '  64'))

    def test_works_int(self):
        self.assertEqual(format_func_again(d=20), ('площадь окружности равна и длина', ' ', '314.1593', ' ', '  63'))

    def test_works_char(self):
        with self.assertRaises(TypeError) as e:
            format_func_again(d='20')
        self.assertEqual('Введено не число ', e.exception.args[0])


if __name__ == '__main__':
    main()
