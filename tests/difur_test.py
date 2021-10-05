from unittest import TestCase, main
from tested.diffur_solver_package import diffur_solver
from tested.diffur_solver_package.diffur_solver import dif_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(diffur_solver))
    return tests


class DiffTest(TestCase):
    def test_works(self):
        self.assertEqual(dif_func(a=12.3, e=12.3), (-5.983353400899203e-14 + 325.7185884161348j))

    def test_wrong_input(self):
        with self.assertRaises(TypeError) as e:
            dif_func(a='12.3', e='12.3')
        self.assertEqual('Введите 2 вещественных числа', e.exception.args[0])


if __name__ == '__main__':
    main()
