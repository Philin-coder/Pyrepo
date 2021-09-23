from unittest import TestCase, main
from tested.solver_package import solver
from tested.solver_package.solver import solver_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(solver))
    return tests


class SolverTest(TestCase):
    def test_float_in_input_d_less_zero(self):
        self.assertEqual(solver_func(a=12.0, b=12.0, c=12.0),
                         ('квадратное уровнение корней не имеет', ' дискриминант равен -572.5358983848622'))

    def test_int_in_input_d_less_zero(self):
        self.assertEqual(solver_func(a=12, b=12, c=12),
                         ('квадратное уровнение корней не имеет', ' дискриминант равен -572.5358983848622'))

    def test_d_is_zero(self):
        self.assertEqual(solver_func(a=5.0, b=400.0, c=1.0), ('-40.0', '-40.0', ' дискриминант равен 0.0'))

    def test_d_more_zero(self):
        self.assertEqual(solver_func(a=1.0, b=400.0, c=1.0), ('-198.0', ' -202.0', 'дискриминант равен 16.0'))

    def test_zero_in_input(self):
        with self.assertRaises(ZeroDivisionError) as e:
            solver_func(a=0.0, b=0.0, c=1.0)
        self.assertEqual('Нельзя делить  на  ноль', e.exception.args[0])

    def test_char_in_input(self):
        with self.assertRaises(TypeError) as e:
            solver_func(a='1.0', b=400.0, c=1.0)
        self.assertEqual('Введите числа', e.exception.args[0])


if __name__ == '__main__':
    main()
